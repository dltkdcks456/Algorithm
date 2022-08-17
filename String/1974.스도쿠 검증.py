import sys
sys.stdin = open('1974.txt')

T = int(input())
for test in range(T):
    num_list = [list(map(int, input().split())) for _ in range(9)]  # 9 x 9 행렬 입력
    num_list_rev = list(zip(*num_list))                             # 세로를 확인하기 위해 전치행렬 구함
    ans = 1                                                         # 결과값
    li = [_ for _ in range(1, 10)]                                  # 1 ~ 9까지 확인할 숫자
    # 가로, 세로
    for i in range(9):                                              # 가로, 세로에 대해 1 ~ 9까지 하나씩 있는지 확인
        for j in li:
            if j not in num_list[i] or j not in num_list_rev[i]:
                ans = 0
                break
        if ans == 0:
            break
    if ans != 0:                                                    # 가로, 세로가 통과했다면 정사각형 모양 진행
        for m in range(0, 9, 3):
            for n in range(0, 9, 3):
                test1 = set()
                for x in range(3):
                    for y in range(3):
                        test1.add(num_list[m + x][n + y])           # 해당 정사각형 배열에서 1 ~ 9까지 숫자 하나씩 있는지 확인
                if len(test1) != 9:                                 # 하나씩 없으면 ans를 0으로 변경
                    ans = 0
                    break
            if ans == 0:
                break
    print(f'#{test + 1} {ans}')                                     # 결과값 출력