from cube import rubiks_cube
from cube import move_rubiks_cube


class Node(object):

    def __init__(self, rubiks_cube, mov, parent_mov=-1):
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

            Args:
                root        The graph's root node. Optional.
        """
        self._graph = dict()

        if root:
            self.root = root
        else:
            self.root = Node(rubiks_cube(), -1, -1)
        self._graph[str(self.root)] = True

    def generate_adjacents(self, node):
        """ Returns the node adjacent list

            Args:
                node        Node instance for which to generate the
                            successor states.

            Return:
                List of adjacent nodes.
        """
        nodes = filter(lambda node: not self._has_node(node),
                       self._get_adjacents(node))

        self._graph[str(nodes)] = True
        return nodes

    def _has_node(self, node):
        """ Checks whether the graph already contains the given node.

            Args:
                node    The node whose existence to determine

            Return:
                True if the graph contains the given node; false if not.

        """
        return self._graph.get(str(node), False)

    def _get_adjacents(self, node):
        """ Returns a possible list of adjacents. Checks whether state is
            valid upon generation.

            Args:
                node        Node instance for which to generate possible
                            successor states.

            Return:
                List of successor states.
        """
        p_mov = node.parent_mov
        n_mov = node.mov
        n_cube = node.rubiks_cube

        # List of movements used to generate adjacent nodes.
        moves = filter(lambda n: n != p_mov, range(12))
        # Using filter to remove the movement that generates the parent node\
        # avoiding to create a adjacent equals to the node's parent.

        return map(lambda m: Node(move_rubiks_cube(n_cube, m), m, n_mov),
                   moves)
