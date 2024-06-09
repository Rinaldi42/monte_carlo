import numpy as np
import matplotlib.pyplot as plt

class MontyHall:

  def __init__(self):
    self.stay = 0
    self.change = 0

  def rounds(self, nRounds):
    for x in range(nRounds):
      winningDoor = np.random.randint(low = 1, high = 4)
      chosenDoor = np.random.randint(low = 1, high = 4)

      if winningDoor == chosenDoor:
        self.stay += 1
      else:
        self.change += 1

montyHall = MontyHall()

nRounds = 10



montyHall.rounds(nRounds)

#plt.bar(['stay', 'change'], [montyHall.stay, montyHall.change], width = 0.4)
#plt.title("Result")
#plt.show()

print(f'percentage of wins with the trade {100 * montyHall.change/nRounds}')