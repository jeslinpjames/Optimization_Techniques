from scipy.optimize import linprog

c = [-200, -150]

A = [[20, 10], [10, 15]]

b = [1200, 600]

x0_bounds = (20, None)
x1_bounds = (10, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

print('Optimal values:', res.x)
print('Maximum profit:', -res.fun)
