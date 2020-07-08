# https://leetcode.com/problems/island-perimeter/

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        peri = 0
        for r in xrange(rows):
            for c in xrange(cols):
                if grid[r][c] == 1:
                    peri += 4
                    if r > 0 and grid[r-1][c] == 1: peri -= 2
                    if c > 0 and grid[r][c-1] == 1: peri -= 2

        return peri

def test_01():
    sol = Solution()
    island = [[1], [0]]
    assert sol.islandPerimeter(island) == 4
    island = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
    assert sol.islandPerimeter(island) == 16
    island = [[0,1,1,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
    assert sol.islandPerimeter(island) == 16
    island = [[0,1,1,0]]
    assert sol.islandPerimeter(island) == 6
    island = [[0,1,0,0]]
    assert sol.islandPerimeter(island) == 4
    island = [[0], [0], [1], [0], [0]]
    assert sol.islandPerimeter(island) == 4

if __name__ == '__main__':
    test_01()
