# https://leetcode.com/problems/word-search/

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row, col = len(board), len(board[0])
        mat = [[0] * col for i in range(row)]
        def dfs(board, r, c, mat, word):
            if not word:
                return True
            elif board[r][c] != word[0]:
                return False
            mat[r][c] = 1
            neighbours = [(nr, nc) for (nr, nc) in [(r+1, c), (r, c+1), (r-1, c),
                            (r, c-1)] if (0 <= nr < row) and (0 <= nc < col) and mat[nr][nc] == 0]
            for (rr, cc) in neighbours:
                if(dfs(board, rr, cc, mat, word[1:])):
                    return True
            if not neighbours and not word[1:]:
                return True
            mat[r][c] = 0
            return False

        for r in range(row):
            for c in range(col):
                if(dfs(board, r, c, mat, word)):
                    return True
        return False

def test_01():
    board = [['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']
            ]
    sol = Solution()
    assert sol.exist(board, "ASADFBCCEESE") == True
    assert sol.exist(board, "ABCCED") == True
    assert sol.exist(board, "SEE") == True
    assert sol.exist(board, "ABCB") == False
    assert sol.exist(board, "") == True
    assert sol.exist(board, "ASADFBCCEESEA") == False
    assert sol.exist(board, "CESCC") == False

if __name__ == '__main__':
    test_01()
