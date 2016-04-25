# This is a project for genome-wide analysis of potential off-target issues in CRISPR/Cas9
# guided genome editing in Populus trichocarpa
#
#
#
# download genomic sequence as fasta file from phytozome
# The following two lines will be needed in every python script:
# from intermine.webservice import Service
# service = Service("http://localhost:8081/phytomine/service")
#
#
#
#
#
#
# extract all 20-nt seqs before a ngg in the whole genome and save as fasta format seqs
# extract from original seq
from Bio import SeqIO
from Bio.Seq import Seq
import re
# get sequences from file by fasta IO
for record in SeqIO.parse("/home/xiaodong/Documents/PtrTCPgenomicsim.fas", "fasta"):
    s = str(record.seq)
    pattern = re.compile('[ATGCatgc]{21}[Gg]{2}')
    patternRC = re.compile('[cC]{2}[ATGCatgc]{21}')
    items = pattern.finditer(s)
    for item in items:
        # write to file in fasta format
        file = open("/home/xiaodong/Documents//output3.fas", "a+")
        file.write('>')
        file.write(record.id)
        file.write('_')
        file.write(str(item.start()))
        file.write('...')
        file.write(str(item.end()))
        file.write('\n')
        file.write(item.group())
        file.write('\n')
    itemsRC = patternRC.finditer(s)
    for itemRC in itemsRC:
        hitRC = Seq(itemRC.group())
        # write to file in fasta format
        file = open("/home/xiaodong/Documents//output3.fas", "a+")
        file.write('>')
        file.write(record.id)
        file.write('_RC_')
        file.write(str(itemRC.end()))
        file.write('...')
        file.write(str(itemRC.start()))
        file.write('\n')
        file.write(str(hitRC.reverse_complement()))
        file.write('\n')

# extract from reverse-complemented seq


# save as fasta file


# merge to one fasta file


# run blast for each 20-nt seq


# output blast statistics


# downstream analysis
