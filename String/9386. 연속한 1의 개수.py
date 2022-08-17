import sys
sys.stdin = open('9386.txt')

T = int(input())
for test in range(T):
    N = int(input())
    num_list = list(map(int, input())) + [0]        # 0을 리스트에 덧붙여 공간을 생성
    cnt = 0                                         # 1의 개수를 담을 변수
    maxV = 0                                        # 1의 최대 개수
    for i in range(N + 1):                          # 1일 경우 개수 증가
        if num_list[i] == 1:
            cnt += 1
        else:
            if cnt > maxV:                          # 최대 개수 찾기
                maxV = cnt
                cnt = 0
    print(f'#{test + 1} {maxV}')
