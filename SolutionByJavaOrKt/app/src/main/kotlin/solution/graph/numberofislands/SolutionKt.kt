package solution.graph.numberofislands

class Solution {
    val water = '0'
    val land = '1'
    val directions = sequenceOf(-1 to 0, 0 to 1, 1 to 0, 0 to -1)

    fun numIslands(grid: Array<CharArray>): Int {
        // solution: 섬 -> 물로 빠뜨려버리기
        fun sink(startX: Int, startY: Int) {
            grid[startX][startY] = water
            val q = ArrayDeque<Pair<Int, Int>>().apply { add(startX to startY) }
            while (q.isNotEmpty()) {
                val (x, y) = q.removeFirst()
                directions
                    .map { it.first + x to it.second + y }
                    .filter { it.first in 0..grid.lastIndex && it.second in 0..grid[0].lastIndex }
                    .filter { grid[it.first][it.second] == land }
                    .forEach {
                        grid[it.first][it.second] = water
                        q.add(it)
                    }
            }
        }

        var island = 0
        grid.indices.forEach { i ->
            grid[i].indices.forEach { j ->
                if (grid[i][j] == land) {
                    island += 1
                    sink(i, j)
                }
            }
        }
        return island
    }
}