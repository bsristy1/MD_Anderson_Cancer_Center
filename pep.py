
with open('list_peptides.txt', 'r') as f:
    lines = f.readlines()
    count = 1
    with open('table3.csv', 'a+') as g:
        for line in lines:

            g.write(">peptide {}".format(count))
            g.write(line)
            count += 1




