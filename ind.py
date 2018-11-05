import os
from sympy.logic.boolalg import to_dnf, to_cnf, BooleanFunction, simplify_logic, Or, as_Boolean, Boolean
from sympy.abc import A, B, C, D, E, F, G, symbols


def restylec(tmp):
    otv = str(tmp)
    otv = otv.replace('A','1')
    otv = otv.replace('B','2')
    otv = otv.replace('C','3')
    otv = otv.replace('D','4')
    otv = otv.replace('F','5')
    otv = otv.replace('G','6')
    otv = otv.replace('H','7')
    otv = otv.replace('(','')
    otv = otv.replace(')','')
    otv = otv.replace('&','')
    otv = otv.replace('|','V')
    otv = otv.replace('  ','')
    return(otv)


expr_temp=0|0
expr_temp2=''
otv=''

resh=input("Введите 1 для подробного решения или введите 2 для краткого ответа, 4 для ввода выражения из файла: ")

if resh=="1":
           
    reb=input("Введите введите выражение целиком: ")
           
    reb = reb.replace('1','A')
    reb = reb.replace('2','B')
    reb = reb.replace('3','C')
    reb = reb.replace('4','D')
    reb = reb.replace('5','F')
    reb = reb.replace('6','G')
    reb = reb.replace('7','H')
    reb = reb.replace('v','|')
    reb = reb.replace(')(',')&(')
    reb = reb.replace('-','~')
    i=0
    print(reb)   
    print(restylec(to_dnf(reb, True)))

#TODO ЧТЕНИЕ С ФАЙЛА И ДОКИНУТЬ ВАРИАНТЫ ПЕРЕМЕННЫХ НА ВХОДЕ (х1,х2,х3...) или (у1,у2, у3...) или я хз еще как но надо добавить
    
os.system("pause")
