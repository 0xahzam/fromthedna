import utils  # Importing the custom written operations library
from dna_features_viewer import GraphicFeature, GraphicRecord

# DNA of HIV-1
dna = """"
1 ggtctctctg gttagaccag atctgagcct gggagctctc tggctaacta gggaacccac
61 tgcttaagcc tcaataaagc ttgccttgag tgcttcaagt agtgtgtgcc cgtctgttgt
121 gtgactctgg taactagaga tccctcagac ccttttagtc agtgtggaaa atctctagca
181 gtggcgcccg aacagggacc tgaaagcgaa agggaaacca gaggagctct ctcgacgcag
241 gactcggctt gctgaagcgc gcacggcaag aggcgagggg cggcgactgg tgagtacgcc
301 aaaaattttg actagcggag gctagaagga gagagatggg tgcgagagcg tcagtattaa
361 gcgggggaga attagatcga tgggaaaaaa ttcggttaag gccaggggga aagaaaaaat
421 ataaattaaa acatatagta tgggcaagca gggagctaga acgattcgca gttaatcctg
481 gcctgttaga aacatcagaa ggctgtagac aaatactggg acagctacaa ccatcccttc
541 agacaggatc agaagaactt agatcattat ataatacagt agcaaccctc tattgtgtgc
601 atcaaaggat agagataaaa gacaccaagg aagctttaga caagatagag gaagagcaaa
661 acaaaagtaa gaaaaaagca cagcaagcag cagctgacac aggacacagc aatcaggtca
721 gccaaaatta ccctatagtg cagaacatcc aggggcaaat ggtacatcag gccatatcac
781 ctagaacttt aaatgcatgg gtaaaagtag tagaagagaa ggctttcagc ccagaagtga
841 tacccatgtt ttcagcatta tcagaaggag ccaccccaca agatttaaac accatgctaa
901 acacagtggg gggacatcaa gcagccatgc aaatgttaaa agagaccatc aatgaggaag
961 ctgcagaatg ggatagagtg catccagtgc atgcagggcc tattgcacca ggccagatga
1021 gagaaccaag gggaagtgac atagcaggaa ctactagtac ccttcaggaa caaataggat
1081 ggatgacaaa taatccacct atcccagtag gagaaattta taaaagatgg ataatcctgg
1141 gattaaataa aatagtaaga atgtatagcc ctaccagcat tctggacata agacaaggac
1201 caaaggaacc ctttagagac tatgtagacc ggttctataa aactctaaga gccgagcaag
1261 cttcacagga ggtaaaaaat tggatgacag aaaccttgtt ggtccaaaat gcgaacccag
1321 attgtaagac tattttaaaa gcattgggac cagcggctac actagaagaa atgatgacag
1381 catgtcaggg agtaggagga cccggccata aggcaagagt tttggctgaa gcaatgagcc
1441 aagtaacaaa ttcagctacc ataatgatgc agagaggcaa ttttaggaac caaagaaaga
1501 ttgttaagtg tttcaattgt ggcaaagaag ggcacacagc cagaaattgc agggccccta
1561 ggaaaaaggg ctgttggaaa tgtggaaagg aaggacacca aatgaaagat tgtactgaga
1621 gacaggctaa ttttttaggg aagatctggc cttcctacaa gggaaggcca gggaattttc
1681 ttcagagcag accagagcca acagccccac cagaagagag cttcaggtct ggggtagaga
1741 caacaactcc ccctcagaag caggagccga tagacaagga actgtatcct ttaacttccc
1801 tcaggtcact ctttggcaac gacccctcgt cacaataaag ataggggggc aactaaagga
1861 agctctatta gatacaggag cagatgatac agtattagaa gaaatgagtt tgccaggaag
1921 atggaaacca aaaatgatag ggggaattgg aggttttatc aaagtaagac agtatgatca
1981 gatactcata gaaatctgtg gacataaagc tataggtaca gtattagtag gacctacacc
2041 tgtcaacata attggaagaa atctgttgac tcagattggt tgcactttaa attttcccat
2101 tagccctatt gagactgtac cagtaaaatt aaagccagga atggatggcc caaaagttaa
2161 acaatggcca ttgacagaag aaaaaataaa agcattagta gaaatttgta cagagatgga
2221 aaaggaaggg aaaatttcaa aaattgggcc tgaaaatcca tacaatactc cagtatttgc
2281 cataaagaaa aaagacagta ctaaatggag aaaattagta gatttcagag aacttaataa
2341 gagaactcaa gacttctggg aagttcaatt aggaatacca catcccgcag ggttaaaaaa
2401 gaaaaaatca gtaacagtac tggatgtggg tgatgcatat ttttcagttc ccttagatga
2461 agacttcagg aagtatactg catttaccat acctagtata aacaatgaga caccagggat
2521 tagatatcag tacaatgtgc ttccacaggg atggaaagga tcaccagcaa tattccaaag
2581 tagcatgaca aaaatcttag agccttttag aaaacaaaat ccagacatag ttatctatca
2641 atacatggat gatttgtatg taggatctga cttagaaata gggcagcata gaacaaaaat
2701 agaggagctg agacaacatc tgttgaggtg gggacttacc acaccagaca aaaaacatca
2761 gaaagaacct ccattccttt ggatgggtta tgaactccat cctgataaat ggacagtaca
2821 gcctatagtg ctgccagaaa aagacagctg gactgtcaat gacatacaga agttagtggg
2881 gaaattgaat tgggcaagtc agatttaccc agggattaaa gtaaggcaat tatgtaaact
2941 ccttagagga accaaagcac taacagaagt aataccacta acagaagaag cagagctaga
3001 actggcagaa aacagagaga ttctaaaaga accagtacat ggagtgtatt atgacccatc
3061 aaaagactta atagcagaaa tacagaagca ggggcaaggc caatggacat atcaaattta
3121 tcaagagcca tttaaaaatc tgaaaacagg aaaatatgca agaatgaggg gtgcccacac
3181 taatgatgta aaacaattaa cagaggcagt gcaaaaaata accacagaaa gcatagtaat
3241 atggggaaag actcctaaat ttaaactgcc catacaaaag gaaacatggg aaacatggtg
3301 gacagagtat tggcaagcca cctggattcc tgagtgggag tttgttaata cccctccctt
3361 agtgaaatta tggtaccagt tagagaaaga acccatagta ggagcagaaa ccttctatgt
3421 agatggggca gctaacaggg agactaaatt aggaaaagca ggatatgtta ctaatagagg
3481 aagacaaaaa gttgtcaccc taactgacac aacaaatcag aagactgagt tacaagcaat
3541 ttatctagct ttgcaggatt cgggattaga agtaaacata gtaacagact cacaatatgc
3601 attaggaatc attcaagcac aaccagatca aagtgaatca gagttagtca atcaaataat
3661 agagcagtta ataaaaaagg aaaaggtcta tctggcatgg gtaccagcac acaaaggaat
3721 tggaggaaat gaacaagtag ataaattagt cagtgctgga atcaggaaag tactattttt
3781 agatggaata gataaggccc aagatgaaca tgagaaatat cacagtaatt ggagagcaat
3841 ggctagtgat tttaacctgc cacctgtagt agcaaaagaa atagtagcca gctgtgataa
3901 atgtcagcta aaaggagaag ccatgcatgg acaagtagac tgtagtccag gaatatggca
3961 actagattgt acacatttag aaggaaaagt tatcctggta gcagttcatg tagccagtgg
4021 atatatagaa gcagaagtta ttccagcaga aacagggcag gaaacagcat attttctttt
4081 aaaattagca ggaagatggc cagtaaaaac aatacatact gacaatggca gcaatttcac
4141 cggtgctacg gttagggccg cctgttggtg ggcgggaatc aagcaggaat ttggaattcc
4201 ctacaatccc caaagtcaag gagtagtaga atctatgaat aaagaattaa agaaaattat
4261 aggacaggta agagatcagg ctgaacatct taagacagca gtacaaatgg cagtattcat
4321 ccacaatttt aaaagaaaag gggggattgg ggggtacagt gcaggggaaa gaatagtaga
4381 cataatagca acagacatac aaactaaaga attacaaaaa caaattacaa aaattcaaaa
4441 ttttcgggtt tattacaggg acagcagaaa tccactttgg aaaggaccag caaagctcct
4501 ctggaaaggt gaaggggcag tagtaataca agataatagt gacataaaag tagtgccaag
4561 aagaaaagca aagatcatta gggattatgg aaaacagatg gcaggtgatg attgtgtggc
4621 aagtagacag gatgaggatt agaacatgga aaagtttagt aaaacaccat atgtatgttt
4681 cagggaaagc taggggatgg ttttatagac atcactatga aagccctcat ccaagaataa
4741 gttcagaagt acacatccca ctaggggatg ctagattggt aataacaaca tattggggtc
4801 tgcatacagg agaaagagac tggcatttgg gtcagggagt ctccatagaa tggaggaaaa
4861 agagatatag cacacaagta gaccctgaac tagcagacca actaattcat ctgtattact
4921 ttgactgttt ttcagactct gctataagaa aggccttatt aggacacata gttagcccta
4981 ggtgtgaata tcaagcagga cataacaagg taggatctct acaatacttg gcactagcag
5041 cattaataac accaaaaaag ataaagccac ctttgcctag tgttacgaaa ctgacagagg
5101 atagatggaa caagccccag aagaccaagg gccacagagg gagccacaca atgaatggac
5161 actagagctt ttagaggagc ttaagaatga agctgttaga cattttccta ggatttggct
5221 ccatggctta gggcaacata tctatgaaac ttatggggat acttgggcag gagtggaagc
5281 cataataaga attctgcaac aactgctgtt tatccatttt cagaattggg tgtcgacata
5341 gcagaatagg cgttactcga cagaggagag caagaaatgg agccagtaga tcctagacta
5401 gagccctgga agcatccagg aagtcagcct aaaactgctt gtaccaattg ctattgtaaa
5461 aagtgttgct ttcattgcca agtttgtttc ataacaaaag ccttaggcat ctcctatggc
5521 aggaagaagc ggagacagcg acgaagagct catcagaaca gtcagactca tcaagcttct
5581 ctatcaaagc agtaagtagt acatgtaatg caacctatac caatagtagc aatagtagca
5641 ttagtagtag caataataat agcaatagtt gtgtggtcca tagtaatcat agaatatagg
5701 aaaatattaa gacaaagaaa aatagacagg ttaattgata gactaataga aagagcagaa
5761 gacagtggca atgagagtga aggagaaata tcagcacttg tggagatggg ggtggagatg
5821 gggcaccatg ctccttggga tgttgatgat ctgtagtgct acagaaaaat tgtgggtcac
5881 agtctattat ggggtacctg tgtggaagga agcaaccacc actctatttt gtgcatcaga
5941 tgctaaagca tatgatacag aggtacataa tgtttgggcc acacatgcct gtgtacccac
6001 agaccccaac ccacaagaag tagtattggt aaatgtgaca gaaaatttta acatgtggaa
6061 aaatgacatg gtagaacaga tgcatgagga tataatcagt ttatgggatc aaagcctaaa
6121 gccatgtgta aaattaaccc cactctgtgt tagtttaaag tgcactgatt tgaagaatga
6181 tactaatacc aatagtagta gcgggagaat gataatggag aaaggagaga taaaaaactg
6241 ctctttcaat atcagcacaa gcataagagg taaggtgcag aaagaatatg cattttttta
6301 taaacttgat ataataccaa tagataatga tactaccagc tataagttga caagttgtaa
6361 cacctcagtc attacacagg cctgtccaaa ggtatccttt gagccaattc ccatacatta
6421 ttgtgccccg gctggttttg cgattctaaa atgtaataat aagacgttca atggaacagg
6481 accatgtaca aatgtcagca cagtacaatg tacacatgga attaggccag tagtatcaac
6541 tcaactgctg ttaaatggca gtctagcaga agaagaggta gtaattagat ctgtcaattt
6601 cacggacaat gctaaaacca taatagtaca gctgaacaca tctgtagaaa ttaattgtac
6661 aagacccaac aacaatacaa gaaaaagaat ccgtatccag agaggaccag ggagagcatt
6721 tgttacaata ggaaaaatag gaaatatgag acaagcacat tgtaacatta gtagagcaaa
6781 atggaataac actttaaaac agatagctag caaattaaga gaacaatttg gaaataataa
6841 aacaataatc tttaagcaat cctcaggagg ggacccagaa attgtaacgc acagttttaa
6901 ttgtggaggg gaatttttct actgtaattc aacacaactg tttaatagta cttggtttaa
6961 tagtacttgg agtactgaag ggtcaaataa cactgaagga agtgacacaa tcaccctccc
7021 atgcagaata aaacaaatta taaacatgtg gcagaaagta ggaaaagcaa tgtatgcccc
7081 tcccatcagt ggacaaatta gatgttcatc aaatattaca gggctgctat taacaagaga
7141 tggtggtaat agcaacaatg agtccgagat cttcagacct ggaggaggag atatgaggga
7201 caattggaga agtgaattat ataaatataa agtagtaaaa attgaaccat taggagtagc
7261 acccaccaag gcaaagagaa gagtggtgca gagagaaaaa agagcagtgg gaataggagc
7321 tttgttcctt gggttcttgg gagcagcagg aagcactatg ggcgcagcct caatgacgct
7381 gacggtacag gccagacaat tattgtctgg tatagtgcag cagcagaaca atttgctgag
7441 ggctattgag gcgcaacagc atctgttgca actcacagtc tggggcatca agcagctcca
7501 ggcaagaatc ctggctgtgg aaagatacct aaaggatcaa cagctcctgg ggatttgggg
7561 ttgctctgga aaactcattt gcaccactgc tgtgccttgg aatgctagtt ggagtaataa
7621 atctctggaa cagatttgga atcacacgac ctggatggag tgggacagag aaattaacaa
7681 ttacacaagc ttaatacact ccttaattga agaatcgcaa aaccagcaag aaaagaatga
7741 acaagaatta ttggaattag ataaatgggc aagtttgtgg aattggttta acataacaaa
7801 ttggctgtgg tatataaaat tattcataat gatagtagga ggcttggtag gtttaagaat
7861 agtttttgct gtactttcta tagtgaatag agttaggcag ggatattcac cattatcgtt
7921 tcagacccac ctcccaaccc cgaggggacc cgacaggccc gaaggaatag aagaagaagg
7981 tggagagaga gacagagaca gatccattcg attagtgaac ggatccttgg cacttatctg
8041 ggacgatctg cggagcctgt gcctcttcag ctaccaccgc ttgagagact tactcttgat
8101 tgtaacgagg attgtggaac ttctgggacg cagggggtgg gaagccctca aatattggtg
8161 gaatctccta cagtattgga gtcaggaact aaagaatagt gctgttagct tgctcaatgc
8221 cacagccata gcagtagctg aggggacaga tagggttata gaagtagtac aaggagcttg
8281 tagagctatt cgccacatac ctagaagaat aagacagggc ttggaaagga ttttgctata
8341 agatgggtgg caagtggtca aaaagtagtg tgattggatg gcctactgta agggaaagaa
8401 tgagacgagc tgagccagca gcagataggg tgggagcagc atctcgagac ctggaaaaac
8461 atggagcaat cacaagtagc aatacagcag ctaccaatgc tgcttgtgcc tggctagaag
8521 cacaagagga ggaggaggtg ggttttccag tcacacctca ggtaccttta agaccaatga
8581 cttacaaggc agctgtagat cttagccact ttttaaaaga aaagggggga ctggaagggc
8641 taattcactc ccaaagaaga caagatatcc ttgatctgtg gatctaccac acacaaggct
8701 acttccctga ttagcagaac tacacaccag ggccaggggt cagatatcca ctgacctttg
8761 gatggtgcta caagctagta ccagttgagc cagataagat agaagaggcc aataaaggag
8821 agaacaccag cttgttacac cctgtgagcc tgcatgggat ggatgacccg gagagagaag
8881 tgttagagtg gaggtttgac agccgcctag catttcatca cgtggcccga gagctgcatc
8941 cggagtactt caagaactgc tgacatcgag cttgctacaa gggactttcc gctggggact
9001 ttccagggag gcgtggcctg ggcgggactg gggagtggcg agccctcaga tcctgcatat
9061 aagcagctgc tttttgcctg tactgggtct ctctggttag accagatctg agcctgggag
9121 ctctctggct aactagggaa cccactgctt aagcctcaat aaagcttgcc ttgagtgctt
9181 c"""

