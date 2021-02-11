class TreeNode:
    def __init__(self,data, depth = 0, parent = None):
        self.data = data
        self.children = []
        self.parent = parent
        self.rightSibling = None
        self.rightRelation = None
        self.leftSibling = None
        self.depth = depth
        self.isRoot = False
    
    def addChild(self, treeNode):
        self.children.append(treeNode)
    
    def removeChild(self, node):
        self.children.pop()

class Tree: #A tree with curNode. Always tracks curNode
    def __init__(self):
        self.root = None
        self.curNode = self.root

    def addChild(self,data):
        tempNode = TreeNode(data, self.curNode.depth + 1, self.curNode)
        self.curNode.addChild(tempNode)
        self.curNode = tempNode

    def init(self, data):
        self.root = TreeNode(data)
        self.root.isRoot = True
        self.curNode = self.root

    def updateNode(self,data):
        self.curNode.data = data
    
    def addSibling(self, data, op):
        tempNode = TreeNode(data, self.curNode.depth, self.curNode.parent)
        if self.curNode.parent != None:
            self.curNode.parent.addChild(tempNode)
        self.curNode.rightSibling = tempNode
        self.curNode.rightRelation = op
        self.curNode = tempNode

    def showCurNode(self):
        print(self.curNode.data)
    
    def toParent(self):
        self.curNode = self.curNode.parent

    #Branch trasversal
    def trasversal(self):
        #Go to most left leaf:

        def itrasversal(node, ignoreChildren = False):
            
            #IgnoreChildren trasverse upward (One way ticket xd)

            #if not node.isRoot():
            #    print(node.data, end = '')

            print(node.data.term())

            if node.isRoot and ignoreChildren:
                return

            if node.children and not ignoreChildren:
                node = node.children[0]
                itrasversal(node)
        
            elif node.rightSibling:
                #print(node.rightRelation, end = '')
                node = node.rightSibling
                itrasversal(node)
            else:
                node = (node.parent)
                itrasversal(node, True)


        trasversingNode = self.root
        itrasversal(trasversingNode)