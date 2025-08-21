

'''
dictOne = {}
eightmers = []
ninemers = []
tenmers = []
elevenmers = []

'''
#firstProt = "MDPTGSQLDSDFSQQDTPCLIIEDSQPESQVLEDDSGSHFSMLSRHLPNLQTHKENPVLDVVSNPEQTAGEERGDGNSGFNEHLKENKVADPVDSSNLDTCGSISQVIEQLPQPNRTSSVLGMSVESAPAVEEEKGEELEQKEKEKEEDTSGNTTHSLGAEDTASSQLGFGVLELSQSQDVEENTVPYEVDKEQLQSVTTNSGYTRLSDVDANTAIKHEEQSNEDIPIAEQSSKDIPVTAQPSKDVHVVKEQNPPPARSEDMPFSPKASVAAMEAKEQLSAQELMESGLQIQKSPEPEVLSTQEDLFDQSNKTVSSDGCSTPSREEGGCSLASTPATTLHLLQLSGQRSLVQDSLSTNSSDLVAPSPDAFRSTPFIVPSSPTEQEGRQDKPMDTSVLSEEGGEPFQKKLQSGEPVELENPPLLPESTVSPQASTPISQSTPVFPPGSLPIPSQPQFSHDIFIPSPSLEEQSNDGKKDGDMHSSSLTVECSKTSEIEPKNSPEDLGLSLTGDSCKLMLSTSEYSQSPKMESLSSHRIDEDGENTQIEDTEPMSPVLNSKFVPAENDSILMNPAQDGEVQLSQNDDKTKGDDTDTRDDISILATGCKGREETVAEDVCIDLTCDSGSQAVPSPATRSEALSSVLDQEEAMEIKEHHPEEGSSGSEVEEIPETPCESQGEELKEENMESVPLHLSLTETQSQGLCLQKEMPKKECSEAMEVETSVISIDSPQKLAILDQELEHKEQEAWEEATSEDSSVVIVDVKEPSPRVDVSCEPLEGVEKCSDSQSWEDIAPEIEPCAENRLDTKEEKSVEYEGDLKSGTAETEPVEQDSSQPSLPLVRADDPLRLDQELQQPQTQEKTSNSLTEDSKMANAKQLSSDAEAQKLGKPSAHASQSFCESSSETPFHFTLPKEGDIIPPLTGATPPLIGHLKLEPKRHSTPIGISNYPESTIATSDVMSESMVETHDPILGSGKGDSGAAPDVDDKLCLRMKLVSPETEASEESLQFNLEKPATGERKNGSTAVAESVASPQKTMSVLSCICEARQENEARSEDPPTTPIRGNLLHFPSSQGEEEKEKLEGDHTIRQSQQPMKPISPVKDPVSPASQKMVIQGPSSPQGEAMVTDVLEDQKEGRSTNKENPSKALIERPSQNNIGIQTMECSLRVPETVSAATQTIKNVCEQGTSTVDQNFGKQDATVQTERGSGEKPVSAPGDDTESLHSQGEEEFDMPQPPHGHVLHRHMRTIREVRTLVTRVITDVYYVDGTEVERKVTEETEEPIVECQECETEVSPSQTGGSSGDLGDISSFSSKASSLHRTSSGTSLSAMHSSGSSGKGAGPLRGKTSGTEPADFALPSSRGGPGKLSPRKGVSQTGTPVCEEDGDAGLGIRQGGKAPVTPRGRGRRGRPPSRTTGTRETAVPGPLGIEDISPNLSPDDKSFSRVVPRVPDSTRRTDVGAGALRRSDSPEIPFQAAAGPSDGLDASSPGNSFVGLRVVAKWSSNGYFYSGKITRDVGAGKYKLLFDDGYECDVLGKDILLCDPIPLDTEVTALSEDEYFSAGVVKGHRKESGELYYSIEKEGQRKWYKRMAVILSLEQGNRLREQYGLGPYEAVTPLTKAADISLDNLVEGKRKRRSNVSSPATPTASSSSSTTPTRKITESPRASMGVLSGKRKLITSEEERSPAKRGRKSATVKPGAVGAGEFVSPCESGDNTGEPSALEEQRGPLPLNKTLFLGYAFLLTMATTSDKLASRSKLPDGPTGSSEEEEEFLEIPPFNKQYTESQLRAGAGYILEDFNEAQCNTAYQCLLIADQHCRTRKYFLCLASGIPCVSHVWVHDSCHANQLQNYRNYLLPAGYSLEEQRILDWQPRENPFQNLKVLLVSDQQQNFLELWSEILMTGGAASVKQHHSSAHNKDIALGVFDVVVTDPSCPASVLKCAEALQLPVVSQEWVIQCLIVGERIGFKQHPKYKHDYVSH"
#gh = ["protein1", "hjghjghg"]
'''
with open('test1.txt', 'r') as file:

    lines = file.readlines()
    for e, line in enumerate(lines):
        if line.startswith(">"):
            dictOne[lines[e].rstrip()] = lines[e + 1].rstrip()
            e += 1

    print(dictOne)
'''

