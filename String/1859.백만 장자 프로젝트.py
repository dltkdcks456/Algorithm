import sys
sys.stdin = open('1859.txt')

def profit(N, arr):
    result = arr[:]
    maxV = 0
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > maxV:
            maxV = arr[i]
        result[i] = maxV
    return sum(result) - sum(arr)


T = int(input())
for test in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    print(f'#{test + 1} {profit(N, num_list)}')