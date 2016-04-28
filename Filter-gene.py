""" This is a project for genome-wide analysis of
 potential off-target issues in CRISPR/Cas9
 guided genome editing
 This script is for filtering 20-nt seqs within annotated genes
"""
# extract all 20-nt seqs before a ngg in the whole genome and save as fasta format seqs
# extract from original seq
from Bio import SeqIO
from Bio.Seq import Seq
import re
