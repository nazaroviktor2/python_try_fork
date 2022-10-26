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

