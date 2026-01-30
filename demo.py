from scheme_eval import evaluate
from LinkList import LinkList,nil
from Frame import Frame
if __name__ == '__main__':
    glo = Frame(None)

    '''
    #single number
    print(evaluate(1,glo))
    print(evaluate(LinkList(1,nil),glo))
    print('*'*10)

    #define function
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
    print('*'*10)
    #define
    definell = LinkList('define',LinkList('defll',LinkList(1,nil)))
    evaluate(definell,glo)
    print('*'*10)

    #cons,car,cdr,length
    con = LinkList('cons',LinkList(2,LinkList(nil,nil)))
    
    defa = LinkList('define',LinkList('a',LinkList(con,nil)))
    evaluate(defa,glo)
    car = LinkList('car',LinkList('a',nil))
    length = LinkList('length',LinkList('a',nil))
    print(evaluate(car,glo))
    print(evaluate(length,glo))
    print('*'*10)

    #if
    eqa_def = LinkList('define',LinkList('pre',LinkList(True,nil)))
    eqa_predic = LinkList('pre',nil)
    eqa_conse = LinkList(1,nil)
    eqa_alt = LinkList(2,nil)
    eqa_if = LinkList('if',LinkList(eqa_predic,
                        LinkList(eqa_conse,LinkList(eqa_alt,nil))))
    print(evaluate(eqa_if,glo))
    print('*'*10)

    #cond
    eqa_c1 = LinkList(LinkList(False,nil),LinkList(-1,nil))
    eqa_c2 = LinkList('else',LinkList(1,nil))
    eqa_cond = LinkList('cond',LinkList(eqa_c1,LinkList(eqa_c2,nil)))
    print(evaluate(eqa_cond,glo))
    print('*'*10)

    #><
    gt = LinkList('>',LinkList(3,LinkList(2,nil)))
    lt = LinkList('<',LinkList(3,LinkList(2,nil)))
    print(evaluate(gt,glo))
    print(evaluate(lt,glo))
    print('*'*10)
    
    #display
    disp = LinkList('display',LinkList(1,nil))
    displn = LinkList('displayln',LinkList(2,nil))
    evaluate(disp,glo)
    evaluate(displn,glo)
    print('*'*10)