def map_step(A, B):
    intermediate = []
    n = len(A) # Assuming A and B are square matMrices of the same size.
    for i in range(n):
        for j in range(n):
            # Emit row of A
            for k in range(n):
                intermediate.append((("C", i, k), ("A", A[i][j])))
            # Emit column of B
            for k in range(n):
                intermediate.append((("C", k, j), ("B", B[i][j])))
    return intermediate

def reduce_step(intermediate):
    """Simplified Reduce step that computes the elements of matrix C."""
    C = {}
    # Aggregate values by key
    for key, value in intermediate:
        if key in C:
            C[key].append(value)
        else:
            C[key] = [value]
    # Compute each element of C
    result_matrix = [[0 for _ in range(len(A))] for _ in range(len(A))]
    for (matrix, i, j), values in C.items():
        a_values = [v for k, v in values if k == "A"]
        b_values = [v for k, v in values if k == "B"]
        result_matrix[i][j] = sum(a*b for a, b in zip(a_values, b_values))
    return result_matrix

# Example input matrices
A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 2]]

# Run the simplified MapReduce
intermediate = map_step(A, B)
C = reduce_step(intermediate)

# Print the result
print("Result Matrix C:")
for row in C:
    print(row)