from edit_distance.app import minDistance


def test_case_1():
    word1 = "horse"
    word2 = "ros"
    r = 3
    assert minDistance(word1, word2) == r

def test_case_2():
    word1 = "intention"
    word2 = "execution"
    r = 5
    assert minDistance(word1, word2) == r