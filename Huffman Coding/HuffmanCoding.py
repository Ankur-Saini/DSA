import heapq

class BinaryTreeNode:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq
    
    def __eq__(self, other):
        return self.freq == other.freq

class HuffmanCoding:
    def __init__(self,path):
        self.path = path
        self.__heap = []
        self.__codes = {}
        
    def __make_frequency_dict(self, text):
        freq_dict = {}
        for char in text:
            if char not in freq_dict:
                freq_dict[char] = 0
            freq_dict[char] += 1
        return freq_dict
    
    def __buildHeap(self, freq_dict):
        for key in freq_dict:
            frequency = freq_dict[key]
            newNode = BinaryTreeNode(key, frequency)
            heapq.push(self.__heap, newNode)
    
    def __buildTree(self):
        while len(self.__heap) > 1:
            binary_tree_node_1 = heapq.heappop(self.__heap)
            binary_tree_node_2 = heapq.heappop(self.__heap)
            freq_sum = binary_tree_node_1.freq + binary_tree_node_2.freq
            new_binary_tree_node = BinaryTreeNode(None, freq_sum)
            new_binary_tree_node.left = binary_tree_node_1
            new_binary_tree_node.right = binary_tree_node_2
            heapq.heapify(self.__heap, new_binary_tree_node)
        return
    
    def __buildCodesHelper(self, root, curr_bits):
        if root == None:
            return None
        if root.value is not None:
            self.__codes[root.value] = curr_bits
        self.__buildCodesHelper(root.left, curr_bits + "0")
        self.__buildCodesHelper(root.right, curr_bits + "1")
    
    def __buildCodes(self):
        root = heapq.heappop(self.__heap)
        self.__buildCodesHelper(root, "")
    
    def compress(self):
        #get file from path
        #read text from file

        text = "fasbsajfhbsafjhbashf"

        #make frequency dictionary using the text
        freq_dict = self.__make_frequency_dict(text)

        #construct the heap from the frequency_dict
        self.__buildHeap(freq_dict)
        
        #construct the binary tree from the heap
        self.__buildTree()
        
        #creating the encoded text using the codes
        self.__buildCodes()
        
        #put this encoded text into the binary file
        
        #return the binary file as output
        
        pass