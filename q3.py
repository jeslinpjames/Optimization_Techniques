from scipy.optimize import linprog

c = [-20, -30]

A = [
    [1, 5],
    [3, 1]
]

b = [125, 80]

x_bounds = (0, None)
y_bounds = (0, None)

result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds])

num_chairs = round(result.x[0])
num_tables = round(result.x[1])
max_profit = -result.fun

print(f"Number of chairs to produce: {num_chairs}")
print(f"Number of tables to produce: {num_tables}")
print(f"Maximum profit: ${max_profit}")
