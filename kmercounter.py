import argparse
from collections import defaultdict


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="infile", type=str, required=True)
    parser.add_argument("-k", dest="k", type=int, required=True)
    parser.add_argument("-m", dest="min", type=int, default=5, required=False)
    return parser.parse_args()

def kmerize(my_seq, k):
    ret = []
    for i in xrange(0, len(my_seq) - k):
        ret.append(my_seq[i : i + k])
    return ret

        ## return [my_seq[i : i + k] for i in xrange(0, len(my_seq) -k)]
        ##
        ##

## parsing a fasta / fastq file
## TODO just a fasta parser for the moment
def parse_file(my_file):
    with open(my_file, "r") as ifi:
        for line in ifi:
            if line.startswith(">"):
                continue
            else:
                yield line


if __name__ == "__main__":
	## We'll need several arguments:
	## k: kmer length
	## i: input file
	## o: output file
	## min_k : minimum kmer count for output
	args = parse_args()
	
	kmer_d = defaultdict(int)
	
	for record in parse_file(args.infile):
		kmers = kmerize(record, args.k)
		for k in kmers:
			if not k in kmer_d:
				kmer_d[k] = 1
			else:
				kmer_d[k] = kmer_d[k] + 1
                del kmers

	for entry in kmer_d:
		if kmer_d[entry] > args.min:
			print entry
