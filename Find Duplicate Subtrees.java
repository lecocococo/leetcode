class Solution {
    private Map<String, Integer> map = new HashMap<>();
    private List<TreeNode> result = new ArrayList<>();
    
    private String dfs(TreeNode root) {
        if (root == null) {
            return "#";
        }
        
        String unique_key = root.val + "|" + dfs(root.left) + "|" + dfs(root.right);
        // 유니크한 키를 부여, 만약 유니크한 키가 있다면 같은 서브트리가 존재한다
        // map.put(unique_key, map.containsKey(unique_key) ? root : null);
        int cnt = map.getOrDefault(unique_key, 0);
        if (cnt == 1)
            result.add(root);
        
        map.put(unique_key, cnt + 1);
            
        return unique_key;
    }
    
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        dfs(root);
        
        return result;
    }

}
