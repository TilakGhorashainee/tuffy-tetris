# Imports
from operator import itemgetter
from collections import defaultdict
from random import Random
import numpy as np
# Some interfaces



class Color:
    CLEAR = "clear"
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    YELLOW = "yellow"
    MAGENTA = "magenta"
    CYAN = "cyan"
    ORANGE = "orange"
    BLACK = "black"
    #AQUATIC THEME
    TIFFANY_BLUE = "tiffany blue"
    AQUAMARINE = "aquamarine"
    HONOLULU_BLUE = "honolulu blue"
    JACARTA = 'jacarta'
    PEARLY_PURPLE = 'pearly purple'
    LEMON_MERINGUE = 'lemon meringue'
    NAPLES_YELLOW = 'naples yellow'
    #FOREST THEME
    DARK_LAVA = 'dark lava'
    COYOTE_BROWN = 'coyote brown'
    CRAYOLAS_OUTER_SPACE = 'crayolas outer space'
    GRAY_ASPARAGUS = 'gray-asparagus'
    AXOLOTL = 'axolotl'
    PHILIPPINE_GRAY = 'philippine gray'
    ARTICHOKE = 'artichoke'
    #INDUSTRIAL THEME
    JAPANESE_INDIGO = 'japanese indigo',
    CARMINE_PINK = 'carmine pink',
    BRIGHT_GRAY = 'bright gray',
    TUFTS_BLUE = 'tufts blue',
    CRAYOLAS_GOLD = 'vampire black',
    SEA_GREEN = 'sea green',
    ASH_GRAY = 'ash gray'
    @staticmethod
    def colors():
        return (Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW,
                Color.MAGENTA, Color.CYAN, Color.ORANGE, Color.BLACK, 
                Color.TIFFANY_BLUE, Color.AQUAMARINE, Color.HONOLULU_BLUE, 
                Color.JACARTA, Color.PEARLY_PURPLE, Color.LEMON_MERINGUE,
                Color.NAPLES_YELLOW, Color.DARK_LAVA, Color.COYOTE_BROWN, 
                Color.CRAYOLAS_OUTER_SPACE, Color.GRAY_ASPARAGUS, Color.AXOLOTL,
                Color.PHILIPPINE_GRAY, Color.ARTICHOKE, Color.JAPANESE_INDIGO, 
                Color.CARMINE_PINK, Color.BRIGHT_GRAY, Color.TUFTS_BLUE, 
                Color.CRAYOLAS_GOLD, Color.SEA_GREEN, Color.ASH_GRAY)


class ViewBase:
    def __init__(self):
        self.rows = []
        self.width = 0
        self.height = 0

    def set_size(self, columns, rows):
        self.width = columns
        self.height = rows
        self.clear()

    def clear(self):
        self.rows = [[Color.CLEAR] * self.width for i in range(self.height)]

    def render_tile(self, x, y, color):
        if (0 <= x < self.width and 0 <= y < self.height):
            self.rows[y][x] = color


class TextView(ViewBase):
    """Renders a board as text."""

    COLOR_CHAR = {
        Color.CLEAR: '.',
        Color.RED: '*',
        Color.BLUE: '#',
        Color.GREEN: 'o',
        Color.YELLOW: 'O',
        Color.MAGENTA: '%',
        Color.CYAN: '&',
        Color.ORANGE: '$',
        #AQUATIC THEME
        Color.TIFFANY_BLUE: '^',
        Color.AQUAMARINE: '!',
        Color.HONOLULU_BLUE: '@',
        Color.JACARTA: '(',
        Color.PEARLY_PURPLE: ')',
        Color.LEMON_MERINGUE: '-',
        Color.NAPLES_YELLOW: '+',
        #FOREST THEME
        Color.DARK_LAVA: '_', 
        Color.COYOTE_BROWN: '=', 
        Color.CRAYOLAS_OUTER_SPACE: 'q', 
        Color.GRAY_ASPARAGUS: 'w', 
        Color.AXOLOTL: 'e',
        Color.PHILIPPINE_GRAY: 'r', 
        Color.ARTICHOKE: 't',
        #INDUSTRIAL THEME
        Color.JAPANESE_INDIGO: 'y',
        Color.CARMINE_PINK: 'u',
        Color.BRIGHT_GRAY: 'i',
        Color.TUFTS_BLUE: 'p',
        Color.CRAYOLAS_GOLD: 'a',
        Color.SEA_GREEN: 's',
        Color.ASH_GRAY: 'd'
    }

    def __init__(self, surf=None):
        ViewBase.__init__(self)

    def show(self):
        str_ = self.get_str()
        print(str_)

    def get_str(self):
        str_ = "\n"
        for column in self.rows:
            for item in column:
                str_ += TextView.COLOR_CHAR[item]
            str_ += "\n"
        return str_


