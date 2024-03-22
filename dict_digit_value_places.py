n=int(input("Enter the number: "))
#n=1223
d={}
d[n%10]='Ones'
n//=10
d[n%10]='Tens'
n//=10
d[n%10]='Hundreds'
n//=10
d[n]='Thousands'
print(d)





