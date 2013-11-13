import sys

def write_outfile(name, header, lines):
    with open(name, "w") as out:
        for line in header:
            out.write(line)
        for line in lines:
            out.write(line)

def load_file(infile):
    header = []
    chroms = []
    lines = []
    with open(infile, "r") as vcf:
        for line in vcf:
            if line.startswith("#"):
                header.append(line)
            else:
                try:
                    chrom = line.split("\t")[0]
                    if (chrom not in chroms):
                        chroms.append(chrom)
                    lines.append(line)
                except:
                    print "I can't handle non-standard vcf formats!"
    return (header, chroms, lines)

def extract_chrom(chrom, lines):
    chrom_lines = []
    for line in lines:
        if (chrom in line):
            chrom_lines.append(line)
    return chrom_lines

def main():
    infile = sys.argv[1]
    name = infile.split(".")[0]
    tup = load_file(infile)
    header = tup[0]
    chroms = tup[1]
    for chrom in chroms:
        chrom_lines = extract_chrom(chrom, tup[2])
        name = name + "." + chrom + ".vcf"
        write_outfile(name, header, chrom_lines)
main()
