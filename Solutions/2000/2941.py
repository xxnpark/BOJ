word = input()
l = len(word)
wlist = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for w in wlist : l -= word.count(w)
print(l)