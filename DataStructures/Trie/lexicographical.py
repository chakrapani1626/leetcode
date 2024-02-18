"""
386. Lexicographical Numbers
Solved
Medium
Topics
Companies
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space.

 """


class TrieNode:
    def __init__(self):
        self.child = [None] * 10
        self.count = 0
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.res = []

    def insert(self, num):
        cur = self.root
        temp = []
        while num:
            temp.append(num % 10)
            num = num // 10
        for i in temp:
            if not cur.child[i]:
                cur.count += 1
                cur.child[i] = TrieNode()
            cur = cur.child[i]
        cur.end = True

    def search(self, cur, val):
        if not cur.count:
            self.res.append(val)
            return
        print(cur.child)
        if cur.end:
            self.res.append(val)
        for i in range(10):
            if cur.child[i]:
                self.search(cur.child[i], 10 * val + i)


class Solution:
    def lexicalOrder(self, n: int):
        obj = Trie()
        for i in range(1, n + 1):
            obj.insert(i)
        res = []
        obj.search(obj.root, 0)
        return obj.res


if __name__ == '__main__':
    obj = Solution()
    print(obj.lexicalOrder(10))
