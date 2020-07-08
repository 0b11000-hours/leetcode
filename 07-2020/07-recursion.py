# https://leetcode.com/problems/island-perimeter/

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def perimeter(x, y, lenx, leny, grid, visited):
            neighbours = [(nx, ny) for (nx, ny) in [(x+1, y), (x, y+1), (x-1,
                            y), (x, y-1)] if (0 <= nx < lenx) and (0 <= ny < leny) and grid[ny][nx] == 1]
            this_peri = 4 - len(neighbours)
            visited[y][x] = 1
            for (xx, yy) in neighbours:
                if visited[yy][xx] == 1:
                    continue
                this_peri += perimeter(xx, yy, lenx, leny, grid, visited)
            return this_peri

        leny = len(grid)
        lenx = len(grid[0])
        def find_one(grid):
            for xx in xrange(lenx):
                for yy in xrange(leny):
                    if grid[yy][xx] == 1:
                        return (xx, yy)
        xx, yy = find_one(grid)
        visited = [[0] * lenx for i in xrange(leny)]
        res = perimeter(xx, yy, lenx, leny, grid, visited)
        return res

def test_01():
    sol = Solution()
    #island = [[1], [0]]
    #assert sol.islandPerimeter(island) == 4
    island = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
    assert sol.islandPerimeter(island) == 16

    #island = [[0,1,1,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
    #assert sol.islandPerimeter(island) == 16
    #island = [[0,1,1,0]]
    #assert sol.islandPerimeter(island) == 6
    island = [[0,1,0,0]]
    assert sol.islandPerimeter(island) == 4
    island = [[0], [0], [1], [0], [0]]
    assert sol.islandPerimeter(island) == 4

if __name__ == '__main__':
    test_01()
