from BankoGame import readDataFromFile, plotResults
import matplotlib.pyplot as plt

dataFrame = readDataFromFile("results.txt")

plotResults(dataFrame[30])