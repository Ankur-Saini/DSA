
class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Map:
    def __init__(self):
        self.buckets = [None] * 10
        self.bucketSize = 5
        self.count = 0

    def getCount(self):
        return self.count

    def getIndex(self, hc):
        return (abs(hc)%self.bucketSize)
    
    def insertKeyValue(self, key, value):
        hc = hash(key)
        index = self.getIndex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next
        head = self.buckets[index]
        newNode = MapNode(key, value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count += 1
        if self.count / self.bucketSize >= 0.7:
            self.rehash()
    
    def getValue(self, key):
        hc = hash(key)
        index = self.getIndex(hc)
        head = self.buckets[index]
        while head != None:
            if head.key == key:
                return head.value
            head = head.next
        return None
    
    # def deleteKey(self, key):
        hc = hash(key)
        index = self.getIndex(hc)
        head = self.buckets[index]
        while head is not None:
            if self.buckets[index].key == key:
                self.buckets[index] = head.next
                self.count -= 1
                return
            if head.next.key == key:
                head.next = head.next.next
                self.count -= 1
                return
        return None

    def deleteKey(self, key):
        hc = hash(key)
        index = self.getIndex(hc)
        head = self.buckets[index]
        prev = None
        while head is not None:
            if head.key == key:
                if prev is None:
                    self.buckets[index] = head.next
                else:
                    prev.next = head.next
                self.count -= 1
                return (head.key, head.value)
            prev = head
            head = head.next
        return None
    
    def loadFactor(self):
        return self.count / self.bucketSize

    def rehash(self):
        temp = self.buckets
        self.buckets = [None] * (2 * self.bucketSize)
        self.bucketSize *= 2
        self.count = 0
        for head in temp:
            while head is not None:
                self.insertKeyValue(head.key, head.value)
                head = head.next

hashMap = Map()
for i in range(10):
    hashMap.insertKeyValue("abc" + str(i), i+1)
    print(hashMap.loadFactor())

for i in range(10):
    print("abc" + str(i) + ": " + str(hashMap.getValue("abc" + str(i))))

# hashMap.insertKeyValue("Max", 10)
# hashMap.insertKeyValue("Checo", 5)
# hashMap.insertKeyValue("Lewis", 2)
# print(hashMap.getCount())
# print(hashMap.getValue("Max"))
# print(hashMap.getValue("Checo"))
# print(hashMap.getValue("Lewis"))
# print(hashMap.deleteKey("Checo"))
# print(hashMap.getValue("Checo"))
# print(hashMap.getCount())
# hashMap.deleteKey("Max")
# print(hashMap.getValue("Max"))
# print(hashMap.getCount())
# print(hashMap.getValue("Lewis"))
# hashMap.deleteKey("Lewis")
# print(hashMap.getCount())
