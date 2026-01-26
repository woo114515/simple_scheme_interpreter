'''
contain default operator
'''
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

add = procedure(f_add,2)
minus = procedure(f_minus,2)
multiple = procedure(f_multiple,2)
devision = procedure(f_devision,2)


operator_dic = {'+':add,'-':minus,'*':multiple,'/':devision}