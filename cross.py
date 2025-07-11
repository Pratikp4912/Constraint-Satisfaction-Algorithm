# Crossword layout with blank (_) and blocked (#) cells
crossword_layout = [
    ['_', '_', '_', '_', '_'],
    ['_', '#', '_', '#', '_'],
    ['_', '_', '_', '_', '_'],
    ['_', '#', '_', '#', '_'],
    ['_', '_', '_', '_', '_']
]

grid_size = len(crossword_layout)

def is_valid(word, row, col, direction, grid):
    for k in range(len(word)):
        r, c = (row + k, col) if direction == 'V' else (row, col + k)
        if r >= grid_size or c >= grid_size:
            return False
        if crossword_layout[r][c] == '#':
            return False
        if grid[r][c] not in ('', word[k]):
            return False
    return True

def place_word(word, row, col, direction, grid):
    placed = []
    for k in range(len(word)):
        r, c = (row + k, col) if direction == 'V' else (row, col + k)
        if grid[r][c] == '':
            grid[r][c] = word[k]
            placed.append((r, c))
    return placed

def remove_word(placed, grid):
    for r, c in placed:
        grid[r][c] = ''

def solve_csp(index, grid, words):
    if index == len(words):
        return True
    word = words[index]
    for i in range(grid_size):
        for j in range(grid_size):
            for direction in ['H', 'V']:
                if is_valid(word, i, j, direction, grid):
                    placed = place_word(word, i, j, direction, grid)
                    if solve_csp(index + 1, grid, words):
                        return True
                    remove_word(placed, grid)
    return False

def print_grid(grid):
    for row in grid:
        print(' '.join(cell if cell else '_' for cell in row))

# === MAIN ===
if __name__ == "__main__":
    n = int(input("Enter number of words (up to 5): "))
    words = []
    for i in range(n):
        word = input(f"Enter word {i + 1}: ").strip().upper()
        words.append(word)

    # Initialize grid based on layout
    grid = [['' if crossword_layout[i][j] == '_' else '#' for j in range(grid_size)] for i in range(grid_size)]

    if solve_csp(0, grid, words):
        print("\nCrossword Solution:")
        print_grid(grid)
    else:
        print("\nNo solution found. Try different words or check layout.")

#3 STAR,RAT,ART