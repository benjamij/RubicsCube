
# Cube faces
FRONT, BACK, DOWN, LEFT, RIGHT, UP = 0, 1, 2, 3, 4, 5

# A dictionary with faces: for better understanding each face can be
# considered a color in rubik's cube.
FACES = {FRONT: 'F', BACK: 'B', DOWN: 'D', LEFT: 'L', RIGHT: 'R', UP: 'U'}


def rubiks_cube():
    """
    Returns a cube in its initial state ('solved' cube), when each cube's \
    face correctly arranged. The cube is represented as an array of faces, \
    each face as an array of rows and each row is an array with three values.
    """
    return [
        [['F1', 'F2', 'F3'], ['F4', 'F5', 'F6'], ['F7', 'F8', 'F9']],
        [['B1', 'B2', 'B3'], ['B4', 'B5', 'B6'], ['B7', 'B8', 'B9']],
        [['D1', 'D2', 'D3'], ['D4', 'D5', 'D6'], ['D7', 'D8', 'D9']],
        [['L1', 'L2', 'L3'], ['L4', 'L5', 'L6'], ['L7', 'L8', 'L9']],
        [['R1', 'R2', 'R3'], ['R4', 'R5', 'R6'], ['R7', 'R8', 'R9']],
        [['U1', 'U2', 'U3'], ['U4', 'U5', 'U6'], ['U7', 'U8', 'U9']]
    ]


def move_rubiks_cube(rubiks_cube, face):
    """ Returns a new RubiksCube with the face rotated.
        Input face can be a value between 0 and 11 (all possible movements)
    """
    cube = None
    if face <= 5:
        cube = _move_cubes_face(rubiks_cube, face, True)
    else:
        _face = face - 6
        cube = _move_cubes_face(rubiks_cube, _face, False)
    return cube


def _move_cubes_face(cube, face, clockwise):
    """ Returns a cube with the face rotated.
    """
    if clockwise:
        return _rotate_clockwise(cube, face)
    else:
        return _rotate_counter_clockwise(cube, face)


def _rotate_clockwise(cube_state, face):
    """ Applies one clockwise movement over a cube's face.

        Args:
            cube_state
            face
    """
    cube = rubiks_cube()

    if face is UP:
        cube[UP] = _rotate_clockwise_matrix(cube_state[UP])
        cube[FRONT][0], cube[RIGHT][0], cube[BACK][0], cube[LEFT][0] = cube_state[LEFT][0], cube_state[FRONT][0], cube_state[RIGHT][0], cube_state[BACK][0]
        cube[DOWN] = cube_state[DOWN]

    elif face is DOWN:
        cube[DOWN] = _rotate_clockwise_matrix(cube_state[DOWN])
        cube[FRONT][2], cube[RIGHT][2], cube[BACK][2], cube[LEFT][2] = cube_state[LEFT][2], cube_state[FRONT][2], cube_state[RIGHT][2], cube_state[BACK][2]
        cube[UP] = cube_state[UP]

    elif face is FRONT:
        cube[FRONT] = _rotate_clockwise_matrix(cube_state[FRONT])
        cube[UP][2] = [cube_state[LEFT][2][2], cube_state[LEFT][1][2], cube_state[LEFT][0][2]]
        cube[LEFT][0][2], cube[LEFT][1][2], cube[LEFT][2][2] = cube_state[DOWN][0][0], cube_state[DOWN][0][1], cube_state[DOWN][0][2]
        cube[DOWN][0] = [cube_state[RIGHT][2][0], cube_state[RIGHT][1][0], cube_state[RIGHT][0][0]]
        cube[RIGHT][0][0], cube[RIGHT][1][0], cube[RIGHT][2][0] = cube_state[UP][2][0], cube_state[UP][2][1], cube_state[UP][2][2]
        cube[BACK] = cube_state[BACK]

    elif face is BACK:
        cube[BACK] = _rotate_clockwise_matrix(cube_state[BACK])
        cube[DOWN][2] = [cube_state[LEFT][0][0], cube_state[LEFT][1][0], cube_state[LEFT][2][0]]
        cube[RIGHT][0][2], cube[RIGHT][1][2], cube[RIGHT][2][2] = cube_state[DOWN][2][2], cube_state[DOWN][2][1], cube_state[DOWN][2][0]
        cube[UP][0] = [cube_state[RIGHT][0][2], cube_state[RIGHT][1][2], cube_state[RIGHT][2][2]]
        cube[LEFT][0][0], cube[LEFT][1][0], cube[LEFT][2][0] = cube_state[UP][0][2], cube_state[UP][0][1], cube_state[UP][0][0]
        cube[FRONT] = cube_state[FRONT]

    elif face is RIGHT:
        cube[RIGHT] = _rotate_clockwise_matrix(cube_state[RIGHT])
        cube[BACK][0][0], cube[BACK][1][0], cube[BACK][2][0] = cube_state[UP][2][2], cube_state[UP][1][2], cube_state[UP][0][2]
        cube[DOWN][0][2], cube[DOWN][1][2], cube[DOWN][2][2] = [cube_state[BACK][2][0], cube_state[BACK][1][0], cube_state[BACK][0][0]]
        cube[UP][0][2], cube[UP][1][2], cube[UP][2][2] = [cube_state[FRONT][0][2], cube_state[FRONT][1][2], cube_state[FRONT][2][2]]
        cube[FRONT][0][2], cube[FRONT][1][2], cube[FRONT][2][2] = [cube_state[DOWN][0][2], cube_state[DOWN][1][2], cube_state[DOWN][2][2]]
        cube[LEFT] = cube_state[LEFT]

    elif face is LEFT:
        cube[LEFT] = _rotate_clockwise_matrix(cube_state[LEFT])
        cube[BACK][0][2], cube[BACK][1][2], cube[BACK][2][2] = cube_state[DOWN][2][0], cube_state[DOWN][1][0], cube_state[DOWN][0][0]
        cube[DOWN][0][0], cube[DOWN][1][0], cube[DOWN][2][0] = [cube_state[FRONT][0][0], cube_state[FRONT][1][0], cube_state[FRONT][2][0]]
        cube[UP][0][0], cube[UP][1][0], cube[UP][2][0] = [cube_state[BACK][2][2], cube_state[BACK][1][2], cube_state[BACK][0][2]]
        cube[FRONT][0][0], cube[FRONT][1][0], cube[FRONT][2][0] = [cube_state[UP][0][0], cube_state[UP][1][0], cube_state[UP][2][0]]
        cube[RIGHT] = cube_state[RIGHT]

    return cube


def _rotate_clockwise_matrix(m):
    """ Rotates the matrix by 90 degrees

        Args:
            matrix
    """
    m[0][0], m[0][1], m[0][2], m[1][0], m[1][1], m[1][2], m[2][0], m[2][1], m[2][2], = m[2][0], m[1][0], m[0][0], m[2][1], m[1][1], m[0][1], m[2][2], m[1][2], m[0][2]
    return m


def _rotate_counter_clockwise(cube_state, face):
    """ Rotates a face by 90 degrees in the counter-clockwise direction applying \
        _rotate_clockwise three times.

        Args:
            cube_state
            face
    """
    cube = _rotate_clockwise(cube_state, face)
    cube = _rotate_clockwise(cube, face)
    return _rotate_clockwise(cube, face)
