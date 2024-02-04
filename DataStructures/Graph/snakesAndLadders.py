class Solution:
    def pathFinder(self, current, n, board, visited):
        if current >= n * n - 1:
            return 0
        print(visited)
        ans = 401
        for move in range(1, 7):
            next_move = current + move
            if next_move >= n * n - 1:
                return 1
            if not visited[next_move // n][next_move % n]:
                if board[next_move // n][next_move % n] == -1:
                    visited[next_move // n][next_move % n] = True
                    ans = min(ans, 1 + self.pathFinder(next_move, n, board, visited))
                    visited[next_move // n][next_move % n] = False
                else:
                    visited[next_move // n][next_move % n] = True
                    x = board[next_move // n][next_move % n] - 1
                    visited[x // n][x % n] = True
                    ans = min(ans, 1 + self.pathFinder(x, n, board, visited))
                    visited[next_move // n][next_move % n] = False
                    visited[x // n][x % n] = False
        return ans

    def snakesAndLadders(self, board) -> int:
        n = len(board)
        for i in range(n // 2):
            for j in range(n):
                board[i][j], board[n - i - 1][j] = board[n - i - 1][j], board[i][j]
        print(board)
        for i in range(n):
            if i % 2 == 1:
                for j in range(n // 2 + n % 2):
                    board[i][j], board[i][n - j - 1] = board[i][n - j - 1], board[i][j]
        print(board)
        visited = [[False] * n for _ in range(n)]
        x = self.pathFinder(0, n, board, visited)
        return x


obj = Solution()

matrix = [[-1, -1, -1], [-1, -1, -1], [-1, -1, 3]]
matrix = [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1],
          [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]
print(obj.snakesAndLadders(matrix))
