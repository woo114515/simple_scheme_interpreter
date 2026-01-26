from scheme_eval import *

glo = Frame(None)

l = LinkList('+',LinkList(1,LinkList(2,nil)))
s = LinkList('*',LinkList(1,LinkList(2,nil)))
t = LinkList('+',LinkList(l,LinkList(s,nil)))
print(evaluate(t,glo))