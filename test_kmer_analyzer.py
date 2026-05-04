#!/usr/bin/env python3
# This file contains test for the functions in kmer_analyzer.py
# run with: pytest test_kmer_analyzer.py


import pytest

## first test validate_sequence:
# sequence shorter than k
# sequence contain character that not "A","T","C","G"
# negative k, or k is not integer


from kmer_analyzer import validate_sequence, update_kmer_count

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
    