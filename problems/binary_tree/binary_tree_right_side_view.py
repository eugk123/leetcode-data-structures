"""
https://leetcode.com/problems/binary-tree-right-side-view
"""
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        level = deque([root])
        result = []
        while level:
            new_level = []
            
            while level:
                curr = level.popleft()
                
                if len(level) == 0:
                    result.append(curr.val)
                
                if curr.left:
                    new_level.append(curr.left)
                    
                if curr.right:
                    new_level.append(curr.right)
            
            # need to add the far right. so a queue is needed here.
            level = deque(new_level)
            