
from collections import deque
import time
import random

from graph import RCGraph
from graph import Node

""" The rubik's cube solver. Contains methods for searching and calculating
    the shortest path.
"""


class Solver:

    def __init__(self, time_limit=3):
        """ Constructor

            Args:
                time_limit          Maximum amount of time (in minutes) to search until terminating
        """
        self.time_limit = time_limit

    def dfs(self, limit):
        graph = RCGraph()
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
        q.appendleft(graph.root)
        count = 0

        while q:
            # Remove element from the left side of the queue
            node = q.popleft()
            count += 1

            # If we reach our limit, then terminate and return the node
            if count >= limit:
                return Node(node.rubiks_cube, node.mov)

            # Generate successor states (i.e. neighbours for the given node)
            nodes = graph.generate_adjacents(node)

            # Appends a random adjacent node from nodes
            q.appendleft(nodes[random.randint(0, len(nodes) - 1)])

        return None

    def bfs(self, offset, target):
        """ Performs a breadth-first search on the given graph, starting at the
            given offset node. The search terminates until either the target node is reached,
            or until the time limit is reached.

            Args:
                offset              The offset node on which to start with the breadth-first search
                target              The target node to reach
        """
        graph = RCGraph(offset)
        # Queue for performing the bfs traversal
        q = []
        q.append(offset)

        # Turn on timer
        start = time.clock()
        while q:
            node = q.pop(0)

            if node.rubiks_cube == target:
                return node

            # Get elapsed time in seconds
            elapsed = time.clock() - start

            # Convert elapsed time to minutes
            elapsed = elapsed / 60.0

            # Terminate if time limit is reached
            if elapsed >= self.time_limit:
                return node

            # Generate successor states (i.e. neighbours for the given node)
            for adj in graph.generate_adjacents(node):
                adj.parent = node
                q.append(adj)

        return None

    def calculate_shortest_path(self, node):
        """
            Args:
                node        The encountered destination state from which to calculate the
                            shortest path
            Return:
                List of moves indicating the shortest path between the offset state and the target state.
        """
        path = [node.rubiks_cube]

        while node.parent is not None:
            node = node.parent
            path.append(node.rubiks_cube)
        return path

    def save_result(self, description, cube_path, file):
        """ Writes the obtained result to file along with a description.

            Args:
                description     Textual description of the iteration to save
                cube_path       Sequence of cube states
                file            Output file (string)

        """
        with open(file, "a") as f:
            f.write(description + "\n")
            f.write(str(cube_path))
            f.write("=======\n\n")
