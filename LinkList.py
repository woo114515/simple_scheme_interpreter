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

    def __repr__(self):
        string = '('
        l = self
        while isinstance(l,LinkList):
            string+=repr(l.first)+','
            l = l.rest
        string = string[:-1]
        string+=')'
        return string
    
    def len(self):
        if not (self.rest is nil):
            return 1 + self.rest.len()
        else:
            return 1

class nil:
    '''
    a class indicate the end of a linklist
    '''