# Manipulating DNA string for better usability
cc = ""

for i in dna:
    if i.isalpha():
        cc += i

dna = cc.upper()

# DNA to mRNA
rna = utils.transcription(dna)

# Initialising first, second and third (forward & reverse) ORF's for both DNA & RNA
# DNA ORFs (Open Reading Frames)

dna_orf_1 = utils.orf(dna, "first", "forward")
dna_orf_2 = utils.orf(dna, "second", "forward")
dna_orf_3 = utils.orf(dna, "third", "forward")
neg_dna_orf_1 = utils.orf(dna, "first", "reverse")
neg_dna_orf_2 = utils.orf(dna, "second", "reverse")
neg_dna_orf_3 = utils.orf(dna, "third", "reverse")

# RNA ORFs (Open Reading Frames)
rna_orf_1 = utils.orf(rna, "first", "forward")
rna_orf_2 = utils.orf(rna, "second", "forward")
rna_orf_3 = utils.orf(rna, "third", "forward")
neg_rna_orf_1 = utils.orf(rna, "first", "reverse")
neg_rna_orf_2 = utils.orf(rna, "second", "reverse")
neg_rna_orf_3 = utils.orf(rna, "third", "reverse")

# Translation : DNA/mRNA → Protein (for each ORF)
dna_protein_orf_1 = utils.dna_translation(dna_orf_1)
dna_protein_orf_2 = utils.dna_translation(dna_orf_2)
dna_protein_orf_3 = utils.dna_translation(dna_orf_3)
neg_dna_protein_orf_1 = utils.dna_translation(neg_dna_orf_1)
neg_dna_protein_orf_2 = utils.dna_translation(neg_dna_orf_2)
neg_dna_protein_orf_3 = utils.dna_translation(neg_dna_orf_3)

