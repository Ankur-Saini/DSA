
import heapq
def kLargest(lst, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    firstKElemnts = lst[:k]
    heapq.heapify(firstKElemnts)
    n = len(lst)
    for i in range(k,n):
        if firstKElemnts[0] < lst[i]:
            heapq.heapreplace(firstKElemnts, lst[i])
    return firstKElemnts

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kLargest(lst, k)
print(*ans, sep='\n')
