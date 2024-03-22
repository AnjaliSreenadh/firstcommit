def patt_rec_st(n):
    if n==0:
        return
    else:
        print("* "*n)
    patt_rec_st(n-1)
num=int(input("Enter the number of rows: "))
patt_rec_st(num)
