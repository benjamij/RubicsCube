
import time
import math
import numpy as np
import matplotlib.pyplot as plt
from solver import Solver


def dfs():
    solver = Solver(3)
    result = []
    for i in range(11):
        t = []
        # Gets 100 samples
        for j in range(100):
            start = time.clock()
            v = solver.dfs(math.pow(2, i))
            t.append(time.clock() - start)
        # Calculates the median time
        result.append(np.median(t))

    # Returns a list of medians
    return result


x = dfs()
plt.plot(x, 'b--', x, 'ro')
plt.xlabel(u"Iterações")
plt.ylabel(u"Tempo (s)")
plt.show()
