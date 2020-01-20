import pygame as pg

# Intializing Pygame
pg.init()

# Display Variables
DISPLAY_WIDTH = 400
DISPLAY_HEIGHT = 400
DISPLAY = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pg.display.set_caption('Tic Tac Toe')

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clock Variables
CLOCK = pg.time.Clock()
FPS = 30

# Board
Matrix = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]


class Board:
    # Some Variables
    key_i = None
    key_j = None
    turn = "X"
    winner = None
    tie = None
    # Running All The Functions

    def main(self):
        self.lines()
        self.print_thingy()
        self.select_block()
        self.type_stuff()
        self.check_winner(Board.turn)

    # Function just to draw lines
    def draw_lines(self, x, y, width, height):
        pg.draw.rect(DISPLAY, BLACK, (x, y, width, height))

    # Making All The Vertical and horizontal lines for the grid
    def lines(self):
        self.hori_gap = int(DISPLAY_WIDTH / 3)
        self.ver_gap = int(DISPLAY_HEIGHT / 3)
        thick = 2
        distance_covered_ver = -1 * thick
        distance_covered_hori = -1 * thick

        for _ in range(3):
            self.draw_lines(distance_covered_ver, 0, thick, DISPLAY_HEIGHT)
            self.draw_lines(0, distance_covered_hori,
                            DISPLAY_WIDTH, thick)
            distance_covered_ver += self.ver_gap
            distance_covered_hori += self.hori_gap

    # Function to print stuff that we can call later on
    def print_stuff(self, font_size, text, color, x, y):
        font = pg.font.Font(None, font_size)
        text_render = font.render(text, 1, color)
        DISPLAY.blit(text_render, (x, y))

    # Printinng O and X on the grid
    def print_thingy(self):
        for i in range(3):
            for j in range(3):
                n = Matrix[j][i]
                xx = self.hori_gap * i + 0.33 * self.hori_gap
                yy = self.ver_gap * j + 0.3 * self.ver_gap
                if n == "X":
                    self.print_stuff(100, str(n), GREEN, xx, yy)
                else:
                    self.print_stuff(100, str(n), BLUE, xx, yy)

    # When we click on the a block it would be selected
    def select_block(self):
        self.click = pg.mouse.get_pressed()
        self.mouse = pg.mouse.get_pos()

        # As we know there are three blocks each consiting of three subblocks we're gonna get the vertical and   #horizontal box one by one and then combine them to get the subblock position
        if self.click[0] == 1:
                # We're getting the which of the vertical box is being clicked through this
            ver_block = self.mouse[1] // (DISPLAY_HEIGHT // 3)
            # We're getting the which of the horizontal box is being clicked through this
            hori_block = self.mouse[0] // (DISPLAY_WIDTH // 3)
            Board.key_i = ver_block
            Board.key_j = hori_block

    # Typing Os And Xs on the grid
    def type_stuff(self):
        # Globaling the matrix list as we need to change it's values now
        global Matrix
        self.keys = pg.key.get_pressed()
        if Board.key_i != None and Board.key_j != None:
            if Board.turn == "0":
                if self.keys[pg.K_o] and Matrix[Board.key_i][Board.key_j] == "" and Board.winner == None:
                    Matrix[Board.key_i][Board.key_j] = "O"
                    Board.turn = "X"
            if Board.turn == "X" and Matrix[Board.key_i][Board.key_j] == "" and Board.winner == None:
                if self.keys[pg.K_x]:
                    Matrix[Board.key_i][Board.key_j] = "X"
                    Board.turn = "0"
            if self.keys[pg.K_SPACE]:
                Matrix = [[""] * 3, [""] * 3, [""] * 3]
                Board.turn = "X"
                Board.winner = None
                Board.tie = None
                empty = []

    # Checking For The Winner
    def check_winner(self, turn):
        # Horizontally
        for i in Matrix:
            if i == ["X"] * 3:
                Board.winner = "X"
            if i == ["O"] * 3:
                Board.winner = "O"
        # Vertically
        if Matrix[0][0] == Matrix[1][0] == Matrix[2][0] == "X"or Matrix[0][1] == Matrix[1][1] == Matrix[2][1] == "X"or Matrix[0][2] == Matrix[1][2] == Matrix[2][2] == "X":
            Board.winner = "X"
        if Matrix[0][0] == Matrix[1][0] == Matrix[2][0] == "O"or Matrix[0][1] == Matrix[1][1] == Matrix[2][1] == "O"or Matrix[0][2] == Matrix[1][2] == Matrix[2][2] == "O":
            Board.winner = "O"
        if Matrix[0][0] == Matrix[1][1] == Matrix[2][2] == "X" or Matrix[0][2] == Matrix[1][1] == Matrix[2][0] == "X":
            Board.winner = "X"
        # Diagonally
        if Matrix[0][0] == Matrix[1][1] == Matrix[2][2] == "O" or Matrix[0][2] == Matrix[1][1] == Matrix[2][0] == "O":
            Board.winner = "O"
        if Board.winner != None:
            self.print_stuff(110, f"Player {Board.winner}", RED, (DISPLAY_WIDTH // 2) - 150, (DISPLAY_WIDTH // 2) - 100)
            self.print_stuff(110, "Won!", RED, (DISPLAY_WIDTH //
                                                2) - 100, (DISPLAY_WIDTH // 2) - 30)

        empty = []
        for i in Matrix:
            empty.append(all(i))

        if not Board.winner:
            if empty == [True] * 3:
                self.print_stuff(
                    110, "Tie!", RED, (DISPLAY_WIDTH // 2) - 70, (DISPLAY_WIDTH // 2) - 30)
# The Main Function


def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        DISPLAY.fill(WHITE)
        # Functions
        Board_object = Board()
        Board_object.main()
        # Updating Everything In Time
        CLOCK.tick(FPS)
        pg.display.update()


main()
