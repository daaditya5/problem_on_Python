""" This program gives the GCD and LCM of given two input numbers """

def gcd_lcm():
    a = int(input("please enter the first number = "))
    b = int(input("please enter the second number = "))
    l1 = [i for i in range(1, a) if a % i == 0]
    l2 = [j for j in range(1, b) if b % j == 0]
    gcd = [x for x in l1 if x in l2][-1]
    lcm = int((a * b)/gcd)
    print('GCD is =',gcd, 'LCM is =', lcm)
