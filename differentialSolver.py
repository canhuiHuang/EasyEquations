from Tree import *

class Bracket:
    def __init__(self,bracket,index):
        self.bracket = bracket
        self.index = index

#ssterm(sst) (Super Simple term):
# ssterm solo puede haber una sola variable. Y esta no puede tener exponenciales de ningun tipo.
# sst esta compuesto de:
# - "np" (negative prefix), esta puede ser null.
# - "c" (coefficient)
# - "v" (variable)
#
# Entonces:
# sst formato --> np c v
# Ejemplos de sst validos: 
#   -27x (np c v)
#   27x  (   c v)
#   -74  (np c  )
#   x    (     v)
#   -x   (np   v)
#
# Ejemplos de sst invalidos:
#   -27x^2
#   27x^1
#   x27
#   17-x



#Determina si arg es un ssterm
def isTerm(arg,var):    #Version Beta XD
    nprefix = '-'
    constants = ['1','2','3','4','5','6','7','8','9','0']
    ops = ['+', '*', '/', '^']
    brackets = ['(', '[', '{', ')', ']', '}', '|']

    varPassed = False

    elemType = ""
    np = False
    c= ""
    v= ''
    varPassed= False

    if len(arg) == 1 and arg in brackets:
        elemType = "container"
        return np,c,v, elemType
    
    if len(arg) == 1 and arg in ops:
        elemType = "operator"
        return np,c,v, elemType

    if len(arg) > 1 and (arg[0] in brackets or arg[0] in ops or arg[0] == var):
        elemType = "invalid"
        return np,c,v, elemType

    for i in range(len(arg)):
        if arg[0] == nprefix:
            np = True
        
        if arg[i] in constants:
            c += arg[i]
            if i + 1 == len(arg) and not varPassed:
                elemType = "term"

        elif arg[i] == var:
            if i + 1 == len(arg) and not varPassed:
                elemType = "term"

            varPassed = True
        else:   #not c nor v
            if c =="":
                if varPassed:
                    elemType = "term"
            if i == 0:
                pass
            else:
                elemType = "invalid"
                break

    if varPassed:
        v = var
    return np, c, v, elemType

class PrimaryTerm:
    def __init__(self, np,c,v):
        self.np = False
        self.c = c
        self.v = v
    
    def term(self):
        t = ""
        if self.np:
            t += '-'
        t += self.c
        t += self.v
        return t

class Container:
    def __init__(self, symbol, customType = ""):
        self.bar = "| |"
        self.symbol = symbol
        self.type = ""
        if symbol in ['(', '[', '{']:
            self.type = "open" 
        elif symbol in [')', ']', '}']:
            self.type = "closed" 
        elif symbol == '|':
            self.type = customType

    def term(self):
        return self.symbol

class Operator:
    def __init__(self, op, operation = ""):
        self.op = op

    def term(self):
        return self.op

ops = ['+','*','/','^','sqrt'] #Ignorando neg. - por el momento.

openBrackets = ['(', '[', '{']
closeBrackets = [')', ']', '}']
brackets = ['(', '[', '{', ')', ']', '}', '|']

ec = "(12x^7 + (72/3)x^(x+3))/((-83x^7 + 9)^(1/2))"


#for i in range(1,len(ec)):
#    term += "ec[i]"
#    if isTerm

l = ["x^7","-231x^", "123", "x", "-231", "-x^"]
#for var in l:
#    np,c,v, esTermino = isTerm(var, 'x')
#    tempObj = Ssterm(np,c,v)
#    print(tempObj.term())

var = 'x'
arbol1 = Tree()
term = ""
elems = []
prevNpCVE = []

i = 0
while i < len(ec):
    if ec[i] != ' ':
        term += ec[i]
    np, c, v, elemType = isTerm(term, var)

    if elemType == "invalid":
        term = term[:-1]
        
        i -= 1

        if prevNpCVE[3] == "term":
            elems.append(PrimaryTerm(prevNpCVE[0],prevNpCVE[1],prevNpCVE[2]))
        elif prevNpCVE[3] == "container":
            elems.append(Container(term))
        elif prevNpCVE[3] == "operator":
            elems.append(Operator(term))

        if i + 2 == len(ec):
            elems.append(Container(ec[i + 1]))

        term = ""
    elif i + 1 == len(ec) and elemType == "term":
        elems.append(PrimaryTerm(np,c,v))

    prevNpCVE = [np, c, v, elemType]
    i += 1

#
print("[", end = '')
for elem in elems:
    print("'", elem.term(), "'", end = '')
print("]")

arbol1.init(elems[0])
i = 1
while i < len(elems):
    if elems[i - 1].term() in openBrackets:
        arbol1.addChild(elems[i])
        print(elems[i].term(),end = '')
    elif elems[i].term() in ops:
        if elems[i + 1].term() in openBrackets:
            arbol1.addSibling(elems[i + 1],elems[i])
            arbol1.addChild(elems[i + 2])
            print(elems[i].term(), elems[i+1].term(), elems[i+2].term(),end = '')
            i+=2
        else:
            arbol1.addSibling(elems[i + 1], elems[i])
            print(elems[i].term(),elems[i+1].term(),end = '')
            i+=1
    elif elems[i].term() in openBrackets:
        #arbol1.addSibling(elems[i],'*')
        arbol1.addChild(elems[i + 1])
        print(elems[i].term(),elems[i+1].term(),end = '')
        i+=1
    elif elems[i].term() in closeBrackets and i+1 < len(elems):
        arbol1.toParent()
        print(")",end = '')
    elif elems[i - 1].term() in closeBrackets:
        if elems[i].term() in openBrackets:
            arbol1.addSibling(elems[i], '*')
            arbol1.addChild(elems[i + 1])
            print(elems[i].term(), elems[i + 1].term(),end = '')
            i+=1
        elif elems[i].term() in ops:
            arbol1.addSibling(elems[i+1], elems[i])
            print(elems[i].term(),elems[i+1].term(),end = '')
            i+=1
        elif elems[i].term() not in ops and elems[i].term() not in brackets:
            arbol1.addSibling(elems[i], "*")
            print(elems[i].term(),end = '')
        else:
            arbol1.toParent()
            print(")",end = '')        
    i+=1
print()

arbol1.trasversal()
arbol1



    






#class differentialSolver:
#    __init__(self):