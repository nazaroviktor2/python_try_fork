from re import A
from time import time


def decorator(f1,f2):
    t1 = 0
    t2 = 0
    def f(*args,**kwargs):
        initial_time = time()
        f1(*args,**kwargs)
        t1=time()-initial_time - time()
        initial_time = time()
        f2(*args,**kwargs)
        t2 = time()-initial_time - time()
        print(t1,"vs",t2)
    return f

def count_duplicate(s):
    res = 0
    sym = []
    g = []
    for i in s.lower():
        if i in g:
            continue
        elif i in sym:
            res += 1
        else:
            sym.append(i)
    return res


def count2(s):
    return len([1 for i in set(s.lower()) if s.lower().count(i) > 1])

new = decorator(count_duplicate,count2)
s = 'aabb'
new(s)

