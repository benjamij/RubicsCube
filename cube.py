import numpy as np

""" This module is responsible for representing and applying
    movements to the given cube.
"""

# FACES is an array of faces where each face is represented by an array of \
# pieces.
FACES = [
    #Front
    [0, 1, 2, 3, 4, 5, 6, 7],
    # Back
    [12, 13, 14, 15, 16, 17, 18, 19],
    # Down
    [5, 6, 7, 9, 10, 17, 18, 19],
    # Up
    [0, 1, 2, 8, 11, 12, 13, 14],
    # Right
    [2, 4, 7, 10, 11, 12, 15, 17],
    # Left
    [0, 3, 5, 8, 9, 14, 16, 19]
]

# Basically, one movement is just a rearrange of pieces that belongs to the \
# same face. The dict MOVEMENTS has the movement code (key) and the array
# (value) which represents the new arrangement of pieces.
MOVEMENTS = {
    # Front face movement (moves pieces: 0, 1, 2, 3, 4, 5, 6 and 7)
    # clockwise:
    0: [5, 3, 0, 6, 1, 7, 4, 2],
    # counterclockwise:
    6: [2, 4, 7, 1, 6, 0, 3, 5],

    # Back face movement (moves pieces: 12, 13, 14, 15, 16, 17, 18 and 19)
    # clockwise:
    1: [17, 15, 12, 18, 13, 19, 16, 14],
    # counterclockwise:
    7: [14, 16, 19, 13, 18, 12, 15, 17],

    # Down face movement (moves pieces: 5, 6, 7, 9, 10, 17, 18 and 19)
    # clockwise:
    2: [19, 9, 5, 18, 6, 7, 10, 17],
    # counterclockwise:
    8: [7, 10, 17, 6, 18, 19, 9, 5],

    # Up face movement (moves pieces: 0, 1, 2, 8, 11, 12, 13 and 14)
    # clockwise:
    3: [2, 11, 12, 1, 13, 14, 8, 0],
    # counterclockwise:
    9: [14, 8, 0, 13, 1, 2, 11, 12],

    # Right face movement (moves pieces: 2, 4, 7, 10, 11, 12, 15 and 17)
    # clockwise:
    4: [7, 10, 17, 15, 4, 2, 11, 12],
    # counterclockwise:
    10: [12, 11, 2, 4, 15, 17, 10, 7],

    # Left face movement (moves pieces: 0, 3, 5, 8, 9, 14, 16 and 19)
    # clockwise:
    5: [14, 8, 0, 16, 3, 19, 9, 5],
    # counterclockwise:
    11: [5, 9, 19, 3, 16, 0, 8, 14]
}


def rubiks_cube():
    """ Returns a cube in its initial state ('solved' cube): each cube's face \
    correctly arranged. The cube is represented as an array of pieces.
    """
    return [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
    ]


def move_rubiks_cube(rubiks_cube, movement):
    """ Applies a movement over the cube.

        Args:
            rubiks_cube     The cube
            movement        The movement code [0 - 11]
        Return:
            The cube moved
    """
    cube = np.array(rubiks_cube).tolist()

    # Face that will be moved
    face = FACES[movement if movement < 6 else movement - 6]

    # New arrangement
    f_movement = MOVEMENTS[movement]

    # Rearranging pieces...
    for i in range(8):
        cube[face[i]] = rubiks_cube[f_movement[i]]

    return cube
