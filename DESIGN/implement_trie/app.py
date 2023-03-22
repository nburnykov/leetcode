class Trie:

    def __init__(self):
        self.trie = dict()

    def insert(self, word: str) -> None:
        _trie = self.trie
        for ch in word:
            if ch in _trie.keys():
                _trie = _trie[ch]
            else:
                _trie[ch] = dict()
                _trie = _trie[ch]
        _trie["*"] = None  # indicates that word stops here

    def search(self, word: str) -> bool:
        _trie = self.trie
        for ch in word:
            if ch in _trie.keys():
                _trie = _trie[ch]
            else:
                return False
        if "*" in _trie:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        _trie = self.trie
        for ch in prefix:
            if ch in _trie.keys():
                _trie = _trie[ch]
            else:
                return False
        return True
