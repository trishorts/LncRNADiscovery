import sys
import io
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

with open(sys.argv[2], "w") as outff:
    with open(sys.argv[1]) as ff:
        print(f"Reading {sys.argv[1]}")
        for line in ff:
            lins = line.split("\t")
            if line.startswith("#"): continue
            elif lins[8].startswith("ID=gene:"): lins[2] = "gene"
            outff.write("\t".join(lins))
