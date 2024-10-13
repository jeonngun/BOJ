while True:
    triangle = []
    A, B, C = map(int, input().split())
    triangle.append(A)
    triangle.append(B)
    triangle.append(C)
    if len(set(triangle)) == 1 and list(set(triangle))[0] == 0:
        break
    elif max(triangle) >= (sum(triangle) - max(triangle)):
        print("Invalid")
    elif len(set(triangle)) == 1:
        print("Equilateral")
    elif len(set(triangle)) == 2:
        print("Isosceles")
    elif len(set(triangle)) == 3:
        print("Scalene")