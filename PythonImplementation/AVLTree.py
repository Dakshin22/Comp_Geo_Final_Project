#import random, math

outputdebug = False

def debug(msg):
    if outputdebug:
        print (msg)

class Node():
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None 

class AVLTree():
    def __init__(self, *args):
        self.node = None 
        self.height = -1  
        self.balance = 0; 
        
        if len(args) == 1: 
            for i in args[0]: 
                self.insert(i)

    def swapEdges(self, edge1, edge2, currY):
        #print("before", "to delete ", edge1)
        #self.display(currY=currY)
        self.delete(edge1, currY-0.01)
        #print("after")
        #self.display(currY=currY)
        self.delete(edge2, currY-0.01)
        #if self.find(edge1, currY):
        #    print("didno't delete")
        #if self.find(edge2, currY):
        #    print("didn't delte 2")
        print("before insertion", self.inorder_traverse())
        self.insert(edge2, currY + 0.03)
        self.insert(edge1, currY + 0.03)
        print("in swap", self.inorder_traverse())
        A = self.find(edge1, currY+ 0.03)

        print("didn't insert", A.key)
        B = self.find(edge2, currY+ 0.03)

        print("didn't insert2", B.key)

    def height(self):
        if self.node: 
            return self.node.height 
        else: 
            return 0 
    
    def is_leaf(self):
        return (self.height == 0) 
    
    def find(self, key, currY):
        tree = self.node
        if tree == None:
            return tree
        elif getXValue(key, currY) < getXValue(tree.key, currY): 
            return tree.left.find(key, currY)
        elif getXValue(key, currY) > getXValue(tree.key, currY): 
            return tree.right.find(key, currY)   
        else: 
            return tree

    def insert(self, key, currY):

        tree = self.node
        
        newnode = Node(key)
        
        if tree == None:
            self.node = newnode 
            self.node.left = AVLTree() 
            self.node.right = AVLTree()
            debug("Inserted key [" + str(key) + "]")
        
        elif getXValue(key, currY) < getXValue(tree.key, currY): 
            self.node.left.insert(key, currY)
            
        elif getXValue(key, currY) > getXValue(tree.key, currY): 
            self.node.right.insert(key, currY)
        
        else: 
            debug("Key [" + str(key) + "] already in tree.")
            
        self.rebalance() 
        
    def rebalance(self):
        ''' 
        Rebalance a particular (sub)tree
        ''' 
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.node.left.balance < 0:  
                    self.node.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()
                
            if self.balance < -1:
                if self.node.right.balance > 0:  
                    self.node.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()
 
    def rrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' right') 
        A = self.node 
        B = self.node.left.node 
        T = B.right.node 
        
        self.node = B 
        B.right.node = A 
        A.left.node = T 

    
    def lrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' left') 
        A = self.node 
        B = self.node.right.node 
        T = B.left.node 
        
        self.node = B 
        B.left.node = A 
        A.right.node = T 

    def update_heights(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()
            
            self.height = max(self.node.left.height,
                              self.node.right.height) + 1 
        else: 
            self.height = -1 

    def update_balances(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height 
        else: 
            self.balance = 0 

    def delete(self, key, currY):
        debug("Trying to delete at node: " + str(self.node.key))
        if self.node != None: 
            if getXValue(self.node.key, currY) == getXValue(key, currY): 
                debug("Deleting ... " + str(key))  
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None # leaves can be killed at will 
                # if only one subtree, take that 
                elif self.node.left.node == None: 
                    self.node = self.node.right.node
                elif self.node.right.node == None: 
                    self.node = self.node.left.node
                
                # worst-case: both children present. Find logical successor
                else:  
                    replacement = self.logical_successor(self.node)
                    if replacement != None: # sanity check 
                        debug("Found replacement for " + str(key) + " -> " + str(replacement.key))  
                        self.node.key = replacement.key 
                        
                        # replaced. Now delete the key from right child 
                        self.node.right.delete(replacement.key, currY)
                    
                self.rebalance()
                return  
            elif getXValue(key, currY) < getXValue(self.node.key, currY): 
                self.node.left.delete(key, currY)  
            elif getXValue(key, currY) > getXValue(self.node.key, currY): 
                self.node.right.delete(key, currY)
                        
            self.rebalance()
        else: 
            return 
    
    def logical_predecessor(self, node):
        ''' 
        Find the biggest valued node in LEFT child
        ''' 
        node = node.left.node 
        if node != None: 
            while node.right != None:
                if node.right.node == None: 
                    return node 
                else: 
                    node = node.right.node  
        return node 

    def logical_successor(self, node):
        ''' 
        Find the smallese valued node in RIGHT child
        ''' 
        node = node.right.node  
        if node != None: # just a sanity check  
            
            while node.left != None:
                debug("LS: traversing: " + str(node.key))
                if node.left.node == None: 
                    return node 
                else: 
                    node = node.left.node  
        return node 

    def check_balanced(self):
        if self == None or self.node == None: 
            return True
        
        # We always need to make sure we are balanced 
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())  
    
    def predecessor(self, edge):
        inOrder = self.inorder_traverse()
        idx = inOrder.index(edge)
        if idx > 0:
            predIdx = idx - 1
            return inOrder[predIdx]
        else:
            return None

    def successor(self, edge):
        inOrder = self.inorder_traverse()
        print(edge, inOrder)
        idx = inOrder.index(edge)
        if idx < len(inOrder) - 1:
            sucIdx = idx + 1
            return inOrder[sucIdx]
        else:
            return None


    def inorder_traverse(self):
        if self.node == None:
            return [] 
        
        inlist = [] 
        l = self.node.left.inorder_traverse()
        for i in l: 
            inlist.append(i) 

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l: 
            inlist.append(i) 
    
        return inlist 

    def display(self, currY, level=0, pref=''):
        '''
        Display the whole tree. Uses recursive def.
        TODO: create a better display using breadth-first search
        '''        
        self.update_heights()  # Must update heights before balances 
        self.update_balances()
        if(self.node != None): 
            print ('-' * level * 2, pref, self.node.key, getXValue(self.node.key, currY),"[" + str(self.height) + ":" + str(self.balance) + "]", 'L' if self.is_leaf() else ' '    )
            if self.node.left != None: 
                self.node.left.display(currY=currY, level=level + 1, pref='<')
            if self.node.left != None:
                self.node.right.display(currY = currY, level=level + 1, pref='>')

def getXValue(segment, yVal):
    slope = (segment.p1.y - segment.p0.y) / (segment.p1.x - segment.p0.x)
    return round(((yVal - segment.p1.y) / slope) + segment.p1.x, 2)
# Usage example
if __name__ == "__main__": 
    a = AVLTree()
    print ("----- Inserting -------")
    #inlist = [5, 2, 12, -4, 3, 21, 19, 25]
    inlist = [7, 5, 2, 6, 3, 4, 1, 8, 9, 0]
    for i in inlist: 
        a.insert(i)
         
    a.display()
    
    print ("----- Deleting -------")
    a.delete(3)
    a.delete(4)
    # a.delete(5) 
    a.display()
    
    print ()
    print ("Input            :", inlist )
    print ("deleting ...       ", 3)
    print ("deleting ...       ", 4)
    print ("Inorder traversal:", a.inorder_traverse())