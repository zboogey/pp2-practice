def solve(numheads, numlegs):
    num_chickens = 0
    num_rabbits = 0
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        if (2 * num_chickens + 4 * num_rabbits) == numlegs:
            return num_chickens, num_rabbits
    return None, None
numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
if chickens is not None and rabbits is not None:
    print("Number of chickens:", chickens)
    print("Number of rabbits:", rabbits)
else:
    print("No solution found.")
