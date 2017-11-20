""" This program will gives the fibonnaci series up to nth(inp) term """

def fib1():
    inp = int(input("please enter the number = "))
    l = []
    if inp == 0:
        l.append(inp)
        print(l)
    elif inp == 1:
        l = [0]
        l.append(inp)
        print(l)
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

def fib2():
    inp = int(input("please enter the number = "))
    a, b = 0, 1; l = []
    for i in range(0, inp):
        l.append(a)
        a, b = b, a+b
    print(l)

