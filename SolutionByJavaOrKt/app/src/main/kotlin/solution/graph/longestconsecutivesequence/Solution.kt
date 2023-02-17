package solution.graph.longestconsecutivesequence

class Solution {
    fun longestConsecutive(nums: IntArray): Int {
        val set = nums.toHashSet()
        var answer = 0
        nums.filter { !set.contains(it - 1) }
            .forEach {
                var cur = it
                var length = 0
                while (set.contains(cur)) {
                    length += 1
                    cur += 1
                }
                answer = maxOf(answer, length)
            }
        return answer
    }
}