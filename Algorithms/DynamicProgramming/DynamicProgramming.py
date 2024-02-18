class Solution:
    def finder(self, n, j):
        if n == 0:
            return 0

        ans = 100
        for i in range(j, 0, -1):
            if n == i * i:
                return 1
            if n > i * i:
                ans = min(ans, 1 + self.finder(n - i * i, n - i * i + 1))
        return ans

    def numSquares(self, n: int) -> int:
        return self.finder(n, n)


if __name__ == '__main__':
    obj = Solution()
    print(obj.numSquares(2))
