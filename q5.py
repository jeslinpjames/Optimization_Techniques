from scipy.optimize import linprog

c = [-5, -3] 
A = [[2, 1], [1, 1]] 
b = [500, 400] 

x0_bounds = (100, None) 
x1_bounds = (50, None) 

result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

num_chocolate_cakes = round(result.x[0])
num_vanilla_cakes = round(result.x[1])
max_revenue = -result.fun

print(f"Number of chocolate cakes to make: {num_chocolate_cakes}")
print(f"Number of vanilla cakes to make: {num_vanilla_cakes}")
print(f"Maximum revenue: ${max_revenue}")
