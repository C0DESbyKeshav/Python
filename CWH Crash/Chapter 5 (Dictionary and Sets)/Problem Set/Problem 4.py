# What will be the length of the following set s:
'''
s = set()
s.add(20)
s.add(20.0)
s.add('20')   # length of s after these operations ?'''

s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(s)
print(len(s))
# Length of the above set will be 2 since python only considers the value and not the data type. 
# 20.0 = 20 so, this will be considered as repeated values in set.
