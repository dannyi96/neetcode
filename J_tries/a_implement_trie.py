# Leetcode link - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

# Hash map based. Can also be implemented as array based
# T: O(n) for insert, search, startsWith, S(t) for number of trie nodes
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True