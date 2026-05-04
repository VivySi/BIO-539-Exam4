#!/usr/bin/env python3
# This file contains test for the functions in kmer_analyzer.py
# run with: pytest test_kmer_analyzer.py


import pytest
import tempfile
from pathlib import Path
import sys

## first test validate_sequence:
# sequence shorter than k
# sequence contain character that not "A","T","C","G"
# test sequence with smallcase characters
# negative k, or k is not integer


from kmer_analyzer import validate_sequence, update_kmer_count, count_kmers_with_context, write_results_to_file, main

# test sequence shorter than k
def test_validate_sequence_shorter_than_k():
    sequence = "ACG"
    k = 5
    result = validate_sequence(sequence, k)
    assert result == False



# test sequence with invalid characters
def test_validate_sequence_invalid_characters():
    sequence = ">ACGSTX"
    k = 3
    result = validate_sequence(sequence, k)
    assert result == False

# test sequence with smallcase characters
def test_validate_sequence_smallcase_characters():
    sequence = "TaCgT"
    k = 3
    result = validate_sequence(sequence, k)
    assert result == False

# test negative k value
def test_validate_sequence_negative_k():
    sequence = "ATCGGTAC"
    k = -1
    result = validate_sequence(sequence, k)
    assert result == False


#second test update_kmer_count:

# new k-mer first adding to the dictionart
def test_update_kmer_count_new_kmer():
    kmer_data = {} # new kmer, here we start with an empty dictionary
    kmer = "ATC"
    next_char = "G"
    
    updated_kmer_data = update_kmer_count(kmer_data, kmer, next_char)
    
    assert updated_kmer_data[kmer]['count'] == 1 # the count should be 1 for the new k-mer
    assert updated_kmer_data[kmer]['next_chars'] == {"G": 1}


# same k-mer seconde time with same next character
def test_update_kmer_count_same_kmer_same_next_char():
    kmer_data = {"ATC": {'count': 1, 'next_chars': {"G": 1}}} # now "ATC" is second time, we already have a dictionary
    kmer = "ATC"
    next_char = "G"     
    updated_kmer_data = update_kmer_count(kmer_data, kmer, next_char)
    assert updated_kmer_data[kmer]['count'] == 2 # count should + 1
    assert updated_kmer_data[kmer]['next_chars'] == {"G": 2} # same next character, so count should + 1


# same k-mer with different next character
def test_update_kmer_count_same_kmer_different_next_char():
    kmer_data = {"ATC": {'count': 2, 'next_chars': {"G": 2}}}
    kmer = "ATC"
    next_char = "A"     
    updated_kmer_data = update_kmer_count(kmer_data, kmer, next_char)
    assert updated_kmer_data[kmer]['count'] == 3
    assert updated_kmer_data[kmer]['next_chars'][next_char] == 1

#third test count_kmers_with_context:
# NOTE: we don't test k is larger than length of sequence here, as it was tested in the first funtion


# test with short, repeat, sample sequence, to see whether we get expected results
# test sequence "ATGATCCATC" 

def test_count_kmers_simple():
    sequence = "ATGATCCATC" # repeat AT three times， with two different next characters.
    k = 2

    result = count_kmers_with_context(sequence, k)
    
    # maunally write the expected results for this sequence
    assert "AT" in result
    assert "TG" in result
    assert "GA" in result
    assert "TC" in result
    assert "CC" in result
    assert "CA" in result

    assert result["AT"] == {'count': 3, 'next_chars': {'G': 1, 'C': 2}}
    assert result["TG"] == {'count': 1, 'next_chars': {'A': 1}}
    assert result["GA"] == {'count': 1, 'next_chars': {'T': 1}}
    assert result["TC"] == {'count': 1, 'next_chars': {'C': 1}}
    assert result["CC"] == {'count': 1, 'next_chars': {'A': 1}}
    assert result["CA"] == {'count': 1, 'next_chars': {'T': 1}}
    


#forth test write_results_to_file:
# create a simple kmer data, to see whether we get expected output file
# and whether the result listed in alphabetical order

#import tempfile
#from pathlib import Path

def test_write_results_to_file_basic():
    # make a simple kmer_data dict to test the output format
    kmer_data = {
        "AT": {"count": 3, "next_chars": {"G": 1, "C": 2}},
        "TG": {"count": 1, "next_chars": {"A": 1}},
    }

    # use a temporary directory to avoid creating actual files on disk
    with tempfile.TemporaryDirectory() as tmpdir:
        out_path = Path(tmpdir) / "out.txt"

        write_results_to_file(kmer_data, out_path)

        with open(out_path, "r") as f:
            lines = f.read().splitlines()

    assert len(lines) == 2

    # expected output format:
    #    - AT: C:2 G:1
    #    - CG: A:2
    assert lines[0] == "AT C:2 G:1"
    assert lines[1] == "TG A:1"

#fifth test main function integration:
# test the whole workflow with a simple input file, and check whether we get expected output file
# import sys
def test_main_integration(tmp_path):
    # create a temporary input file with some sequences
    input_path = tmp_path / "seqs.txt" # define the input file path
    input_path.write_text("ATGC\nAT3X\nATGATC\n")  # some line with invalid character, will skip.
    output_path = tmp_path / "out.txt" # define the output file path

    # input arguments for main(): input file, k, output file
    sys.argv = ["kmer_analyzer.py", str(input_path), "2", str(output_path)]

    main()

    assert output_path.exists()
    content = output_path.read_text().strip().splitlines()
    assert any(line.startswith("AT") for line in content)
