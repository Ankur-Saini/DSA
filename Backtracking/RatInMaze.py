
from os import *
from sys import *
from collections import *
from math import *

ans = []

def isValid(row, col, arr, visited, n):
    if row < 0 or row >=n or col < 0 or col >= n or arr[row][col] == 0 or visited[row][col]:
        return False
    return True

def explore(row, col, arr, visited, n, pathTaken):
    global ans

    if arr[row][col] == 0:
        return 
    if row == (n-1) and col == (n-1):
        ans.append(pathTaken)
        return

    drow = [1, 0, 0, -1]
    dcol = [0, -1, 1, 0]
    dpath = ["D", "L", "R", "U"]

    for i in range(4):
        next_row = row + drow[i]
        next_col = col + dcol[i]
        if isValid(next_row, next_col, arr, visited, n):
            visited[next_row][next_col] = True
            # pathTaken += dpath[i]
            explore(next_row, next_col, arr, visited, n, pathTaken + dpath[i])

            # backtrack
            visited[next_row][next_col] = False
            # pathTaken = pathTaken[:-1]


def searchMaze(arr, n):
    # Write your code here.
    global ans
    ans = []

    visited = [[False for i in range(n)] for i in range(n)]



    

    visited[0][0] = True
    explore(0, 0, arr, visited, n, "")
    return ans
