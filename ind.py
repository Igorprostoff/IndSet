import os
from sympy.logic.boolalg import to_dnf, to_cnf, BooleanFunction
from sympy.abc import A, B, C, D, E, F, G, symbols


def restyle():
    otv = str(to_dnf(expr_temp))
    otv = otv.replace('A','1')
    otv = otv.replace('B','2')
    otv = otv.replace('C','3')
    otv = otv.replace('D','4')
    otv = otv.replace('E','5')
    otv = otv.replace('F','6')
    otv = otv.replace('G','7')
    otv = otv.replace('(','')
    otv = otv.replace(')','')
    otv = otv.replace('&','')
    otv = otv.replace('|','V')
    otv = otv.replace('  ','')
    return(otv)

def restylec(tmp):
    otv = str(tmp)
    otv = otv.replace('A','1')
    otv = otv.replace('B','2')
    otv = otv.replace('C','3')
    otv = otv.replace('D','4')
    otv = otv.replace('E','5')
    otv = otv.replace('F','6')
    otv = otv.replace('G','7')
    otv = otv.replace('(','')
    otv = otv.replace(')','')
    otv = otv.replace('&','')
    otv = otv.replace('|','V')
    otv = otv.replace('  ','')
    return(otv)


expr_temp=''
expr_temp2=''
otv=''
zad=input("Введите номер задачи: ")
if (zad=="11") or (zad=="12"):
    resh=input("Введите 1 для подробного решения или введите 2 для краткого ответа: ")
    if resh=="1":
        
        while 1:
            
            reb=input("Введите по одному ребра вида (1,5), для окончания ввода выражения введите 0: ")
            
            reb = reb.replace('1','A')
            reb = reb.replace('2','B')
            reb = reb.replace('3','C')
            reb = reb.replace('4','D')
            reb = reb.replace('5','E')
            reb = reb.replace('6','F')
            reb = reb.replace('7','G')
            
            if reb=="0":
                if expr_temp=='':
                    print("Не было введено выражение")
                    break
                else:
                    print("ОТВЕТ: ",restyle())
                    break
            
            if expr_temp2=='':
                expr_temp = (symbols(reb[1])|symbols(reb[3]))
                print("Промежуточный результат: ",restyle())
            else:
                expr_temp = (expr_temp2) & (symbols(reb[1])|symbols(reb[3]))
                print("Промежуточный результат: ",restyle())
            expr_temp2 = to_dnf(expr_temp)
        
    else:
        
        while 1:
            
            reb=input("Введите по одному ребра вида (1,5), для окончания ввода выражения введите 0: ")
            
            if reb=="0":
                print("ОТВЕТ: ",restyle())
                break
            
            reb = reb.replace('1','A')
            reb = reb.replace('2','B')
            reb = reb.replace('3','C')
            reb = reb.replace('4','D')
            reb = reb.replace('5','E')
            reb = reb.replace('6','F')
            reb = reb.replace('7','G')
            
            if expr_temp2=='':
                expr_temp = (symbols(reb[1])|symbols(reb[3]))
            else:
                expr_temp = (expr_temp2) & (symbols(reb[1])|symbols(reb[3]))
            expr_temp2 = to_dnf(expr_temp)


#ВТОРАЯ ЧАСТЬ ЗАДАНИЯ, НОМЕРА 13 и 14 ######################################################################################################################################################################################################
            
else:
    resh=input("Введите 1 для подробного решения или введите 2 для краткого ответа: ")
    if resh=="1":
        
        while 1:
            
            reb=input("Введите вершину и смежные с ней вершины скобкой вида (1,5,6), для окончания ввода выражения введите 0: ")
            
            reb = reb.replace('1','A')
            reb = reb.replace('2','B')
            reb = reb.replace('3','C')
            reb = reb.replace('4','D')
            reb = reb.replace('5','E')
            reb = reb.replace('6','F')
            reb = reb.replace('7','G')
            reb = reb.replace(',','')
            reb = reb.replace('(','')
            reb = reb.replace(')','')
            if reb=="0":
                if expr_temp=='':
                    print("Не было введено выражение")
                    break
                else:
                    print("ОТВЕТ: ",restylec(expr_temp2))
                    break
            
            if expr_temp2=='':
                i=0
                while i<(len(reb)):
                    if i==0:
                        expr_temp=symbols(reb[i])
                        
                    else:
                        expr_temp=expr_temp | symbols(reb[i])
                        
                    i=i+1
            else:
                i=0
                while i<(len(reb)):
                    if i==0:
                        expr_temp=symbols(reb[i])
                        
                    else:
                        expr_temp=expr_temp | symbols(reb[i])
                        
                    i=i+1
                    expr_temp=expr_temp2 & expr_temp
                    
            expr_temp2 = BooleanFunction.simplify(expr_temp)
            print("Промежуточный ответ", restylec(expr_temp2))
        
    else:
        
        while 1:
            
            reb=input("Введите вершину и смежные с ней вершины скобкой вида (1,5,6), для окончания ввода выражения введите 0: ")
            
            reb = reb.replace('1','A')
            reb = reb.replace('2','B')
            reb = reb.replace('3','C')
            reb = reb.replace('4','D')
            reb = reb.replace('5','E')
            reb = reb.replace('6','F')
            reb = reb.replace('7','G')
            reb = reb.replace(',','')
            reb = reb.replace('(','')
            reb = reb.replace(')','')
            if reb=="0":
                if expr_temp=='':
                    print("Не было введено выражение")
                    break
                else:
                    print("ОТВЕТ: ",restylec(expr_temp2))
                    break
            
            if expr_temp2=='':
                i=0
                while i<(len(reb)):
                    if i==0:
                        expr_temp=symbols(reb[i])
                    else:
                        expr_temp=expr_temp | symbols(reb[i])
                    i=i+1
            else:
                i=0
                while i<(len(reb)):
                    if i==0:
                        expr_temp=symbols(reb[i])
                    else:
                        expr_temp=expr_temp | symbols(reb[i])
                    i=i+1
                    expr_temp=expr_temp2 & expr_temp
            expr_temp2 = BooleanFunction.simplify(expr_temp)
os.system("pause")
