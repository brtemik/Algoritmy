class FibHeap:
    
     
    class Node:
        def __init__(self, data):
            self.data = data
            self.parent = self.child = self.left = self.right = None
            self.degree = 0
            self.mark = False
            
    #функция "пробега" по узлам
    def iterate(self, head):
        node = stop = head
        flag = False
        while True:
            if node == stop and flag is True:
                break
            elif node == stop:
                flag = True
            yield node
            node = node.right
    
    
    root_list, min_node = None, None
    
    
    total_nodes = 0
    
    
    def find_min(self):
        return self.min_node
         
    
    def extract_min(self):
        z = self.min_node
        if z is not None:
            if z.child is not None:
                
                children = [x for x in self.iterate(z.child)]
                for i in range(0, len(children)):                          
                    self.merge_with_root_list(children[i])
                    children[i].parent = None
            self.remove_from_root_list(z)
            
            if z == z.right:
                self.min_node = self.root_list = None
            else:
                self.min_node = z.right
                self.consolidate()
            self.total_nodes -= 1
        return z.data
                    
    
    def insert(self, data):
        n = self.Node(data)
        n.left = n.right = n
        self.merge_with_root_list(n)
        if self.min_node is None or n.data < self.min_node.data:
            self.min_node = n
        self.total_nodes += 1
        
    
    def decrease_key(self, x, k):
        for node in self.iterate(self.root_list):
            
            if node.data ==x:
                
                if k > node.data: 
                    
                    return None
                node.data = k 
                y = node.parent 
                if y is not None and node.data < y.data: 
                    self.cut(node, y)
                    self.cascading_cut(y)
                    
                if node.data < self.min_node.data:
                    self.min_node = node
            else:
                
                if node.child!=None:
                   
                    for node in self.iterate(node.child):
                    
                        if node.data ==x:
                            if k > node.data: 
                                
                                return None
                            node.data = k 
                            y = node.parent 
                            if y is not None and node.data < y.data: 
                                self.cut(node, y)
                                self.cascading_cut(y)
                                
                            if node.data < self.min_node.data:
                                self.min_node = node




                
    def delete(self, x):
       
               
        self.decrease_key(x , float("-inf"))
        self.extract_min()
    
    
    def merge(self, h2):
        H = FibHeap()
        H.root_list, H.min_node = self.root_list, self.min_node
        
        last = h2.root_list.left
        h2.root_list.left = H.root_list.left
        H.root_list.left.right = h2.root_list
        H.root_list.left = last
        H.root_list.left.right = H.root_list
        
        if h2.min_node.data < H.min_node.data:
            H.min_node = h2.min_node
        
        H.total_nodes = self.total_nodes + h2.total_nodes
        return H
        
    
    # если ребенок стал больше родителя, то сы его "срезаем" и помещаем в рутлист
    def cut(self, x, y):
        self.remove_from_child_list(y, x)
        y.degree -= 1
        self.merge_with_root_list(x)
        x.parent = None
        x.mark = False
    
    
    def cascading_cut(self, y):
        z = y.parent
        if z is not None:
            if y.mark is False:
                y.mark = True
            else:
                self.cut(y, z)
                self.cascading_cut(z)
    
    #функция сжатия кучи
    def consolidate(self):
        A = [None] * self.total_nodes
        nodes = [w for w in self.iterate(self.root_list)]
        for w in range(0, len(nodes)):                                      
            x = nodes[w]
            d = x.degree
            while A[d] != None:
                y = A[d] 
                if x.data > y.data:
                    temp = x
                    x, y = y, temp
                self.heap_link(y, x)
                A[d] = None
                d += 1
            A[d] = x
        
        for i in range(0, len(A)):                                        
            if A[i] is not None:
                if A[i].data < self.min_node.data:
                    self.min_node = A[i]
        
    #связывает родителся и ребенка
    def heap_link(self, y, x):
        self.remove_from_root_list(y)
        y.left = y.right = y
        self.merge_with_child_list(x, y)
        x.degree += 1
        y.parent = x
        y.mark = False
        
       
    def merge_with_root_list(self, node):
        if self.root_list is None:
            self.root_list = node
        else:
            node.right = self.root_list.right
            node.left = self.root_list
            self.root_list.right.left = node
            self.root_list.right = node
            
    
    def merge_with_child_list(self, parent, node):
        if parent.child is None:
            parent.child = node
        else:
            node.right = parent.child.right
            node.left = parent.child
            parent.child.right.left = node
            parent.child.right = node
            
    
    def remove_from_root_list(self, node):
        if node == self.root_list:
            self.root_list = node.right
        node.left.right = node.right
        node.right.left = node.left
        
    
    def remove_from_child_list(self, parent, node):
        if parent.child == parent.child.right:
            parent.child = None
            node.parent = None
        elif parent.child == node:
            parent.child = node.right
            node.right.parent = parent
        node.left.right = node.right
        node.right.left = node.left


            
    def printRootList(self, heap):
        rootList = [x.data for x in heap.iterate(heap.root_list)]
        return rootList

    def printChildren(self, heap):
        children = []
        for x in heap.iterate(heap.root_list):
            
            
                
            self.recurs(x,children)
                
        return children


      
    
    def recurs(self,x,chlist):
        if x.child !=None:
            y = x.child
            chlist.append([x.data,'->',y.data])
            if y.child !=None:
                self.recurs(y,chlist)
                
            else:
                first = y
                while y.right != first:
                    y = y.right
                    chlist.append([y.parent.data,'->',y.data])
                    self.recurs(y, chlist)
                    

    def printEverything(self, heap):
        print(self.printRootList(heap))
        print(self.printChildren(heap))


def buildHeap(heap, heaplist):
    for node in heaplist:
        heap.insert(node)
    return heap


