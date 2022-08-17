import sys
sys.stdin = open('1979.어디에 단어가 들어갈 수 있을까.txt')

T = int(input())
for test in range(T):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # 조건부
    for i in range(N):                      # 행에 대한 조건 확인
        cnt_c = 0
        cnt_r = 0
        for j in range(N):                  # 1이면 cnt를 1씩 증가
            if puzzle[i][j] == 1:
                cnt_c += 1
                if j == N-1:                # 마지막 라인에서 cnt가 1이면 개수 확인 후 종료
                    if cnt_c == K:
                        ans += 1
            else:                           # 해당 자리가 0이면 개수 카운트 후 cnt 0으로 초기화
                if cnt_c == K:
                    ans += 1
                cnt_c = 0

            if puzzle[j][i] == 1:           # 열에 대한 조건문, 위 조건과 대칭
                cnt_r += 1
                if j == N-1:
                    if cnt_r == K:
                        ans += 1
            else:
                if cnt_r == K:
                    ans += 1
                cnt_r = 0
    print(f'#{test + 1} {ans}')