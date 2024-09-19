a = input()
error = 0
for i in a:
    try:
        int(i)
        error += 1
    except:
        pass
if not error >= 1:
    print(len(a))