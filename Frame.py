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
        if value in self.bounds:
            value = self.bounds.get(name)
        else:
            if self.father == None:
                raise Exception(f"there is no symbol {name}")
            value = self.father.get(name)
        return value
    
    def subframe(self):
        sub = Frame(self)
        return sub