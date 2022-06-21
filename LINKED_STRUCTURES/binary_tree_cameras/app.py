###########################################################################################
# leetcode problem  https://leetcode.com/problems/binary-tree-cameras/
###########################################################################################

from typing import Optional

from utils import TreeNode


def minCameraCover(root: Optional[TreeNode]) -> int:
    """
    camera -> observed -> observeme -> camera -> ...  optimal state sequence
    """

    def check_subtree(subroot: TreeNode) -> (str, int):
        if subroot is None:
            return "observed", 0

        l_status, l_count = check_subtree(subroot.left)
        r_status, r_count = check_subtree(subroot.right)
        count = l_count + r_count

        if r_status == "observeme" or l_status == "observeme":
            return "camera", count + 1
        if r_status == "camera" or l_status == "camera":
            return "observed", count
        if subroot != root:  # in case if both children are under observation
            return "observeme", count
        else:
            return "", count + 1  # if both children are observed we still need to put camera at root

    _, count = check_subtree(root)
    return count