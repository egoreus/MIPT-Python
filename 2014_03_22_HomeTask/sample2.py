__author__ = 'egorzinovev'
N=5

# 1
dict1 = dict([(x, x**2) for x in range(N)])

# 2
dict2 = dict({(x, x**2) for x in range(N)})

# 3
dict3 = dict((x, x**2) for x in range(N))

print(dict1)
print(dict2)
print(dict3)