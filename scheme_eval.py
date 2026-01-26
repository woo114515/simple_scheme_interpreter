'''
functions evaluate the values of the formula,
which input in the format of LinkList 
'''

def isnumber(var):
    '''
    determine whether the variable is a number
    '''
    if isinstance(var,int):
        return True
    if isinstance(var,float):
        return True
    return False

def isoperator(var):
    return False

def evaluate(equation):
    first = equation.first
    #operator
    if isoperator(first):
        pass
    #number
    if isnumber(first):
        pass

    
    #define value

    #define function
    
    #symbols
    pass

def eval(operator):
    pass
