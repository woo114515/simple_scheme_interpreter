from scheme_eval import evaluate
from LinkList import LinkList,nil
from Frame import Frame
if __name__ == '__main__':
    glo = Frame(None)
    fuc = LinkList('sum',LinkList('a',LinkList('b',nil)))
    add = LinkList('+',LinkList('a',LinkList('b',nil)))
    d = LinkList('define',LinkList(fuc,add))
    l = LinkList('sum',LinkList(1,LinkList(2,nil)))
    s = LinkList('*',LinkList(1,LinkList(2,nil)))
    t = LinkList('+',LinkList(l,LinkList(s,nil)))
    k = LinkList("1",nil)
    b = LinkList('begin',LinkList(d,LinkList(l,nil)))
    tr = LinkList('and',LinkList(True,LinkList(True,nil)))
    print(evaluate(tr,glo))
    print(evaluate(b,glo))

    #define
    definell = LinkList('define',LinkList('defll',LinkList(1,nil)))
    evaluate(definell,glo)


    #cons,car,cdr
    con = LinkList('cons',LinkList(2,LinkList(nil,nil)))
    
    defa = LinkList('define',LinkList('a',LinkList(con,nil)))
    evaluate(defa,glo)
    car = LinkList('car',LinkList('a',nil))
    print(evaluate(car,glo))
    