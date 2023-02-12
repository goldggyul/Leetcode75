package solution.graph.clonegraph;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    private Map<Integer, Node> nodes = new HashMap<>();

    private Node createNodeOf(Node node) {
        if (nodes.containsKey(node.val)) {
            return nodes.get(node.val);
        }
        Node newNode = new Node(node.val);
        nodes.put(node.val, newNode);
        node.neighbors.forEach(neighbor -> {
            Node newNeighbor = createNodeOf(neighbor);
            newNode.neighbors.add(newNeighbor);
        });
        return newNode;
    }

    public Node cloneGraph(Node node) {
        if (node == null) return null;
        return createNodeOf(node);
    }

    private static class Node {
        public int val;
        public List<Node> neighbors;

        public Node() {
            val = 0;
            neighbors = new ArrayList<Node>();
        }

        public Node(int _val) {
            val = _val;
            neighbors = new ArrayList<Node>();
        }

        public Node(int _val, ArrayList<Node> _neighbors) {
            val = _val;
            neighbors = _neighbors;
        }
    }
}