import sys
sys.stdin = open('4408.txt')

T = int(input())
for test in range(T):
    room1 = [i for i in range(1, 401, 2)]
    room2 = [j for j in range(2, 401, 2)]
    N = int(input())
    student = []
    for _ in range(N):
        start, end = map(int, input().split())
        if start > end:
            start, end = end, start
        if start % 2:
            start = room1.index(start)
        else:
            start = room2.index(start)
        if end % 2:
            end = room1.index(end)
        else:
            end = room2.index(end)
        student.append([start, end])
    student.sort()
    print(student)

    cnt = 0
    flag = 0
    while N > 1:
        while flag + 1 <= N - 1:
            if student[flag][1] < student[flag + 1][0]:
                student.pop(flag)
                N -= 1
            else:
                flag += 1
        cnt += 1
        flag = 0

    print(f'#{test + 1} {cnt}')