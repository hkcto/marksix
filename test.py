def fn(x):
    return x in [1,2]

l = filter(fn, [1,2,3,4,5,6])
print(list(l))