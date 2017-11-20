""" this program gives the output which is first non repeated string """

def non_rep1():
    word = input("please enter the string = ")
    list_word = list(word)
    for i in range(len(list_word)):
        vary = list_word[i]
        list_word[i] = 0
        if vary not in list_word:
            print(vary)
            break
        else:
            list_word[i] = vary
    else:
        print("no repeated character")

def non_rep2():
    inp = input("please enter the string = ")
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

def non_rep3():
    inp = input("please enter the string = ")
    return [char for char in inp if inp.count(char) == 1][0]
