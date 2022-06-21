###########################################################################################
# leetcode problem  https://leetcode.com/problems/short-encoding-of-words/
###########################################################################################

from typing import List


def minimumLengthEncoding2(words: List[str]) -> int:
    """
    A brute force approach O(n) = nlog(n) + n^2
    """
    s_words = sorted(words, key=len)
    len_collapse = 0
    len_all = 0
    len_words = len(s_words)
    for w in words:
        len_all += len(w)
    for i in range(0, len(s_words) - 1):
        for j in range(i + 1, len(s_words)):
            if s_words[i] == s_words[j][-len(s_words[i]):]:  # if word i is a substring of word j ending part
                len_collapse += len(s_words[i])
                len_words -= 1
                break

    return len_all - len_collapse + len_words


class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.end_nodes = []

    def insert(self, word: str):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        self.end_nodes.append((node, len(word)))


def minimumLengthEncoding(words: List[str]) -> int:
    tr = Trie()
    for w in set(words):
        tr.insert(w[::-1])

    return sum(ln + 1 for node, ln in tr.end_nodes if len(node.children) == 0)
