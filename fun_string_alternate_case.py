def string_alter_case(st,l):
    for i in range(l):
        if i%2==0:
            print(a[i].upper(), end="")
        else:
            print(a[i].lower(), end="")
a=str(input("Enter the string: "))
l=len(a)
string_alter_case(a,l)

