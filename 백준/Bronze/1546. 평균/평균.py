N = int(input())
score = input().split()
M = max(map(int, score))
new = []
if N == len(score):
    for i in score:
        new.append(int(i)/M*100)
print(sum(new)/N)