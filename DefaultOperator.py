'''
contain default operator
'''
from LinkList import LinkList,nil
from Frame import Frame
import scheme_eval
class procedure:
    def __init__(self,function,arg_num,need_env = False):
        self.function = function
        self.arg_num = arg_num
        self.need_envirnment = need_env


def f_add(a,b):
    return a+b

def f_minus(a,b):
    return a-b

def f_multiple(a,b):
    return a*b

def f_devision(a,b):
    return float(a)/float(b)

def isodd(num):
    if num%2 == 0:
        return False
    return True

def isnull(num):
    if num==0:
        return True
    return False

def greater_than(a,b):
    if a>b:
        return True
    return False

def less_than(a,b):
    if a<b:
        return True
    return False

def equal_to(a,b):
    if a==b:
        return True
    return False

def makecons(first,rest):
    if isinstance(rest,LinkList):
        return LinkList(first,rest)
    if rest is nil:
        return LinkList(first,rest)
    raise Exception(f'{first} and {rest} cannot form a list')
    

def fcar(lists):
    assert isinstance(lists,LinkList),f"{lists} must be a list"
    return lists.first

def fcdr(lists):
    assert isinstance(lists,LinkList),f"{lists} must be a list"
    return lists.rest

def flength(lists):
    assert isinstance(lists,LinkList)
    t = lists
    count = 0
    while not t is nil:
        count+=1
        t = t.rest
    return count

def fand(lists,env):
    for condition in lists:
        if not scheme_eval.evaluate(condition,env):
            return False
    return True

def f_or(conditions,env):
    for condition in conditions:
        if scheme_eval.evaluate(condition,env):
            return True
    return False

def fbegin(equations,env):
    assert isinstance(equations,LinkList)
    assert isinstance(env,Frame)
    t = equations
    while not (t is nil):
        value = scheme_eval.evaluate(t.first,env)
        t = t.rest
    return value

def fif(equation,env):
    assert isinstance(equation,LinkList)
    predicate = equation.first
    consequent = equation.rest.first
    alternative = None
    if not equation.rest.rest is nil:
        alternative = equation.rest.rest.first
    condition = scheme_eval.evaluate(predicate,env)
    if condition:
        value = scheme_eval.evaluate(consequent,env)
    else:
        value = None
        if alternative!=None:
            value = scheme_eval.evaluate(alternative,env)
    return value

def fcond(equation,env):
    assert isinstance(equation,LinkList)
    t = equation
    while not t is nil:
        clause = t.first
        t = t.rest
        if clause.first == 'else':
            value = scheme_eval.evaluate(clause.rest,env)
            return value
        else:
            predicate = clause.first
            consequent = clause.rest
            condition = scheme_eval.evaluate(predicate,env)
            if condition:
                value = scheme_eval.evaluate(consequent,env)
                return value
    return None

def display(content):
    print(content,end='')

def dsiplayln(content):
    print(content)

def boolean_to_scheme(value):
    if type(value) is bool:
        return True
    return False

def isnum(var):
    return isinstance(var,int)

def isnumber(var):
    return isinstance(var,int) or isinstance(var,float)

def issymbol(var,env):
    if var in env.bounds:
        return True
    return False

def isatom(var,env):
    if issymbol(var,env):
        return True
    if boolean_to_scheme(var):
        return True
    if isnumber(var):
        return True
    if var is nil:
        return True
    return False

def islist(var):
    if not isinstance(var,LinkList):
        return False
    t = var
    while not t is nil:
        if isinstance(t.first,LinkList):
            return False
        t = t.rest
    return True

def isprocedure(var,env):
    if var in operator_dic:
        return True
    if issymbol(var,env):
        value = env.get(var)
        if isinstance(value,procedure):
            return True
    return False

def abs(var):
    assert isnumber(var),TypeError(f"{var} is not a number")
    if var<0:
        return -var
    return var

def remainder(a,b):
    assert isnumber(a),TypeError(f"{a} is not a number")
    assert isnumber(b),TypeError(f"{b} is not a number")
    if a<0:
        return -(abs(a)%b)
    return a%b

add = procedure(f_add,2)
minus = procedure(f_minus,2)
multiple = procedure(f_multiple,2)
devision = procedure(f_devision,2)
odd = procedure(isodd,1)
null = procedure(isnull,1)
greater = procedure(greater_than,2)
less = procedure(less_than,2)
equal = procedure(equal_to,2)
cons = procedure(makecons,2)
car = procedure(fcar,1)
cdr = procedure(fcdr,1)
length = procedure(flength,1)
fuc_and = procedure(fand,None,True)
fuc_or = procedure(f_or,None,True)
fuc_begin = procedure(fbegin,None,True)
fuc_if = procedure(fif,None,True)
fuc_cond = procedure(fcond,None,True)
fuc_display = procedure(display,1)
fuc_displayln = procedure(dsiplayln,1)
fuc_isboolean = procedure(boolean_to_scheme,1)
fuc_isnum = procedure(isnum,1)
fuc_isnumber = procedure(isnumber,1)
fuc_issymbol = procedure(issymbol,1,True)
fuc_isatom = procedure(isatom,1,True)
fuc_islist = procedure(islist,1)
fuc_isprocedure = procedure(isprocedure,1,True)
fuc_abs = procedure(abs,1)
fuc_remainder = procedure(remainder,2)

operator_dic = {'+':add,'-':minus,'*':multiple,'/':devision,
                'odd?':odd,'null?':null,"cons":cons,"car":car,
                "cdr":cdr,"length":length,"and":fuc_and,"or":fuc_or,
                "begin":fuc_begin,"if":fuc_if,"cond":fuc_cond,
                ">":greater,"<":less,"=":equal,"display":fuc_display,
                "displayln":fuc_displayln,"boolean?":fuc_isboolean,
                "number?":fuc_isnumber,"num?":fuc_isnum,
                "symbol?":fuc_issymbol,"atom?":fuc_isatom,"list?":
                fuc_islist,"procedure?":fuc_isprocedure,"abs":fuc_abs
                ,"remainder":fuc_remainder}