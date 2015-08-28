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
    parser.add_argument("-s", dest="size", type=int, required=True)
    parser.add_argument("-c", dest="chroms", type=int, required=False, default=1)
    parser.add_argument("-o", dest="outfile", type=str, required=False, default="out.fa")
    parser.add_argument("-i", dest="infile", type=str, required=False)
    return parser.parse_args()

def get_letter(error_rate=0.0):
    ## TODO integrate error_rate
    return None

def gen_linear_chrom(size):
    for i in xrange(0, size):
        yield random.sample(alphabet, 1)[0]

def make_ref(size, num_chroms=1):
    for i in xrange(0, num_chroms):
        yield str(i + 1), gen_linear_chrom(size)

def write_out(ref, oname):
    with open(oname, "w") as ofi:
        for chrom in ref:
            ofi.write("> " + chrom[0] + "\n")
            ofi.write("".join([x for x in chrom[1]]) + "\n")

if __name__ == "__main__":
    #print sys.argv[1]
    args = parse_args()
    x = make_ref(args.size, args.chroms)
    write_out(x, args.outfile)
