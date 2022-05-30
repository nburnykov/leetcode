from DFS_BFS.longest_matrix_path.app import longestIncreasingPath


def test_case_1():
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    r = 4
    assert longestIncreasingPath(matrix) == r


def test_case_2():
    matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
    r = 4
    assert longestIncreasingPath(matrix) == r


def test_case_3():
    matrix = [[1]]
    r = 1
    assert longestIncreasingPath(matrix) == r


def test_case_4():
    matrix = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [19, 18, 17, 16, 15, 14, 13, 12, 11, 10],
              [20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [39, 38, 37, 36, 35, 34, 33, 32, 31, 30],
              [40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [59, 58, 57, 56, 55, 54, 53, 52, 51, 50],
              [60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [79, 78, 77, 76, 75, 74, 73, 72, 71, 70],
              [80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],
              [100, 101, 102, 103, 104, 105, 106, 107, 108, 109], [119, 118, 117, 116, 115, 114, 113, 112, 111, 110],
              [120, 121, 122, 123, 124, 125, 126, 127, 128, 129], [139, 138, 137, 136, 135, 134, 133, 132, 131, 130],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    r = 4
    assert longestIncreasingPath(matrix) == r

def test_case_5():
    matrix = [[7,8,9],[9,7,6],[7,2,3]]
    r = 6
    assert longestIncreasingPath(matrix) == r

def test_case_6():
    matrix = [[13,5,13,9],[5,0,2,9],[10,13,11,10],[0,0,13,13]]
    r = 6
    assert longestIncreasingPath(matrix) == r
