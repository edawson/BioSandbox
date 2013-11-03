import sys, os, re
from collections import OrderedDict

snp = {}
header = []

def load_file(infile):
    global snp
    global header
    with open(infile, "r") as snp_file:
        for line in snp_file:
            if (line.startswith("#")):
                header.append(line)
            else:
                try:
                    position = line.split("\t")[1]
                    snp[position] = line
                except:
                    print "I don't know what to do with weird VCF formatting!"


def indel_filter(snp_file, indel_file):
    global snp
    global header
    indel = {}

    with open(indel_file, "r") as indel_vcf:
        for line in indel_vcf:
            if (line.startswith("#")):
                continue
            else:
                position = line.split("\t")[1]
                pos = int(position)
                if (position in snp.keys() or str(pos + 1) in snp.keys()
                or str(pos + 2) in snp.keys() or str(pos + 3) in snp.keys()
                or str(pos - 1) in snp.keys() or str(pos + 2) in snp.keys()
                or str(pos + 3) in snp.keys()):
                    del snp[position]

def snp_filter(snp_file):
    global snp
    dead_keys = ()
    for key in snp:
        neighbors = ()
        for i in snp:
            if (abs(int(key) - int(i)) <= 5 and i != key):
                neighbors.append(i)
        if (len(neighbors) >= 4):
            for x in neighbors:
                dead_keys.append(x)

    for dead in dead_keys:
        del snp[dead]

def write_out(outfile):
    global snp
    global header
    with open(outfile, "w") as out_vcf:
        for line in header:
            out_vcf.write(line)
        for key in snp:
            outfile.write(snp[key])
        
def main():
    snp_file = sys.argv[1]
    indel_file = sys.argv[2]
    name1 = sys.argv[3]
    name2 = sys.argv[4]
    load_file(snp_file)
    indel_filter(snp_file, indel_file)
    outfile = name1 + "." + name2 + ".vcf"
    write_out(outfile)
main()
