package solution.graph.courseschedule;

import java.util.*;
import java.util.stream.IntStream;

class SolutionJava {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] inDegree = new int[numCourses];
        Map<Integer, List<Integer>> outDegree = new HashMap<>();
        for (int[] req : prerequisites) {
            inDegree[req[0]] += 1;
            if (outDegree.containsKey(req[1])) {
                outDegree.get(req[1]).add(req[0]);
            } else {
                outDegree.put(req[1], new ArrayList<>(List.of(req[0])));
            }
        }
        Queue<Integer> q = new LinkedList<>();
        IntStream.range(0, numCourses)
                .filter(course -> inDegree[course] == 0)
                .forEach(q::add);
        while (!q.isEmpty()) {
            int cur = q.poll();
            if (!outDegree.containsKey(cur))
                continue;
            outDegree.get(cur).stream()
                    .filter(next -> inDegree[next] > 0)
                    .forEach(next -> {
                        inDegree[next] -= 1;
                        if (inDegree[next] == 0) {
                            q.add(next);
                        }
                    });
        }
        return Arrays.stream(inDegree).allMatch(degree -> degree == 0);
    }
}