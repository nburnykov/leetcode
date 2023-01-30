from LINKED_STRUCTURES.right_side_view.app import rightSideView
from utils import compose_binary_tree


def test_case_1():
    t = [1,2,3,None,5,None,4]
    tt = compose_binary_tree(t)
    r = [1,3,4]
    assert rightSideView(tt) == r
