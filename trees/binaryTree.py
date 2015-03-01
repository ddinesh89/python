class BinaryTree(object):
    def __init__(self,value) :
        self.value = value
        self.leftBranch = None
        self.rightBranch = None
        self.parent = None
        
    def setLeftBranch(self,node) :
        self.leftBranch = node
        node.parent = self
    
    def setRightBranch(self,node) :
        self.rightBranch = node
        node.parent = self
    
    def setParent(self,node) :
        self.parent = node
        
    def getValue(self) :
        return self.value
        
    def getLeftBranch(self) :
        return self.leftBranch
    
    def getRightBranch(self) :
        return self.rightBranch
    
    def getParent(self) :
        return self.parent
    
    def __str__(self) :
        return self.value
        
#create the tree nodes
n5 = BinaryTree(5)
n2 = BinaryTree(2)
n1 = BinaryTree(1)
n4 = BinaryTree(4)
n8 = BinaryTree(8)
n6 = BinaryTree(6)
n7 = BinaryTree(7)
n3 = BinaryTree(3)

#assign the branches
n5.setLeftBranch(n2)
n5.setRightBranch(n8)
n2.setLeftBranch(n1)
n2.setRightBranch(n4)
n8.setLeftBranch(n6)
n6.setRightBranch(n7)
n4.setLeftBranch(n3)

def equality(node,value) :
    """ returns True if node.value equals
    given value. Takes a tree's node and int
    as arguments"""
    return node.getValue() == value

def lesserFn(node,value) :
    """ returns True if given value is
    lesser than node.value. Takes a tree's node and int
    as arguments"""
    return value < node.getValue()

def traceRoute(node) :
    """ Prints the route to reach the given
    tree node"""
    if not node.getParent() :
        return [node]
    else :
        return [node] + traceRoute(node.getParent())

def DFSBinaryTree(root,value) :
    """ Depth first search of a given tree
    given the starting node to search from 
    and the value to search for"""
    stack = [root]
    while len(stack) > 0 :
        print "Node at "+ str(stack[0].getValue())
        if equality(stack[0],value) :
            return True
        else :
            temp = stack.pop(0)
            if temp.getRightBranch() :
                stack.insert(0,temp.getRightBranch())
            if temp.getLeftBranch() :
                stack.insert(0,temp.getLeftBranch())
    return False
    
def BFSBinaryTree(root,value) :
    """ breadth first seach of a given tree
    given the starting node to search from
    and the value to search for"""
    queue = [root]
    while len(queue) > 0 :
        print "Node at "+ str(queue[0].getValue())
        if equality(queue[0],value) :
            return True
        else :
            temp = queue.pop(0)
            if temp.getLeftBranch() :
                queue.append(temp.getLeftBranch())
            if temp.getRightBranch() :
                queue.append(temp.getRightBranch())
    return False

def DFSOrderedBinaryTree(root,value) :
    """ Depth first search of a given ordered tree
    given the starting node to search from 
    and the value to search for"""
    stack = [root]
    while len(stack) > 0 :
        print "Node at "+ str(stack[0].getValue())
        if equality(stack[0],value) :
            return True
        else :
            temp = stack.pop(0)
            if lesserFn(temp,value) :
                if temp.getLeftBranch() :
                    stack.insert(0,temp.getLeftBranch())
            else :
                if temp.getRightBranch() :
                    stack.insert(0,temp.getRightBranch())
    return False
    
def DFSOrderedBinaryTreeWithPath(root,value) :
    """ Depth first search along with path to reach of a given ordered tree
    given the starting node to search from 
    and the value to search for"""
    stack = [root]
    while len(stack) > 0 :
        if equality(stack[0],value) :
            return traceRoute(stack[0])
        else :
            temp = stack.pop(0)
            if lesserFn(temp,value) :
                if temp.getLeftBranch() :
                    stack.insert(0,temp.getLeftBranch())
            else :
                if temp.getRightBranch() :
                    stack.insert(0,temp.getRightBranch())
    return False

""" To print out the trace route assign the function to a variable
and iterate through the variable to get the nodes and print the value
for ex: foo = DFSOrderedBinaryTreeWithPath(n5,6) and then
print [e.getValue() for e in foo]
"""

def buildDTree(sofar, todo) :
    """ Builds a decision tree.
    sofar is the list of nodes visited so far
    and todo is the list of nodes to be completed"""
    if len(todo) == 0 :
        return BinaryTree(sofar)
    else :
        withNode = buildDTree(sofar + [todo[0]],todo[1:])
        withoutNode = buildDTree(sofar,todo[1:])
        here = BinaryTree(sofar)
        here.setLeftBranch(withNode)
        here.setRightBranch(withoutNode)
        return here

def printBinaryTree(tree) :
    """Prints out the values of the binary tree"""
    if not tree.getParent() :
        print tree.getValue()
        left = printBinaryTree(tree.getLeftBranch())
        right = printBinaryTree(tree.getRightBranch())
    elif tree.getLeftBranch() and tree.getRightBranch():
        print tree.getValue()
        printBinaryTree(tree.getLeftBranch())
        printBinaryTree(tree.getRightBranch())
    elif tree.getLeftBranch() :
        print tree.getValue()
        printBinaryTree(tree.getLeftBranch())
    elif tree.getRightBranch() :
        print tree.getValue()
        printBinaryTree(tree.getRightBranch())
    else :
        print tree.getValue()
        
