T = int(input())
for test in range(T):
    N = int(input())
    num_list = list(map(int, input()))
    cnt = 0
    maxV = 0
    for i in range(N):
        if num_list[i] == 1:
            if i == N - 1:
                cnt += 1
                if maxV < cnt:
                    maxV = cnt
            else:
                cnt +=1
        else:
            if maxV < cnt:
                maxV = cnt
            cnt = 0

    print(f'#{test + 1} {maxV}')