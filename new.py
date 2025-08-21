with open('A_allele_predictions.txt', 'r') as f:
    x = f.readlines()
    with open('all_allele_predictions.txt', 'a+') as g:
        for line in x:
            g.write(line)


with open('B_allele_predictions.txt', 'a+') as h:
    y = h.readlines()
    with open('all_allele_predictions.txt', 'a+') as a:
        for l in y:
            a.write(line)

with open('C_allele_predictions.txt', 'a+') as i:
    y = i.readlines()
    with open('all_allele_predictions.txt', 'a+') as b:
        for ine in y:
            b.write(line)




