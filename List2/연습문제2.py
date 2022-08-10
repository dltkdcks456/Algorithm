import sys
sys.stdin = open('연습문제2.txt')

T = int(input())
for test in range(T):
    num_list = list(map(int, input().split()))
    N = len(num_list)
    ans = 0

    s_list = []
    for i in range(1 << N):
        s = 0
        for j in range(N):
            if i & (1 << j):
                s += num_list[j]
        if i == 0:
            continue
        else:
            s_list.append(s)
            if s == 0:
                ans = 1

    print(f'#{test + 1} {ans}')