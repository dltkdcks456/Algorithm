import sys
sys.stdin = open('1966.swea.txt')

T = int(input())
for test in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    #버블 정렬: 스스로 창조해낸 것..
    for i in range(N):
        for j in range(N - i - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j + 1], num_list[j] = num_list[j], num_list[j + 1]
    print(num_list)

    #버블 정렬2: 기존 버블 정렬
    for i in range(N - 1, 0, -1):
        for j in range(i):
            if num_list[j] > num_list[j + 1]:
                num_list[j + 1], num_list[j] = num_list[j], num_list[j + 1]
    print(num_list)

    #버블 정렬 최적화1: swap이 있었던 경우는 계속 진행을 하고, swap이 없는 경우가 생기면 바로 종료
    for i in range(N - 1, 0, -1):
        swap = False
        for j in range(i):
            if num_list[j] >= num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
                swap = True
        if not swap:
            break
    print(num_list)

    #버블 정렬 최적화2: 가장 마지막에 swap한 위치를 기억하고, 버블정렬 범위를 축소 시킴
    end = len(num_list) - 1
    while end > 0:
        last_swap = 0
        for i in range(end):
            if num_list[i] > num_list[i + 1]:
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
                last_swap = i
        end = i
    print(num_list)


    #선택 정렬: 수업시간에 했던 정렬
    for i in range(N - 1):
        Min = i
        for j in range(i + 1, N):
            if num_list[Min] > num_list[j]:
                Min = j
        num_list[i], num_list[Min] = num_list[Min], num_list[i]
    print(num_list)