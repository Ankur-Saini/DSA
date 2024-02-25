def printFactorial(n, ans):
    if n == 0:
        print(ans)
        return
    ans = ans * n
    printFactorial(n-1 , ans)

printFactorial(5, 1)
