


keywords = {2: ['a','b','c'], 3 : ['d','e','f'], 4: ['g','h','i'], 5: ['j','k','l'], 6: ['m','n','o'], 7: ['p','q','r','s'], 8: ['t','u','v'], 9: ['w','x','y', 'z']}
def keypad(n):
    #Implement Your Code Here
    if n == 0:
        return [""]
    last_integer = n % 10
    smaller_integer = n // 10
    sub_list = keypad(smaller_integer)
    length = len(sub_list)
    final_list = list()
    for char in keywords[last_integer]:
        for i in range(length):
            final_list.append(sub_list[i] + char)
    return final_list
    

n = int(input())
ans = keypad(n)
for s in ans:
    print(s)