def get_proteins():
    currentSeq = ""
    identifiers = []
    sequences = []
    with open('uniprot_human_proteome.fasta', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            if line.startswith('>'):
                count = 1
                identifiers.append(line.replace(">", ""))
            else:
                count = 0
            if count == 0:
                currentSeq = currentSeq + line
            if count == 1:
                sequences.append(currentSeq)
                currentSeq = ""
        sequences.append(currentSeq)
        del sequences[0]

    with open('table1.csv', 'w+') as out:
        for i in range(len(identifiers)):
            out.write(identifiers[i] + "\t" + sequences[i] + "\n")


def get_peptides(protein, count1, workdi):
    with open('table3.csv', 'a+') as table2:
        protein = protein.strip("\n")
        for i in range(len(protein)):

            preseq = protein[i - 10:i]
            postseq = protein[i + 1:i + 11]



            seq = protein[i:i+8]
            workdi += 1
            if i < 10:
                if len(seq) == 8:
                    table2.write(str(count1) + "\t" + seq + "\t"
                             + str(i) + "\t" + str(i + 7) + "\t" + " First10 " + "\t" + postseq + "\t" + str(8) + "\n")

            elif len(protein) - i < 10:
                if len(seq) == 8:
                    table2.write(str(count1) + "\t" + seq + "\t"
                                 + str(i) + "\t" + str(i + 7) + "\t" + preseq + "\t" + "Last10" + "\t" + str(8) + "\n")
                else:
                    continue
            else:
                if len(seq) == 8:
                    table2.write(str(count1) + "\t" + seq + "\t"
                                 + str(i) + "\t" + str(i + 7) + "\t" + preseq + "\t" + postseq + "\t" + str(8) + "\n")
                else:
                    continue


            seq = protein[i:i + 9]
            workdi += 1
            if i < 10:
                if len(seq) == 9:
                    table2.write(str(count1) + "\t" + seq + "\t"
                                 + str(i) + "\t" + str(i + 7) + "\t" + " First10 " + "\t" + postseq + "\t" + str(9) + "\n")

            elif len(protein) - i < 10:
                if len(seq) == 9:
                    table2.write(str(count1) + "\t" + seq + "\t"
                                 + str(i) + "\t" + str(i + 7) + "\t" + preseq + "\t" + "Last10" + "\t" + str(9) + "\n")
                else:
                    continue
            else:
                if len(seq) == 9:
                    table2.write(str(count1) + "\t" + seq + "\t"
                                 + str(i) + "\t" + str(i + 7) + "\t" + preseq + "\t" + postseq + "\t" + str(9) + "\n")
                else:
                    continue


            seq = protein[i:i + 10]
            workdi += 1
            if i < 10:
                if len(seq) == 10:
                    table2.write(str(count1) + "\t" + seq + "\t"
                                 + str(i) + "\t" + str(i + 7) + "\t" + " First10 " + "\t" + postseq + "\t" + str(10) + "\n")

            elif len(protein) - i < 10:
                if len(seq) == 10:
                    table2.write(str(count1) + "\t" + seq + "\t"
                                 + str(i) + "\t" + str(i + 7) + "\t" + preseq + "\t" + "Last10" + "\t" + str(10) + "\n")
                else:
                    continue
            else:
                if len(seq) == 10:
                    table2.write(str(count1) + "\t" + seq + "\t"
                                 + str(i) + "\t" + str(i + 7) + "\t" + preseq + "\t" + postseq + "\t" + str(10) + "\n")
                else:
                    continue



            seq = protein[i:i + 11]
            workdi += 1
            if i < 10:
                if len(seq) == 11:
                    table2.write(str(count1) + "\t" + seq + "\t"
                                 + str(i) + "\t" + str(i + 7) + "\t" + " First10 " + "\t" + postseq + "\t" + str(11) + "\n")

            elif len(protein) - i < 10:
                if len(seq) == 11:
                    table2.write(str(count1) + "\t" + seq + "\t"
                                 + str(i) + "\t" + str(i + 7) + "\t" + preseq + "\t" + "Last10" + "\t" + str(11) + "\n")
                else:
                    continue
            else:
                if len(seq) == 11:
                    table2.write(str(count1) + "\t" + seq + "\t"
                                 + str(i) + "\t" + str(i + 7) + "\t" + preseq + "\t" + postseq + "\t" + str(11) + "\n")
                else:
                    continue



def main():
    workdi = 0
    get_proteins()
    with open('table1.csv', 'r') as t1:
        x = 0
        for line in t1:
            x += 1
            # global protein_name
            # protein_name = line.split('\t')[0]
            get_peptides(line.split('\t')[1], x, workdi)


if __name__ == '__main__':
    main()


'''

 main_dict = {prot1 : {'eight': eightmers} , {'nine': ninemers} , {'ten': tenmers} , {'eleven': elevenmers}
for value in main_dict.values():
    eight={}
    eight[value]= seq[]
   '''





