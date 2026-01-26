
from scheme_eval import *

glo = Frame(None)

l = LinkList('+',LinkList(1,LinkList(3,nil)))
s = LinkList('*',LinkList(3,LinkList(2,LinkList(4,nil))))
t = LinkList('+',LinkList(l,LinkList(s,nil)))

print(s)
print(evaluate(t,glo))