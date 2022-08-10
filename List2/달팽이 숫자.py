import sys
sys.stdin = open('달팽이 숫자.txt')

T = int(input())
for _ in range(10):
    N = int(input())
    total_list = [[0 for _ in range(N)] for _ in range(N)]

    dx = [1, 0, -1, 0]                                                              # 우, 하, 좌, 상
    dy = [0, 1, 0, -1]
    step = 0                                                                        # 입력될 값 and 각 단계의 값
    direction = 0                                                                   # 방향키
    x = y = 0                                                                       # 초기값
    while step < N * N:                                                             # 25까지 하기 조건문 반복
        if y + dy[direction % 4] < N and x + dx[direction % 4] < N:                 # 범위를 이탈하면 안되므로 각각의 x, y 좌표값은 N 미만
            if total_list[y + dy[direction % 4]][x + dx[direction % 4]] == 0:       # 한 칸 진행할 곳의 값이 0이면 이동 가능
                step += 1                                                           # 해당 칸에 step 기록 후 step과 x, y 좌표값을 상승/여전히 direction은 동일
                total_list[y][x] = step
                x = x + dx[direction % 4]
                y = y + dy[direction % 4]
            else:                                                                   # 앞 칸에 숫자가 있으면 방향 전환 후 step과 x, y좌표값 상승
                direction += 1
                step += 1
                total_list[y][x] = step
                x = x + dx[direction % 4]
                y = y + dy[direction % 4]

        elif y + dy[direction % 4] == N or x + dx[direction % 4] == N:              # x, y 좌표가 범위를 초과하는 경우
            direction += 1                                                          # 방향 전환 및 다른 변수 값 조정
            step += 1
            total_list[y][x] = step
            x = x + dx[direction % 4]
            y = y + dy[direction % 4]

    print(f'#{N}')
    for i in range(N):                                                              # 결과 출력
        print(*total_list[i])