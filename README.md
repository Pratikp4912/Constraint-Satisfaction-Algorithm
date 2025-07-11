# Constraint-Satisfaction-Algorithm
import itertools

# Cryptarithmetic
def cryptarithmetic():
    print("\nCryptarithmetic: SEND + MORE = MONEY\n")
    for p in itertools.permutations(range(10), 8):
        s, e, n, d, m, o, r, y = p
        if s * m == 0: continue
        send = s*1000 + e*100 + n*10 + d
        more = m*1000 + o*100 + r*10 + e
        money = m*10000 + o*1000 + n*100 + e*10 + y
        if send + more == money:
            print(f"SEND={send}, MORE={more}, MONEY={money}")
            return
    print("No solution found.")

# Crossword
def crossword():
    print("\nCrossword Puzzle\n")
    grid = [['+', '-', '+'], ['+', '-', '+'], ['+', '-', '+']]
    words = ["CAT", "DOG"]

    def can_place(word, r, c):
        return c + len(word) <= 3 and all(grid[r][c+i] in ['-', word[i]] for i in range(len(word)))

    def place(word, r, c): [grid[r].__setitem__(c+i, word[i]) for i in range(len(word))]
    def remove(r, c, l): [grid[r].__setitem__(c+i, '-') for i in range(l)]

    def backtrack(i):
        if i == len(words): return True
        for r in range(3):
            for c in range(3):
                if can_place(words[i], r, c):
                    place(words[i], r, c)
                    if backtrack(i+1): return True
                    remove(r, c, len(words[i]))
        return False

    if backtrack(0): [print(' '.join(row)) for row in grid]
    else: print("No solution.")

# Map Coloring
def map_coloring():
    print("\nMap Coloring: Australia\n")
    regions = ['WA','NT','SA','Q','NSW','V','T']
    adj = {'WA':['NT','SA'],'NT':['WA','SA','Q'],'SA':['WA','NT','Q','NSW','V'],'Q':['NT','SA','NSW'],
           'NSW':['Q','SA','V'],'V':['SA','NSW'],'T':[]}
    colors = ['Red','Green','Blue']
    assign = {}

    def valid(r, c): return all(assign.get(n) != c for n in adj[r])

    def bt(i):
        if i == len(regions): return True
        for c in colors:
            if valid(regions[i], c):
                assign[regions[i]] = c
                if bt(i+1): return True
                del assign[regions[i]]
        return False

    if bt(0): [print(f"{r}: {assign[r]}") for r in regions]
    else: print("No solution.")

# Menu
while True:
    print("\n1.Cryptarithmetic  2.Crossword  3.Map Coloring  4.Exit")
    ch = input("Choose: ")
    if ch == '1': cryptarithmetic()
    elif ch == '2': crossword()
    elif ch == '3': map_coloring()
    elif ch == '4': break
    else: print("Invalid.")
