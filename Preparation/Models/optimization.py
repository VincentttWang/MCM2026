import numpy as np
from scipy.optimize import linprog, minimize

class Optimizer:
    @staticmethod
    def solve_linear(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None):
        """
        Solves linear programming problem:
        Minimize: c^T * x
        Subject to: A_ub * x <= b_ub
                    A_eq * x == b_eq
        """
        res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
        return res

    @staticmethod
    def solve_nonlinear(fun, x0, constraints=(), bounds=None):
        """
        Solves non-linear programming problem:
        Minimize: fun(x)
        Subject to: constraints
        """
        res = minimize(fun, x0, method='SLSQP', bounds=bounds, constraints=constraints)
        return res

if __name__ == "__main__":
    print("--- Linear Programming Test ---")
    # Maximize z = 29x1 + 45x2 -> Minimize -z = -29x1 - 45x2
    # Subject to:
    # x1 - x2 - 5 <= 0
    # x1 + 3x2 <= 30
    # 2x1 + x2 <= 20
    # x1, x2 >= 0
    
    c = [-29, -45]
    A = [[1, -1], [1, 3], [2, 1]]
    b = [5, 30, 20]
    bounds = [(0, None), (0, None)]
    
    res = Optimizer.solve_linear(c, A_ub=A, b_ub=b, bounds=bounds)
    print("Optimization Success:", res.success)
    print("Optimal Value:", -res.fun) # Negate back for maximization
    print("Values:", res.x)
    
    print("\n--- Non-linear Optimization Test ---")
    # Minimize f(x) = (x1 - 1)^2 + (x2 - 2.5)^2
    # Subject to:
    # x1 - 2x2 + 2 >= 0
    # -x1 - 2x2 + 6 >= 0
    # x1 - 2x2 + 2 >= 0 -> 2x2 - x1 <= 2 (Standard form is g(x) >= 0 usually for minimize, 
    # but scipy constraints are dictionary {'type': 'ineq', 'fun': ...} where ineq means fun(x) >= 0)
    
    fun = lambda x: (x[0] - 1)**2 + (x[1] - 2.5)**2
    # Constraints: x[0] - 2*x[1] + 2 >= 0
    cons = ({'type': 'ineq', 'fun': lambda x:  x[0] - 2 * x[1] + 2},
            {'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 6},
            {'type': 'ineq', 'fun': lambda x: -x[0] + 2 * x[1] + 2})
    
    bnds = ((0, None), (0, None))
    
    res_nl = Optimizer.solve_nonlinear(fun, [2, 0], constraints=cons, bounds=bnds)
    print("Optimization Success:", res_nl.success)
    print("Optimal Value:", res_nl.fun)
    print("Values:", res_nl.x)
