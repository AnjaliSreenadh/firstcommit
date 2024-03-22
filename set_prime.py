s1={10,13,15,23,16,6,41,30,11,22,53,20,29}
s_l=list(s1)
print("The set is: ,s1")
print("Prime numbers in the set are")
for i in range(len(s_l)):
    for j in range(2,(s_l[i]-1)):
        if s_l[i]%j==0:
            break
    else:
        print(s_l[i])





