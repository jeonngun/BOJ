cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()
for i in cro:
    if i in a:
        a = a.replace(i, "*")

print(len(a))