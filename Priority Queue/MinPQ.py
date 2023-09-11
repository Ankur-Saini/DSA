class PriorityQueueNode:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def getSize(self):
        return len(self.pq)
    
    def isEmpty(self):
        return self.getSize == 0
    
    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].value
    
    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex - 1) // 2
            if self.pq[childIndex].priority < self.pq[parentIndex].priority:
                self.pq[childIndex], self.pq[parentIndex] = self.pq[parentIndex], self.pq[childIndex]
                childIndex = parentIndex
            else:
                break

    def insert(self, value, priority):
        pqNode = PriorityQueueNode(value, priority)
        self.pq.append(pqNode)
        self.__percolateUp()

    # def __percolateDown(self):
    #     parentIndex = 0
    #     self.pq[0] = self.pq.pop()
    #     n = self.getSize()
    #     while parentIndex < n:
    #         leftChild = 2 * parentIndex + 1
    #         rightChild = 2 * parentIndex + 2
    #         print("LC: ", leftChild)
    #         print("RC: ", rightChild)
    #         if leftChild > n and rightChild > n:
    #             break
    #         elif leftChild < n and rightChild > n:
    #             self.pq[leftChild], self.pq[parentIndex] = self.pq[parentIndex], self.pq[leftChild]
    #             parentIndex = leftChild
    #             continue
    #         elif leftChild > n and rightChild < n:
    #             self.pq[rightChild], self.pq[parentIndex] = self.pq[parentIndex], self.pq[rightChild]
    #             parentIndex = rightChild
    #             continue
    #         elif self.pq[leftChild].priority < self.pq[rightChild].priority:
    #             minIndex = leftChild
    #         else:
    #             minIndex = rightChild
    #         if self.pq[parentIndex].priority > self.pq[minIndex].priority:
    #             self.pq[parentIndex], self.pq[minIndex] = self.pq[minIndex], self.pq[parentIndex]
    #             parentIndex = minIndex
    #             continue
    #         else:
    #             break

    # def __percolateDown(self):
    #     parentIndex = 0
    #     n = self.getSize()
    #     while parentIndex < n:
    #         leftChild = 2 * parentIndex + 1
    #         rightChild = 2 * parentIndex + 2
    #         if leftChild >= n:
    #             break
    #         elif rightChild >= n:
    #             minIndex = leftChild
    #         else:
    #             if self.pq[leftChild].priority < self.pq[rightChild].priority:
    #                 minIndex = leftChild
    #             else:
    #                 minIndex = rightChild
    #         if self.pq[minIndex].priority < self.pq[parentIndex].priority:
    #             self.pq[minIndex], self.pq[parentIndex] = self.pq[parentIndex], self.pq[minIndex]
    #             parentIndex = minIndex

    def __percolateDown(self):
        parentIndex = 0
        leftChild = 2 * parentIndex + 1
        rightChild = 2 * parentIndex + 2
        n = self.getSize()
        while leftChild < n:
            minIndex = parentIndex
            if self.pq[minIndex].priority > self.pq[leftChild].priority:
                minIndex = leftChild
            if rightChild < n and self.pq[minIndex].priority > self.pq[rightChild].priority:
                minIndex = rightChild
            if minIndex == parentIndex:
                break
            self.pq[minIndex], self.pq[parentIndex] = self.pq[parentIndex], self.pq[minIndex]
            parentIndex = minIndex
            leftChild = 2 * parentIndex + 1
            rightChild = 2 * parentIndex + 2


    def remove(self):
        deletedValue = self.pq[0].value
        self.pq[0] = self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return deletedValue
    
minPQ = PriorityQueue()
# minPQ.insert(1, 10)
# minPQ.insert(2, 15)
# minPQ.insert(3, 25)
# minPQ.insert(4, 37)
# minPQ.insert(5, 43)
# print([x.priority for x in minPQ.pq])
# minPQ.insert(6, 77)
# print([x.priority for x in minPQ.pq])
# print("Delted element: ", minPQ.remove())
# print("Size: ", minPQ.getSize())
# print("Minimum value: ", minPQ.getMin())
# print([x.priority for x in minPQ.pq])
# minPQ.insert(1, 10)
# minPQ.insert(2, 20)
# minPQ.insert(3, 30)
# minPQ.insert(4, 60)
# minPQ.insert(5, 100)
# print([x.priority for x in minPQ.pq])
# print("Delted element: ", minPQ.remove())
# print("Size: ", minPQ.getSize())
# print("Minimum value: ", minPQ.getMin())
# print([x.priority for x in minPQ.pq])
minPQ.insert('A', 10)
minPQ.insert('C', 5)
minPQ.insert('B', 19)
minPQ.insert('D', 4)
for i in range(4):
    print(minPQ.remove())