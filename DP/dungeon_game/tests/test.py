from DP.dungeon_game.app import calculateMinimumHP


def test_case_1():
    dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    r = 7
    assert calculateMinimumHP(dungeon) == r