N = 3   # 행
M = 4   # 열
# N개의 원소를 갖는 0으로 초기화된 2차원 배열을 생성하시오.
arr1 = [0] * N

# 크기가 N*M 이고 0으로 초기화된 2차원 배열
# arr2 = [[0] * M] * N
arr2 = [[0] * M for i in range(N)] # 1차원 배열을 만들고 그것을 가리키는 래퍼런스가 3개
                       # 얕은 복사가 된다.
# print(arr3)
# arr2[0][0] = 1
# print(arr2)

arr3 = [[1], [2, 3], [3, 4, 5]]