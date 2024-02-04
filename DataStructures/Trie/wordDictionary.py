class TrieNode:
    def __init__(self):
        self.child = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for let in word:
            if let not in cur.child:
                cur.child[let] = TrieNode()
            cur = cur.child[let]
        cur.endOfWord = True

    def search(self, word: str, ) -> bool:
        cur = self.root
        for i in range(len(word)):
            if word[i] == '.':
                for c in cur.child:
                    if self.finder(cur.child[c], word[i + 1:]):
                        return True
            else:
                if word[i] not in cur.child:
                    return False
                cur = cur.child[word[i]]
        return cur.endOfWord

    def finder(self, root, word):
        cur = root
        for i in range(len(word)):
            if word[i] == '.':
                for c in cur.child:
                    if self.finder(cur.child[c], word[i + 1:]):
                        return True
            else:
                if word[i] not in cur.child:
                    return False
                cur = cur.child[word[i]]
        return cur.endOfWord


# Your WordDictionary object will be instantiated and called as such:
if __name__ == '__main__':
    wordDictionary = WordDictionary()
    print(wordDictionary.addWord("a"))
    print(wordDictionary.addWord("a"))
    print(wordDictionary.addWord("a"))
    print(wordDictionary.search("."))  # return False
    print(wordDictionary.search("aa"))  # return True
    print(wordDictionary.search(".a"))  # return True
    print(wordDictionary.search("a."))  # return True
