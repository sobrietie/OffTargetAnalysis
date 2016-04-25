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
import re
for record in SeqIO.parse("/home/xiaodong/Documents/PtrTCPgenomicsim.fas","fasta"):
    s = str(record.seq)
    id = record.id
    pattern = re.compile('[ATGCatgc]{21}[Gg]{2}')
    patternRC = re.compile('[cc]{2}[ATGCatgc]{21}')
    items = pattern.finditer(s)
    for item in items:
        print('>')
        print(id)
        print(item.start())
        print('...')
        print(item.end())
        print(item.group())
    itemsRC = patternRC.finditer(s)
    for i in itemsRC:
        print('>')
        print(id)
        print('RC')
        print(item.start())
        print('...')
        print(item.end())
        print(item.group())



    # save as fasta file

# extract from reverse-complemented seq


# save as fasta file


# merge to one fasta file


# run blast for each 20-nt seq


# output blast statistics


# downstream analysis
