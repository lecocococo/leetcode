class Solution {
    Map<String, TreeNode> map;
    
    private String dfs(TreeNode root) {
        if (root == null) {
            return "#";
        }
        
        String unique_key = root.val + "|" + dfs(root.left) + "|" + dfs(root.right);
        // 유니크한 키를 부여, 만약 유니크한 키가 있다면 같은 서브트리가 존재한다
        map.put(unique_key, map.containsKey(unique_key) ? root : null);
        
        return unique_key;
    }
    
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        map = new HashMap<>();
        List<TreeNode> result = new ArrayList<>();
        
        dfs(root);
        
        for (TreeNode node : map.values()) {
            if (node != null) {
                result.add(node);
            }
        }
        
        return result;
    }

}
