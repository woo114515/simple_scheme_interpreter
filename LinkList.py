'''
define the data structure interpreter based on
'''
class LinkList:
    '''
    A linklist which our interpreter based on,
    consisted of first and rest 
    '''
    def __init__(self,fisrt,rest):
        assert ((rest is nil) or isinstance(rest,LinkList)),"it cannot form a LinkList"
        self.first = fisrt
        self.rest = rest
        self.current = self

    def __repr__(self):
        string = '('
        l = self
        while isinstance(l,LinkList):
            string+=repr(l.first)+','
            l = l.rest
        string = string[:-1]
        string+=')'
        return string
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is nil:
            raise StopIteration
        else:
            value = self.current.first
            self.current = self.current.rest
            return value

class nil:
    '''
    a class indicate the end of a linklist
    '''
