__author__ = 'egorzinovev'
N = 5
dict3 = dict((x, x**2) for x in range(N))
dict2 = {}
dict2.items()
new_dict = dict(zip(dict3.values(),dict3.keys()))
print (new_dict)
d=dict{(x,y) for y,x in d.items()}