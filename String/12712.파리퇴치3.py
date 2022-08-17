import sys
sys.stdin = open('12712.txt')

T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    pari = [list(map(int, input().split())) for i in range(N)]
    # 가로, 세로
    dr = [0, 1, 0, -1]              # 우, 하, 좌, 상
    dc = [1, 0, -1, 0]
    dx = [1, 1, -1, -1]             # 대각선 조건
    dy = [1, -1, 1, -1]
    maxV = 0
    for i in range(N):
        for j in range(N):
            Sum_rc = pari[i][j]
            Sum_xy = pari[i][j]
            for k in range(4):                          # 4가지 방향 진행
                for d in range(1, M):                   # 뻗어나가는 거리
                    if 0 <= i + dr[k] * d < N and 0 <= j + dc[k] * d < N:       # 가로, 세로 방향의 합
                        Sum_rc += pari[i + dr[k] * d][j + dc[k] * d]
                    if 0 <= i + dx[k] * d < N and 0 <= j + dy[k] * d < N:       # 대각선 방향의 합
                        Sum_xy += pari[i + dx[k] * d][j + dy[k] * d]
            if maxV < max(Sum_rc, Sum_xy):          # 최대값 구하기
                maxV = max(Sum_rc, Sum_xy)

    print(f'#{test + 1} {maxV}')