rna_protein_orf_1 = utils.rna_translation(rna_orf_1)
rna_protein_orf_2 = utils.rna_translation(rna_orf_2)
rna_protein_orf_3 = utils.rna_translation(rna_orf_3)
neg_rna_protein_orf_1 = utils.rna_translation(neg_rna_orf_1)
neg_rna_protein_orf_2 = utils.rna_translation(neg_rna_orf_2)
neg_rna_protein_orf_3 = utils.rna_translation(neg_rna_orf_3)


# Saving proteins into FASTA file
# Perform Basic Local Alignment using NCBI-BLAST for specific protein details
# Upload proteins.fasta to https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE=Proteins
with open('proteins.fasta', 'w') as file:
    file.write('>Protein (DNA ORF1 Forward)  \n' + dna_protein_orf_1 + '\n')
    file.write('>Protein (DNA ORF2 Forward) \n' + dna_protein_orf_2 + '\n')
    file.write('>Protein (DNA ORF3 Forward) \n' + dna_protein_orf_3 + '\n')
    file.write('\n')
    file.write('>Protein (DNA ORF1 Reverse) \n' + neg_dna_protein_orf_1 + '\n')
    file.write('>Protein (DNA ORF2 Reverse) \n' + neg_dna_protein_orf_2 + '\n')
    file.write('>Protein (DNA ORF3 Reverse) \n' + neg_dna_protein_orf_3 + '\n')
    file.write('\n')
    file.write('>Protein (RNA ORF1 Forward)  \n' + rna_protein_orf_1 + '\n')
    file.write('>Protein (RNA ORF2 Forward) \n' + rna_protein_orf_2 + '\n')
    file.write('>Protein (RNA ORF3 Forward) \n' + rna_protein_orf_3 + '\n')
    file.write('\n')
    file.write('>Protein (RNA ORF1 Reverse) \n' + neg_rna_protein_orf_1 + '\n')
    file.write('>Protein (RNA ORF2 Reverse) \n' + neg_rna_protein_orf_2 + '\n')
    file.write('>Protein (RNA ORF3 Reverse) \n' + neg_rna_protein_orf_3 + '\n')
    
