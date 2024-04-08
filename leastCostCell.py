import numpy as np

def leastCostCell(cost_matrix, supply, demand):
    m, n = cost_matrix.shape
    allocation = np.zeros((m, n))
    
    while np.any(supply) and np.any(demand):
        # Find the cell with the least cost
        min_cost_index = np.unravel_index(np.argmin(cost_matrix, axis=None), cost_matrix.shape)
        i, j = min_cost_index
        
        # Allocate the minimum of supply and demand
        quantity = min(supply[i], demand[j])
        allocation[i, j] = quantity
        supply[i] -= quantity
        demand[j] -= quantity
        
        # Update cost matrix to reflect the allocation
        cost_matrix[i, j] = np.inf # Set the cost of the allocated cell to infinity
        
        # Remove the row or column if supply or demand becomes zero
        if supply[i] == 0:
            cost_matrix = np.delete(cost_matrix, i, axis=0)
            allocation = np.delete(allocation, i, axis=0)
            supply = np.delete(supply, i)
        if demand[j] == 0:
            cost_matrix = np.delete(cost_matrix, j, axis=1)
            allocation = np.delete(allocation, j, axis=1)
            demand = np.delete(demand, j)
    
    return allocation

def calculate_cost(allocation, cost_matrix):
    if allocation.size == 0: # Check if allocation matrix is empty
        return 0 # Return 0 if no allocation is made
    return np.sum(allocation * cost_matrix)

# Example problem
cost_matrix = np.array([
    [3, 1, 7, 4],
    [2, 6, 5, 9],
    [8,3, 3, 2]
])

supply = np.array([300, 400, 500])
demand = np.array([250, 350, 400, 200])

# Apply the Least Cost Cell Method
allocation = leastCostCell(cost_matrix, supply, demand)
min_cost = calculate_cost(allocation, cost_matrix)

# Print the results
print("Allocation Matrix:")
print(allocation)
print("\n\nMinimum cost = ", min_cost)
