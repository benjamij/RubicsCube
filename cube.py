import copy
import numpy as np


FRONT, BACK, DOWN, LEFT, RIGHT, UP = 0, 1, 2, 3, 4, 5

# A dictionary with faces: for better understanding each face can be
# considered a color in rubik's cube.
FACES = {FRONT: 'F', BACK: 'B', DOWN: 'D', LEFT: 'L', RIGHT: 'R', UP: 'U'}


class RubiksCube(object):
    """docstring for Cube"""

    def __init__(self, cube=None):
        if cube:
            self.cube = cube
        else:
            self.cube = self.initial_state()

    def initial_state(self):
        """
        Returns a 'solved' cube, each cube's face correctly arranged.
        The cube is represented as an array of faces, each face as an array \
        of rows and each row is an array with three values.

        The solved cube looks like:
        [
        [['F1', 'F2', 'F3'], ['F4', 'F5', 'F6'], ['F7', 'F8', 'F9']],
        [['B1', 'B2', 'B3'], ['B4', 'B5', 'B6'], ['B7', 'B8', 'B9']],
        ...
        [['U1', 'U2', 'U3'], ['U4', 'U5', 'U6'], ['U7', 'U8', 'U9']]
        ]
        """
        #  For each value in the dict 'FACES' ('F', 'B'... 'U'),
        # calls _generate_face passing the value as argument
        return [self._generate_face(value) for value in FACES.itervalues()]

    def _generate_face(self, face):
        """
        Generates a cube's face correctly arranged.
        An face is represented as a 3x3 matrix (array of arrays), each value \
        in the matrix representes a cubelet's face in the cube's face.

        A matrix for face 'a':
        [['a1', 'a2', 'a3'],
         ['a4', 'a5', 'a6'],
         ['a7', 'a8', 'a9']]
        """
        matrix = []
        for i in range(3):
            matrix.append(["%s%d" % (face, x+(3*i)) for x in range(1, 4)])
        return matrix


def move_rubiks_cube(rubiks_cube, face):
    """
    Returns a new RubiksCube with the face rotated.
    Input face can be a value between 0 and 11 (all possible movements)
    """
    cube = None
    if face <= 5:
        cube = _move_cubes_face(rubiks_cube.cube, face, True)
    else:
        _face = face - 6
        cube = _move_cubes_face(rubiks_cube.cube, _face, False)
    return RubiksCube(cube)


def _move_cubes_face(cube, face, clockwise):
    """
    Returns a cube with the face rotated.
    """
    if clockwise:
        return _rotate_clockwise(cube, face)
    else:
        return _rotate_counter_clockwise(cube, face)


def _rotate_clockwise(cube_state, face):
    """
    Applies one clockwise movement over a cube's face.
    """
    cube = copy.deepcopy(cube_state)

    if face is UP:
        cube[UP] = _rotate_clockwise_matrix(cube[UP])
        cube[FRONT][0], cube[RIGHT][0], cube[BACK][0], cube[LEFT][0] = cube_state[LEFT][0], cube_state[FRONT][0], cube_state[RIGHT][0], cube_state[BACK][0]

    elif face is DOWN:
        cube[DOWN] = _rotate_clockwise_matrix(cube[DOWN])
        cube[FRONT][2], cube[RIGHT][2], cube[BACK][2], cube[LEFT][2] = cube_state[LEFT][2], cube_state[FRONT][2], cube_state[RIGHT][2], cube_state[BACK][2]

    elif face is FRONT:
        cube[FRONT] = _rotate_clockwise_matrix(cube[FRONT])
        cube[UP][2] = [cube_state[LEFT][2][2], cube_state[LEFT][1][2], cube_state[LEFT][0][2]]
        cube[LEFT][0][2], cube[LEFT][1][2], cube[LEFT][2][2] = cube_state[DOWN][0][0], cube_state[DOWN][0][1], cube_state[DOWN][0][2]
        cube[DOWN][0] = [cube_state[RIGHT][2][0], cube_state[RIGHT][1][0], cube_state[RIGHT][0][0]]
        cube[RIGHT][0][0], cube[RIGHT][1][0], cube[RIGHT][2][0] = cube_state[UP][2][0], cube_state[UP][2][1], cube_state[UP][2][2]

    elif face is BACK:
        cube[BACK] = _rotate_clockwise_matrix(cube[BACK])
        cube[DOWN][2] = [cube_state[LEFT][0][0], cube_state[LEFT][1][0], cube_state[LEFT][2][0]]
        cube[RIGHT][0][2], cube[RIGHT][1][2], cube[RIGHT][2][2] = cube_state[DOWN][2][2], cube_state[DOWN][2][1], cube_state[DOWN][2][0]
        cube[UP][0] = [cube_state[RIGHT][0][2], cube_state[RIGHT][1][2], cube_state[RIGHT][2][2]]
        cube[LEFT][0][0], cube[LEFT][1][0], cube[LEFT][2][0] = cube_state[UP][0][2], cube_state[UP][0][1], cube_state[UP][0][0]

    elif face is RIGHT:
        cube[RIGHT] = _rotate_clockwise_matrix(cube[RIGHT])
        cube[BACK][0][0], cube[BACK][1][0], cube[BACK][2][0] = cube_state[UP][2][2], cube_state[UP][1][2], cube_state[UP][0][2]
        cube[DOWN][0][2], cube[DOWN][1][2], cube[DOWN][2][2] = [cube_state[BACK][2][0], cube_state[BACK][1][0], cube_state[BACK][0][0]]
        cube[UP][0][2], cube[UP][1][2], cube[UP][2][2] = [cube_state[FRONT][0][2], cube_state[FRONT][1][2], cube_state[FRONT][2][2]]
        cube[FRONT][0][2], cube[FRONT][1][2], cube[FRONT][2][2] = [cube_state[DOWN][0][2], cube_state[DOWN][1][2], cube_state[DOWN][2][2]]

    elif face is LEFT:
        cube[LEFT] = _rotate_clockwise_matrix(cube[LEFT])
        cube[BACK][0][2], cube[BACK][1][2], cube[BACK][2][2] = cube_state[DOWN][2][0], cube_state[DOWN][1][0], cube_state[DOWN][0][0]
        cube[DOWN][0][0], cube[DOWN][1][0], cube[DOWN][2][0] = [cube_state[FRONT][0][0], cube_state[FRONT][1][0], cube_state[FRONT][2][0]]
        cube[UP][0][0], cube[UP][1][0], cube[UP][2][0] = [cube_state[BACK][2][2], cube_state[BACK][1][2], cube_state[BACK][0][2]]
        cube[FRONT][0][0], cube[FRONT][1][0], cube[FRONT][2][0] = [cube_state[UP][0][0], cube_state[UP][1][0], cube_state[UP][2][0]]

    return cube


def _rotate_clockwise_matrix(matrix):
    """
    Rotates the matrix by 90 degrees
    """
    # numpy.rot90() Rotate an array by 90 degrees in the counter-clockwise
    # direction.
    return np.rot90(np.array(matrix), 3).tolist()


def _rotate_counter_clockwise(cube_state, face):
    """
    Rotates a face by 90 degrees in the counter-clockwise direction applying \
    _rotate_clockwise three times.
    """
    cube = _rotate_clockwise(cube_state, face)
    cube = _rotate_clockwise(cube, face)
    return _rotate_clockwise(cube, face)
