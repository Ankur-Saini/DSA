import os
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
    def __init__(self, path):
        self.path = path
        self.__heap = []
        self.__codes = {}
        self.__reverseCodes = {}

    def __make_freq_dict(self, text):
        freqDict = {}
        for char in text:
            if char not in freqDict:
                freqDict[char] = 0
            freqDict[char] += 1
        return freqDict
    
    def __make_heap(self, freqDict):
        for char in freqDict:
            frequency = freqDict[char]
            newNode = BinaryTreeNode(char, frequency)
            heapq.heappush(self.__heap, newNode)
    
    def __build_tree(self):
        while (len(self.__heap) > 1):
            leftNode = heapq.heappop(self.__heap)
            rightNode = heapq.heappop(self.__heap)
            totalFreq = leftNode.freq + rightNode.freq
            newNode = BinaryTreeNode(None, totalFreq)
            newNode.left = leftNode
            newNode.right = rightNode
            heapq.heappush(self.__heap, newNode)
        return
    
    def __build_codes_helper(self, root, currBits):

        if root is None:
            return None
        if root.value is not None:
            self.__codes[root.value] = currBits
            self.__reverseCodes[currBits] = root.value
            return

        self.__build_codes_helper(root.left, currBits + '0')
        self.__build_codes_helper(root.right, currBits + '1')
    
    def __build_codes(self):
        root = heapq.heappop(self.__heap)
        self.__build_codes_helper(root, '')
    
    def __get_encoded_text(self, text):
        encodedText = ""
        for char in text:
            encodedText += self.__codes[char]
        return encodedText
    
    def __get_padded_encoded_text(self, encodedText):
        paddedAmount = 8 - (len(encodedText) % 8)
        for i in range(paddedAmount):
            encodedText += '0'
        
        paddedInfo = "{0:08b}".format(paddedAmount)
        paddedEncodedText = paddedInfo + encodedText
        return paddedEncodedText
    
    def __get_bytes_array(self, paddedEncodedText):
        array = []
        for i in range(0, len(paddedEncodedText), 8):
            byte = paddedEncodedText[i:i+8]
            array.append(int(byte, 2))
        return array
    
    def compress(self):
        fileName, fileExtension = os.path.splitext(self.path)
        outputPath = fileName + ".bin"
        
        with open(self.path, 'r+') as file, open(outputPath, 'wb') as output:
            # Get file from path
            # Read text from file
            text = file.read()
            text = text.rstrip()

            # Make a frequency dictionary
            freqDict = self.__make_freq_dict(text)

            # Construct a heap from the freq dictionary
            self.__make_heap(freqDict)

            # Construct a binary tree from the heap
            self.__build_tree()

            # Create code for characters 
            self.__build_codes()

            # create the encoded text
            encodedText = self.__get_encoded_text(text)

            # put the encoded text into the binary file
            paddedEncodedText = self.__get_padded_encoded_text(encodedText)

            # return the binary file as output
            bytesArray = self.__get_bytes_array(paddedEncodedText)
            finalBytes = bytes(bytesArray)
            output.write(finalBytes)
        print("Compressed")
        return outputPath
    
    def __remove_padding(self, text):
        paddedInfo = text[:8]
        extraPadding = int(paddedInfo, 2)

        text = text[8:]
        textWithoutPadding = text[:-1 * extraPadding]
        return textWithoutPadding
    
    def __decode_text(self, text):
        # bitCodes = {v:k for k,v in self.__codes.items()}
        decodedText = ""
        currentBits = ""
        for bit in text:
            currentBits += bit
            if currentBits in self.__reverseCodes:
                char = self.__reverseCodes[currentBits]
                decodedText += char
                currentBits = ""
        return decodedText
    
    def decompress(self, inputPath):
        fileName, fileExtension = os.path.splitext(inputPath)
        outputPath = fileName + "_decompressed" + ".txt"
        with open(inputPath, 'rb') as file, open(outputPath, 'w') as output:
            bitString = ""
            byte = file.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bitString += bits
                byte = file.read(1)
            actualText = self.__remove_padding(bitString)
            decompressedText = self.__decode_text(actualText)
            output.write(decompressedText)
        return 

path = "/Users/ankursaini/Desktop/text.txt"
h = HuffmanCoding(path)
outputPath = h.compress()
h.decompress(outputPath)


