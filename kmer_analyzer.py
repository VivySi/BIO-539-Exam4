# import sys
import sys

# first function: validate_sequence, here we check if the sequence is valid (length and characters)
def validate_sequence(sequence, k):
    """
    Check whether a DNA sequence is valid for k-mer analysis.

    Parameters
    ----------
    sequence : str
        The input DNA sequence (should contain only A, T, C, G).
    k : int
        Length of the k-mer; must be a positive integer not greater than len(sequence).

    Returns
    -------
    bool
        True if the sequence is valid, False otherwise.
    """
    if len(sequence) < k:  # check if the sequence is shorter than k
        # print("your sequence is too short or k is too large")
        return False

    if sequence.startswith('>'):  # check if the sequence starts with '>'
        # print("your sequence starts with '>'")
        return False

    if k < 1 or not isinstance(k, int):  # check if k is less than 1 or not int
        # print("k must be a positive integer")
        return False

    for nucleotide in sequence:
        if nucleotide not in 'ATCG':  # check whether there is an invalid character
            # print("your sequence contains invalid characters")
            return False

    return True

# second function: update_kmer_count, here we update the k-mer count and the next character count in the dictionary

def update_kmer_count(kmer_data, kmer, next_char):
    """
    Update k-mer frequency and following-character counts.

    Parameters
    ----------
    kmer_data : dict
        Dictionary storing k-mer statistics. Keys are k-mer strings.
        Values are dicts with keys 'count' (int) and 'next_chars' (dict).
    kmer : str
        The current k-mer to update.
    next_char : str
        The character that immediately follows this k-mer in the sequence.

    Returns
    -------
    dict
        The updated kmer_data dictionary.
    """
    
    if kmer not in kmer_data:
        kmer_data[kmer] = {'count': 0, 'next_chars': {}} # here change 1 to 0
    
    kmer_data[kmer]['count'] += 1
    
    if next_char not in kmer_data[kmer]['next_chars']:
        kmer_data[kmer]['next_chars'][next_char] = 0 
    kmer_data[kmer]['next_chars'][next_char] += 1

    return kmer_data


# third function:

def count_kmers_with_context(sequence, k):
    kmer_data = {}
    
    for i in range(len(sequence) - k):
        kmer = sequence[i:i+k]
        next_char = sequence[i+k]
        
        kmer_data = update_kmer_count(kmer_data, kmer, next_char)
    
    return kmer_data


def write_results_to_file(kmer_data, output_filename):
    sorted_kmers = sorted(kmer_data.keys())
    
    with open(output_filename, 'w') as f:
        for kmer in sorted_kmers:
            next_chars = kmer_data[kmer]['next_chars']
            
            next_char_str = " ".join(
                f"{char}:{freq}" 
                for char, freq in sorted(next_chars.items())
            )
            
            f.write(f"{kmer} {next_char_str}\n")


def main():
    sequence_file = sys.argv[1]
    k = int(sys.argv[2])
    output_file = sys.argv[3]
    
    print(f"Reading sequences from {sequence_file}...")

    with open(sequence_file, 'r') as f:
        for sequence in f:
            sequence = sequence.strip()

            if not validate_sequence(sequence, k):
                print(f"  Warning: Skipping sequence")
                continue
            
            kmer_data = count_kmers_with_context(sequence, k) 
            
            write_results_to_file(kmer_data, output_file)

if __name__ == '__main__':
    main()
