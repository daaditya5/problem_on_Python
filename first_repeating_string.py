""" this program gives the output which is first repeated string """

def first_rep1():
    inp = input('plase enter the string: ')
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


def first_rep2():
    inp = input('plase enter the string: ')
    d = {}
    for i in inp:
        if i not in d:
            d[i] = 1
        else:
            return i


def first_rep3():
    inp = input('plase enter the string: ')
    return [char for char in inp if inp.count(char) > 1][0]