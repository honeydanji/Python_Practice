import random
import math

DELTA = 0.01   
LIMIT_STUCK = 100 #상수는 뭐 안쓰더라도 이 코드있다고 상관있나.
NumEval = 0    

def createProblem(): ### 똑같은 수치문제니까. 읽어오고 변수 만들고 하는건 똑같다. #최소값 찾는 알고리즘만 달라
    ## Read in an expression and its domain from a file.
    ## Then, return a problem 'p'.
    ## 'p' is a tuple of 'expression' and 'domain'.
    ## 'expression' is a string.
    ## 'domain' is a list of 'varNames', 'low', and 'up'.
    ## 'varNames' is a list of variable names.
    ## 'low' is a list of lower bounds of the varaibles.
    ## 'up' is a list of upper bounds of the varaibles.
    fileName = "problem/" + input("Enter the filename of function:") + ".txt"
    infile = open(fileName,'r')
    expression = infile.readline() #txt파일 공식적힌 첫째줄
    varName = []
    low = []
    up = []
    line = infile.readline()        
    while line != '':
        data = line.split(',')
        varName.append(data[0])
        low.append(float(data[1]))
        up.append(float(data[2]))
        line = infile.readline() 
             
    infile.close()
    domain = [varName, low, up]
    return expression, domain # expression : 최적화에 쓰이는 함수 (정해진 공식)

def randomInit(p): ###
    domain = p[1]  # p : 해결해야할 문제
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
    varNames = p[1][0]  # p[1] is domain: [varNames, low, up]
    for i in range(len(varNames)):
        assignment = varNames[i] + '=' + str(current[i])
        exec(assignment)
    return eval(expr)

def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal
    curCopy = current[:]
    domain = p[1]        # [VarNames, low, up]
    l = domain[1][i]     # Lower bound of i-th
    u = domain[2][i]     # Upper bound of i-th
    if l <= (curCopy[i] + d) <= u:
        curCopy[i] += d
    return curCopy

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