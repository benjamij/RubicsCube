__author__ = 'Benjamin Jakobus'
from graph import *
import math
from solver import *
import matplotlib.pyplot as plt


# Run experiment

# Max limit for BFS is three minutes
TIME_LIMIT = 3

# Create graph with initial configuration
graph = RCGraph()
solver = Solver(graph)
# List of lists containing the results [[x-axis], [y-axis]]
results = [[], []]

# Turn on timer
start = time.clock()

for i in range(0, 20):
    # Limit for DFS is 2 raised to the power of i
    limit = math.pow(2, i)
    for j in range(0, 100):
        v = solver.dfs(graph.root, limit)
        u = solver.bfs(v, graph.root, TIME_LIMIT)

        # Calculate shortest path
        path = solver.calculate_shortest_path(u)

        # Result item
        results[0].append(limit)
        results[1].append(len(path))

        # Save result to file
        solver.save_result("Iteration i=" + str(i) + ", j= " + str(j), path, "result.txt")

# Get elapsed time in seconds
elapsed = time.clock() - start

print 'Total time taken: ' + str(elapsed) + ' seconds'

plt.plot(results[0], results[1])
plt.ylabel('some numbers')
plt.show()