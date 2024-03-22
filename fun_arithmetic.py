def sum(a,b):
    print(a+b)
def diff(a,b):
    return a-b
def prod(a,b):
    return a*b
def quot(a,b):
    return a//b
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
#print("sum is",sum(x,y))
sum(x,y)
print("Difference is: ",diff(x,y))
print("Product is: ",prod(x,y))
print("Quotient is: ",quot(x,y))

