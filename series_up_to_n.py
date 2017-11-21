""" This program will give you the integer series up to nth term.
    please run the integer function and pass nth term as argument and print it"""

def integer(n):
    i = 1; l = []
    while i <= n:
        l.append(i)
        i += 1
    return l
