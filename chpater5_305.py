



def flatten(n_list):
    output=[]
    for item in n_list:
        if type(item) == list:
            output += flatten(item)
        else:
            output.append(item)
    
    return output


test_list= [1,2,[1,2,[1,2],1,2,3,4,]] 
print(flatten(test_list))
             