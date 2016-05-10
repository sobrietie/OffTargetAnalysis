from Bio import SeqIO
from Bio.Seq import Seq
file = open("shortgenestartend.tsv", 'r')
for line in file:
    table = line.split()
    print(table[0])
    count = 0
    for target in SeqIO.parse("shorttarget.fas", "fasta"):
        targetid = str(target.id)
        if targetid.startswith(table[1]):
            targettable = targetid.split(sep='_')
            targetspan = targettable[-1].split(sep='...')
            span1 = int(targetspan[0])
            span2 = int(targetspan[1])
            if min(span1, span2) > int(table[2]) and max(span1, span2) < int(table[3]):
                count += 1
                print('targetspan')
                print(targetspan)
                print(table[2:])
                print(targetid)
                print(target.seq)
    print(count, "target(s) found")





