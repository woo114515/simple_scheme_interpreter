'''
functions evaluate the values of the formula,
which input in the format of LinkList 
'''
from LinkList import LinkList,nil
from Frame import Frame
from DefaultOperator import *

def evaluate(equation,env):
    '''
    
    :param equation: is LinkList 
    :param frame: is Frame
    '''
    assert isinstance(env,Frame)
    
    #self-evaluate    
    if not isinstance(equation, LinkList):
        if f_isnumber(equation):
            return equation
        
        value = env.get(equation)
        if value != None:
            if type(value) == LinkList:
                return value.__repr__
            if type(value) == Procedure:
                return value.__repr__
    
    oprends = DefaultOperators[equation.first]
    assert isinstance(oprends, Procedure)
    
    return apply(oprends, equation.rest, env)



def apply(operator,args,env):
    assert isinstance(operator,Procedure),"operator must be a procedure"
    assert isinstance(args,LinkList),"args must be a LinkList"
    assert isinstance(env,Frame),"env must be a Frame"
    arguments = []
    t = args
    while not t is nil:
        value = evaluate(t.first,env)
        arguments.append(value)
        t = t.rest
    if operator.need_frame:
        arguments.append(env) 
    return operator.apply(*arguments)
