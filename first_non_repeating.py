def non_rep(word):
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

while True:
    word = input("please enter the string = ")
    if word == 'done':
        break
    else:
        non_rep(word)
