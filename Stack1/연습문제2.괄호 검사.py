import sys
sys.stdin = open('연습문제2.txt')

T = int(input())

def f(li):
    L = []
    top = -1
    ans = 1
    for i in li:
        if i == '(':        # ( 이 입력되면 stack에 저장
            L.append(i)
            top += 1        # top의 위치가 1상승
        elif i == ')' and top == -1: # stack 내부에 원소가 없고, )가 저장될 때는 오류
            ans = -1
        else:
            L.pop()         # )가 입력될 때는 stack에 (를 pop해서 빼옴
            top -= 1
    if top >= 0:            # 모든 자료 검색이 끝났는데 stack에 자료가 남아있으면 오류
        ans = -1
    return ans

for test in range(T):
    li = input()
    print(f'#{test + 1} {f(li)}')