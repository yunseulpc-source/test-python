from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("SCIP")

x = solver.IntVar(0, 10, "x")

x = solver.IntVar(0, 10, "x")
y = solver.IntVar(0, 10, "y")

# x + 2y <= 14
solver.Add(x + 2 * y <= 14)

# maximize 3x + 4y
solver.Maximize(3 * x + 4 * y)

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("Objective =", solver.Objective().Value())
    print("x =", x.solution_value())
    print("y =", y.solution_value())
else:
    print("No optimal solution")
