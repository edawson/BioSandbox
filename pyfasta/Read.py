

class Read():
    """
    Read: represents a single sequencing read, long or short,
    contains some metadata such as quality and identifiers,
    and of course the DNA sequence.
    """
    def __init__(self, sequence, qual_scores, identifier, comment_line):

        self.seq = sequence
        self.quals = qual_scores
        self.ident = identifier
        self.comment = comment_line
        self.length = len(self.seq)

    def kmerize(self, k=None):
        if k is None:
            k = self.length
        for i in xrange(0, self.length - k + 1):
            yield self.seq[i:i+k]


