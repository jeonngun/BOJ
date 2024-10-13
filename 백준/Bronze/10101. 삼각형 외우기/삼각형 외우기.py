triangle = []
n = 1
while n <= 3:
    n += 1
    triangle.append(int(input()))
A, B, C = triangle[0], triangle[1], triangle[2]
if sum(triangle) == 180 and len(set(triangle)) == 1:
    print("Equilateral")
elif sum(triangle) == 180 and len(set(triangle)) == 2:
    print("Isosceles")
elif sum(triangle) == 180 and len(set(triangle)) == 3:
    print("Scalene")
elif sum(triangle) != 180:
    print("Error")