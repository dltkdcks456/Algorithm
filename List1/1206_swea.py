import sys

sys.stdin = open('input_1206_swea')

for _ in range(10):                             # 10번의 테스트 진행
    row = int(input())                          # 건물이 들어설 수 있는 거리 길이
    building = list(map(int, input().split()))  # 건물의 층수

    ans = 0                                     # 조망권이 확보된 건물
    for each in range(2, row - 2):
        l_2 = building[each - 2]                # 왼쪽 2번 째부터 오른쪽 2번 째까지의 건물 높이
        l_1 = building[each - 1]
        r_1 = building[each + 1]
        r_2 = building[each + 2]                # 양쪽 건물들보다 높아야 조망권 확보가 가능
        if building[each] > l_2 and building[each] > l_1 and building[each] > r_1 and building[each] > r_2:
            ans += building[each] - max([l_2, l_1, r_2, r_1]) # 가장 높은 빌딩과의 차이를 합해줌
    print(f'#{_ + 1} {ans}')