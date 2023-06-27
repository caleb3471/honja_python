dna_list = input("염기서열을 입력하세요. > ")

#dna 종류 초기화 
dna_a=dna_t=dna_g=dna_c = 0
not_input = 0


for dna in dna_list:
    if dna == 'a':
        dna_a += 1
    elif dna == "t":
        dna_t += 1
    elif dna == "g":
        dna_g += 1
    elif dna == "c":
       dna_c += 1 
    else:
        not_input += 1

print("a의 개수 : ", dna_a )
print("t의 개수 : ", dna_t )
print("g의 개수 : ", dna_g )
print("c의 개수 : ", dna_c )
