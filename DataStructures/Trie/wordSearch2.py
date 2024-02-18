"""212. Word Search II
Hard
Topics
Companies
Hint
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once in a word."""


class TrieNode:
    def __init__(self):
        self.child = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, i, j, board, count, cur, visited):
        if count >= 10:
            return
        row = [1, 0, -1, 0]
        col = [0, 1, 0, -1]
        for m in range(4):
            x = i + row[m]
            y = j + col[m]
            if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and not visited[x][y]:
                visited[x][y] = True
                if board[x][y] not in cur.child:
                    cur.child[board[x][y]] = TrieNode()
                self.insert(x, y, board, count + 1, cur.child[board[x][y]], visited)
                visited[x][y] = False

    def search(self, word):
        cur = self.root
        for let in word:
            if let not in cur.child:
                return False
            cur = cur.child[let]
        return True


class Solution:
    def findWords(self, board, words):
        d = {}
        res = []
        m = len(board)
        n = len(board[0])
        visited = [[False for i in range(n)] for j in range(m)]
        obj = Trie()
        for i in range(m):
            for j in range(n):
                visited[i][j] = True
                if board[i][j] not in obj.root.child:
                    obj.root.child[board[i][j]] = TrieNode()
                obj.insert(i, j, board, 1, obj.root.child[board[i][j]], visited)
                visited[i][j] = False

        for word in words:
            if obj.search(word):
                res.append(word)

        return res


if __name__ == '__main__':
    obj = Solution()
    x = obj.findWords([['a']], ['a'])
    print(x)
