# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 자바 진짜 끔찍하다... 파이썬 쓰다가 자바 못쓰겠네
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 보기에 갈끔한 버전(좀 느리고 메모리도 많이 사용)
#         if inorder:
#             root = inorder.index(preorder.pop(0))
            
#             node = TreeNode(inorder[root])
#             node.left = self.buildTree(preorder,inorder[0:root])
#             node.right = self.buildTree(preorder,inorder[root+1:])
#             return node

        # 해시맵을 이용(빠르고 메모리 차지도 덜함)
        in_order = {val:i for i,val in enumerate(inorder)}
                
        def dfs(left, right):
            if left > right:
                return None
            
            node = TreeNode(preorder.pop(0))
            
            mid = in_order[node.val]
            node.left = dfs(left, mid - 1)
            node.right = dfs(mid + 1, right)
            
            return node
        
        return dfs(0, len(preorder) - 1)
