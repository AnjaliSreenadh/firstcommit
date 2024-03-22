n=int(input("Enter the number: "))
print("The factors of the given number are: ")
for i in range(2,(n//2)+1):
    if n%i==0:
        print(i)
