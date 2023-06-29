
list_sh = [1,2,[3,4], 5,[6,7], [8,9]]

print(list_sh[2][1])

new_list=[]
for i in range(0,len(list_sh)):
    if type(list_sh[i]) == int:
        new_list.append(list_sh[i])
    else:
        for j in range(0,len(list_sh[i])):
            new_list.append(list_sh[i][j])
            

print(new_list)
    