n=int(input("Enter the number"))
n_s=str(n)
b_d=0
for i in n_s:
  j=int(i)
  if j>b_d:
    b_d=j
print("The biggest digit of the given number is: ",b_d)