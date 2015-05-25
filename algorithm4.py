
import math
import time
import numpy as np
import matplotlib.pyplot as plt
from solver import Solver
from cube import rubiks_cube

result_full = []


def dfs_bfs():
    solver = Solver(3)
    result = [[], []]  # Keeps the execution time + path length
    bfs_target = rubiks_cube()
    for i in range(4):
        print '# i = ', i
        t = []
        l = []
        for j in range(100):
            print'### j = ', j
            start = time.clock()
            v = solver.dfs(math.pow(2, i))
            u = solver.bfs(v, bfs_target)
            p = solver.calculate_shortest_path(u)  # Path from v to cube's initial state
            total_time = time.clock() - start
            if total_time < 180:
                print "### time %d length %d" % (total_time, len(p))
                t.append(total_time)
                l.append(len(p))
                result_full.append(len(p))
        result[0].append(np.median(t))
        result[1].append(np.median(l))
    return result

result_1 = dfs_bfs()
plt.figure(1)
# To plot the i X time
plt.plot(result_1[0], 'b--', result_1[0], 'ro')
plt.xlabel(u"Valores de i")
plt.ylabel(u"Tempo (s)")

# To plot the i X length
plt.figure(2)
plt.plot(result_1[1], 'b--', result_1[1], 'ro')
plt.xlabel(u"Valores de i")
plt.ylabel(u"Tamanho do caminho")
plt.show()


plt.figure(3, figsize=(15, 10))
plt.plot(result_full, 'bo')
plt.xlabel(u"Iterações")
plt.ylabel(u"Tamanho do caminho")
plt.show()
