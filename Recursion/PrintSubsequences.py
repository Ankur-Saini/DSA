def printSubsequences(s, output = ""):
    if s == "":
        print(output)
        return
    printSubsequences(s[1:], output)
    printSubsequences(s[1:], output + s[0])


s = input()
printSubsequences(s)