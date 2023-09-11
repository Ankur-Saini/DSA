import heapq
def kSmallest(lst, k):
    ######################
    #PLEASE ADD CODE HERE#
    ######################
    firstKElements = lst[:k]
    heapq._heapify_max(firstKElements)
    n = len(lst)
    for i in range(k, n):
        if firstKElements[0] > lst[i]:
            heapq._heapreplace_max(firstKElements, lst[i])
    return firstKElements

# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
ans.sort()
print(*ans, sep=' ')
# print(ans)