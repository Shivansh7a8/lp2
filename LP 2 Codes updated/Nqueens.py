def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i = row
    j = col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens_util(board, row, N, solutions):
    if row == N:
        # Found a solution, add it to the list
        solutions.append(board.copy())
    else:
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                solve_n_queens_util(board, row + 1, N, solutions)
                board[row][col] = 0


def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)
    return solutions
solutions = solve_n_queens(4)
for solution in solutions:
    for row in solution:
        print(row)
    print()
