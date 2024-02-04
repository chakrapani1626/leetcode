class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for let in word:
            if not cur.child[ord(let) - 97]:
                cur.child[ord(let) - 97] = TrieNode()
            cur = cur.child[ord(let) - 97]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for let in word:
            if not cur.child[ord(let) - 97]:
                return False
            cur = cur.child[ord(let) - 97]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for let in prefix:
            if not cur.child[ord(let) - 97]:
                return False
            cur = cur.child[ord(let) - 97]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
