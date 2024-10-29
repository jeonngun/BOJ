# 와나 생각하느라 머리깨지는줄알았네.....
N = int(input()) # 시도횟수 N 입력받기
n = 1
result = 0
while n <= N: # 시도횟수가 N일때까지 while문 반복
    n += 1
    word = list(input()) 
    word_c = 0
    for i in range(0, len(word)):
        try: # 0부터 word의 길이까지 앞뒤 알파벳 비교해서 다르면 word_c에 1을 더함
            if word[i] != word[i+1]:
                word_c += 1
        except:
            pass
    if len(set(word)) > word_c: # 알파벳 중복제거한 word의 길이가 word_c보다 크면 그룹단어라고 가정.
        result += 1 # 그룹단어일때 result에 1을 추가하여 단어수를 셈
print(result) 