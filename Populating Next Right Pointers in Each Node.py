from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
#       두방법중 뭐가 빠른지는 정확히 측정이 불가능/돌릴떄마다 바뀜(아마 아래쪽 풀이가 더 빠를거 같긴함)
        if root is None or root.left is None:
            return root
        
        root.left.next = root.right
        
        if root.next:
            root.right.next = root.next.left
            
        self.connect(root.left)
        self.connect(root.right)
        
        return root
        
#         if not root:
#             return None
#         cur = root
#         nxt = cur.left
#         while nxt:
#             if cur.next:
#                 cur.left.next = cur.right
#                 cur.right.next = cur.next.left
#                 cur = cur.next
#             else: 
#                 cur.left.next = cur.right
#                 cur = nxt
#                 nxt = nxt.left

#         return root
