from collections import defaultdict
class Solution:
    def numSubmatrixSumTarget(self, matrix, target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        sub_matrix = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                top = sub_matrix[i-1][j] if i-1>=0 else 0
                left = sub_matrix[i][j-1] if j-1>=0 else 0
                top_left = sub_matrix[i-1][j-1] if min(i,j)-1 >= 0 else 0
                sub_matrix[i][j] = matrix[i][j] + top + left - top_left

        res = 0
        for r1 in range(m):
            for r2 in range(r1, m):
                count = defaultdict(int)
                count[0] = 1
                for c in range(n):
                    cur_sum = sub_matrix[r2][c] - (sub_matrix[r1 - 1][c] if r1 > 0 else 0)
                    diff = cur_sum - target
                    res += count[diff]
                    count[cur_sum] += 1
        return res

obj = Solution()

matrix = [[0,1,0],
          [1,1,1],
          [0,1,0]]

print(obj.numSubmatrixSumTarget(matrix,0))