class Solution:
    def finder(self, i, j, word, board, visited):
        if len(word) == 0:
            return True
        row = [1, 0, -1, 0]
        col = [0, 1, 0, -1]
        for m in range(4):
            x = i + row[m]
            y = j + col[m]
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == word[0] and not visited[x][
                y]:
                visited[x][y] = True
                if self.finder(x, y, word[1:], board, visited):
                    visited[x][y] = False
                    return True
                visited[x][y] = False
        return False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        d = {}
        res = []
        m = len(board)
        n = len(board[0])
        visited = [[False for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] not in d:
                    d[board[i][j]] = [(i, j)]
                else:
                    d[board[i][j]].append((i, j))
        for word in words:
            if word[0] in d:
                for cor in d[word[0]]:
                    # print(word[0],cor)
                    visited[cor[0]][cor[1]] = True
                    if self.finder(cor[0], cor[1], word[1:], board, visited):
                        visited[cor[0]][cor[1]] = False
                        res.append(word)
                        break
                    visited[cor[0]][cor[1]] = False
        return res

