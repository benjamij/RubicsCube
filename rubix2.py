__author__ = 'Benjamin Jakobus'

import networkx as nx
import random
import copy
import matplotlib.pyplot as plt
from collections import deque
COLORS = ['white', 'red', 'blue', 'orange', 'green', 'yellow']

# Movement directions
RIGHT       = 'right'
UP          = 'up'
GROUP_RIGHT = 'group_r'
GROUP_UP    = 'group_u'

# Indexes
FRONT       = 0
BACK        = 1
BOTTOM      = 2
LEFT        = 3
RIGHT       = 4
TOP         = 5

# def convert_to_tuple(state):
#     tuples = []
#     for side in state:
#         tuples.append((tuple(side[0]), tuple(side[1]), tuple(side[2])))

    # return tuple(tuples)

def generate_graph(state):
    stack = deque()
    stack.append(state)
    G = nx.Graph()
    while stack:
        state = stack.pop()
        # state_tuple = tuple(tuple(l) for l in state)
        # state_tuple = convert_to_tuple(state)

        if G.has_node(str(state)) is not True:
            G.add_node(str(state))

        states = generate_successor_states(state)

        for successor in states:
            # successor_tuple = convert_to_tuple(successor)
            if G.has_node(str(successor)):
                G.add_edge(str(successor), str(state))
                continue

            G.add_node(str(successor))
            G.add_edge(str(successor), str(state))
            stack.append(successor)
    return G



def generate_successor_states(state):
    states = []
    # Apply all possible movements
    for i in range(0, 3):
        states.append(apply_movement(state, RIGHT, i))
        # states.append(apply_movement(state, UP, i))
        #TODO: Do the same for up and group movements

    return states



def create_random_state():
    """ Generates a random state for the cube

        state[0] = front
        state[1] = back
        state[2] = bottom
        state[3] = left
        state[4] = right
        state[5] = top
    """
    return [
        random_matrix(), # Front
        random_matrix(), # Back
        random_matrix(), # Bottom
        random_matrix(), # Left
        random_matrix(), # Right
        random_matrix() # Top
    ]

def random_matrix():
    row_1 = [random.choice(COLORS), random.choice(COLORS), random.choice(COLORS)]
    row_2 = [random.choice(COLORS), random.choice(COLORS), random.choice(COLORS)]
    row_3 = [random.choice(COLORS), random.choice(COLORS), random.choice(COLORS)]

    return [row_1, row_2, row_3]

def apply_movement(state, movement, index):
    """ Accepts a state and direction of movement as input.
        Returns a new state with the movement applied to the specified row/column.
    """
    # Create a deep copy of the state to which the movement is to be applied
    new_state = copy.deepcopy(state)
    if movement is RIGHT:
        new_state[FRONT][index] = state[LEFT][index]
        new_state[RIGHT][index] = state[FRONT][index]
        new_state[BACK][index] = state[RIGHT][index]
        new_state[LEFT][index] = state[BACK][index]
    elif movement is UP:
        for i in range(0, 3):
            new_state[TOP][i][index] =  state[FRONT][i][index]
            new_state[BACK][i][index] =  state[TOP][i][index]
            new_state[BOTTOM][i][index] =  state[BACK][i][index]
            new_state[FRONT][i][index] =  state[BOTTOM][i][index]
    elif movement is GROUP_RIGHT:
        None
    elif movement is GROUP_UP:
        None

    return new_state


G = generate_graph(create_random_state())

nx.draw(G,with_labels=False)
plt.show()