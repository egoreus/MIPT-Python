__author__ = 'egorzinovev'

def f(l=[]):
    l.append(len(l)+1)
    print(l)

print(f(f(f([]))))