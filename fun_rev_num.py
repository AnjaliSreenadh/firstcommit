def rev_num(n):
    rev=0
    while(n>0):
        rev=(rev*10)+(n%10)
        n//=10
    return rev
num=int(input("Enter the number: "))
print("Reverse of the given number is:",rev_num(num))


