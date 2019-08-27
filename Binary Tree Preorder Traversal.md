```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        res = [root.val]
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)
        
        return res
```
