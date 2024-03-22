def str_count_case(st):
    l_c=0
    u_c=0
    for i in st:
        if i>='a'and i<='z':
            l_c+=1
        if i>='A' and i<='Z':
            u_c+=1
    return l_c,u_c
s=(input("Enter the string: "))
x,y=str_count_case(s)
print("Number of lower case characters in the given string: ", x)
print("Number of uppercase characters in te given string: ", y)
