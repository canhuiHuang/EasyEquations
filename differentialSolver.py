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
    #ops = ['+', '-', '*', '/', '^']

    varPassed = False

    itIsTerm = False
    np = False
    c= ""
    v= False
    for i in range(len(arg)):
        if arg[0] == nprefix:
            np = True
        
        if arg[i] in constants:
            c += arg[i]
            if i + 1 == len(arg) and not varPassed:
                itIsTerm = True

        elif arg[i] == var:
            if i + 1 == len(arg) and not varPassed:
                itIsTerm = True

            varPassed = True
            v = True
        else:   #not c nor v
            if c =="":
                if v:
                    itIsTerm = True
            if i == 0:
                pass
            else:
                itIsTerm = False
                break

    
    if np:
        print(nprefix + " ", end = '')
    print(c + " ", end = '')
    if v:
        print(var)
    else:
        print()

    return itIsTerm

        
    


        
        
        
        

    


op = ['+','*','/','^','sqrt'] #Ignorando neg. - por el momento.

openBrackets = ['(', '[', '{']
closeBrackets = [')', ']', '}']
brackets = ['(', '[', '{', ')', ']', '}']

ec = "(x^7 + (7/3)x^(x+3))/((-8x^7 + 9)^(1/2))"

arbol1 = Tree(ec[0])
term = ""
#for i in range(1,len(ec)):
#    term += "ec[i]"
#    if isTerm

#l = ["x^7","-231x^", "123", "x", "-231", "-x^"]
l = ["x37","x3", "+", "1", "-1", "-23", "x", "-x", "761x", "-238x", "-37x-", "-37xx"]

for var in l:
    if isTerm(var, 'x'):
        print("si")
    else:
        print("no")




#class differentialSolver:
#    __init__(self):