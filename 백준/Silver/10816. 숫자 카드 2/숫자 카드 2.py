import sys

# 상근이가 가지고 있는 숫자 카드의 개수
N = int(sys.stdin.readline())
# 상근이가 가지고 있는 정수 리스트로
sg = sys.stdin.readline().split()
# 상근이가 가지고 있는 정수를 중복제거 한 뒤 그 값을 키 값으로 0 딕셔너리 생성
SG = {}
for i in set(sg):
    SG[i] = 0
# 상근이가 가지고 있는 정수 리스트에 대하여 정수가 나올때마다 딕셔너리 카운팅+1
# count 함수가 시간이 오래걸릴거같아서 씀
for j in sg:
    SG[j] += 1
# 카드뭉치 개수
M = int(sys.stdin.readline())
# 카드뭉치 리스트
cards = sys.stdin.readline().split()

# 정수 개수를 밸류로 구해놓은 딕셔너리 'SG'에 대해서 정답 기술
for k in cards:
    try:
        print(SG[k], end=' ')
    except:
        print(0, end=' ')