import time
import random
import string
from spellchecker import SpellChecker

class Player():
    """
    Player class
    """
    def __init__(self, name): 
        self.name = name

    def best_players():
        pass

class BreakException(Exception):
    pass

class Board():
    """
    Board class
    """
    def __init__(self, height, width, bombs, timeout):
        self.height = height
        self.width = width
        self.bombs = bombs
        self.timeout = timeout
                                                                                           
    def create_board(self):
        """
        Create board draft
        """
        board_draft = [(x, y) for y in range(self.height) for x in range(self.width)]

        """
        Generate bombs
        """
        bombs_index = []
        while len(bombs_index) < self.bombs:
            bomb = random.randint(0, (len(board_draft) - 1))
            if bomb not in bombs_index:
                bombs_index.append(bomb) 

        """
        Fill draft board with bombs and with bombs values
        """
        self.board = board_draft.copy()
        for item in bombs_index: # fill board with bombs
            self.board[item] = "X"

        xs = [p[0] for p in board_draft] # extract x from board_draft
        ys = [p[1] for p in board_draft] # extract y from board_draft

        """
        0  1 1 1 1 1 1 1  2

        7  8 8 8 8 8 8 8  3
        7  8 8 8 8 8 8 8  3
        7  8 8 8 8 8 8 8  3
        7  8 8 8 8 8 8 8  3
        7  8 8 8 8 8 8 8  3
        7  8 8 8 8 8 8 8  3
        7  8 8 8 8 8 8 8  3

        6  5 5 5 5 5 5 5  4
        """

        for index in range(0, (self.height*self.width)): # fill board with bombs values
            count_bombs = 0
            if xs[index] == 0 and ys[index] == 0 and "X" not in self.board[index]: # cell(0, 0), correct indexes to prevent from going outside the range E.g(index = 0, xs[index] - 1 = Error: Out of range)
                if self.board[index+1] == "X": # check cell for a bomb
                    count_bombs += 1 # count bombs
                if self.board[index+self.width] == "X":
                    count_bombs += 1
                if self.board[index+(self.width+1)] == "X":
                    count_bombs += 1
                self.board[index] = count_bombs # add cell with bombs value to board
           
            elif ys[index] == 0 and index > 0 and index < (self.width-1) and "X" not in self.board[index]: # cells((0<x<width-1), 0)
                if self.board[index-1] == "X":
                    count_bombs += 1
                if self.board[index+1] == "X":
                    count_bombs += 1
                if self.board[index+self.width] == "X":
                    count_bombs += 1
                if self.board[index+self.width-1] == "X":
                    count_bombs += 1
                if self.board[index+self.width+1] == "X":
                    count_bombs += 1
                self.board[index] = count_bombs
              
            elif xs[index] == (self.width - 1) and ys[index] == 0 and "X" not in self.board[index]: # cell((width-1), 0)
                if self.board[index-1] == "X":
                    count_bombs += 1
                if self.board[index + self.width] == "X":
                    count_bombs += 1
                if self.board[index + self.width - 1] == "X":
                    count_bombs += 1
                self.board[index] = count_bombs

            elif xs[index] == (self.width - 1) and index > (self.width + self.width - 2) and index < ((self.height*self.width) - self.width + 1) and "X" not in self.board[index]: # cells((width-1), (0<y<height-1))
                if self.board[index-1] == "X":
                    count_bombs += 1
                if self.board[index+self.width] == "X":
                    count_bombs += 1
                if self.board[index+self.width-1] == "X":
                    count_bombs += 1
                if self.board[index-self.width] == "X":
                    count_bombs += 1
                if self.board[index-self.width-1] == "X":
                    count_bombs += 1
                self.board[index] = count_bombs

            elif index == ((self.height*self.width)-1) and "X" not in self.board[index]: # cell((width-1), (height-1))
                if self.board[index-1] == "X":
                    count_bombs += 1
                if self.board[index-self.width] == "X":
                    count_bombs += 1
                if self.board[index-self.width-1] == "X":
                    count_bombs += 1
                self.board[index] = count_bombs

            elif ys[index] == (self.height-1) and index > ((self.height*self.width) - self.width) and index < ((self.height*self.width) - 1) and "X" not in self.board[index]: # cells((0<x<width-1), (height-1))
                if self.board[index-1] == "X":
                    count_bombs += 1
                if self.board[index-self.width-1] == "X":
                    count_bombs += 1
                if self.board[index-self.width] == "X":
                    count_bombs += 1
                if self.board[index-self.width+1] == "X":
                    count_bombs += 1
                if self.board[index+1] == "X":
                    count_bombs += 1
                self.board[index] = count_bombs

            elif xs[index] == 0 and ys[index] == (self.height-1) and "X" not in self.board[index]: # cell(0, (height-1))
                if self.board[index+1] == "X":
                    count_bombs += 1
                if self.board[index-self.width] == "X":
                    count_bombs += 1
                if self.board[index-(self.width-1)] == "X":
                    count_bombs += 1
                self.board[index] = count_bombs

            elif xs[index] == 0 and index > (self.width-1) and index < ((self.height*self.width) - self.width - 1) and "X" not in self.board[index]: # cells(0, 0<y<(height-1))
                if self.board[index+1] == "X":
                    count_bombs += 1
                if self.board[index+self.width] == "X":
                    count_bombs += 1
                if self.board[index+(self.width+1)] == "X":
                    count_bombs += 1
                if self.board[index-self.width] == "X":
                    count_bombs += 1
                if self.board[index-(self.width-1)] == "X":
                    count_bombs += 1
                self.board[index] = count_bombs

            elif xs[index] > 0 and xs[index] < (self.width-1) and ys[index] > 0 and ys[index] < (self.height-1) and "X" not in self.board[index]: # cells that can have maximum amount of bombs
                if self.board[index+1] == "X":
                    count_bombs += 1
                if self.board[index-1] == "X":
                    count_bombs += 1
                if self.board[index+self.width] == "X":
                    count_bombs += 1
                if self.board[index+self.width-1] == "X":
                    count_bombs += 1
                if self.board[index+self.width+1] == "X":
                    count_bombs += 1
                if self.board[index-self.width] == "X":
                    count_bombs += 1
                if self.board[index-self.width-1] == "X":
                    count_bombs += 1
                if self.board[index-self.width+1] == "X":
                    count_bombs += 1
                self.board[index] = count_bombs
        
        self.display_board = [] # board which player sees
        for item in self.board:
            self.display_board.append("-") 

    def play_game(self):
        if game_mode == "noguess" or game_mode == "timerush": # display on the board random safe cell
            while True:
                p = random.choice(range(0, ((self.height*self.width)-1)))
                if self.board[p] == 0:
                    self.display_board[p] = "S"
                    x1 = p % self.width
                    y1 = (p-x1)/self.width
                    y1 = int(y1)
                    break
                else:
                    continue
       
        for index, item in enumerate(self.display_board, start=1): # print board
            print("", item, end=" |" if index % self.width else "\n")
        game_over = False 
        start_time = time.time()
        move = 0 # count player moves
        print()
        while (time.time() < start_time + self.timeout):
            while True:
                user_cell = input("Enter cell position:").split() # user cell position
                if len(user_cell) == 2:
                    try:
                        separate_input = list(map(int, user_cell))
                        x = separate_input[0]
                        y = separate_input[1]
                        idx = x + (y*(self.width)) # convert user x and y input to index in board[]
                    except ValueError:
                        print("Oops, that was no valid format. Try X Y.")
                    else:
                        if x > self.width-1 or y > self.height-1 or x < 0 or y < 0:
                            print("Out of range! Try again..")

                        elif move == 0 and (game_mode == "noguess" or game_mode == "timerush"):  
                            if self.display_board[idx] == "S":
                                move += 1
                                break
                            else:
                                print(f"You have to enter S position({x1}, {y1}) to start the game!")

                        else:
                            move += 1
                            break

                elif len(user_cell) == 3:
                    if move == 0:
                        print("You cant flag on first move!")

                    elif user_cell[2].lower() != "f":
                        print("Wrong format! If you want to flag a cell try X Y F")
                        continue

                    elif user_cell[2].lower() == "f":
                        try:
                            separate_input = list(map(int, user_cell[:2]))
                            x = separate_input[0]
                            y = separate_input[1]
                            idx = x + (y*(self.width)) # convert user x and y input to index in board[]
                        except ValueError:
                            print("Oops, that was no valid format. Try X Y.")
                        else:
                            if x > self.width-1 or y > self.height-1 or x < 0 or y < 0:
                                print("Out of range! Try again..")

                            else:
                                move += 1
                                break
                else:
                    print("Wrong format! Try X Y to dig or X Y F to flag")  
                        
            if move == 1:
                start_time = time.time()

            print(move)

            if len(user_cell) == 3:
                if self.display_board[idx] == "F":
                    self.display_board[idx] = "-"
           
                elif self.display_board[idx] == "-":
                    self.display_board[idx] = "F"

                else:
                    print("You cant flag opened cell!")

            elif len(user_cell) == 2:
                if self.display_board[idx] == "F":
                    print(f"To unflag this cell type {x} {y} F")

                elif self.display_board[idx] != "-" and self.display_board[idx] != "S":
                    print("You already opened this cell!\n")

                elif self.board[idx] == "X":
                    self.display_board = self.board.copy()
                    game_over = True
                    if game_mode == "timerush":
                        raise BreakException()
                    break

                elif self.board[idx] > 0 and self.board[idx] < 9:
                    self.display_board[idx] = self.board[idx]

                elif self.board[idx] == 0:
                    self.display_board[idx] = self.board[idx]
                    for i in range(0, (self.width*self.height)):
                        for j in range(0, (self.width*self.height)):
                            if self.display_board[j] == 0:
                                if  j == 0:
                                    self.display_board[j+1] = self.board[j+1]
                                    self.display_board[j+self.width] = self.board[j+self.width]
                                    self.display_board[j+self.width+1] = self.board[j+self.width+1]

                                if j > 0 and j < self.width-1:
                                    self.display_board[j-1] = self.board[j-1]
                                    self.display_board[j+1] = self.board[j+1]
                                    self.display_board[j+self.width] = self.board[j+self.width]
                                    self.display_board[j+self.width-1] = self.board[j+self.width-1]
                                    self.display_board[j+self.width+1] = self.board[j+self.width+1]

                                if j == (self.width-1):
                                    self.display_board[j-1] = self.board[j-1]
                                    self.display_board[j+self.width] = self.board[j+self.width]
                                    self.display_board[j+self.width-1] = self.board[j+self.width-1]

                                if j % self.width == (self.width-1) and j > self.width-1 and j < ((self.height*self.width)-self.width): 
                                    self.display_board[j-1] = self.board[j-1]
                                    self.display_board[j-self.width] = self.board[j-self.width]
                                    self.display_board[j-self.width-1] = self.board[j-self.width-1]
                                    self.display_board[j+self.width] = self.board[j+self.width]
                                    self.display_board[j+self.width-1] = self.board[j+self.width-1]

                                if j == ((self.height*self.width)-1):
                                    self.display_board[j-1] = self.board[j-1]
                                    self.display_board[j-self.width] = self.board[j-self.width]
                                    self.display_board[j-self.width-1] = self.board[j-self.width-1]

                                if j > ((self.height*self.width)-self.width) and j < ((self.height*self.width)-1):
                                    self.display_board[j-1] = self.board[j-1]
                                    self.display_board[j+1] = self.board[j+1]
                                    self.display_board[j-self.width] = self.board[j-self.width]
                                    self.display_board[j-self.width-1] = self.board[j-self.width-1]
                                    self.display_board[j-self.width+1] = self.board[j-self.width+1]

                                if j == ((self.height*self.width)-self.width):
                                    self.display_board[j+1] = self.board[j+1]
                                    self.display_board[j-self.width] = self.board[j-self.width]
                                    self.display_board[j-self.width+1] = self.board[j-self.width+1]

                                if j % self.width == 0 and j > 0 and j < ((self.height*self.width)-self.width):
                                    self.display_board[j+1] = self.board[j+1]
                                    self.display_board[j-self.width] = self.board[j-self.width]
                                    self.display_board[j-self.width+1] = self.board[j-self.width+1]
                                    self.display_board[j+self.width] = self.board[j+self.width]
                                    self.display_board[j+self.width+1] = self.board[j+self.width+1]

                                if j > self.width-1 and j % self.width != 0 and j % self.width != (self.width-1) and j < ((self.height*self.width)-self.width):
                                    self.display_board[j+1] = self.board[j+1]
                                    self.display_board[j-1] = self.board[j-1]
                                    self.display_board[j+self.width] = self.board[j+self.width]
                                    self.display_board[j+self.width-1] = self.board[j+self.width-1]
                                    self.display_board[j+self.width+1] = self.board[j+self.width+1]
                                    self.display_board[j-self.width] = self.board[j-self.width]
                                    self.display_board[j-self.width-1] = self.board[j-self.width-1]
                                    self.display_board[j-self.width+1] = self.board[j-self.width+1]

            for index, item in enumerate(self.display_board, start=1):
                print("", item, end=" |" if index % self.width else "\n")
            print()
            if (self.display_board.count("-") + self.display_board.count("F")) == self.bombs and game_over == False and game_mode != "timerush": # if sum of flags and not opened cells equals to number of bombs than player wins
                end_time = time.time()
                elapsed_time = (end_time - start_time)
                print("Congrats! Youw complete the board in", format(elapsed_time,".3f"), "seconds")
                break
            
            elif (self.display_board.count("-") + self.display_board.count("F")) == self.bombs and game_over == False and game_mode == "timerush":
                print("Wowk?!")
                break

        else:
            print("Out of time!")
            game_over = True
            if game_mode == "timerush":
                raise BreakException()
            
        if game_over == True and game_mode != "timerush":
            for index, item in enumerate(self.board, start=1):
                print("", item, end=" |" if index % self.width else "\n")
            end_time = time.time()
            elapsed_time = (end_time - start_time)
            print("You lost! Elapsed time", format(elapsed_time,".3f"), "seconds.")
            action = ""
            while action not in ["m", "q"]:
                action = input("Enter (m) for main menu, (r) to restart or (q) to quit: ").lower()
                if action == "m":
                    main_menu()
                    break
                
                elif action == "q":
                    print("Ending..")
                    break

                elif action == "r":
                    game()
                    break

                else:
                    print("try again..")

        elif game_over == False and game_mode != "timerush":
            action = ""
            while action not in ["m", "q"]:
                action = input("Enter (m) for main menu, (r) to restart or (q) to quit: ").lower()
                if action == "m":
                    main_menu()
                    break

                elif action == "r":
                    game()
                    break
                
                elif action == "q":
                    print("Ending..")
                    break

                else:
                    print("try again..")


