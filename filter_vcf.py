import sys

## A script used to filter
## a SNP VCF file and correct
## for some oddities in Varscan output.

## Eric T Dawson
## Texas Advanced Computing Center
## November 2013

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
                    snp[str(position)] = str(line)
                except:
                    print "I don't know what to do with non-standard VCF formatting!"


def indel_filter(snp_file, indel_file):
    ## If a snp falls within ten base pairs of an indel, remove it.
    global snp
    global header
    with open(indel_file, "r") as indel_vcf:
        for line in indel_vcf:
            if (line.startswith("#")):
                continue
            else:
                position = line.split("\t")[1]
                pos = int(position)
                window = range(pos-9, pos+10)
                for x in window:
                    if (str(x) in snp.keys()):
                        del snp[str(x)]

def snp_filter():
    ## If 3 or more snps fall within ten base pairs
    ## of each other, remove them all.
    global snp
    dead_keys = []
    for key in snp:
        neighbors = []
        high = int(key) + 10
        low = int(key) - 10
        for x in range(int(key), high):
            if (str(x) in snp.keys() and str(x) != key):
                neighbors.append(str(x))
        if (len(neighbors) >= 2):
            if (not key in dead_keys):
                dead_keys.append(key)
            for y in neighbors:
                if (y not in dead_keys):
                    dead_keys.append(y)
    for dead in dead_keys:
        del snp[dead]

def remove_modulo():
    ## Used for VarScan generated VCFs, as GATK
    ## can't handle the modulo operator in the allele
    ## frequency column
    global snp
    for key in snp:
        snp[key] = snp[key].replace("%", "")

def write_out(outfile):
    ## Sort the keys (positions in the chromosome)
    ## and print out the header to preserve VCF formatting
    global snp
    global header
    with open(outfile, "w") as out_vcf:
        for line in header:
            out_vcf.write(line)
        sort_snp = []
        for key in snp.keys():
            sort_snp.append(int(key))
        sort_snp.sort()
        for key in sort_snp:
            out_vcf.write(snp[str(key)])
        
def main():
    snp_file = sys.argv[1]
    indel_file = sys.argv[2]
    name1 = sys.argv[3]
    name2 = sys.argv[4]
    load_file(snp_file)
    remove_modulo()
    snp_filter()
    indel_filter(snp_file, indel_file)
    outfile = name1 + "." + name2 + ".vcf"
    write_out(outfile)
main()
