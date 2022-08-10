import sys

sys.stdin = open('input_Gravity.txt')

T = int(input())                                    # 테스트 케이스

for i in range(T):                                  # for문을 통해 입력값을 받음
    total_area = int(input())
    num_list = list(map(int, input().split()))

    max_cnt = 0                                     # 가장 멀리 떨어지는 낙차 값의 초기값

    for num in range(total_area - 1):               # 각 라인 마다 비교 진행
        fall = 0
        for other in range(num + 1, total_area):    # 다른 라인보다 크다면 1칸의 낙차가 허용되므로 1을 추가
            if num_list[num] > num_list[other]:
                fall += 1
        if fall > max_cnt:                          # 각 라인별 낙차를 구하고 최대값을 구함
            max_cnt = fall
    print(f'#{i + 1} {max_cnt}')