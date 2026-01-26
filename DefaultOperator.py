'''
contain default operator
'''
from LinkList import LinkList,nil
class procedure:
    def __init__(self,function,arg_num):
        self.function = function
        self.arg_num = arg_num


def f_add(a,b):
    return a+b

def f_minus(a,b):
    return a-b

def f_multiple(a,b):
    return a*b

def f_devision(a,b):
    return float(a)/float(b)

def isodd(num):
    if odd%2 == 0:
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

operator_dic = {'+':add,'-':minus,'*':multiple,'/':devision,
                'odd?':odd,'null?':null,"con":con,"car":car,
                "cdr":cdr,"length":length}