# https://leetcode.com/problems/course-schedule-ii/

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        mat = [[0] * numCourses for i in range(numCourses)]
        no_incoming = list(range(numCourses))
        for row, col in prerequisites:
            mat[row][col] = 1
            if row in no_incoming:
                no_incoming.remove(row)
        res = []
        while len(no_incoming) != 0:
            n = no_incoming.pop(0)
            res.append(n)
            for m in range(numCourses):
                if mat[m][n] == 1:
                    mat[m][n] = 0
                    if 1 not in mat[m]:
                        no_incoming.append(m)
        for row in mat:
            if 1 in row:
                return []
        return res

def test_01():
    sol = Solution()
    assert sol.findOrder(2, [[1, 0]]) == [0, 1]
    assert sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3]
    #assert sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 2, 1, 3]
    assert sol.findOrder(2, [[1, 0], [0, 1]]) == []

if __name__ == '__main__':
    test_01()
