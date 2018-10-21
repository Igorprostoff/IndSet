import sympy.physics.mechanics as me
import sympy as sm
import math as m
import numpy as np

x, y = me.dynamicsymbols('x y')
a, b, r = sm.symbols('a b r', real=True)
eqn = sm.Matrix([[0]])
eqn[0] = a*x**3+b*y**2-r
eqn = eqn.row_insert(eqn.shape[0], sm.Matrix([[0]]))
eqn[eqn.shape[0]-1] = a*sm.sin(x)**2+b*sm.cos(2*y)-r**2
matrix_list = []
for i in eqn:matrix_list.append(i.subs({a:2.0, b:3.0, r:1.0}))
print(sm.nsolve(matrix_list,(x,y),(np.deg2rad(30),3.14)))
