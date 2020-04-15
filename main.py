from manimlib.imports import *
from enum import Enum


class RubikPos(Enum):
    UBL = 1
    UBR = 2
    UFR = 3
    UFL = 4
    DFL = 5
    DFR = 6
    DBR = 7
    DBL = 8
    UB = 9
    UR = 10
    UF = 11
    UL = 12
    BL = 13
    BR = 14
    FR = 15
    FL = 16
    DF = 17
    DR = 18
    DB = 19
    DL = 20
    U = 21
    D = 22
    F = 23
    B = 24
    L = 25
    R = 26

# U is OUT
# D is IN
# F is DOWN
# B is UP
#


DRAW_ORDER = [OUT, IN, DOWN, UP, LEFT, RIGHT]
COLOR_ORDER = [WHITE, YELLOW, GREEN, BLUE, ORANGE, RED]
# UFR Orientation
STICKER_MAP = {
    RubikPos.UBL: 0b100110,
    RubikPos.UBR: 0b100101,
    RubikPos.UFR: 0b101001,
    RubikPos.UFL: 0b101010,
    RubikPos.DFL: 0b011010,
    RubikPos.DFR: 0b011001,
    RubikPos.DBR: 0b010101,
    RubikPos.DBL: 0b010110,
    RubikPos.UB:  0b100100,
    RubikPos.UR:  0b100001,
    RubikPos.UF:  0b101000,
    RubikPos.UL:  0b100010,
    RubikPos.BL:  0b000110,
    RubikPos.BR:  0b000101,
    RubikPos.FR:  0b001001,
    RubikPos.FL:  0b001010,
    RubikPos.DF:  0b011000,
    RubikPos.DR:  0b010001,
    RubikPos.DB:  0b010100,
    RubikPos.DL:  0b010010,
    RubikPos.U:   0b100000,
    RubikPos.D:   0b010000,
    RubikPos.F:   0b001000,
    RubikPos.B:   0b000100,
    RubikPos.L:   0b000010,
    RubikPos.R:   0b000001
}


class Cubie(object):

    def __init__(self, base, squares):
        self.base = base
        self.squares = squares
        self.group = VGroup()
        self.group.add(self.base)
        for square in squares:
            self.group.add(square)

    def draw(self, scene):
        scene.play(ShowCreation(self.group))


def create_cubie(pos):
    base = Cube(fill_color=GREY, stroke_width=1, fill_opacity=1, side_length=1)
    for i, d in enumerate(DRAW_ORDER):
        if STICKER_MAP[pos] & (1 << i) != 0:
            base.shift(base.side_length * d)

    squares = []
    for i, d in enumerate(DRAW_ORDER):
        if STICKER_MAP[pos] & (1 << i) == 0:
            continue
        square = Square(
            side_length=base.side_length * 0.8,
            shade_in_3d=True,
        )
        square.set_fill(COLOR_ORDER[i], opacity=1)
        square.flip()
        square.shift(base.side_length * OUT / 2.0 * 1.02)
        square.apply_matrix(z_to_vector(d))
        for i, d in enumerate(DRAW_ORDER):
            if STICKER_MAP[pos] & (1 << i) != 0:
                square.shift(base.side_length * d)

        squares.append(square)
    return Cubie(base, squares)


class RubiksCubeScene(SpecialThreeDScene):
    def construct(self):
        phi_init = 70 * DEGREES
        self.set_camera_orientation(phi=phi_init)
        self.begin_ambient_camera_rotation(rate=0.7)
        group = VGroup()
        for i in range(1, 27):
            cubie = create_cubie(RubikPos(i))
            cubie.draw(self)
         
        self.wait(10)


class RubiksCubeScrambleScene(SpecialThreeDScene):
    def construct(self):
        phi_init = 70 * DEGREES
        self.set_camera_orientation(phi=phi_init)
        self.begin_ambient_camera_rotation(rate=0.7)

        group = VGroup()
        for i in range(1, 27):
            cubie = create_cubie(RubikPos(i))
            cubie.draw()

