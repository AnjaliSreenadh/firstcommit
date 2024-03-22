def sum_rec(n):
    if n<10:
        return n
    else:
        return n%10+sum_rec(n//10)
num=int(input("Enter the number: "))
print("Sum of digits of the given number: ",sum_rec(num))






