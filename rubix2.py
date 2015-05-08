__author__ = 'Benjamin Jakobus'

import networkx as nx
import random
import copy
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
from rubix_viz import *
from matplotlib import *
COLORS = ['white', 'red', 'blue', 'orange', 'green', 'yellow']

# Movement directions
RIGHT       = 'right'
UP          = 'up'

# Indexes
FRONT       = 0
BACK        = 1
BOTTOM      = 2
LEFT        = 3
RIGHT       = 4
TOP         = 5


def generate_graph(state):
    stack = deque()
    stack.append(state)
    G = nx.Graph()
    while stack:
        state = stack.pop()

        if G.has_node(str(state)) is not True:
            G.add_node(str(state))

        states = generate_successor_states(state)

        for successor in states:
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
        # For each row and column, apply right movement and up movement
        states.append(apply_movement(state, RIGHT, i))

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
        # Moving the middle row of the cube
        new_state[FRONT][index] = state[LEFT][index]
        new_state[RIGHT][index] = state[FRONT][index]
        new_state[BACK][index] = state[RIGHT][index]
        new_state[LEFT][index] = state[BACK][index]
        if index is 0:
            # Moving the top row of the cube. This means that we also need to
            # rotate the elements in the TOP
            numpy_array = np.array(new_state[TOP])
            new_state[TOP] = np.rot90(numpy_array, 1).tolist()
        elif index is 2:
            # Moving the bottom row of the cube. This means that we also need to
            # rotate the elements in the BOTTOM
            numpy_array = np.array(new_state[BOTTOM])
            new_state[BOTTOM] = np.rot90(numpy_array, 1).tolist()
    elif movement is UP:
        for i in range(0, 3):
            new_state[TOP][i][index] =  state[FRONT][i][index]
            new_state[BACK][i][index] =  state[TOP][i][index]
            new_state[BOTTOM][i][index] =  state[BACK][i][index]
            new_state[FRONT][i][index] =  state[BOTTOM][i][index]
        if index is 0:
            # Moving the outer side of the cube...So, need to rotate left
            numpy_array = np.array(new_state[LEFT])
            new_state[LEFT] = np.rot90(numpy_array, 1).tolist()
        elif index is 2:
            # Moving the outer side of the cube...So, need to rotate right
            numpy_array = np.array(new_state[RIGHT])
            new_state[RIGHT] = np.rot90(numpy_array, 1).tolist()
    return new_state

print 'Generating graph...'
# G = generate_graph(create_random_state())
#
# nx.draw(G, with_labels=False)
# plt.show()


# Cublet test
state_1 = create_random_state()
state_2 = apply_movement(state_1, UP, 0)

# Display the first cublet of state 1
fig1 = plt.figure(figsize=(4, 4))
print state_1
cublet1 = [state_1[FRONT][0][0], state_1[BACK][0][0], state_1[TOP][0][0], state_1[BOTTOM][0][0], state_1[RIGHT][0][0], state_1[LEFT][0][0]]
print cublet1
ax1 = CubeAxes(cublet1, fig1)
fig1.add_axes(ax1)
ax1.draw_cube()
plt.savefig('1.png')

fig2 = plt.figure(figsize=(4, 4))
print state_2
cublet2 = [state_2[FRONT][0][0], state_2[BACK][0][0], state_2[TOP][0][0], state_2[BOTTOM][0][0], state_2[RIGHT][0][0], state_2[LEFT][0][0]]
print cublet2
ax2 = CubeAxes(cublet2, fig2)
fig2.add_axes(ax2)
ax2.draw_cube()
plt.savefig('2.png')