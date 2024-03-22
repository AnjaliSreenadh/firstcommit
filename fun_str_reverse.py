def str_rev(st):
    rev=''
    for i in st:
        rev=i+rev
    return rev
s=input("Enter the string: ")
r=str_rev(s)
print("The reverse of the string is: ",r)
