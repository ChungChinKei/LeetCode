```python
class Solution:
    def preOrder(self, root):
        if not root: return []
        
        res = []
        res += self.preOrder(root.left)
        res += [root.val]
        res += self.preOrder(root.right)
        
        return res
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root: return -1 
        
        res = self.preOrder(root)
        
        return res[k-1]
```
