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
    for line in file:
        table = line.split()
        print(table[0])
    file.close()
