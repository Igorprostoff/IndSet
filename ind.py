import os
from sympy.logic.boolalg import to_dnf
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

expr_temp=''
expr_temp2=''
otv=''

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
os.system("pause")
