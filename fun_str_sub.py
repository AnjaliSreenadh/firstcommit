def str_sub(st,sub_st):
    if sub_st in st:
        return 1
    else:
        return 0
s=input("Enter the string: ")
s_s=input("Enter the substring: ")
x=str_sub(s,s_s)
if x:
    print("Substring found in main string")
else:
    print("Substring not found n main string")
