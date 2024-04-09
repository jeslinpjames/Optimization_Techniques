"""
Algorithm:
hungarian_algorithm(cost_matrix):
    - Get the dimensions n, m of the cost_matrix.
    - Check if the cost matrix is square.
    - Subtract the minimum value of each row from all elements in that row.
    - Subtract the minimum value of each column from all elements in that column.
    - Repeat until all zeros in the cost matrix are covered with the minimum number of lines:
        - Find all uncovered zeros in the cost matrix.
        - Cover the rows and columns of uncovered zeros.
        - Update the count of covered lines.
        - If all zeros are covered, proceed to the next step.
        - Otherwise, update the cost matrix by subtracting the minimum uncovered value from uncovered elements
          and adding it to doubly covered elements.
    - Allocate assignments based on zeros in the cost matrix.
    - Calculate the total cost based on assigned zeros and original row and column minimums.
    - Return the optimal assignment and the minimum total cost.

Main code:
- Define the cost matrix.
- Call the hungarian_algorithm function with the cost matrix.
- Print the optimal assignment matrix and the minimum total cost.

"""

import numpy as np

def hungarian_algorithm(cost_matrix):
    """
    Solves the Assignment Problem using the Hungarian Algorithm.

    Args:
        cost_matrix (numpy.ndarray): A 2D array representing the cost matrix.

    Returns:
        numpy.ndarray: A 2D array representing the optimal assignment.
        float: The minimum total cost.
    """
    n, m = cost_matrix.shape
    if n != m:
        raise ValueError("Cost matrix must be a square matrix.")

    # Step 1: Subtract the row minimum from each row
    row_mins = np.min(cost_matrix, axis=1)
    cost_matrix = cost_matrix - row_mins[:, None]

    # Step 2: Subtract the column minimum from each column
    col_mins = np.min(cost_matrix, axis=0)
    cost_matrix = cost_matrix - col_mins

    # Step 3: Cover all zeros with the minimum number of lines
    lines = 0
    while lines < n:
        # Find the minimum number of lines needed to cover all zeros
        covered_rows = np.zeros(n, dtype=bool)
        covered_cols = np.zeros(n, dtype=bool)
        while True:
            # Find the uncovered zeros
            zero_indices = np.where((cost_matrix == 0) & (~covered_rows[:, None]) & (~covered_cols[None, :]))[0:2]
            if zero_indices[0].size == 0:
                break
            # Cover the row of each uncovered zero
            covered_rows[zero_indices[0]] = True
            # Cover the column of each uncovered zero
            covered_cols[zero_indices[1]] = True
            lines = np.sum(covered_rows) + np.sum(covered_cols)

        if lines < n:
            # Find the minimum uncovered value
            min_uncovered = np.min(cost_matrix[~covered_rows][:, ~covered_cols])
            # Subtract the minimum uncovered value from all uncovered elements
            cost_matrix[covered_rows][:, ~covered_cols] -= min_uncovered
            # Add the minimum uncovered value to all doubly covered elements
            cost_matrix[~covered_rows][:, covered_cols] += min_uncovered

    # Step 4: Allocate the assignments
    assignment = np.zeros((n, n), dtype=int)
    total_cost = 0
    for i in range(n):
        for j in range(n):
            if cost_matrix[i, j] == 0:
                assignment[i, j] = 1
                total_cost += row_mins[i] + col_mins[j]

    return assignment, total_cost

# Example usage
cost_matrix = np.array([[9, 11, 14, 11, 7],
                        [6, 15, 13, 13, 10],
                        [12, 13, 6, 8, 8],
                        [11, 9, 10, 12, 9],
                        [7,12,14,10,14]])
assignment, total_cost = hungarian_algorithm(cost_matrix)

print("Optimal Assignment:")
print(assignment)
print(f"Minimum Total Cost: {total_cost}")