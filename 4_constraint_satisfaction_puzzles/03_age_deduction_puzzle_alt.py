from ortools.sat.python import cp_model


def solve_ages():
    model = cp_model.CpModel()

    # Declare variables for ages
    H = model.NewIntVar(11, 24, "H")
    K = model.NewIntVar(11, 24, "K")
    L = model.NewIntVar(11, 24, "L")
    O = model.NewIntVar(11, 24, "O")
    Y = model.NewIntVar(11, 24, "Y")

    # Intermediate variable for the age difference
    age_diff_OH = model.NewIntVar(
        0, 13, "age_diff_OH"
    )  # Max difference can be 13 (24 - 11)

    # Constraints
    model.Add(H != Y)  # H is not the same age as Y
    model.Add(K < H)  # K is younger than H
    model.Add(H - K < 8)  # K is less than 8 years younger than H
    model.Add(Y < L)  # Y is younger than L
    model.Add(L == H)  # L is the same age as H
    model.Add(O < H - 10)  # O is more than 10 years younger than H
    model.Add(age_diff_OH == H - O)  # Age difference between O and H
    model.AddModuloEquality(1, H - O, 2)  # The difference is odd

    # All ages must be different
    model.AddAllDifferent([H, K, L, O, Y])

    # Solve the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print("Ages:")
        print(f"H: {solver.Value(H)}")
        print(f"K: {solver.Value(K)}")
        print(f"L: {solver.Value(L)}")
        print(f"O: {solver.Value(O)}")
        print(f"Y: {solver.Value(Y)}")
    else:
        print("No solution found.")


# Run the solver
solve_ages()
