def printKeypad(n, output = ""):
    if n == "":
        print(output)
        return
    num = n[0]
    for char in keywords[int(num)]:
        printKeypad(n[1:], output + char)




keywords = {2: ['a','b','c'], 3 : ['d','e','f'], 4: ['g','h','i'], 5: ['j','k','l'], 6: ['m','n','o'], 7: ['p','q','r','s'], 8: ['t','u','v'], 9: ['w','x','y', 'z']}
n = input()
printKeypad(n)