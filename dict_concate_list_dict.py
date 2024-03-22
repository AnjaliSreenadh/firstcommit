n1=int(input("Enter the limit of the lists: "))
print("Enter the elements to the first list")
l1=[]
l2=[]
for i in range(n1):
      x=input()
      l1.append(x)

print("Enter the elements to the second list")

for i in range(n1):
    x=input()
    l2.append(x)
d=zip(l1,l2)
print(dict(d))
