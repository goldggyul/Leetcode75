package solution.graph.clonegraph

class Node(var `val`: Int) {
    var neighbors: ArrayList<Node?> = ArrayList<Node?>()
}

class SolutionKt {

    private val map = hashMapOf<Int, Node>()

    private fun createNewNodeAndRegister(number: Int): Node {
        val node = Node(number)
        map[node.`val`] = node
        return node
    }

    fun copy(originalNode: Node): Node {
        if (originalNode.`val` in map) {
            return map[originalNode.`val`]!!
        }
        val node = createNewNodeAndRegister(originalNode.`val`)
        originalNode.neighbors
            .filterNotNull()
            .forEach { original ->
                val neighbor = copy(original)
                node.neighbors.add(neighbor)
            }
        return node
    }

    fun cloneGraph(node: Node?): Node? {
        if (node == null) return null
        return copy(node)
    }
}