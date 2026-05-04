# BIO-539-Exam4
Here is a repository for BIO 539 Exam 4, which contain a python sciprt works as kmer analyzer`kmer_analyzer.py`, a pytest script`test_kmer_analyzer.py`, and of course, this readme.

# Usage
run the kmer analyzer python sciprt (`kmer_analyzer.py`) in command line by: 
`python kmer_analyzer.py sequence_file.txt k result.txt`

Change `sequence_file.txt` to your sequence file name;
Change `k` to your prefered substrings of length;
Change `result.txt` to your output file name.  

run the pytest scirpt in command line by `pytest kmer_analyzer.py`

# Pytest scirpt
Pytest scirpt includes 9 test functions.

First test validate_sequence:
- sequence shorter than k;
- sequence contain character that not "A","T","C","G";
- negative k, or k is not integer.

Second test update_kmer_count:
- new k-mer first adding to the dictionart;
- same k-mer seconde time with same next character;
- same k-mer with different next character.

Third test count_kmers_with_context:
- test with short, repeat, sample sequence, to see whether we get expected results.
- NOTE: we don't test k is larger than length of sequence here, as it was tested in the first funtion.

Forth test write_results_to_file:
- create a simple kmer data, to see whether we get expected output file;
- whether the result listed in alphabetical order.

Fifth test main (personally think might not be necessary):
- create a temporary input file and path, test the whole workflow with a simple input file, and check whether we get expected output file.


# AI statement

