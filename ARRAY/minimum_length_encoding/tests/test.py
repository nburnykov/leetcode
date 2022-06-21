from ARRAY.minimum_length_encoding.app import minimumLengthEncoding, Trie


def test_case_1():
    words = ["time", "me", "bell"]
    r = 10
    assert minimumLengthEncoding(words) == r

def test_case_2():
    words = ["t"]
    r = 2
    assert minimumLengthEncoding(words) == r

def test_case_3():
    words = ["time","time","time","time"]
    r = 5
    assert minimumLengthEncoding(words) == r

def test_case_4():
    tr = Trie()
    tr.insert('poppyplaytime')
    tr.insert('poppstrytime')
    print(tr.__dict__)
