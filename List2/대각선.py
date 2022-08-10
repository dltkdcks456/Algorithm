N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s = 0
for i in range(N):
    for j in range(N):
        if i == j:
            s += arr[i][j]

s = 0
for i in range(N):
    s += arr[i][i]

s = 0
for j in range(N):
    s += arr[N - i - 1][i]

# 양쪽 대각선일 경우 홀수일 때 가운데 값을 한 번 빼줘야 함.ㅜㅜ