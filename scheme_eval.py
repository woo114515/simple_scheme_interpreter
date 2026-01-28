'''
functions evaluate the values of the formula,
which input in the format of LinkList 
'''
from LinkList import LinkList,nil
from Frame import Frame
from DefaultOperator import *

# the usual input is "1", not 1
def isnumber(var):
    '''
    determine whether the variable is a number
    '''
    try:
        var = eval(var)
        if isinstance(var,int):
            return True
        if isinstance(var,float):
            return True
    except:
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

def isdefine(var):
    if var == "define":
        return True
    return False

'''
把这些函数定义扔到DefaultOperator里去
'''

def evaluate(equation,env):
    '''
    
    :param equation: is LinkList 
    :param frame: is Frame
    '''
    # the usual input is "1", not 1
    # AND WHERE IS THE VARIABE LIKE 'a', 'x' a shit mount! (doge)
    # you should fix it, @BarCodein
    if not isinstance(equation,LinkList):
        if isnumber(equation):
            return eval(equation)
        else:
            return equation

    
    first = equation.first
    #operator
    if isoperator(first,env):
        operator = operator_dic[first]
        args = equation.rest#this might be changed later
        return apply(operator,env,args)
    #number
    if isnumber(first):
        return eval(first)
    # the usual input is "1", not 1

    
    #define
    if isdefine(first):
        args = equation.rest#this might be changed later
        assign(env,args)
    
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

def assign(env,args):
    assert isinstance(env,Frame)
    if isinstance(args.first,LinkList):
        # defining function
        symbol = args.first.first
        equation = args.rest
        argument = args.first.rest
        func = Lambda(env,argument,equation)
        fuct = procedure(func,flength(argument))
        env.bound(symbol,fuct)
        pass
    else:
        symbol = args.first
        equation = args.rest
        value = evaluate(equation,env)
        env.bound(symbol,value)

def Lambda(env,args,equation):
    pass
