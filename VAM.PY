import numpy as np

def calculate_penalties(cost_matrix):
    row_penalties = np.abs(np.sort(cost_matrix, axis=1)[:, 0] - np.sort(cost_matrix, axis=1)[:, 1])
    col_penalties = np.abs(np.sort(cost_matrix, axis=0)[0, :] - np.sort(cost_matrix, axis=0)[1, :])
    return row_penalties, col_penalties

def vogels_approximation(cost_matrix, supply, demand):
    m, n = cost_matrix.shape
    allocation = np.zeros((m, n))
    
    while np.any(supply) and np.any(demand):
        row_penalties, col_penalties = calculate_penalties(cost_matrix)
        max_penalty_row = np.argmax(row_penalties)
        
        # Find the cell with the least cost in the row with the maximum penalty
        min_cost_index = np.argmin(cost_matrix[max_penalty_row, :])
        i, j = max_penalty_row, min_cost_index
        
        # Allocate the minimum of supply and demand
        quantity = min(supply[i], demand[j])
        allocation[i, j] = quantity
        supply[i] -= quantity
        demand[j] -= quantity
        
        # Cancel the column with the allocated demand
        cost_matrix[:, j] = np.inf
    
    return allocation

def calculate_cost(allocation, cost_matrix):
    return np.sum(allocation * cost_matrix)

# Example problem
cost_matrix = np.array([
    [3, 1, 7, 4],
    [2, 6, 5, 9],
    [8,3, 3, 2]
])

supply = np.array([300, 400, 500])
demand = np.array([250, 350, 400, 200])

# Apply the Vogel's Approximation Method
allocation = vogels_approximation(cost_matrix, supply, demand)
min_cost = calculate_cost(allocation, cost_matrix)

# Print the results
print("Allocation Matrix:")
print(allocation)
print("\n\nMinimum cost = ", min_cost)
