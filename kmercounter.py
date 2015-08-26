import argparse


def parse_args():
	return None

def kmerize():
	return None

def parse_file():
	return None


if __name__ == "__main__":
	## We'll need several arguments:
	## k: kmer length
	## i: input file
	## o: output file
	## min_k : minimum kmer count for output
	args = parse_args()
	
	kmer_d = defaultdict(1)
	
	for record in parse_file:
		kmers = kmerize(record)
		for k in kmers:
			if not k in kmer_d:
				kmer_d[k] = 1
			else:
				kmer_d[k] = kmer_d[k] + 1
	for entry in kmer_d:
		if kmer_d[entry] > args.min:
			print entry
