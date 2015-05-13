import networkx as nx
from sympy.combinatorics.permutations import Permutation
from math import factorial
import random

from cube import RubiksCube
from cube import move_rubiks_cube


class Node(object):

    def __init__(self, rubiks_cube, mov, parent_mov):
        """ Constructor

            Args:
                rubiks_cube     The rubik's cube to which this node belongs
                mov             The movement that this node represents
                parent_mov      The parent's movement
        """
        self.rubiks_cube = rubiks_cube
        self.mov = mov
        self.parent_mov = parent_mov
        # Parent node
        self.parent = None


class RCGraph(object):
    """ Represents the rubik's cube in graph form. Relies on networkx.
    """
    def __init__(self):
        """ Constructor. Initializes the graph with a solved cube.
        """
        self._graph = nx.Graph()
        self.root = Node(RubiksCube(), -1, -1)
        self._graph.add_node(self.root)

    def generate_adjacents(self, node):
        """ Returns the node adjacent list

            Args:
                node        Node instance for which to generate the
                            successor states.

            Return:
                List of adjacent nodes.
        """
        nodes = self._get_possible_adjacents(node)
        while(not self._is_valid_adjacents(nodes)):
            nodes = self._get_possible_adjacents(node)
        for n in nodes:
            self._add_node(n, node)
        return nodes

    def _get_possible_adjacents(self, node):
        """ Returns a possible list of adjacents. Checks whether state is valid
            upon generation.

            Args:
                node        Node instance for which to generate possible
                            successor states.

            Return:
                List of successor states.
        """
        # List of 12 or 11 random movements, one for each child
        p_mov = node.parent_mov

        # The permutation of 12 movements (0, 1, 2, ..., 11) to ensure that
        # there is no equal adjacent nodes
        moves = Permutation.unrank_nonlex(12, random.randint(1,
                                          factorial(12))).list()

        if p_mov > 0:
            # Removes the movement which creates a adjacent equals to the
            # node's parent
            moves.remove(p_mov)

        return [Node(move_rubiks_cube(node.rubiks_cube, m), m, node.mov) for m in moves]

    def _is_valid_adjacents(self, nodes):
        """ Checks if the generated adjacent is valid,
            the list of nodes will be valid if it none of its nodes already exist \
            in the graph.

            Args:
                nodes       The list of nodes whose validity to check.
        """
        for rb in nodes:
            if self._graph.has_node(rb):
                return False
        return True

    def _add_node(self, node, parent=None):
        """ Adds a new node in the graph.

            Args:
                node        The node that is to be added to the graph.
                parent      (Optional) parent of the node to attach to the graph.
        """
        self._graph.add_node(node)
        if parent:
            self._graph.add_edge(node, parent)
        else:
            self._graph.add_edge(node, self.root)
