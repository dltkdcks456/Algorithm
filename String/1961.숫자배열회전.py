import sys
sys.stdin = open('1961.txt')

T = int(input())
for test in range(T):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test + 1}')
    for t in range(N):
        for k in range(N):
            print(num_list[N - k - 1][t], end="")
        print(f'\0', end="")
        for j in range(N):
            print(num_list[N - 1 - t][N - j - 1], end="")
        print(f'\0', end="")
        for i in range(N):
            print(num_list[i][N - 1 - t], end="")
        print()



