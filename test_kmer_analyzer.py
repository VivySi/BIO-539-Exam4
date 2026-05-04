#!/usr/bin/env python3


import pytest

from kmer_analyzer import validate_sequence


## test validate_sequence
# test sequence shorter than k
def test_validate_sequence_shorter_than_k():
    sequence = "ACG"
    k = 5
    result = validate_sequence(sequence, k)
    if result == False:
        print("Yeah! Test passed!✅ Sequence is shorter than k.")
        
    assert result == False

test_validate_sequence_shorter_than_k()


# test sequence with invalid characters
def test_validate_sequence_invalid_characters():
    sequence = ">ACGSTX"
    k = 3
    result = validate_sequence(sequence, k)
    if result == False:
        print("Yeah! Test passed!✅: Sequence contains invalid characters.")
        
    assert result == False

test_validate_sequence_invalid_characters()

# test negative k value
def test_validate_sequence_negative_k():
    sequence = "ATCGGTAC"
    k = -1
    result = validate_sequence(sequence, k)
    if result == False:
        print("Yeah! Test passed!✅: Negative k value is invalid.")
    assert result == False

test_validate_sequence_negative_k()  


