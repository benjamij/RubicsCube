__author__ = 'Benjamin Jakobus'

from collections import deque
from graph import *
import time
import math

""" The rubik's cube solver. Shuffles a rubik's cube and then
    attempts to solve it.
"""

def dfs(graph, offset, limit):
    """ Performs a depth-first search on the given graph
        until the specified limit is reached.

        Args:
        graph       RCGraph instance on which to execute the depth-first search
        offset      Node on which to start with the depth-first search
        limit       The maximum number of nodes to visit until the search is to be
                    terminated

        Return:
                    The node that was encountered at the given limit.

    """
    # Recursion in Python is expensive, so we will use a queue for our DFS traversal
    q = deque()

    # Start with the root node (i.e. solved rubik's cube)
    q.appendleft(offset)
    count = 0
    while q:
        # Remove element from the left side of the queue
        node = q.popleft()
        count += 1

        # If we reach our limit, then terminate and return the node
        if count >= limit:
            return node

        # Generate successor states (i.e. neighbours for the given node)
        for adj in graph.generate_adjacents(node):
            # Always add nodes to the left side of the queue - this way
            # we ensure a FIFO order when processing the nodes
            q.appendleft(adj)
    return None

def bfs(graph, offset, target, time_limit):
    """ Performs a breadth-first search on the given graph, starting at the
        given offset node. The search terminates until either the target node is reached,
        or until the time limit is reached.

        Args:
            graph               RCGraph instance on which to execute the breadth-first search
            offset              The offset node on which to start with the breadth-first search
            target              The target node to reach
            time_limit          Maximum amount of time (in minutes) to search until terminating
    """
    # Queue for performing the bfs traversal
    q = []
    q.append(offset)

    # Turn on timer
    start = time.clock()
    while q:
        node = q.pop(0)

        if node.rubiks_cube.cube is target.rubiks_cube.cube:
            return node

        # Get elapsed time in seconds
        elapsed = time.clock() - start

        # Convert elapsed time to minutes
        elapsed = elapsed / 60.0

        # Terminate if time limit is reached
        if elapsed >= time_limit:
            return node

        # Generate successor states (i.e. neighbours for the given node)
        for adj in graph.generate_adjacents(node):
            adj.parent = node
            q.append(adj)

    return None

def calculate_shortest_path(node):
    """
        Args:
            node        The encountered destination state from which to calculate the
                        shortest path
        Return:
            List of moves indicating the shortest path between the offset state and the target state.
    """
    path = [node.rubiks_cube.cube]

    while node.parent is not None:
        node = node.parent
        path.append(node.rubiks_cube.cube)
    return path

def save_result(description, cube_path, file):
    """ Writes the obtained result to file along with a description.

        Args:
            description     Textual description of the iteration to save
            cube_path       Sequence of cube states
            file            Output file (string)

    """
    with open(file, "a") as f:
        f.write(description + "\n")
        f.write(cube_path)
        f.write("=======\n\n")


# Run experiment
# ====================
# Max limit for BFS is three minutes
TIME_LIMIT = 3

# Create graph with initial configuration
graph = RCGraph()
for i in range(0, 20):
    # Limit for DFS is 2 raised to the power of i
    limit = math.pow(2, i)
    for j in range(0, 100):
        v = dfs(graph, graph.root, limit)
        u = bfs(graph, v, graph.root, TIME_LIMIT)

        # Calculate shortest path
        path = calculate_shortest_path(u)

        # Save result to file
        save_result("Iteration i=" + str(i) + ", j= " + str(j), path, "result.txt")
# ====================

#
# graph = RCGraph()
#
# v = dfs(graph, graph.root, 10)
# print 'dfs ok'
# u = bfs(graph, v, graph.root, 1)
# print 'bfs ok'
# # Calculate shortest path
# path = calculate_shortest_path(u)
# print path