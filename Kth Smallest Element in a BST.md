```python
class Solution:
    def inorder(self, root):
        if not root: return []
        
        res = []
        res += self.inorder(root.left)
        res += [root.val]
        res += self.inorder(root.right)
        
        return res
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root: return 
        
        res = self.inorder(root)
        
        return res[k-1]
```
