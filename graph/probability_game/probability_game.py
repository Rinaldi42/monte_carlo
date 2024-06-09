import numpy as np
import matplotlib.pyplot as plt

#   0, 1, 2, 3, 4, 5, 6, 7, 8, 9,  
graph = [
    0, 1, 1, 1, 1, 0, 0, 0, 0, 0, # 0
    0, 0, 0, 0, 0, 0, 0, 0, 1, 0, # 1
    0, 0, 0, 0, 0, 0, 0, 1, 0, 1, # 2
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, # 3
    0, 0, 0, 0, 0, 1, 1, 0, 0, 0, # 4
    0, 0, 0, 0, 0, 0, 0, 0, 1, 0, # 5
    0, 0, 0, 0, 0, 0, 0, 0, 1, 1, # 6 
    0, 0, 0, 0, 0, 0, 0, 0, 1, 1, # 7
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, # 8
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, # 9

]

matriz = np.array(graph).reshape(10, 10)

class Game:

  def __init__(self, board, heaven, hell):
    self.heaven = heaven
    self.nHeaven = 0
    self.hell = hell
    self.nHell = 0
    self.board = board
    self.pathList = [
        [sum(1 for value in row if value > 0), [col for col, value in enumerate(row) if value > 0]]
        for row in board]
    self.position = 0

  def dice(self, possibilities):
    return np.random.randint(low = 0, high = possibilities)

  def play(self):
    self.position = 0
    while self.position != self.heaven and self.hell:
      nextPosition = self.pathList[self.position][1][self.dice(self.pathList[self.position][0])]
      self.position = nextPosition
      if self.position == self.heaven:
        self.nHeaven += 1
        break
      elif self.position == self.hell:
        self.nHell += 1
        break

  def rounds(self, nRounds):
    for n in range(nRounds):
     self.play()

game = Game(board = matriz, heaven = 8, hell = 9)

nRounds = 40

game.rounds(nRounds)

#plt.bar(['heaven', 'hell'], [game.nHell, game.nHeaven], width = 0.4)
#plt.title("Result")
#plt.show()

print(f'HELL{100 * game.nHell/nRounds}, HEAVEN {100 * game.nHeaven/nRounds}')