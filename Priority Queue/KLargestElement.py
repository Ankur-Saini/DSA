import heapq
def kthLargest(lst, k):
    ######################
    #PLEASE ADD CODE HERE#
    ######################
    firstKElements = lst[:k]
    heapq.heapify(firstKElements)
    n = len(lst)
    for i in range(k,n):
        if firstKElements[0] < lst[i]:
            heapq.heapreplace(firstKElements, lst[i])
    return firstKElements[0]


# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)