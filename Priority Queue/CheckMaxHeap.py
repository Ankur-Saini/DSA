


# import heapq
def checkMaxHeap(lst):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    # maxHeap = lst[::]
    # heapq._heapify_max(maxHeap)
    # n = len(lst)
    # for i in range(n):
    #     if maxHeap[i] != lst[i]:
    #         return False
    # return True
    n = len(lst)
    for i in range(n//2):
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2
        if lst[i] < lst[leftChild]:
            return False
        elif rightChild < n and lst[i] < lst[rightChild]:
            return False
    return True


# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')
