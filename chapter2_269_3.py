

dna_list = input("염기 서열을 입력해주세요. > ")
    
codonlist = []
codon_dict = {}
    
    
for i in range(0, len(dna_list)//3):
    codon_name=""
    for j in range(0,3):
        
        codon_name += dna_list[0]
        dna_list = dna_list[1:]
   
    codonlist.append(codon_name)        

    if codon_name not in codon_dict:
        codon_dict[codon_name] = 1
    else:
        codon_dict[codon_name] = codon_dict.get(codon_name) +1
        


print(codon_dict)


