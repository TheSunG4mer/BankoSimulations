import numpy as np
from ConstructBankoSheet import getRandomSheet
import matplotlib.pyplot as plt

def mod_rest(x, m):
    return x // m, x % m

def incodeNumberInArray(x):
    A = np.zeros(3, dtype=np.int32)
    d, r = divmod(x - 1, 30)
    A[d] += 1 << r
    return A

def incodeSheetIntoMatrix(L):
    A = np.zeros((3, 3), dtype=np.int32)
    for i, l in enumerate(L):
        for x in l:
            d, r = divmod(x - 1, 30)
            A[i, d] += 1 << r
    return A


class BankoGame:
    def __init__(self, number_of_sheets):
        self.number_of_sheets = number_of_sheets
    

    def startNewGame(self):
        list_of_sheets = [getRandomSheet() for _ in range(self.number_of_sheets)]
        self.arrayOfSheets = np.array(list_of_sheets)
        self.number_of_announced_numbers = 0

    def announceNumber(self, number):
        self.number_of_announced_numbers += 1
        self.arrayOfSheets = self.arrayOfSheets & np.bitwise_not(incodeNumberInArray(number))
    
    def getMaximalNumberOfFinnishedRows(self):
        return np.max(np.sum(np.all(self.arrayOfSheets == 0, axis=2), axis=1))

    def runGame(self):
        numbers_to_be_announced = np.random.permutation(np.arange(1, 91))
        self.startNewGame()
        largest_number_of_finnished_rows = 0
        row_finnishing_numbers = []
        for x in numbers_to_be_announced:
            self.announceNumber(x)
            if self.getMaximalNumberOfFinnishedRows() > largest_number_of_finnished_rows:
                largest_number_of_finnished_rows += 1
                row_finnishing_numbers.append(self.number_of_announced_numbers)
                if largest_number_of_finnished_rows == 3:
                    break
        return row_finnishing_numbers
    
    def runTurnament(self, number_of_games):
        results = [[0 for _ in range(90)] for _ in range(3)]
        for game_number in range(number_of_games):
            if game_number % (max(number_of_games // 20, 1)) == 0:
                print(f"Game number: {game_number}")
            
            row_finnishing_numbers = self.runGame()
            for i in range(3):
                results[i][row_finnishing_numbers[i] - 1] += 1
        return results

def plotResults(results):
    for row in results:
        plt.plot(range(1, 91), row)
    plt.show()
    cummulative_results = []
    for row in results:
        cummulative_results.append([sum(row[:i+1]) for i in range(90)])
    for row in cummulative_results:
        plt.plot(range(1, 91), row)
    plt.show()


if __name__ == "__main__":
    # game = BankoGame(10)
    # print(game.runGame())
    # game = BankoGame(100)
    # print(game.runGame())
    # game = BankoGame(1000)
    # print(game.runGame())
    game = BankoGame(1)
    results = game.runTurnament(100000)
    plotResults(results)
