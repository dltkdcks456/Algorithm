import sys
sys.stdin = open('13994.txt')

T = int(input())
for test in range(T):
    N = int(input())
    bus_case = [list(map(int, input().split())) for _ in range(N)]
    bus_line = [0] * 1001                               # 총 버스 정류장
    for i in bus_case:
        if i[0] == 1:                                   # 일반 버스인 경우 해당 정류장 모두 1증가
            for j in range(i[1], i[2] + 1):
                bus_line[j] += 1
        elif i[0] == 2:                                 # 급행 버스인 경우 2차이씩 정류장 모두 1증가
            for k in range(i[1], i[2] + 1, 2):
                bus_line[k] += 1
        else:
            if i[1] % 2:
                for l in range(i[1], i[2] + 1):         # 광역 버스가 홀수인 경우 3의 배수이면서 10의 배수가 아닌 수 1증가
                    if l % 3 == 0 and l % 10 != 0:
                        bus_line[l] += 1
            else:                                       # 짝수인 경우 4의 배수 증가가
                for q in range(i[1], i[2]+ 1):
                    if q % 4 == 0:
                        bus_line[q] += 1
    ans = 0
    for p in bus_line:
        if p > ans:
            ans = p
    print(f'#{test + 1} {ans}')