# visualising DNA
record = GraphicRecord(sequence=dna, features=[
    GraphicFeature(start=5, end=10, strand=+1, color='#ffcccc'),
    GraphicFeature(start=8, end=15, strand=+1, color='#ccccff')
])

ax, _ = record.plot(figure_width=20)
record.plot_sequence(ax)
record.plot_translation(ax, (8, 23), fontdict={'weight': 'bold'})
ax.figure.savefig('sequence.png', bbox_inches='tight')


# LOGS
# print("DNA =>", dna)
# print("RNA =>", rna)
# print("GC Content =>", utils.gc_content(dna), "%")
# print("\n")
# print("DNA (ORF1 Forward) =>", dna_orf_1)
# print("RNA (ORF1 Forward) =>", rna_orf_1)
# print("\n")
# print("PROTEIN (DNA ORF1 Forward) =>", dna_protein_orf_1)
# print("PROTEIN (RNA ORF1 Forward) =>", rna_protein_orf_1)
# print("\n")
# print("PROTEIN STRAND (DNA ORF1 Forward) =>",
#       utils.translation_shortform(dna_protein_orf_1))
# print("PROTEIN STRAND (RNA ORF1 Forward) =>",
#       utils.translation_shortform(rna_protein_orf_1))
# print("\n")
# print("PROTEIN STRAND FULLFORM (DNA ORF1 Forward) =>")
# print(utils.translation_fullform(utils.translation_shortform(dna_protein_orf_1)))
# print("\n")
# print("PROTEIN STRAND FULLFORM (RNA ORF1 Forward) =>")
# print(utils.translation_fullform(utils.translation_shortform(rna_protein_orf_1)))
