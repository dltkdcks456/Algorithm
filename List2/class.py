import sys
sys.stdin = open('input.txt')

N = 2
M = 3
arr = [list(map(int, input().split())) for _ in range(N)]

di = [0, 0, -1, 1] # 상 하 좌 우
dj = [-1, 1, 0, 0]

for i in range(N):
    for j in range(M):
        for d in range(1, 3):
            for k in range(4):
                ni = i + di[k] * d
                nj = j + dj[k] * d
                if 0 <= ni < N and 0 <= nj < M:
                    print(ni, nj)

for i in range(N):
    for j in range(M):
        for k in range(4):
            for d in range(1, 3):
                ni = i + di[k] * d
                nj = j + dj[k] * d
                if 0 <= ni < N and 0 <= nj < M:
                    print(ni, nj)