import sys
sys.stdin = open('5356.txt')

T = int(input())
for test in range(T):
    num_list = [list(input()) for i in range(5)]
    maxV = 0
    ans = []

    for j in num_list:                                  # 최고 긴 길이를 찾기
        if maxV < len(j):
            maxV = len(j)
    for k in range(maxV):                               # 최소 길이부터 진행하면서 각 리스트의 길이를 넘어가면 미출력
        for l in range(5):
            if len(num_list[l]) > k:
                ans.append(num_list[l][k])              # 제한된 길이 내에 있는 값들을 모두 추출
    print(f'#{test + 1}', end=' ')
    print(''.join(ans))