'''
module of program's frame
'''
class Frame:
    '''
    frame where programes run
    '''
    
    def __init__(self,father_frame):
        self.father = father_frame
        self.bounds = {}

    def bound(self,name,value):
        self.bounds[name] = value

    def get(self,name):
        '''
        return variable
        
        '''
        value = self.bounds.get(name)
        if value == None:
            value = self.father.get(name)
        return value
    
    def subframe(self):
        sub = Frame(self)
        return sub