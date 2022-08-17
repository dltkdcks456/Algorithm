import sys
sys.stdin = open('연습문제3.txt')

li = list(map(int, input().split()))    # 입력
N = len(set(li))   # 노드 개수
sequence = [[] for _ in range(N)]
for i in range(0, len(li), 2):
    sequence[li[i] - 1].append(li[i + 1] - 1)
    sequence[li[i + 1] - 1].append(li[i] - 1)

def dfs(v, N):          #n: 시작 위치 N: 찾을 노드 개수
    visited = [0] * N
    stack = [0] * N
    top = - 1
    print(v + 1)
    visited[v] = 1
    while True:
        for w in sequence[v]:
            if visited[w] == 0:
                top += 1
                stack[top] = v
                v = w
                print(v + 1)
                visited[w] = 1
                break
        else:
            if top == -1:
                break
            else:
                v = stack.pop()
                top -= 1
dfs(0, N)