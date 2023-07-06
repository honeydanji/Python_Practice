import random
import math
import sys
sys.path.append('../02')  # Adds the 02 directory to the Python path

DELTA = 0.01   # Mutation(돌연변이) step size 
NumEval = 0    # Total number of evaluations


def main():
    # Create an instance of numerical optimization problem
    p = Numeric()
    p = createProblem()   # 'p': (expr, domain)
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)


def createProblem(): ### 파일에서 식과 도메인을 읽어와 문제를 표현하는 튜플을 반환한다.
    ## Read in an expression and its domain from a file.
    ## Then, return a problem 'p'.
    ## 'p' is a tuple of 'expression' and 'domain'.
    ## 'expression' is a string.
    ## 'domain' is a list of 'varNames', 'low', and 'up'.   
    ## 'varNames' is a list of variable names.
    ## 'low' is a list of lower bounds of the varaibles.
    ## 'up' is a list of upper bounds of the varaibles.
    fileName = input("Enter the filename of a function")
    infile = open(fileName, 'r') # 파일 열고, 읽기 모드
    expression = infile.readline() # 첫번째 줄 읽기
  
    varName = []
    low = []
    up = []
    
    line = infile.readline() # 한 줄 읽기
    while line !="":
        data = line.split(",")
        varName.append(data[0])
        low.append(float(data[1]))
        up.append(float(data[2]))
        line = infile.readline().strip()    
    infile.close() # 다 읽었으면 파일을 닫아준다.
    domain = [varName, low, up]    
    
    return expression, domain


def steepestAscent(p):
    current = randomInit(p) # 'current' is a list of values
    valueC = evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        successor, valueS = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC

def randomInit(p): ### 초기점 생성 함수
    domain = p[1]
    low = domain[1]
    up = domain[2]
    init = []
    
    for i in range(len(low)):
        r = random.uniform(low[i], up[i])
        init.append(r)
        
    return init    # Return a random initial point
                   # as a list of values

def evaluate(current, p):
    ## Evaluate the expression of 'p' after assigning
    ## the values of 'current' to the variables
    global NumEval
    
    NumEval += 1
    expr = p[0]         # p[0] is function expression
    varNames = p[1][0]  # p[1] is domain
    for i in range(len(varNames)):
        assignment = varNames[i] + '=' + str(current[i])
        exec(assignment)
    return eval(expr)


def mutants(current, p): ###
    neighbors = []
    for i in range(len(current)):
        mutant = mutate(current, i, DELTA, p)
        neighbors.append(mutant)
        mutant = mutate(current, i, -DELTA, p)
        neighbors.append(mutant)
        
    return neighbors     # Return a set of successors


def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal
    curCopy = current[:]
    domain = p[1]        # [VarNames, low, up]
    l = domain[1][i]     # Lower bound of i-th
    u = domain[2][i]     # Upper bound of i-th
    if l <= (curCopy[i] + d) <= u:
        curCopy[i] += d
    return curCopy

def bestOf(neighbors, p): ###
    best = neighbors[0]
    bestValue = evaluate(best, p)

    for neighbor in neighbors[1:]:
        neighborValue = evaluate(neighbor, p)
        if neighborValue > bestValue:
            best = neighbor
            bestValue = neighborValue

    return best, bestValue

def describeProblem(p):
    print()
    print("Objective function:")
    print(p[0])   # Expression
    print("Search space:")
    varNames = p[1][0] # p[1] is domain: [VarNames, low, up]
    low = p[1][1]
    up = p[1][2]
    for i in range(len(low)):
        print(" " + varNames[i] + ":", (low[i], up[i])) 

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

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



