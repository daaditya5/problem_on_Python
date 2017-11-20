inp = input('plase enter the string: ')

def first_rep1(inp):
    l = list(inp)
    for i in range(len(l)):
        x = l[i]
        l[i] = 0
        if x in l:
            return x
            break
        else:
            l[i] = x
    else:
        return None

print(first_rep1(inp))


def first_rep2(inp):
    d = {}
    for i in inp:
        if i not in d:
            d[i] = 1
        else:
            return i

print(first_rep2(inp))


def first_rep3(inp):
    return [char for char in inp if inp.count(char) > 1][0]

print(first_rep3(inp))