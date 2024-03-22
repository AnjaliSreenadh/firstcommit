print("Symmetric difference update")
a={1,21,23,'hi'}
b={1,2,5,10,'myset','hi'}
a.symmetric_difference_update(b)
print(a)
print("Symmetric difference")
c={1,10,'difference','python'}
d=b.symmetric_difference(c)
print(d)
print("Difference update")
print(c.difference_update(b))
