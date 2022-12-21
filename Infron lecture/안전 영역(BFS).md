# 📢 안전영역

❓ **비효율적인 부분**

- 전체 영역 순회 시 현재 비의 양에 대한 조건을 함께 사용하지 않아서 2번 순회하는 영역이 생김

✔ **해결사항**

- 전체 순회 시 비의 양을 초과하는 영역을 탐색하도록 진행

```python
# import sys
# #sys.stdin=open("input.txt", "r")
# dx=[-1, 0, 1, 0]
# dy=[0, 1, 0, -1]
# sys.setrecursionlimit(10**6)
# def DFS(x, y, h):
#     ch[x][y]=1
#     for i in range(4):
#         xx=x+dx[i]
#         yy=y+dy[i]
#         if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>h:
#             DFS(xx, yy, h)

# if __name__=="__main__":
#     n = int(input())
#     cnt = 0
#     res = 0
#     board=[list(map(int, input().split())) for _ in range(n)]
#     for h in range(100):
#         ch=[[0]*n for _ in range(n)]
#         cnt=0
#         for i in range(n):
#             for j in range(n):
#                 if ch[i][j]==0 and board[i][j]>h:
#                     cnt+=1
#                     DFS(i, j, h)
#         res=max(res, cnt)
#         if cnt==0:
#             break
#     print(res)

# from collections import deque
# def BFS(r, c):
#     q = deque()
#     q.append([r, c])
#     while q:
#         rs, rc = q.popleft()
#         for d in range(4):
#             nr = rs + dr[d]
#             nc = rc + dc[d]
#             if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
#                 visited[nr][nc] = 1
#                 q.append([nr, nc])



# if __name__ == "__main__":
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     maxV = max(map(max, arr))
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]

#     res = 0
#     for i in range(1, maxV):
#         # 최소 높이부터 최대 높이까지 잠긴다는 가정으로 진행하기
#         visited = [[0] * N for _ in range(N)]
#         for ri in range(N):
#             for ci in range(N):
#                 if arr[ri][ci] <= i:
#                     visited[ri][ci] = 1
                    
#         cnt = 0
#         for rr in range(N):
#             for cc in range(N):
#                 if visited[rr][cc] == 0:
#                     cnt += 1
#                     BFS(rr, cc)
#         if cnt > res:
#             res = cnt
#     print(res)

from collections import deque
def BFS(r, c):
    q = deque()
    q.append([r, c])
    while q:
        rs, rc = q.popleft()
        for d in range(4):
            nr = rs + dr[d]
            nc = rc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] > i:
                visited[nr][nc] = 1
                q.append([nr, nc])


if __name__ == "__main__":
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = max(map(max, arr))
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    res = 0
    for i in range(1, maxV):
        # 최소 높이부터 최대 높이까지 잠긴다는 가정으로 진행하기
        visited = [[0] * N for _ in range(N)]
        # 해당 코드 삭제 부분(의미없음)
        # for ri in range(N):
        #     for ci in range(N):
        #         if arr[ri][ci] <= i:
        #             visited[ri][ci] = 1
                    
        cnt = 0
        for rr in range(N):
            for cc in range(N):
                if visited[rr][cc] == 0 and arr[rr][cc] > i:
                    cnt += 1
                    BFS(rr, cc)
            
        if cnt > res:
            res = cnt
    print(res)
```