def main_menu():
    """
    Minesweeper main menu
    """

    spell = SpellChecker(language=None, case_sensitive=None)
    spell.word_frequency.load_dictionary("/home/bestseller/Dokumenty/python/my_words.json")

    while True:
        answer = ""
        global game_mode
        game_mode = input("Select game mode standart, noguess, timerush or custom: ").lower()
        if game_mode in spell:
            game()
            break
        else:
            corr = spell.correction(game_mode)
            if corr not in spell:
                print("Select game mode again..\n")
                continue

            if corr in spell:
                while answer not in ["yes", "no", "y","n"]:
                    answer = input(f"Do you mean {corr}? (Y/N): ").lower()
                    if answer == "y":
                        game_mode = corr
                        game()
                        break

                    elif answer == "n":
                        continue
                        
                    else:
                        print("Please, enter (Y/N)")
    
def game():
    easy = Board(9, 9, 10, 1200)
    medium = Board(16, 16, 40, 1200)
    advance = Board(16, 30, 100, 1200)

    if game_mode == "standart":
        print("\nIn STANDART mode, a starting position is not provided, and you can hit bomb on first move.\n")
        while True:
            difficulty = input("Select game dificulty E (easy), M (medium) , A (advance) or B (back): ").lower()
            if difficulty == "e" or difficulty == "m" or difficulty == "a" or difficulty == "b":
                break
            else:
                print("Wrong input, try again..\n")
        print()
        if difficulty == "e":
            easy.create_board()
            easy.play_game()

        elif difficulty == "m":
            medium.create_board()
            medium.play_game()

        elif difficulty == "a":
            advance.create_board()
            advance.play_game()

        elif difficulty == "b":
            main_menu()

    elif game_mode == "noguess":
        print("\nIn NOGUESS mode, a starting position is provided, and you never need to guess to complete the board.\n")
        while True:
            difficulty = input("Select game dificulty E (easy), M (medium) , A (advance) or B (back): ").lower()
            if difficulty == "e" or difficulty == "m" or difficulty == "a" or difficulty == "b":
                break
            else:
                print("Wrong input, try again..\n")
        print()

        if difficulty == "e":
            easy.create_board()
            easy.play_game()
        
        elif difficulty == "m":
            medium.create_board()
            medium.play_game()

        elif difficulty == "a":
            advance.create_board()
            advance.play_game()
        
        elif difficulty == "b":
            main_menu()

    elif game_mode == "timerush":
        print("In TIMERUSH mode you race against the clock, after each round time to complete the board is decreased dramatically.\nFirst round lasts 9min, 5 rounds must be completed to win.")
        rnd = 0
        try:
            while True:
                t = 540
                if rnd < 5:
                    if rnd != 0:
                        t = t - (60*(rnd))
                    print("Creating new board, please wait..")
                    for i in range(3):
                        print(i)
                        time.sleep(1)
                    timerush = Board(9, 9, 3, t)
                    timerush.create_board()
                    timerush.play_game()
                    rnd += 1
                else:
                    break
        except BreakException:
            pass

        if rnd == 5:
            print("Whaat a beast, you won timerush mode!")

        else:
            print("You lost!")

    elif game_mode == "custom":

        while True:
            try:
                h, w, b = [int(h) for h in input("Enter height, width and bombs in one line: ").split()]
            except ValueError:
                print("Oops, that was no valid format. Try width height bombs (9 9 10)")
            else:
                if h * w <= b:
                    print("You cant have more bombs than cells!")
                
                elif b < 0:
                    print("You need at least one bomb on board..")
                
                elif h > 30 or w > 30:
                    print("Max height and width 30x30!")

                elif h < 2 and w < 2:
                    print("Min height and width 2x2!")
                
                else:
                    break

        custom = Board(h, w, b, 1200)
        custom.create_board()
        custom.play_game()


if __name__ == '__main__':
    main_menu()