import sys
sys.stdin = open('input_Baby gin.txt')

T = int(input())

for test in range(T):                   # 테스트 케이스
    cnt = [0] * 10                      # 숫자 개수를 담을 리스트
    run = triplet = 0                   # run과 triplet의 수

    number = input()
    for j in number:
        cnt[int(j)] += 1                # 각각의 숫자에 대해 카운트 진행

    for k in range(len(cnt)):           # triplet인 경우에 해당하는 조건문
        while cnt[k] >= 1:
            if cnt[k] >= 3:
                cnt[k] -= 3
                triplet += 1
                continue

            if cnt[k] >= 1 and cnt[k + 1] >= 1 and cnt[k + 2] >= 1:  # run에 해당하는 조건문
                cnt[k] -= 1
                cnt[k + 1] -= 1
                cnt[k + 2] -= 1
                run += 1
                continue

            else:                       # 그 어느 것에도 만족하지 않을 시 break 진행
                break

    if (run + triplet) * 3 == len(number):  # 총 6개의 카드이므로 run, triplet의 합과 3을 곱하면 6이된다
        print(f'#{test + 1} 1')
    else:
        print(f'#{test + 1} 0')             # 해당 조건 불만족 시 0 출력