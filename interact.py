'''
main function 
offer 
'''

from LinkList import *
from Frame import *
from scheme_eval import *

def interact():
    
    inpu = input(">>>\n")
    expr = intepret(inpu)
    print(expr)
    globe_env = Frame()
    outpu = str(evaluate(expr, globe_env))
    print(outpu)

def intepret(inpu):
        
    pair = nil
    
    def format_string(string):
        
        class stack:
            def __init__(self, name):
                self.name = name
                self.stimulate = []
                self.index = -1
            def push(self, val):
                self.stimulate.append(val)
                self.index += 1
            def pop(self):
                self.index -= 1
                return self.stimulate[self.index+1]
        
        brackets = stack("brackets")
        list_formated = []
        is_new_arg = True
        is_first_space = False
        is_sub = False
        index = 0

        for i in range(len(string)):
            
            # ()

            if string[i] == '(':
                brackets.push(i)
                is_sub = True
            elif string[i] == ')':
                if brackets.index > 0:
                    brackets.pop()
                else:
                    start = brackets.pop()
                    list_formated.append(intepret(string[start:i+1]))
                # still inside a parent expression if the stack isn't empty
                is_sub = brackets.index >= 0
            # space

            # not space
            elif string[i] == ' ':
                if is_first_space:
                    index +=1
                    is_first_space = False
                    is_new_arg = True 
            
            # is space
            elif not is_sub:
                if is_new_arg:
                    list_formated.append(string[i])
                    is_new_arg = False
                    is_first_space = True
                else:
                    list_formated[index] += string[i]
        
        return list_formated

    if inpu[0] != '(':
        return inpu
    else:
        inpu_list = format_string(inpu[1:len(inpu)-1])
        for i in range(len(inpu_list)-1,-1,-1):
            pair = LinkList(inpu_list[i], pair)

    return pair
        
    