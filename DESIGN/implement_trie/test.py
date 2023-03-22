from DESIGN.implement_trie.app import Trie


def test_case_1():
    tr = Trie()
    tr.insert("apple")
    assert tr.search("apple")
    assert not tr.search("app")
    assert tr.startsWith("app")
    tr.insert("app")
    assert tr.search("app")