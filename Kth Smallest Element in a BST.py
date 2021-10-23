class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder_list = []
        def dfs(root):
            if root:
                dfs(root.left)
                inorder_list.append(root.val)
                dfs(root.right)
            return -1
        dfs(root)
        
        return inorder_list[k-1]