class Piece:
    L_SHAPE = {"tiles": ((0, 0), (0, 1), (0, 2), (1, 2)),
               "x_adj": 1,
               "y_adj": 2,
               "color": Color.YELLOW}
    R_SHAPE = {"tiles": ((0, 0), (1, 0), (0, 1), (0, 2)),
               "x_adj": 1,
               "y_adj": 2,
               "color": Color.ORANGE}
    O_SHAPE = {"tiles": ((0, 0), (0, 1), (1, 0), (1, 1)),
               "x_adj": 1,
               "y_adj": 1,
               "color": Color.CYAN}
    T_SHAPE = {"tiles": ((0, 0), (1, 0), (1, 1), (2, 0)),
               "x_adj": 2,
               "y_adj": 1,
               "color": Color.MAGENTA}
    S_SHAPE = {"tiles": ((0, 0), (0, 1), (1, 1), (1, 2)),
               "x_adj": 1,
               "y_adj": 2,
               "color": Color.BLUE}
    Z_SHAPE = {"tiles": ((0, 0), (1, 0), (1, 1), (2, 1)),
               "x_adj": 2,
               "y_adj": 1,
               "color": Color.GREEN}
    I_SHAPE = {"tiles": ((0, 0), (1, 0), (2, 0), (3, 0)),
               "x_adj": 3,
               "y_adj": 0,
               "color": Color.RED}
    #DEFAULT THEME
    L_SHAPE_YELLOW = {"color": Color.YELLOW}
    R_SHAPE_ORANGE = {"color": Color.ORANGE}
    O_SHAPE_CYAN = {"color": Color.CYAN}
    T_SHAPE_MAGENTA = {"color": Color.MAGENTA}
    S_SHAPE_BLUE = {"color": Color.BLUE}
    Z_SHAPE_GREEN = {"color": Color.GREEN}  
    I_SHAPE_RED = {"color": Color.RED} 


    # AQUATIC THEME
    L_SHAPE_TIFFANY_BLUE = {"color": Color.TIFFANY_BLUE}
    R_SHAPE_AQUAMARINE = {"color": Color.AQUAMARINE}
    O_SHAPE_HONOLULU_BLUE = {"color": Color.HONOLULU_BLUE}
    T_SHAPE_JACARTA = {"color": Color.JACARTA}
    S_SHAPE_PEARLY_PURPLE = {"color": Color.PEARLY_PURPLE}
    Z_SHAPE_LEMON_MERINGUE = {"color": Color.LEMON_MERINGUE}  
    I_SHAPE_NAPLES_YELLOW = {"color": Color.NAPLES_YELLOW} 

    #FOREST THEME
    L_SHAPE_DARK_LAVA = {"color": Color.DARK_LAVA}
    R_SHAPE_COYOTE_BROWN = {"color": Color.COYOTE_BROWN}
    O_SHAPE_CRAYOLAS_OUTER_SPACE = {"color": Color.CRAYOLAS_OUTER_SPACE}
    T_SHAPE_GRAY_ASPARAGUS = {"color": Color.GRAY_ASPARAGUS}
    S_SHAPE_AXOLOTL = {"color": Color.AXOLOTL}
    Z_SHAPE_PHILIPPINE_GRAY = {"color": Color.PHILIPPINE_GRAY}  
    I_SHAPE_ARTICHOKE = {"color": Color.ARTICHOKE} 

    #INDUSTRIAL THEME
    L_SHAPE_JAPANESE_INDIGO = {"color": Color.JAPANESE_INDIGO}
    R_SHAPE_CARMINE_PINK = {"color": Color.CARMINE_PINK}
    O_SHAPE_BRIGHT_GRAY = {"color": Color.BRIGHT_GRAY}
    T_SHAPE_TUFTS_BLUE = {"color": Color.TUFTS_BLUE}
    S_SHAPE_CRAYOLAS_GOLD = {"color": Color.CRAYOLAS_GOLD}
    Z_SHAPE_SEA_GREEN = {"color": Color.SEA_GREEN}  
    I_SHAPE_ASH_GRAY = {"color": Color.ASH_GRAY} 



    SHAPES = (L_SHAPE, R_SHAPE, O_SHAPE, T_SHAPE, S_SHAPE, Z_SHAPE, I_SHAPE)

    def __init__(self, x, y, shape, color, rot=0):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.rotation = rot

    def move(self, x, y):
        self.x += x
        self.y += y

    def __iter__(self):
        for x_offset, y_offset in self.shape["tiles"]:
            if self.rotation == 0:
                yield (self.x + x_offset, self.y + y_offset)
            elif self.rotation == 1:
                yield (self.x - y_offset + self.shape["y_adj"],
                       self.y + x_offset)
            elif self.rotation == 2:
                yield (self.x - x_offset + self.shape["x_adj"],
                       self.y - y_offset + self.shape["y_adj"])
            elif self.rotation == 3:
                yield (self.x + y_offset,
                       self.y - x_offset + self.shape["x_adj"])

    def render(self, v):
        for x, y in self:
            v.render_tile(x, y, self.color)

    def rotate(self, clockwise=True):
        if clockwise:
            self.rotation = (self.rotation + 1) % 4
        else:
            self.rotation = (self.rotation - 1) % 4

    def rotated(self, clockwise=True):
        p = Piece(self.x, self.y, self.shape, self.color, self.rotation)
        p.rotate(clockwise)
        return p


