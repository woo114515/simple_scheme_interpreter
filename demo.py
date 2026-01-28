from scheme_eval import *

glo = Frame(None)

l = LinkList('+',LinkList(1,LinkList(2,nil)))
s = LinkList('*',LinkList(1,LinkList(2,nil)))
t = LinkList('+',LinkList(l,LinkList(s,nil)))
k = LinkList("1",nil)
print(evaluate(k,glo))