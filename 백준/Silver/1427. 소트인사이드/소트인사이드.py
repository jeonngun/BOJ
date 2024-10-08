N = int(input())
a = list(map(int, str(N))) # N에 대하여 정수를 원소로 갖는 리스트 생성
result = list(reversed(sorted(a))) # 리스트 오름차순 후 역순(내림차순)정렬
print("".join(list(map(str, result))))