from Tree import *

class Bracket:
    def __init__(self,bracket,index):
        self.bracket = bracket
        self.index = index


'''
#TEsting
arbol = Tree()
arbol.showCurNode()

arbol.addChild(2)
arbol.showCurNode()

arbol.addChild(3)
arbol.showCurNode()

arbol.addSibling(4,'+')
arbol.showCurNode()
arbol.addSibling(5,'+')
arbol.showCurNode()
arbol.addSibling(6,'+')
arbol.showCurNode()

arbol.addChild(7)
arbol.showCurNode()
arbol.addSibling(8,'+')
arbol.showCurNode()

arbol.toParent()
arbol.showCurNode()
arbol.addSibling(10,'+')
arbol.showCurNode()

arbol.toParent()
arbol.addSibling(12,'+')

arbol.addChild(13)
arbol.addSibling(14,'+')

arbol.addChild(15)

arbol.addChild(16)
arbol.addSibling(17,'+')
arbol.addSibling(18,'+')

arbol.toParent()
arbol.addSibling(20,'+')

arbol.toParent()
arbol.addSibling(22,'+')

arbol.toParent()
arbol.toParent()

print("\n\n\n")

arbol.trasversal()
'''

    


    



op = ['+','*','/','^','sqrt'] #Ignorando neg. - por el momento.

openBrackets = ['(', '[', '{']
closeBrackets = [')', ']', '}']
brackets = ['(', '[', '{', ')', ']', '}']

test = "(x^7 + (7/3)x^(x+3))/((-8x^7 + 9)^(1/2))"

print(test)
test = test[:-1]
print(test)
test = test[:-1]
print(test)
test = test[:-1]
print(test)

for i in range(10):
    print(i)
    i -= 1



#class differentialSolver:
#    __init__(self):