import argparse
import random
import sys


alphabet = ["A", "C", "T", "G"]
rev_dict = {
            "A": "T",
            "C": "G",
            "T": "A",
            "G": "C"
            }

def reverse_complement(my_seq):
    return [rev_dict[i] for i in my_seq]

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", dest="readlength", type=int, required=True)
    parser.add_argument("-o", dest="outfile", type=str, required=False, default="reads.fa")
    parser.add_argument("-i", dest="infile", type=str, required=False)
    return parser.parse_args()

def parse_fasta(infile)
    ## TODO
    with open(infile, "r") as ifi:
        
    return None


def write_out(ref, oname):
    with open(oname, "w") as ofi:
        
if __name__ == "__main__":
    args = parse_args()
