def quadratic(x,y,z):
    d=(y**2)-(4*x*z)**(0.5)
    if d>=0:
        print("The roots are real")
    else:
        print("The root is imaginary")
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
quadratic(a,b,c)