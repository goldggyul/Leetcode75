package solution.graph.courseschedule

fun main() {
    println(SolutionKt().canFinish(2, arrayOf(intArrayOf(0, 1))))
}

class SolutionKt {

    fun canFinish(numCourses: Int, prerequisites: Array<IntArray>): Boolean {
        val preCount = IntArray(numCourses)
        val nextCourses = List<MutableList<Int>>(numCourses) { mutableListOf() }
        prerequisites.forEach { (next, pre) ->
            preCount[next] += 1
            nextCourses[pre].add(next)
        }
        val q = ArrayDeque<Int>().apply {
            preCount.forEachIndexed { course, count ->
                if (count == 0) {
                    add(course)
                }
            }
        }
        while (q.isNotEmpty()) {
            val cur = q.removeFirst()
            nextCourses[cur].filter { preCount[it] > 0 }
                .forEach {
                    preCount[it] -= 1
                    if (preCount[it] == 0) {
                        q.add(it)
                    }
                }
        }
        return preCount.all { it == 0 }
    }
}