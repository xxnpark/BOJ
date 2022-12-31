num = 0
for i in range(int(input())):
    word = input() + " "
    nword = ""
    for i in range(len(word)-1):
        if word[i] != word[i+1] : nword += word[i]
    breaker = False
    for s in nword :
        if len(nword.split(s)) > 2:
            breaker = True
            break
    if breaker == True : continue
    num += 1
print(num)