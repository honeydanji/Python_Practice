import random
import math
from problem import Numeric

DELTA = 0.01   # Mutation(돌연변이) step size 
NumEval = 0    # Total number of evaluations

def main():
    p = Numeric()
    # Create an instance of numerical optimization problem
    p.setVariables
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    p.storeResult(solution, minimum)
    p.describe()
    displaySetting(p)
    
def steepestAscent(p):
    current = p.randomInit # 'current' is a list of values
    valueC = p.evaluate(current)
    while True:
        neighbors = p.mutants(current)
        successor, valueS = bestOf(neighbors)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC

def bestOf(neighbors,p): ###
    best = neighbors[0]
    bestValue = p.evaluate(best)

    for neighbor in neighbors[1:]:
        neighborValue = p.evaluate(neighbor)
        if neighborValue > bestValue:
            best = neighbor
            bestValue = neighborValue

    return best, bestValue

def displaySetting(p):
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", p.getDelta())
    

def displayResult(solution, minimum):
    print()
    print("Solution found:")
    print(coordinate(solution))  # Convert list to tuple
    print("Minimum value: {0:,.3f}".format(minimum))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)  # Convert the list to a tuple

main()



