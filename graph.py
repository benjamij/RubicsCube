import networkx as nx
from sympy.combinatorics.permutations import Permutation

from cube import rubiks_cube
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

    def __init__(self, root=None):
        """ Constructor. Initializes the graph with a solved cube.
        """
        self._graph = nx.Graph()
        if root:
            self.root = root
        else:
            self.root = Node(rubiks_cube(), -1, -1)
        self._graph.add_node(self.root)

    def generate_adjacents(self, node):
        """ Returns the node adjacent list

            Args:
                node        Node instance for which to generate the
                            successor states.

            Return:
                List of adjacent nodes.
        """
        nodes = filter(lambda node: not self._graph.has_node(node),
                       self._get_adjacents(node))

        self._graph.add_nodes_from(nodes)
        return nodes

    def _get_adjacents(self, node):
        """ Returns a possible list of adjacents. Checks whether state is valid
            upon generation.

            Args:
                node        Node instance for which to generate possible
                            successor states.

            Return:
                List of successor states.
        """
        p_mov = node.parent_mov
        n_mov = node.mov
        n_cube = node.rubiks_cube

        # Removes the movement which creates a adjacent equals to the node's
        # parent
        moves = filter(lambda n: n != p_mov,

                       # The permutation of 12 movements (0, 1, 2, ..., 11) to
                       #ensure that there is no equal adjacent nodes
                       Permutation.unrank_nonlex(12, 479001600).list())

        return map(lambda m: Node(move_rubiks_cube(n_cube, m), m, n_mov),
                   moves)
