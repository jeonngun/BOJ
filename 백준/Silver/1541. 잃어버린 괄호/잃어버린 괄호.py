n = input().split('-')
N = []
for i in n:
    if "+" in i:
        ii = i.split('+')
        iii = []
        for j in ii:
            try:
                iii.append(str(int(j)))
            except:
                iii.append(j)
        N.append(str(eval("+".join(iii))))
    else:
        N.append(str(int(i)))
print(eval("-".join(N)))