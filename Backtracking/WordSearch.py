from typing import List

def isValid(row, col, board, visited, k, word, n, m):
    if row < 0 or row >= n or col < 0 or col >= m or visited[row][col] or board[row][col] != word[k]:
        return False
    return True

def constructWord(row, col, board, visited, k, word, n, m):
    if k == len(word):
        return True
    
    if row == n-1 and col == n-1:
        return False

    drow = [1, 0, 0, -1]
    dcol = [0, -1, 1, 0]
    dpath = ["D", "L", "R", "U"]

    # Backtracking
    for i in range(4):
        next_row = row + drow[i]
        next_col = col + dcol[i]
        if isValid(next_row, next_col, board, visited, k, word, n, m):
            visited[next_row][next_col] = True
            ans = constructWord(next_row, next_col, board, visited, k+1, word, n, m)
            if ans:
                return True
            visited[next_row][next_col] = False


def present(board: List[List[str]], word: str, n: int, m: int) -> bool:
    # Write your code here
    visited = [[False for i in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == word[0]:
                ans = constructWord(i, j, board, visited, 1, word, n, m)
                if ans:
                    return True
    return False
                
