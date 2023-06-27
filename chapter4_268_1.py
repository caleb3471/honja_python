list_q = [1,2,3,4,1,2,3,1,4,1,2,3]

list_1 = [i for i in list_q if i==1]
list_2 = [i for i in list_q if i==2]
list_3 = [i for i in list_q if i==3]
list_4 = [i for i in list_q if i==4]

dict_al = {
    1 : len(list_1),
    2 : len(list_2),
    4 : len(list_4)
}

print(dict_al)
