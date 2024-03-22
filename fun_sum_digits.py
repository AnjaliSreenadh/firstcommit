def sum_digits(n):
    sum=0
    while(n>0):
        sum=sum+(n%10)
        n//=10
    return sum
num=int(input("Enter the number: "))

s=sum_digits(num)
print("Sum of digits of the given number : ",s)