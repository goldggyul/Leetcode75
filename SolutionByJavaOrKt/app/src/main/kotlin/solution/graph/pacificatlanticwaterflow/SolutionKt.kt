package solution.graph.pacificatlanticwaterflow

class Solution {
    fun pacificAtlantic(heights: Array<IntArray>): List<List<Int>> {
        val (row, col) = heights.size to heights[0].size

        val pacific = Array(row) { BooleanArray(col) { false } }
        val atlantic = Array(row) { BooleanArray(col) { false } }

        val dirs = arrayOf(-1 to 0, 0 to 1, 1 to 0, 0 to -1)
        fun flow(ocean: Array<BooleanArray>, x: Int, y: Int) {
            ocean[x][y] = true
            for ((dx, dy) in dirs) {
                val nx = x + dx
                val ny = y + dy
                if (nx !in 0 until row || ny !in 0 until col || ocean[nx][ny] || heights[nx][ny] < heights[x][y]) {
                    continue
                }
                ocean[nx][ny] = true
                flow(ocean, nx, ny)
            }
        }

        // 위 아래
        (0 until col).forEach {
            flow(ocean = pacific, x = 0, y = it)
            flow(ocean = atlantic, x = row - 1, y = it)
        }
        // 왼쪽 오른쪽
        (0 until row).forEach {
            flow(ocean = pacific, x = it, y = 0)
            flow(ocean = atlantic, x = it, y = col - 1)
        }
        return (0 until row).flatMap { i -> (0 until col).map { j -> listOf(i, j) } }
            .filter { (i, j) -> pacific[i][j] && atlantic[i][j] }
    }
}