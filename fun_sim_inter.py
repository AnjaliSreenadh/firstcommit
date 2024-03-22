def simple_interest(p,t,r=5):
    s_i=(p*r*t)/100
    return s_i
prin_amt=int(input("Enter the principal amount: "))
time_dur=int(input("Enter the time period in years: "))
print("The simple interest for the given rate is: ",simple_interest(prin_amt,time_dur))