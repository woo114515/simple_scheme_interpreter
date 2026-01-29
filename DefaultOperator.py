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

def makecon(first,rest):
    return LinkList(first,rest)

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

add = procedure(f_add,2)
minus = procedure(f_minus,2)
multiple = procedure(f_multiple,2)
devision = procedure(f_devision,2)
odd = procedure(isodd,1)
null = procedure(isnull,1)
con = procedure(makecon,2)
car = procedure(fcar,1)
cdr = procedure(fcdr,1)
length = procedure(flength,1)
fuc_and = procedure(fand,None,True)
fuc_or = procedure(f_or,None,True)
fuc_begin = procedure(fbegin,None,True)

operator_dic = {'+':add,'-':minus,'*':multiple,'/':devision,
                'odd?':odd,'null?':null,"con":con,"car":car,
                "cdr":cdr,"length":length,"and":fuc_and,"or":fuc_or,
                "begin":fuc_begin}