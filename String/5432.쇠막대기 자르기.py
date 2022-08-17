import sys
sys.stdin = open('5432.txt')

T = int(input())
for test in range(T):
    bar_list = list(input().replace('()', '0'))         # 레이저 부위를 0으로 변경
    cnt = bar = 0                                       # 잘린 막대기를 셀 때는 cnt, 겹쳐진 막대기 개수는 bar 변수로 정의
    for i in bar_list:
        if i == '(':                                    # 막대기가 추가 될 때 bar + 1
            bar += 1
        elif i == '0':                                  # 레이저를 만나면 잘린 개수 추가
            cnt += bar
        elif i == ')':                                  # 막대기가 끝나면 끝단에 잘린 막대기 1 추가
            cnt += 1
            bar -= 1
    print(f'#{test + 1} {cnt}')