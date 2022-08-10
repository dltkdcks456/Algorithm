N = int(input())
arr = [[1]*N for _ in range(N)]
print(arr)

# s_l = 0
# s_r = 0
# for i in range(N):
#     for j in range(N):
#         if i < j:
#             s_l += arr[i][j]
#         elif i > j:
#             s_r += arr[i][j]
# print(s_l, s_r)

s_l = 0
s_r = 0
for i in range(N):
    for j in range(i + 1, N):
        s_l += arr[i][j]
        s_r += arr[j][i]

print(s_l, s_r)