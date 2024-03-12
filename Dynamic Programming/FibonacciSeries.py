
# Recursive bottom up approach
def fibo(n):
    if n == 0 or n == 1:
        return n
    elif memo[n] != -1:
        return memo[n]
    else:
        memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]
    
# Iterative bottom up approach
def iterative(n):
    # dp[0] = 0
    # dp[1] = 1
    for i in range(2, n+1):
        if i == 0 or i == 1:
            dp[i] = i
        else:
            dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

n = int(input())
memo = [-1] * (n+1)
dp = [-1] * (n+1)
print(str(n) + "th fibonacci number is: " + str(fibo(n)))
print(str(n) + "th fibonacci number is: " + str(fibo(n)))
