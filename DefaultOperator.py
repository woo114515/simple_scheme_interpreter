'''
contain default operator
'''


class Procedure:
    """
    """
    
    def __init__(self, name, need_frame=False):
        self.name = name

    def __repr__(self):
        return f"Procedure:{self.name}"

DefaultOperators = {}
class DefaultOperator(Procedure):

    """
    Buil-in 
    """

    def __init__(self, name, function, need_frame=False):
        self.name = name
        self.function = function
        DefaultOperators[name] = self
        self.need_frame = need_frame
    
    def apply(self, *args):
        return self.function(*args)



def f_add(*args):
    return sum(args)

def f_minus(a,b):
    return a-b

def f_multiple(*args):
    anw = 1
    for i in args:
        anw = anw * i
    return anw
    
def f_division(a,b):
    return float(a)/float(b)

def f_abs(x):
    if x > 0:
        return x
    else:
        return -x
    
def f_quotient(a, b):
    return a // b

def f_reminder(a, b):
    return a % b

def f_isnumber(var):
    '''
    determine whether the variable is a number
    '''
    if isinstance(var,int):
        return True
    if isinstance(var,float):
        return True
    return False

add = DefaultOperator("+", f_add)
minus = DefaultOperator("-", f_minus)
multiple = DefaultOperator("*", f_multiple)
division = DefaultOperator("/", f_division)
quotient = DefaultOperator("quotient", f_quotient)
reminder = DefaultOperator("reminder", f_reminder)
isnumber = DefaultOperator("num?", f_isnumber)


