import sys
sys.stdin = open('9367.txt')

T = int(input())
for test in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    cnt = 1                                 # 최소 개수
    maxV = 1                                # 나열된 수의 최대 개수
    for i in range(N - 1):
        if C[i + 1] == C[i] + 1:            # 나열된 수이면 개수 1 증가
            cnt += 1
            if cnt > maxV:                  # 최대치 지속 갱신
                maxV = cnt
        else:
            cnt = 1
    print(f'#{test + 1} {maxV}')