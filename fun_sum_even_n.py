def sum_even(n):
    sum=0
    for i in range(n+1):
        if i% 2==0:
            sum+=i
    return sum
a=int(input("Enter the limit: "))
s=sum_even(a)
print("Sum is: ",s)

