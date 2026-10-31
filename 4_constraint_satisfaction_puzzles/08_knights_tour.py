from ortools.sat.python import cp_model


def knight_tour():
    model = cp_model.CpModel()

    # Board size
    n = 8

    # Create variables for the knight's position at each step
    x = [model.NewIntVar(0, n - 1, f"x{i}") for i in range(n * n)]
    y = [model.NewIntVar(0, n - 1, f"y{i}") for i in range(n * n)]
    step = list(range(n * n))

    # Add constraints to ensure the knight visits each square exactly once
    model.AddAllDifferent(step)

    # Possible knight moves
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    # Add constraints for knight moves
    for i in range(n * n - 1):
        for dx, dy in moves:
            model.Add(x[i + 1] == x[i] + dx).OnlyEnforceIf([y[i + 1] == y[i] + dy])
            model.Add(y[i + 1] == y[i] + dy).OnlyEnforceIf([x[i + 1] == x[i] + dx])

    # Add constraints to ensure the knight stays within the board
    for i in range(n * n):
        model.Add(x[i] >= 0)
        model.Add(x[i] < n)
        model.Add(y[i] >= 0)
        model.Add(y[i] < n)

    # Add constraint for returning to the starting position
    model.Add(x[0] == x[n * n - 1])
    model.Add(y[0] == y[n * n - 1])

    # Solve the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print("Knight's Tour Path:")
        for i in range(n * n):
            print(f"Step {i + 1}: (x={solver.Value(x[i])}, y={solver.Value(y[i])})")
    else:
        print("No solution found.")


# Run the knight's tour solver
knight_tour()
