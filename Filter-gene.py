""" This is a project for genome-wide analysis of
 potential off-target issues in CRISPR/Cas9
 guided genome editing
 This script is for filtering 20-nt seqs within annotated genes
"""
import sys
if len(sys.argv) < 2:
    print("No input file specified.")
    sys.exit()
if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    # fetch sys.argv[1] but without the first two characters
    if option == 'version':  # 当命令行参数为-- version，显示版本号
        print('Version 0.1')
    elif option == 'help':  # 当命令行参数为--help时，显示相关帮助内容
        print("""
        This program filters Cas9 target seqs
        that locate within an annotated genes
        from the file targets_all.fas
        an input file listing gene, chromosome, gene start
        and gene end is required.
        Please refer to the sample for details.
        The output will include:
        Target seqs stored in targets_filtered.fas;
        A list of target seqs within annotated genes stored
        in list_filtered
        Options include:
        --version : Prints the version number
        --help : Display this help""")
    else:
        print('Unknown option.')
        sys.exit()
else:
    file = open(sys.argv[1], 'r')
    # seq_out = open("tragets_filtered.fas", "+a")
    for line in file:
        table = line.split()
        list_out = open("list_filtered", "+a")
        list_out.write(table[0])
        list_out.write('\n')
        count = 0
        file1 = open("list_all", 'r')
        for line1 in file1:
            targetid = str(line1)
            if targetid.startswith('>'+table[1]):
                targettable = targetid.split(sep='-')
                targetspan = targettable[-1].split(sep='...')
                span1 = int(targetspan[0])
                span2 = int(targetspan[1])
                if min(span1, span2) > int(table[2]) and max(span1, span2) < int(table[3]):
                    count += 1
                    list_out.write(targetid)
        list_out.write(str(count))
        list_out.write('target(s) found\n')
        list_out.close()
    file1.close()
file.close()

