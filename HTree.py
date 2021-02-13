class TreeNode:
    def __init__(self,data, depth = 0, parent = None):
        self.data = data
        self.children = []
        self.parent = parent
        self.rightSibling = None
        self.rightRelation = ''
        self.leftSibling = None
        self.depth = depth
        self.isRoot = False
    
    def addChild(self, treeNode):
        self.children.append(treeNode)

    def setRightRelation(self,op):
        self.rightRelation = op
    
    def removeChild(self, node):
        self.children.pop()

class HTree: #A tree with curNode. Always tracks curNode
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

    def showInfo(self):
        print("Me: ", self.curNode.data.term())
        print("rOp: ", self.curNode.rightRelation)

    def updateNode(self,data):
        self.curNode.data = data
    
    def addSibling(self, data, op):
        tempNode = TreeNode(data, self.curNode.depth, self.curNode.parent)
        if self.curNode.parent != None:
            self.curNode.parent.addChild(tempNode)
        self.curNode.setRightRelation(op)
        self.curNode.rightSibling = tempNode
        
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

            #if node.data.type != "container":
                #print(node.data.term(), end = '')
                #if node.rightSibling:
                    #print(node.rightRelation.term(), end = '')
            #else:
                #print(node.data.term("dynamic"), end = '')
                #if node.rightSibling and node.data.typeState == 1:
                    #print(node.rightRelation.term(), end = '')

            print(node.data.term(), end = '')

            if node.depth == self.root.depth and ignoreChildren:
                if node.rightSibling:
                #print(node.rightRelation, end = '')
                    node = node.rightSibling
                    itrasversal(node)
                return

            elif node.children and not ignoreChildren:
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

        def next(self):
        #Go to most left leaf:

            def itrasversal(node, ignoreChildren = False):
                
                #IgnoreChildren trasverse upward (One way ticket xd)

                #if not node.isRoot():
                #    print(node.data, end = '')

                #if node.data.type != "container":
                    #print(node.data.term(), end = '')
                    #if node.rightSibling:
                        #print(node.rightRelation.term(), end = '')
                #else:
                    #print(node.data.term("dynamic"), end = '')
                    #if node.rightSibling and node.data.typeState == 1:
                        #print(node.rightRelation.term(), end = '')

                print(node.data.term(), end = '')

                if node.depth == self.root.depth and ignoreChildren:
                    if node.rightSibling:
                    #print(node.rightRelation, end = '')
                        node = node.rightSibling
                        itrasversal(node)
                    return

                elif node.children and not ignoreChildren:
                    node = node.children[0]
                    itrasversal(node)
            
                elif node.rightSibling:
                    #print(node.rightRelation, end = '')
                    node = node.rightSibling
                    itrasversal(node)
                else:
                    node = (node.parent)
                    itrasversal(node, True)