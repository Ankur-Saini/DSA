

def printKeypad(n, output = ""):
    if n == 0:
        print(output)
        return 
    last_digit = n % 10
    smaller_num = n // 10
    for char in keywords[last_digit]:
        printKeypad(smaller_num, char + output)



keywords = {2: ['a','b','c'], 3 : ['d','e','f'], 4: ['g','h','i'], 5: ['j','k','l'], 6: ['m','n','o'], 7: ['p','q','r','s'], 8: ['t','u','v'], 9: ['w','x','y', 'z']}
n = int(input())
printKeypad(n)
