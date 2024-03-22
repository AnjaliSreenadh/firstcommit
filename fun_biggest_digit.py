def big_dig(n):
    big=0
    while(n>0):
        d=n%10
        n//=10
        if big<d:
            big=d
    return big
num=int(input("Enter the number: "))
b=big_dig(num)
print("The biggest digit of the given number: ",b)


