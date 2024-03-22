def sum_fact(n):
    s=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            s+=i
    return s
a=int(input("Enter the number: "))
s_f=sum_fact(a)
print("Sum of factors: ",s_f)
