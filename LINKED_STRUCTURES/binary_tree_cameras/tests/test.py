from LINKED_STRUCTURES.binary_tree_cameras.app import minCameraCover
from utils import compose_binary_tree


def test_case_1():
    root = [0, 0, None, 0, 0]
    r = 1
    lt = compose_binary_tree(root)

    assert minCameraCover(lt) == r

def test_case_2():
    root = [0,0,None,0,None,0,None,None,0]
    r = 2
    lt = compose_binary_tree(root)

    assert minCameraCover(lt) == r