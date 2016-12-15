class BinHeap:
    def __init__(self):
        self.heaplist = []
        self.heapsize = 0

    def left(self, i):
        return i * 2 + 1

    def right(self, i):
        return i * 2 + 2

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l <= self.heapsize and self.heaplist[l] > self.heaplist[i]:
            largest = l
        else:
            largest = i
        if r <= self.heapsize and self.heaplist[r] > self.heaplist[largest]:
            largest = r
        if largest != i:  
            tmp = self.heaplist[i]
            self.heaplist[i] = self.heaplist[largest]
            self.heaplist[largest] = tmp
            self.heapify(largest)

    def buildHeap(self, list):
        self.heaplist = list
        self.heapsize = len(list) - 1
        for i in range(len(list) // 2, -1, -1):
            self.heapify(i)

    
    def findMax(self):
        return self.heaplist[0]

    def getHeap(self):
        return self.heaplist

    def insert(self,x):
        self.heaplist.append(x)
        self.heapsize = self.heapsize + 1
        for i in range(len(self.heaplist) //2,-1,-1):
            self.heapify(i)

    def extractMax(self):
        self.heaplist[0] = self.heaplist[self.heapsize]
        self.heaplist.pop()
        self.heapsize = self.heapsize - 1
        for i in range(len(self.heaplist) //2,-1,-1):
            self.heapify(i)
            
    def changeKey(self,x,y):
        if x in self.heaplist:
            self.heaplist[self.heaplist.index(x)] = y
            for i in range(len(self.heaplist) //2,-1,-1):
                self.heapify(i)
            

    
        
    def delete(self, x):
        self.changeKey(x, float("inf"))
        self.extractMax()
        
