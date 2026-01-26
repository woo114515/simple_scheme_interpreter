'''
functions evaluate the values of the formula,
which input in the format of LinkList 
'''
from LinkList import LinkList,nil
from Frame import Frame
from DefaultOperator import *
def isnumber(var):
    '''
    determine whether the variable is a number
    '''
    if isinstance(var,int):
        return True
    if isinstance(var,float):
        return True
    return False

def isoperator(var,frame):
    if var in operator_dic:
        return True
    if var in frame.bounds:
        return True
    return False

def evaluate(equation,env):
    '''
    
    :param equation: is LinkList 
    :param frame: is Frame
    '''
    assert isinstance(env,Frame),"env must in LinkList form"
    if not isinstance(equation,LinkList):
        return equation
    first = equation.first
    #operator
    if isoperator(first,env):
        operator = operator_dic[first]
        args = equation.rest
        return apply(operator,env,args)
    #number
    if isnumber(first):
        return first

    
    #define value

    #define function
    
    #symbols
    pass

def apply(operator,env,args):
    assert isinstance(operator,procedure),"operator must be a procedure"
    assert isinstance(args,LinkList),"args must be a LinkList"
    assert isinstance(env,Frame),"env must be a Frame"
    arguments = []
    t = args
    while not t is nil:
        value = evaluate(t.first,env)
        arguments.append(value)
        t = t.rest
    func = operator.function
    apply_value = func(*arguments)
    return apply_value
