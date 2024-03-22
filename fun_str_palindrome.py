def str_palindrome(st):
    rev=''
    for i in st:
        rev=i+rev
    return rev
s=input("Enter the string: ")
r=str_palindrome(s)
if s==r:
    print("String is palindrome or symmetric")
else:
    print("String is not palindrome or symmetric")
