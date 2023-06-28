

dna_list = input("염기 서열을 입력해주세요. > ")

    
codonlist = []
codon_dict = {}
    
#전체 갯수를 3으로 나누어 실행    
for i in range(0, len(dna_list)//3):
    codon_name=""
    #3개씩 끊어서 저장 해야 하기 때문에 3번 수행 
    #첫번째 글자를 codon_name에 추가하고 첫번째 글자를 제외하고 리스트를 초기화
    for j in range(0,3):
        
        codon_name += dna_list[0]
        dna_list = dna_list[1:]
    
    #한세트를 완성했으면 리스트에 추가
    codonlist.append(codon_name)        

    #딕셔너리에 해당 염기서열이 존재하는지 확인하고 존재한다면 현재값의 +1 없다면 새로 생성하고 1을 할당
    
    if codon_name not in codon_dict:
        codon_dict[codon_name] = 1
    else:
        codon_dict[codon_name] = codon_dict.get(codon_name) +1
        

print(codon_dict)


