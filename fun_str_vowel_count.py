def str_vowel_count(st):
    count=0
    for i in st:
        if i=='a' or i=='A' or i=='E' or i=='e' or  i=='i' or  i=='I' or i=='o' or i=='0' or i=='u' or i=='U':
            count+=1
    return count
s=input("Enter the string: ")
c=str_vowel_count(s)
print("The number of vowel characters in the string is : ",c)
