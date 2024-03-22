def list_vowel_non(s):
    vowel=[]
    non_vowel=[]
    for i in s:
        if i=='a' or i=='A' or i=='E' or i=='e' or i=='i' or i=='I' or i=='o' or i=='0' or i=='u' or i=='U':
            vowel.append(i)
        else:
            non_vowel.append(i)
    print("Vowel list: ", vowel)
    print("Non Vowel list: ",non_vowel)

st=input("Enter the string")
list_vowel_non(st)




