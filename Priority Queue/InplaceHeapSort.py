def downHeapify(arr, index, n):
    parentIndex = index
    leftChild = 2 * parentIndex + 1
    rightChild = 2 * parentIndex + 2
    # n = len(arr)
    while leftChild < n:
        # print(arr)
        # print("Parent Index: ", parentIndex)
        minIndex = parentIndex
        if arr[minIndex] > arr[leftChild]:
            minIndex = leftChild
        if rightChild < n and arr[minIndex] > arr[rightChild]:
            minIndex = rightChild
        if minIndex == parentIndex:
            return None
        arr[parentIndex], arr[minIndex] = arr[minIndex], arr[parentIndex]
        parentIndex = minIndex
        leftChild = 2 * parentIndex + 1
        rightChild = 2 * parentIndex + 2
    # return arr

def heapSort(arr):
    n = len(arr)
    # Buidling inplace heap
    for i in range(n//2 - 1, -1, -1):
        downHeapify(arr, i, len(arr))
    # Soting the heap
    # print(arr)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        downHeapify(arr, 0, i)
        # print(arr)
        # print(arr)


n = input()
arr = [int(ele) for ele in input().split()]
heapSort(arr)
for ele in arr:
    print(ele,end=' ')
