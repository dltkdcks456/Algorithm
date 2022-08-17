import sys
sys.stdin = open('9489.txt')

T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for i in range(N)]
    maxV = 0
    for i in range(N):
        cnt_c = 0
        for j in range(M):                      # 가로로 1이 연속된 경우의 수
            if area[i][j] == 1:                 # 1일 경우 개수 1증가
                cnt_c += 1
                if j == M - 1:                  # 경계선에서의 조건
                    if cnt_c > maxV:
                        maxV = cnt_c
            else:
                if cnt_c > maxV:                # 최대값 찾기
                    maxV = cnt_c
                cnt_c = 0

    for m in range(M):                          # 세로에 대한 정의
        cnt_r = 0
        for n in range(N):                      # 1인 경우 개수 1 증가
            if area[n][m] == 1:
                cnt_r += 1
                if n == N - 1:
                    if cnt_r > maxV:            # 경계선일 경우 조건 설정
                        maxV = cnt_r
            else:
                if cnt_r > maxV:                # 최대값 갱신
                    maxV = cnt_r
                cnt_r = 0
    print(f'#{test + 1} {maxV}')