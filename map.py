import tkinter as tk
from tkinter import messagebox

# Available colors for map coloring
COLORS = ['red', 'green', 'blue', 'yellow']

def is_valid(country, color, assignment, neighbors):
    for neighbor in neighbors.get(country, []):
        if assignment.get(neighbor) == color:
            return False
    return True

def backtrack(countries, neighbors, assignment):
    if len(assignment) == len(countries):
        return assignment

    unassigned = [c for c in countries if c not in assignment]
    current = unassigned[0]

    for color in COLORS:
        if is_valid(current, color, assignment, neighbors):
            assignment[current] = color
            result = backtrack(countries, neighbors, assignment)
            if result:
                return result
            del assignment[current]

    return None

def parse_input(input_text):
    neighbors = {}
    countries = set()
    for line in input_text.strip().split('\n'):
        parts = line.split(':')
        if len(parts) != 2:
            continue
        country = parts[0].strip()
        adjacent = [x.strip() for x in parts[1].split(',') if x.strip()]
        neighbors[country] = adjacent
        countries.add(country)
        for adj in adjacent:
            countries.add(adj)
    return list(countries), neighbors

def solve():
    input_data = input_text.get("1.0", tk.END)
    countries, neighbors = parse_input(input_data)
    assignment = backtrack(countries, neighbors, {})
    if assignment:
        draw_result(assignment)
    else:
        messagebox.showinfo("Result", "No valid coloring found!")

def draw_result(assignment):
    canvas.delete("all")
    x, y = 20, 20
    for country, color in assignment.items():
        canvas.create_rectangle(x, y, x+100, y+40, fill=color, outline='black')
        canvas.create_text(x+50, y+20, text=country, fill='white', font=('Arial', 10, 'bold'))
        y += 50
        if y > 400:
            y = 20
            x += 120

# --- GUI Setup ---
root = tk.Tk()
root.title("Map Coloring CSP Solver")

tk.Label(root, text="Enter Countries and their Neighbors (format: A: B, C, D)", font=("Arial", 12)).pack(pady=5)

input_text = tk.Text(root, height=10, width=50)
input_text.pack()

example = """India: Pakistan, China, Nepal
Pakistan: India, Afghanistan
China: India, Nepal
Nepal: India, China
Afghanistan: Pakistan"""

input_text.insert(tk.END, example)

solve_btn = tk.Button(root, text="Solve Map Coloring", command=solve, font=("Arial", 12), bg='lightblue')
solve_btn.pack(pady=10)

canvas = tk.Canvas(root, width=600, height=500, bg='white')
canvas.pack()

root.mainloop()
