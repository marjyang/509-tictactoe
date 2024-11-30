from random import randint

class Board:
  def __init__(self):
    self.__rows = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

  def __str__(self):
    s = '-------\n'
    for row in self.__rows:
      for cell in row:
        s = s + '|'
        if cell == None:
          s=s+' '
        else:
          s=s+cell
      s = s + '|\n-------\n'
    return s

  # access and update cells
  def get(self, x, y):
    return self.__rows[x][y]

  def set(self, x, y, value):
    self.__rows[x][y] = value

  # check if input is in the appropriate range & cell is empty
  def is_valid(self, x, y):
    return 0 <= x < 3 and 0 <= y < 3 and self.__rows[x][y] is None

  # check validity and place the x/o on board
  def make_move(self, x, y, symbol):
      if self.is_valid(x, y):
          self.__rows[x][y] = symbol
          return True
      return False

  # check winner - horizontals/verticals & diagonals
  def check_winner(self):
    for i in range(3):
      if self.__rows[i][0] == self.__rows[i][1] == self.__rows[i][2] and self.__rows[i][0] is not None:
        return self.__rows[i][0]
      if self.__rows[0][i] == self.__rows[1][i] == self.__rows[2][i] and self.__rows[0][i] is not None:
        return self.__rows[0][i]
    if self.__rows[0][0] == self.__rows[1][1] == self.__rows[2][2] and self.__rows[0][0] is not None:
      return self.__rows[0][0]
    if self.__rows[0][2] == self.__rows[1][1] == self.__rows[2][0] and self.__rows[0][2] is not None:
      return self.__rows[0][2]
    return None

  # check if all cells are full
  def full_board(self):
    for row in self.__rows:  
        for cell in row:
            if cell is None:
                return False
    return True 

class Game:
  def __init__(self, playerX, playerO):
    self._board = Board()
    self._playerX = playerX
    self._playerO = playerO
    self._current_player = "X"

  def run(self):
    while True:
      # display board
      print(self._board)

      # get move from player (human)
      if self._current_player == "X":
          x, y = self._playerX.get_move(self._board)
      # get move from player (bot)
      else:
          x, y = self._playerO.get_move(self._board)

      # if invalid move, exit loop 
      if not self._board.make_move(x, y, self._current_player):
          return

      # check if winning sequence is played
      winner = self._board.check_winner()
      if winner:
          print(self._board)
          print(f"{winner} wins!")
          break

      # check if board is full - draw
      elif self._board.full_board():
          print(self._board)
          print("draw!")
          break
      
      # rotate players
      self._current_player = "O" if self._current_player == "X" else "X"

class Human:
  # prompt user to enter coordinates
  # validate user input
  # check for errors
  def get_move(self, board):
    while True:
      try:
        move = input("please enter your move as x,y coordinates:")
        x,y = map(int, move.split(","))
        if board.is_valid(x,y):
          return x,y
        else:
          print("invalid move. rows and columns must be 0-2 and in an empty space. try again")
      except (ValueError, IndexError):
        print("invalid input. enter as 'x,y' like '0,1'. try again.")

class Bot:
  # use randint to have bot player choose random coordinates
  def get_move(self, board):
    while True:
      x = randint(0,2)
      y = randint(0,2)
      if board.is_valid(x,y):
        return x,y


game = Game(Human(), Bot())
game.run()