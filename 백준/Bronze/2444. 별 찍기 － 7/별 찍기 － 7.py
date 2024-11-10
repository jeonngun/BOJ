N = int(input())
n = 1
for i in range(1, 2*N, 2):
    print(" "*((2*N-1-i)//2)+"*"*i)
for j in range((2*(N-1))-1, 0, -2):
    print(" "*((2*N-1-j)//2)+"*"*j)