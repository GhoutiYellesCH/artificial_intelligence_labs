# Artificial Intelligence Labs

This repository contains academic laboratory assignments and implementations for an Artificial Intelligence course, covering search algorithms, constraint satisfaction problems (CSP), and optimization.

---

## Structure Overview

### 1. Lab 1: NumPy & Matrix Operations
- **`1_numpy_matrix_inversion.py`**: Implementation of matrix inversion using NumPy (`np.linalg.inv`).
- **`1_numpy_matrix_inversion_screenshot.png`**: Extracted screenshot preview of the original IDE implementation.
- **`1_numpy_matrix_inversion_screenshot.ps`**: Original PostScript document of the implementation.

### 2. Lab 2: Uninformed & Informed Search Algorithms
- **`2_bfs_and_dfs_search.py`**: Breadth-First Search (BFS) and Depth-First Search (DFS) on state spaces.
- **`2_ucs_and_astar_search.py`**: Uniform Cost Search (UCS) and A* (A-Star) heuristic search algorithms.

### 3. Lab 3: Advanced Search Algorithms
- **`3_search_algorithms/`**:
  - **`bfs_and_dfs_search.py`**: Breadth-First and Depth-First Search implementation.
  - **`depth_limited_search.py`**: Depth-Limited Search (DLS).
  - **`ucs_and_astar_search.py`**: Uniform Cost Search (UCS) and A* Search.
- **`3_depth_limited_search.py`**: Depth-Limited Search standalone script.
- **`3_dls_and_ids_search.py`**: Depth-Limited Search (DLS) and Iterative Deepening Search (IDS).
- **`3_ucs_and_astar_search.py`**: Clean implementation of UCS and A* search.

### 4. Lab 4: Constraint Satisfaction Problems (CSP)
Located in **`4_constraint_satisfaction_puzzles/`**:
- **`01_basic_linear_constraints.py`**: Basic linear integer constraints with Google OR-Tools CP-SAT.
- **`02_send_more_money_cryptarithmetic.py`**: Classic SEND + MORE = MONEY cryptarithmetic puzzle.
- **`03_age_deduction_puzzle.py`**: Age deduction logic problem.
- **`03_age_deduction_puzzle_alt.py`**: Alternative formulation for the age logic puzzle.
- **`04_zebra_einstein_riddle.py`**: Einstein's Riddle (Zebra Puzzle).
- **`05_magic_square_puzzle.py`**: 3x3 Magic Square constraint solver.
- **`06_eight_queens_puzzle.py`**: 8-Queens chessboard problem.
- **`07_sudoku_solver.py`**: 9x9 Sudoku grid constraint solver.
- **`08_knights_tour.py`**: Knight's Tour board traversal.
- **`5_draft_solutions/`**: Preliminary drafts for Lab 5 exercises.

**`4_environment_and_archive/`**:
- **`test_cp_model_basic.py`**: Minimal test verifying the OR-Tools CP-SAT solver.
- **`terminal_cp_model_debug.log`**: Terminal log from environment testing.
- **`4_venv_backup.tar.gz`**: Virtualenv and environment archive backup.

### 5. Lab 5: CSP Optimization & Scheduling
Located in **`5_csp_optimization_and_scheduling/`**:
- **`00_basic_arithmetic_csp.py`**: Basic arithmetic constraint relations.
- **`01_arithmetic_relations_all_solutions.py`**: Enumerating all solutions for a system of equations.
- **`02_polynomial_equation_csp.py`**: Multi-variable nonlinear constraint optimization.
- **`03_safe_combination_lock_puzzle.py`**: 9-digit safe code combination riddle.
- **`04_knapsack_optimization.py`**: 0/1 Knapsack optimization problem.
- **`05_task_scheduling_makespan_optimization.py`**: Project scheduling with precedence constraints and makespan minimization.
- **`06_worker_task_assignment_optimization.py`**: Optimal worker-to-task assignment minimizing duration.
