from tkinter import *
from tkinter import messagebox
from game import GameBrain

FONT = ("Arial", 20)
BACKGROUND_COLOR = 'BLACK'
FOREGROUND_COLOR = 'WHITE'


class GameInterface:
    def __init__(self, gamebrain: GameBrain):
        self.game = gamebrain
        self.mode = True  # True for single-player, False for two-player
        self.first = True  # True if Player 1 uses X, False if Player 1 uses O
        self.turn = 1  # Tracks turns
        self.game_on = False

        # Tkinter window setup
        self.window = Tk()
        self.window.title('Tic Tac Toe')
        self.window.config(padx=10, pady=10, bg=BACKGROUND_COLOR)
        self.window.resizable(False, False)

        # Load images
        self.load_images()

        # Setup UI
        self.setup_labels()
        self.setup_buttons()
        self.build_tiles()

        self.window.mainloop()

    def load_images(self):
        """Loads all necessary images."""
        self.on_img = PhotoImage(file='assets/toggle-on.png')
        self.off_img = PhotoImage(file='assets/toggle-off.png')
        self.human_img = PhotoImage(file='assets/2p.png')
        self.computer_img = PhotoImage(file='assets/1p.png')
        self.cross_img = PhotoImage(file='assets/cross.png')
        self.circle_img = PhotoImage(file='assets/circle.png')
        self.blank = PhotoImage(file='assets/blank.png')
        self.red_cross = PhotoImage(file='assets/red-cross-100.png')
        self.blue_circle = PhotoImage(file='assets/blue-circle-100.png')

    def setup_labels(self):
        """Sets up toggle labels."""
        self.p1_label = Label(image=self.computer_img, bg=BACKGROUND_COLOR)
        self.p1_label.grid(row=0, column=2)

        self.p2_label = Label(image=self.human_img, bg=BACKGROUND_COLOR)
        self.p2_label.grid(row=0, column=0)

        self.p1_or_p2 = Label(image=self.on_img, bg=BACKGROUND_COLOR)
        self.p1_or_p2.bind('<Button-1>', self.toggle_mode)
        self.p1_or_p2.grid(row=0, column=1)

        self.player1_first = Label(image=self.cross_img, bg=BACKGROUND_COLOR)
        self.player1_first.grid(row=1, column=2)

        self.player1_second = Label(image=self.circle_img, bg=BACKGROUND_COLOR)
        self.player1_second.grid(row=1, column=0)

        self.cross_or_circle = Label(image=self.on_img, bg=BACKGROUND_COLOR)
        self.cross_or_circle.bind('<Button-1>', self.toggle_symbol)
        self.cross_or_circle.grid(row=1, column=1)

    def setup_buttons(self):
        """Sets up the start/reset button."""
        self.start_button = Button(text='Start', command=self.start_game)
        self.start_button.grid(row=2, column=0, columnspan=3, sticky='EW')
        self.window.rowconfigure(2, pad=30)

    def build_tiles(self):
        """Builds the Tic Tac Toe grid."""
        self.tiles = []
        for i in range(3):
            row = []
            for j in range(3):
                button = Button(image=self.blank, relief=SOLID, command=lambda x=i, y=j: self.user_turn(x, y), state=DISABLED)
                button.grid(row=i + 3, column=j, sticky='EW')
                row.append(button)
            self.tiles.append(row)

    def toggle_mode(self, event):
        """Toggles between single-player and two-player mode."""
        self.mode = not self.mode
        self.p1_or_p2.config(image=self.off_img if not self.mode else self.on_img)

    def toggle_symbol(self, event):
        """Toggles between X and O for the first player."""
        self.first = not self.first
        self.cross_or_circle.config(image=self.off_img if not self.first else self.on_img)

    def start_game(self):
        """Starts a new game."""
        self.game.reset()
        self.game_on = True
        self.turn = 1

        self.player1_img = [self.blue_circle, self.red_cross][self.first]
        self.player2_img = [self.blue_circle, self.red_cross][not self.first]

        for row in self.tiles:
            for button in row:
                button.config(image=self.blank, state=NORMAL)

        self.start_button.config(text='Reset')
        if self.mode and not self.first:  # If single-player and computer starts
            self.pc_turn()

    def pc_turn(self):
        """Handles the computer's turn."""
        if not self.game_on:
            return

        x, y = self.game.computer_turn(self.first)
        if x != -1 and y != -1:
            self.mark_tile(x, y, self.player2_img)
            self.check_game_status(not self.first)

    def user_turn(self, x, y):
        """Handles the player's turn."""
        if not self.game_on or self.tiles[x][y]['state'] == DISABLED:
            return

        current_player = (self.turn % 2 == 1)  # Player 1 if odd turn, Player 2 if even turn
        if self.mode:  # Single-player
            if not current_player:
                return  # Player's turn only on odd turns

            self.game.available[x, y] = self.first
            self.mark_tile(x, y, self.player1_img)
            self.check_game_status(self.first)

            if self.game_on:
                self.pc_turn()
        else:  # Two-player
            symbol = self.first if current_player else not self.first
            img = self.player1_img if current_player else self.player2_img

            self.game.available[x, y] = symbol
            self.mark_tile(x, y, img)
            self.check_game_status(symbol)
            self.turn += 1

    def mark_tile(self, x, y, img):
        """Marks a tile and disables it."""
        self.tiles[x][y].config(image=img, state=DISABLED)

    def check_game_status(self, current_player):
        """Checks if the game is over and handles the result."""
        if self.game.check_result(current_player):
            # Determine the winner's symbol based on the starting player
            winning_symbol = 'X' if current_player else 'O'
            self.end_game(f"Player {winning_symbol} wins!")
        elif self.game.is_draw():
            self.end_game("It's a draw!")



    def end_game(self, message):
        """Ends the game and shows the result."""
        self.game_on = False
        messagebox.showinfo("Game Over", message)
        for row in self.tiles:
            for button in row:
                button.config(state=DISABLED)
