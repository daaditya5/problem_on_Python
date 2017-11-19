def fibennaci(inp):
    """ This program will gives the fibennaci series up to nth(inp) term """
    l = []
    if inp == 0:
        l.append(inp)
        print(inp,'th term is', l)
    elif inp == 1:
        l = [0]
        l.append(inp)
        print(inp,'th term is', l)
    elif inp > 1:
        l = [0, 1]
        a = 0
        b = 1
        while inp >= 3:
            c = a + b
            l.append(c)
            a = b
            b = c
            inp -= 1
        print(l)

while True:
    inp = input("please enter the nth term = ")
    if inp == 'done':
        break
    else:
        inp = int(inp)
        fibennaci(inp)