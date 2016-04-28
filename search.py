""" This is a project for genome-wide analysis of
 potential off-target issues in CRISPR/Cas9
 guided genome editing
 This script is for searching 20-nt seqs from a input genome
"""
# extract all 20-nt seqs before a ngg in the whole genome and save as fasta format seqs
# extract from original seq
from Bio import SeqIO
from Bio.Seq import Seq
import re
import sys
if len(sys.argv) < 2:
    print('No input file specified.')
    sys.exit()
if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
# fetch sys.argv[1] but without the first two characters
    if option == 'version':  # 当命令行参数为-- version，显示版本号
        print('Version 0.1')
    elif option == 'help':  # 当命令行参数为--help时，显示相关帮助内容
        print("""
        This program identifies all 23-nt Cas9 target
        sequences in the specified DNA sequence(s).
        A fasta format input is required.
        The output will be stored in targets_all.fas.
        Options include:
        --version : Prints the version number
        --help : Display this help""")
    else:
        print('Unknown option.')
    sys.exit()
# get sequences from file by fasta IO
for record in SeqIO.parse(sys.argv[1], "fasta"):
    # find 20+ngg motif in each sequence
    s = str(record.seq)
    # search in the + strand
    pattern = re.compile('[ATGCatgc]{21}[Gg]{2}')
    # search in the - strand
    patternRC = re.compile('[cC]{2}[ATGCatgc]{21}')
    items = pattern.finditer(s)
    for item in items:
        # write hits from the + strand to file in fasta format
        file = open("targets_all.fas", "a+")
        file.write('>')
        file.write(record.id)
        file.write('_')
        file.write(str(item.start()+1))  # to make it non-coder style
        file.write('...')
        file.write(str(item.end()+1))  # to make it non-coder
        file.write('\n')
        file.write(item.group())
        file.write('\n')
        file.close()
    itemsRC = patternRC.finditer(s)
    for itemRC in itemsRC:
        hitRC = Seq(itemRC.group())
        # write hits from the - strand to file in fasta format
        file = open("targets_all.fas", "a+")
        file.write('>')
        file.write(record.id)
        file.write('_RC_')
        file.write(str(itemRC.end()+1))  # to make it non-coder style
        file.write('...')
        file.write(str(itemRC.start()+1))  # to make it non-coder style
        file.write('\n')
        file.write(str(hitRC.reverse_complement()))
        file.write('\n')
        file.close()
