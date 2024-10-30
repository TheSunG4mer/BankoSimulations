from BankoGame import readDataFromFile, plotResults
import matplotlib.pyplot as plt
from CalculateProbabilities import getRowProb, getTwoRowProb, getFullSheetProb, nIndependentSheets, cdfToPmf, pmfToCdf, plotProbabilities

def normalize(data):
    return [x / sum(data) for x in data]

dataFrame = readDataFromFile("results.txt")

#plotResults(dataFrame[30])

n = 100

simulated30 = dataFrame[n]
exact30 = nIndependentSheets(n)

sRow, sTwoRow, sFullSheet = map(normalize, simulated30)
eRow, eTwoRow, eFullSheet = map(cdfToPmf, exact30)

plotProbabilities([sRow, eRow, sTwoRow, eTwoRow, sFullSheet, eFullSheet])