//level order => bfs 사용
class Solution {
    List<List<Integer>> result = new ArrayList<List<Integer>>();
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        // Queue<TreeNode> queue = new ArrayDeque<>();
        if(root== null)
            return result;
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        // int cnt = 1;
        
        //반대로 바꿔서 저장할지 말지 결정하는 flag
        boolean flag = false;
        while(!queue.isEmpty()){
            int size = queue.size();
            List<Integer> list = new ArrayList<>();
            //큐의 크기만큼 반복하는 이유: 큐에 들어있는 노드수 만큼 자손을 다시 큐에 넣고 val값을 저장해야 되기때문 
            for (int i=0;i<size;i++){
                TreeNode node = queue.poll();
                
                if(node.left!=null){
                    queue.offer(node.left);
                }
                if(node.right!=null){
                    queue.offer(node.right);
                }
                
                if(flag){
                    list.add(0,node.val);
                }
                else{
                    list.add(node.val);
                }
            }
            result.add(list);
            flag = !flag;
        }
        return result;
        
    }
}
