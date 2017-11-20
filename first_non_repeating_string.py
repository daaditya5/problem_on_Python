inp = input('please enter the string = ')

def non_rep1(inp):
    l = list(inp)
    for i in range(len(l)):
        x = l[i]
        l[i] = 0
        if x not in l:
            return x
            break
        else:
            l[i] = x

    return None

#print(non_rep1(inp))


def non_rep2(inp):
    return [char for char in inp if inp.count(char) == 1][0]

print(non_rep2(inp))
