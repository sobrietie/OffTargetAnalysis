import re
record = 'Chr1'
s = 'AAATATATTGACAGATGAGATTGAAAGGACAAGAAAGTATATGCCCTTTTGAGGTCACCTTCTTCAATCAAAGAGGCTCCTAGTTTCCTCTGTTCCCATGGAACCTAAGGGCCCAAATCATCATCAACTACAGGTGCCCTCTTTCTTGAATCCTCCACAAAAAGCAAGCATGCCAGAGAACAACATCAACAACCATAACAAGCAGCCT'
pattern = re.compile('[ATGC]{21}[Gg]{2}')
items = re.finditer(pattern, s)
for item in items:
    print('>')
    print(record)
    print(item.start())
    print('...')
    print(item.end())
    print(item.group())
    file = open("/home/xiaodong/Documents//output2.fas", "a+")
    file.write('>')
    file.write(record)
    file.write('_')
    file.write(str(item.start()))
    file.write('...')
    file.write(str(item.end()))
    file.write('\n')
    file.write(item.group())
    file.write('\n')
    file.close()
