def freq_count(a):
    b=[]
    for i in range(n):
        if a[i] not in b:
            b.append(a[i])
    for i in range(len(b)):
        count = 0
        for j in range(n):
            if b[i] == a[j]:
                count += 1
        print("Count of", b[i], ":", count)

n=int(input("Enter the limit: " ))
l=[]
print("Enter the elements to the list")
for i in range(n):
   x=int(input())
   l.append(x)
c=freq_count(l)


