class Trie:

    def __init__(self):
        self.head = {}

    def insert(self, word: str) -> None:
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True

    def search(self, word: str) -> bool:
        cur = self.head

        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        return '*' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.head

        for ch in prefix:
            if ch not in cur:
                return False
            cur = cur[ch]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)