class Board:


    def __init__(self, n_columns, n_rows, board=None, autogen=True):
        self.height = n_rows
        self.columns = [self.height] * n_columns
        self.rand = Random()
        self.autogen = autogen

        self.reset()

    def reset(self):
        self.piece = None
        self.hold_block = None
        self.hold_used = False
        self.first_hold = False
        self.drop_x = 0
        self.drop_y = 0
        self.finalize_ready = False
        self.tiles = defaultdict(lambda: Color.CLEAR)
        self.score = 0
        self.level = 1
        self.lines = 0
        self.game_over = False

    def clear_tile(self, x, y):
        self.tiles[(x, y)] = Color.CLEAR

        # Move all the tiles above this row down one space
        for y_tile in range(y, self.columns[x] - 1, -1):
            self.tiles[(x, y_tile)] = self.tiles[(x, y_tile - 1)]

        # And reset the top of of the columns
        while (self.columns[x] < self.height and
               self.tiles[(x, self.columns[x])] == Color.CLEAR):
            self.columns[x] += 1

    def clear_row(self, row):
        for col in range(len(self.columns)):
            self.clear_tile(col, row)

    def row_full(self, row):
        for col in range(len(self.columns)):
            if self.tiles[(col, row)] == Color.CLEAR:
                return False
        return True

    def set_tile_color(self, x, y, color):
        assert color != Color.CLEAR
        self.tiles[(x, y)] = color
        if self.columns[x] > y:
            self.columns[x] = y

    def piece_can_move(self, x_move, y_move):
        """Returns True if a piece can move, False otherwise."""
        for base_x, base_y in self.piece:
            x = x_move + base_x
            y = y_move + base_y
            if not 0 <= x < len(self.columns) or y >= self.columns[x]:
                return False
        return True

    def drop_piece(self):
        """Either drops a piece down one level, or finalizes it and creates another piece."""
        if self.piece is None:
            return
        if not self.piece_can_move(0, 1):
            # We want to give a short leeway for the player to move the piece, once it's hit bottom
            if self.finalize_ready:
                self.finalize_piece()
                if self.autogen:
                    self.generate_piece()
            else:
                self.finalize_ready = True
        else:
            self.piece.move(0, 1)
            self.finalize_ready = False

    def full_drop_piece(self):
        """Either drops a piece down one level, or finalizes it and creates another piece."""
        if self.piece is None:
            return
        while self.piece_can_move(0, 1):
            self.piece.move(0, 1)
        self.finalize_piece()
        self.generate_piece()

    def move_piece(self, x_move, y_move):
        """Move a piece some number of spaces in any direction"""
        if self.piece is None:
            return
        if self.piece_can_move(x_move, y_move):
            self.piece.move(x_move, y_move)

    def rotate_piece(self, clockwise=True):
        if self.piece is None:
            return
        if self.piece_can_rotate(clockwise):
            self.piece.rotate(clockwise)

    def piece_can_rotate(self, clockwise):
        """Returns True if a piece can drop, False otherwise."""
        p = self.piece.rotated(clockwise)
        for x, y in p:
            if not 0 <= x < len(self.columns) or y >= self.columns[x]:
                return False
        return True
    
    def make_piece(self):
        middle = len(self.columns) // 2
        shape = self.rand.choice(Piece.SHAPES)
        made_piece = Piece(middle - shape["x_adj"], 0, shape, shape["color"])
        return made_piece

    def hold_piece(self):
        if self.piece is None:
            return
        if self.hold_used is False:
            self.hold_used = True
            self.drop_x = self.piece.x
            self.drop_y = self.piece.y
            self.piece.x = 0
            self.piece.y = 0
            self.hold_block = self.piece
            self.hold_generate_piece()
        else:
            self.drop_x = self.piece.x
            self.drop_y = self.piece.y
            self.piece.x = 0
            self.piece.y = 0
            self.hold_block, self.piece = self.piece, self.hold_block
            self.hold_generate_piece()

    def get_hold_piece(self):
        if self.hold_block is not None:
            return self.hold_block
        else:
            return 

    def get_hold_color(self):
        if self.hold_block != None:
            return self.hold_block.color
        else:
            return
            
    def hold_generate_piece(self):
        if self.game_over:
            return

        if self.first_hold is False:
            self.piece = self.make_piece()
            self.first_hold = True

        self.piece.x = self.drop_x
        self.piece.y = self.drop_y
        self.piece

        if not self.piece_can_move(0, 0):
            # Show piece on the board
            self.finalize_piece()

            # And mark the game as over
            self.game_over = True
            self.piece = None

    def generate_piece(self):
        """Creates a new piece at random and places it at the top of the board."""
        if self.game_over:
            return

        self.piece = self.make_piece()

        if not self.piece_can_move(0, 0):
            # Show piece on the board
            self.finalize_piece()

            # And mark the game as over
            self.game_over = True
            self.piece = None

    def finalize_piece(self):
        for x, y in self.piece:
            self.set_tile_color(x, y, self.piece.color)

        rows_cleared = 0
        for y in range(0, self.height + 1):
            if self.row_full(y):
                self.clear_row(y)
                rows_cleared += 1

        self.score += (rows_cleared * rows_cleared) * 10
        self.lines += rows_cleared
        self.level = self.lines // 10 + 1

        self.piece = None

    def render(self, v):
        v.clear()
        v.set_size(len(self.columns), self.height)
        for (x, y), color in self.tiles.items():
            v.render_tile(x, y, color)
        if self.piece is not None:
            self.piece.render(v)
        v.set_score(self.score)
        v.set_level(self.level)
        


    def leaderboard(self, username):
        leaderboard = []
        with open("leaderboard.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                currentLine = line.split(",")
                leaderboard.append([currentLine[0], int(currentLine[1])])
        f.close()

        leaderboard.append([str(username), int(self.score)])

        leaderboard = sorted(leaderboard, key=itemgetter(1), reverse=True)

        fi = open("leaderboard.txt", "w")
        for score in leaderboard:
            fi.write(score[0])
            fi.write(', ')
            fi.write(str(score[1]))
            fi.write("\n")
        fi.close()
        
        print(leaderboard)
