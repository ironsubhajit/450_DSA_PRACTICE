// Dfs with java
import java.util.*;

class DfsTrav{

    void adj_list_add_edge(ArrayList<ArrayList<Integer>> adj_list, int src, int dest) {
        adj_list.get(src).add(dest);
        adj_list.get(dest).add(src);
    }

    public ArrayList<Integer> dfsGraph(int v, ArrayList<ArrayList<Integer>> adj){
        boolean vis[] = new boolean[v+1];
        ArrayList<Integer> ans = new ArrayList<>();

        for(int i = 0; i < v+1; i++){
            if(!vis[i])
                dfs(i, adj, vis, ans);
        }

        return ans;
    }

    public void dfs(int v, ArrayList<ArrayList<Integer>> adj, boolean[] vis, ArrayList<Integer> ans){
        vis[v] = true;
        ans.add(v);
        for(Integer neighbor: adj.get(v)){
            if(!vis[neighbor]){
                dfs(neighbor, adj, vis, ans);
            }
        }
    }

    public static void main(String[] args){
        int v = 4;
        int e = 4;
        ArrayList<ArrayList<Integer>> adj_list = new ArrayList<>();

        for (int i = 0; i < v + 1; i++) {
            // Add inside array
            adj_list.add(new ArrayList<Integer>());
        }

        DfsTrav graph = new DfsTrav();
        graph.adj_list_add_edge(adj_list, 1, 2);
        graph.adj_list_add_edge(adj_list, 1, 3);
        graph.adj_list_add_edge(adj_list, 2, 3);
        graph.adj_list_add_edge(adj_list, 3, 4);

        System.out.println("Adjacency List for the Graph: ");
        for (int i = 0; i < adj_list.size(); i++) {
            System.out.print(i + " -> ");
            // Loop through all elements of current row
            for (int j = 0; j < adj_list.get(i).size(); j++)
                System.out.print(adj_list.get(i).get(j) + " ");
            System.out.println();
        }

        ArrayList<Integer> out = new ArrayList<>();
        out = graph.dfsGraph(v, adj_list);
        for(Integer node: out){
            System.out.print(node+" ");
        }
        // System.out.println(graph.dfsGraph(v, adj_list));

    }
}