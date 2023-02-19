package solution.graph.aliendictionary

fun main() {
    println(Solution().alienOrder(arrayOf("ac", "ab", "zc", "zb")))
}

class Solution {
    fun alienOrder(words: Array<String>): String {
        val indegree = HashMap<Char, Int>()
        val outdegree = HashMap<Char, MutableList<Char>>()

        words.flatMap { it.toCharArray().asIterable() }.forEach {
            indegree[it] = 0
            outdegree[it] = mutableListOf()
        }

        for (i in 0 until words.lastIndex) {
            val before = words[i]
            val after = words[i + 1]
            if ((before.length > after.length) && before.startsWith(after)) {
                return ""
            }
            for ((b, a) in before.zip(after)) {
                if (b == a) {
                    continue
                }
                if (a !in outdegree[b].orEmpty()) {
                    outdegree[b]?.add(a)
                    indegree[a] = indegree[a]!! + 1
                }
                break
            }
        }

        val q = ArrayDeque(indegree.filter { it.value == 0 }.keys)
        val ans = buildString {
            while (q.isNotEmpty()) {
                val letter = q.removeFirst()
                append(letter)
                outdegree[letter]?.forEach {
                    indegree[it] = indegree[it]!! - 1
                    if (indegree[it] == 0) {
                        q.add(it)
                    }
                }
            }
        }
        if (ans.length < indegree.size) {
            return ""
        }
        return ans
    }
}