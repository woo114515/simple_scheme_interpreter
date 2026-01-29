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
    if isinstance(var,int):
        return True
    if isinstance(var,float):
        return True
    return False

def isoperator(var,env):
    if var in operator_dic:
        return True
    if var in env.bounds:
        value = env.bounds.get(var)
        if isinstance(value,procedure):
            return True
    return False

def issymbol(var,frame):
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
    assert isinstance(env,Frame)
    # AND WHERE IS THE VARIABE LIKE 'a', 'x' a shit mount! (doge)
    # you should fix it, @BarCodein
    if not isinstance(equation,LinkList):
        if isnumber(equation):
            return equation
        if issymbol(equation,env):
            return env.bounds.get(equation)
        raise Exception(f"{equation} can't be caculate")
        

    
    first = equation.first
    #operator
    if isoperator(first,env):
        if issymbol(first,env):
            operator = env.get(first)
        else:
            operator = operator_dic[first]
        args = equation.rest#this might be changed later
        return apply(operator,env,args)
    #number
    if isnumber(first):
        return first

    
    #define
    if isdefine(first):
        args = equation.rest#this might be changed later
        assign(env,args)
    
    #symbols
    pass

def apply(operator,env,args):
    '''
    function to call back operator on args
    '''
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
    '''
    function dealing with command 'define'
    '''
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

def Lambda(env,argument,equation):
    '''
    function to define a fuction
    '''
    assert isinstance(env,Frame)
    func_env = env.subframe()
    
    def fuc(*args):
        for symbol,value in zip(argument,args):
            func_env.bound(symbol,value)
        answer = evaluate(equation,func_env)
        return answer
    return fuc
