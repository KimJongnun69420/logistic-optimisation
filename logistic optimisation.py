from scipy.optimize import linprog

# Define the cost coefficients: production costs and transportation costs
# c_X = 20, c_Y = 25 (Production costs)
# c_XA = 5, c_XB = 10, c_YA = 15, c_YB = 10 (Transportation costs)
c = [20, 25, 5, 10, 15, 10]

# Define the constraint matrix A and the right-hand side vector b
A = [
    [1, 0, -1, -1, 0, 0],  # Total transportation from Factory X <= Production at Factory X (P_X)
    [0, 1, 0, 0, -1, -1],  # Total transportation from Factory Y <= Production at Factory Y (P_Y)
    [0, 0, 1, 0, 1, 0],    # Demand at Warehouse A (T_XA + T_YA) >= 400
    [0, 0, 0, 1, 0, 1],    # Demand at Warehouse B (T_XB + T_YB) >= 200
    [1, 0, 0, 0, 0, 0],    # Production at Factory X (P_X) <= 500
    [0, 1, 0, 0, 0, 0]     # Production at Factory Y (P_Y) <= 300
]
b = [0, 0, 400, 200, 500, 300]

# Define the bounds for each variable (non-negative)
# Variables: P_X, P_Y, T_XA, T_XB, T_YA, T_YB
bounds = [(0, None)] * 6  # Each variable must be >= 0

# Solve the linear programming problem using the 'highs' method
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

# Check the result and output the solution
if result.success:
    print("Optimization Successful!")
    print(f"Minimum Cost: {result.fun:.2f}")
    print("Optimal Values (P_X, P_Y, T_XA, T_XB, T_YA, T_YB):")
    print(result.x)
else:
    print("Optimization Failed!")