def printLeafNodesOfBinaryTree(tree) :
    """Prints out the leaf values of the binary tree"""
    if not tree.getParent() :
        left = printLeafNodesOfBinaryTree(tree.getLeftBranch())
        right = printLeafNodesOfBinaryTree(tree.getRightBranch())
    elif tree.getLeftBranch() and tree.getRightBranch():
        printLeafNodesOfBinaryTree(tree.getLeftBranch())
        printLeafNodesOfBinaryTree(tree.getRightBranch())
    elif tree.getLeftBranch() :
        printLeafNodesOfBinaryTree(tree.getLeftBranch())
    elif tree.getRightBranch() :
        printLeafNodesOfBinaryTree(tree.getRightBranch())
    else :
        print tree.getValue()

""" knapsack object class """
class knapsack(object) :
    def __init__(self,value,weight) :
        self.value = value
        self.weight = weight
    
    def getValue(self) :
        return self.value

    def getWeight(self) :
        return self.weight

def valueFn(listOfObj) :
    return sum([obj.getValue() for obj in listOfObj])
    
def constFn(listOfObj,constWeight) :
    return sum([obj.getWeight() for obj in listOfObj]) <= constWeight

def printKnapsackObj(objList) :
    print [e.getValue() for e in objList]

def searchDFDTree(root,valueFn,constFn,constWeight) :
    """ returns the best combination of items to keep in 
    a knapsack given the root of the decision tree, the 
    fn to calculate value , fn to calculate constraint weight
    and the actual weight constraint using DFS"""
    stack = [root]
    best = None
    visited = 0
    while len(stack) > 0 :
        visited += 1
        if constFn(stack[0].getValue(),constWeight) :
            if best == None :
                best = stack[0]
                printKnapsackObj(best.getValue())
            elif valueFn(stack[0].getValue()) > valueFn(best.getValue()) :
                best = stack[0]
                printKnapsackObj(best.getValue())
            temp = stack.pop(0)
            if temp.getRightBranch() :
                stack.insert(0,temp.getRightBranch())
            if temp.getLeftBranch() :
                stack.insert(0,temp.getLeftBranch())
        else :
            stack.pop(0)
    print visited
    return best

def searchBFDTree(root,valueFn,constFn,constWeight) :
    """ returns the best combination of items to keep in 
    a knapsack given the root of the decision tree, the 
    fn to calculate value , fn to calculate constraint weight
    and the actual weight constraint using BFS"""
    queue = [root]
    best = None
    visited = 0
    while len(queue) > 0 :
        visited += 1
        if constFn(queue[0].getValue(),constWeight) :
            if best == None :
                best = queue[0]
                printKnapsackObj(best.getValue())
            elif valueFn(queue[0].getValue()) > valueFn(best.getValue()) :
                best = queue[0]
                printKnapsackObj(best.getValue())
            temp = queue.pop(0)
            if temp.getLeftBranch() :
                queue.append(temp.getLeftBranch())
            if temp.getRightBranch() :
                queue.append(temp.getRightBranch())
        else :
            queue.pop(0)
    print visited
    return best

def DTImplicit(toConsider,available) :
    """ Builds a decision tree implicitly
    returns the solution and steps to solution"""
    if toConsider == [] or available == 0 :
        result = (0,())
    elif toConsider[0].getWeight() > available :
        result = DTImplicit(toConsider[1:],available)
    else :
        nextItem = toConsider[0]
        withVal, withTaken = DTImplicit(toConsider[1:],available - nextItem.getWeight())
        withVal += nextItem.getValue()
        withoutVal, withoutTaken = DTImplicit(toConsider[1:],available)
        if withVal > withoutVal :
            result = (withVal,withTaken+(nextItem,))
        else :
            result = (withoutVal,withoutTaken)
    return result

""" To view the solution for implicit decision tree fn
assign the return value to two variables. For ex,
val, taken = DTImplicit(stuff,10) and then use the 
printKnapsackObj fn to print out the values, 
printKnapsackObj(taken)"""

def DFSTreeWithoutLoop(root,value) :
    """ Search algorithm that keeps track of
    visited nodes to avoid infinte loops
    in case of graphs"""
    stack = [root]
    seen = []
    while len(stack) > 0 :
        print "Visited Node :" +str(stack[0].getValue())
        if equality(stack[0],value) :
            return True
        else :
            temp = stack.pop(0)
            seen.append(temp)
            if temp.getRightBranch() :
                if not temp.getRightBranch() in seen :
                    stack.insert(0,temp.getRightBranch())
            if temp.getLeftBranch() :
                if not temp.getLeftBranch() in seen :
                    stack.insert(0,temp.getLeftBranch())
    return False
    
def BFSTreeWithoutLoop(root,value) :
    """ Search algorithm that keeps track of
    visited nodes to avoid infinte loops
    in case of graphs"""
    queue = [root]
    seen = []
    while len(queue) > 0 :
        print "Visited Node :" +str(queue[0].getValue())
        if equality(queue[0],value) :
            return True
        else :
            temp = queue.pop(0)
            seen.append(temp)
            if temp.getLeftBranch() :
                if not temp.getLeftBranch() in seen :
                    queue.append(temp.getLeftBranch())
            if temp.getRightBranch() :
                if not temp.getRightBranch() in seen :
                    queue.append(temp.getRightBranch())      
    return False