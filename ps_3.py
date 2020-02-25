
from typing import List, Optional
import numpy as np
import _collections
from TreeNodeSetup import TreeNode, Helper

class Problem:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """


if __name__ == "__main__":
    # Run actual funcs
    solver = Problem()
    
    input = '[3,5,1,6,2,0,8,null,null,7,4]'

    root = Helper.string_to_tree(input)
    
    result = solver.distanceK(root, TreeNode(5), 2)
    print(result)
