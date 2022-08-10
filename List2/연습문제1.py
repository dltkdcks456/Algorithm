import sys
sys.stdin = open('연습문제1.txt')

T = int(input())
for test in range(T):

    def around(arr, N):
        s = 0
        for i in range(N):
            for j in range(N):
                for k in range(4):
                    ni = i + dj[k]
                    nj = j + di[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        s = s + abs(arr[i][j] - arr[ni][nj])
        return s

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [1, 0, 1, 0] # 우, 하, 좌, 상
    dj = [0, 1, 0, -1]
    ans = around(arr, N)
    print(f'#{test + 1} {ans}')