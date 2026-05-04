# BIO-539-Exam4
Here is a repository for BIO 539 Exam 4, which contains a python sciprt works as kmer analyzer `kmer_analyzer.py`, a pytest script `test_kmer_analyzer.py`, and of course, this readme. 

There are five functions in `kmer_analyzer.py`, use `help()`to see docstrings for each fucntion.

# Usage
run the kmer analyzer python sciprt (`kmer_analyzer.py`) in command line by:   
`python kmer_analyzer.py sequence_file.txt k result.txt`

Change `sequence_file.txt` to your sequence file name;  
Change `k` to your prefered substrings of length;  
Change `result.txt` to your output file name.  

Run the pytest scirpt in command line by `pytest kmer_analyzer.py`

NOTE: 
For the input file, the line with invalid character (not in "A, T, C, T") will be skipped and *Warning: Skipping sequence* will show up.  
Remerber to remove ">" before each sequence, ">" will be seen as a invalid character.

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


# AI use statement
I used AI help with debugging throughout the coding process. The `test_write_results_to_file_basic` and `test_main_integration functions` in the pytest script were generated entirely with AI support, bacause I have no idea about how to test this two function. I also used AI tools to learn how to write clear and complete docstrings. While writing and testing the Python script in Jupyter Notebook within Visual Studio Code, I additionally used the built‑in AI features to generate very very little parts of the code and explanatory comments.

