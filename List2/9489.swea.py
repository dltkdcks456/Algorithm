import sys
sys.stdin = open('9489.swea.txt')

T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    item = [list(map(int, input().split())) for i in range(N)]

    cnt = 0
    maxV = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if item[i][j] == 1:
                cnt += 1
                if maxV < cnt:
                    maxV = cnt
            else:
                if maxV < cnt:
                    maxV = cnt
                cnt = 0
    cnt = 0

    for i in range(M):
        cnt = 0
        for j in range(N):
            if item[j][i] == 1:
                cnt += 1
                if maxV < cnt:
                    maxV = cnt
            else:
                if maxV < cnt:
                    maxV = cnt
                cnt = 0

    print(f'#{test + 1} {maxV}')