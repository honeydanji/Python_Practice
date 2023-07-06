import random
import math

LIMIT_STUCK = 100 # Max number of evaluations enduring no improvement
NumEval = 0    # Total number of evaluations


def createProblem():
    ## Read in a TSP (# of cities, locatioins) from a file.
    ## Then, create a problem instance and return it.
    fileName = "problem/tsp" + input("Enter the filename of function:") + ".txt"
    infile = open(fileName, 'r')
    # First line is number of cities
    numCities = int(infile.readline())
    locations = []
    line = infile.readline()  # The rest of the lines are locations
    while line != '':
        locations.append(eval(line)) # Make a tuple and append
        line = infile.readline()
    infile.close()
    table = calcDistanceTable(numCities, locations)
    return numCities, locations, table


def calcDistanceTable(numCities, locations): ###
    table = []  #2d
    
    for i in range(numCities):
        row = [] #돌때마다 한줄이 초기화. 리스트 안에 리스트로.             
        
        for j in range(numCities): #tsp30.txt 이걸 표로 봐
            dx = locations[i][0] - locations[j][0]
            dy = locations[i][1] - locations[j][1]
            d = round(math.sqrt(dx**2 + dy**2),1) #제곱의 루트 math.sqrt. 소수첫째자리까지 반올림.
            row.append(d)        
        table.append(row)   
    
    return table # A symmetric matrix of pairwise distances

def randomInit(p):   # Return a random initial tour
    n = p[0]
    init = list(range(n))
    random.shuffle(init)
    return init


def evaluate(current, p): ###
    ## Calculate the tour cost of 'current'
    ## 'p' is a Problem instance
    ## 'current' is a list of city ids
    global NumEval
    NumEval += 1 
    
    n = p[0] #도시수
    table = p[2] #아까 distance 계산한거 2번째에 넣었잖아
    cost = 0
       
    for i in range(n-1):
        locFrom = current[i] #현재, 랜덤으로 섞인 table들의 거리 계산을 위해 좌표
        locTo = current[i+1] 
        cost += table[locFrom][locTo] #2d테이블 거리들 다 더해
    cost += table[current[n-1]][current[0]]    
    return cost

def inversion(current, i, j):  # Perform inversion
    curCopy = current[:]
    while i < j:
        curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
        i += 1
        j -= 1
    return curCopy

def describeProblem(p):
    print()
    n = p[0]
    print("Number of cities:", n)
    print("City locations:")
    locations = p[1]
    for i in range(n):
        print("{0:>12}".format(str(locations[i])), end = '')
        if i % 5 == 4:
            print()
            
def displayResult(solution, minimum):
    print()
    print("Best order of visits:")
    tenPerRow(solution)       # Print 10 cities per row
    print("Minimum tour cost: {0:,}".format(round(minimum)))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def tenPerRow(solution):
    for i in range(len(solution)):
        print("{0:>5}".format(solution[i]), end='')
        if i % 10 == 9:
            print()