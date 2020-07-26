# https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        end = len(graph) - 1
        def dfs(start, path):
            path.append(start)
            if start == end:
                res.append(path[::])
                path.pop()
                return
            for i in graph[start]:
                dfs(i, path)
            path.pop()
        dfs(0, [])
        return res
