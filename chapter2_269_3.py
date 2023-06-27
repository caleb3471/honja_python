
while(True):
    dna_list = input("염기 서열을 입력해주세요. > ")
    
    codonlist = []
    
    
    for i in range(0, len(dna_list)//3):
        print(len(dna_list))
        for j in range(0,3):
            codon_name=""
            codon_name += dna_list[0]
            dna_list = dna_list[1:]
            print(codon_name)
            
    """codonlist.append(codon_name)        
    print(codonlist[i])        
    """

