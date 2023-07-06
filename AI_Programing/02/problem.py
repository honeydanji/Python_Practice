import math
import random

## interface or 부모 클래스
# 자식 클래스가 따라야 하는 구조만 정의한다.
class Problem:
    def __init__(self): # 클래스의 객체(인스턴스)가 생성될 때 호출되는 생성자
        self._solution = [] # ' ._ ' << 외부에서 보이지 않게 하는 표현. 
        self._Value = 0
        self._numEval = 0  # 자동으로 수정된다.
        # 파이썬 : self == 자바 : this 같다.
        
    def setVariables(self): # createProblem
        pass    # 문제가 주어지면 설정한다.
    
    def randomInit(self): # 초기값
        pass    # 문제가 주어지면 설정한다. 
        
    def evaluate(self):
        pass    # 문제가 주어지면 설정한다. 
    
    def mutants(self):
        pass    # 문제가 주어지면 설정한다. 
    
    def mutate(self):
        pass    # 문제가 주어지면 설정한다.

    def randomMutant(self):
        pass    # 문제가 주어지면 설정한다. 
    
    def describe(self):
        pass    # 문제가 주어지면 설정한다. 
        
    def storeResult(self, solution, value):
        self._solution = solution # this.solution = solution 
        self._value = value
        
    def report(self):
        print()
        print("Total number of evaluations: {0:,}".format(self._numEval))    
            
class Numeric(Problem): # 소괄호에 부모클래스를 넣는다.
    def __init__(self):
        Problem.__init__(self) # 부모 클래스 생성자
        self._expression = ''
        self._domain = []
        self._delta = 0.01
        
    def getDelta(self):
        return self._delta
     
    # 문제 생성 클래스 (createProblem)
    def setVariables(self): ### 똑같은 수치문제니까. 읽어오고 변수 만들고 하는건 똑같다. #최소값 찾는 알고리즘만 달라
        fileName = "problem/" + input("Enter the filename of function:") + ".txt"
        infile = open(fileName,'r')
        self._expression = infile.readline() #txt파일 공식적힌 첫째줄
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
        self._domain = [varName, low, up] 
        # 문제가 정의 되었다.
        # return >> 클래스를 호출할 때는 필요없다?
        # 값 자체를 저장해서 사용할 수 있기 때문이다. 
        # 즉 파라미터로 받을 필요없이 바로 self로 해서 사용하면 된다.
    
    def randomInit(self): ###
        domain = self._domain[1] 
        low = domain[1]
        up = domain[2]
        init = []
        for i in range(len(low)): 
            r = random.uniform(low[i], up[i]) 
            init.append(r)
    
        return init    # Return a random initial point
                   # as a list of values
        
    def evaluate(self, current):
        self._NumEval += 1
        expr = self._expression     # p[0] is function expression
        varNames = self._domain[0]  # p[1] is domain: [varNames, low, up]
        for i in range(len(varNames)):
            assignment = varNames[i] + '=' + str(current[i])
            exec(assignment)
        return eval(expr)
        
    def mutants(self, current): ###
        neighbors = []
        for i in range(len(current)):
            mutant = self.mutate(current, i, self._delta)
            neighbors.append(mutant)
            mutant = self.mutate(current, i, -self._delta)
            neighbors.append(mutant)
        return neighbors     # Return a set of successors


    def mutate(self, current, i, d): ## Mutate i-th of 'current' if legal
        curCopy = current[:]
        domain = self._domain        # [VarNames, low, up]
        l = domain[1][i]     # Lower bound of i-th
        u = domain[2][i]     # Upper bound of i-th
        if l <= (curCopy[i] + d) <= u:
            curCopy[i] += d
        return curCopy

    def randomMutant(self, current): ### #딱 1개만 뽑아내는거. steepest ascent의 mutant는 모든 후보들 다 뽑아내는거;
        i = random.randint(0, len(current)-1) #steepest ascent 후보들 중에 하나 랜덤 뽑는다 생각해~ current가 5가 나올테니 인덱스로 적용시키기 위해 -1
        if random.uniform(0,1)>0.5: #1/2확률보다 크면
            d = self._delta
        else:
            d = -self._delta        
            return self.mutate(current, i, d) # Return a random successor  
    
    def describe(self):
        print()
        print("Objective function:")
        print(self._domain[0])   # Expression
        print("Search space:")
        varNames = self._domain[1][0] # p[1] is domain: [VarNames, low, up]
        low = self._domain[1][1] 
        up = self._domain[1][2]
        for i in range(len(low)):
            print(" " + varNames[i] + ":", (low[i], up[i]))
            
    def report(self):
        print()
        print("Solution found:")
        print(self.coordinate(self._solution))  # Convert list to tuple
        print("Minimum value: {0:,.3f}".format(self._value))
        Problem.report(self)    #return super().report()    
    
    def coordinate(self):
        c = [round(value, 3) for value in self._solution]
        return tuple(c)  # Convert the list to a tuple
        
        
        
        
        
        
        
        
class Tsp(Problem):
    def __init__(self) -> None:
        Problem.__init__(self)
        self._numCities = 0
        self._locations = []
        self._distanceTables = []
    
    def setVariables(self):
        ## Read in a TSP (# of cities, locatioins) from a file.
        ## Then, create a problem instance and return it.
        fileName = "problem/tsp" + input("Enter the filename of function:") + ".txt"
        infile = open(fileName, 'r')
        # First line is number of cities
        numCities = int(infile.readline())
        self._locations = []
        line = infile.readline()  # The rest of the lines are locations
        while line != '':
            self._locations.append(eval(line)) # Make a tuple and append
            line = infile.readline()
        infile.close()
        self._distanceTables = self.calcDistanceTable()
        
        #return self._numCities, self._locations, table
        
    
    def calcDistanceTable(self): ###
        table = []  #2d
    
        for i in range(self._numCities):
            row = [] #돌때마다 한줄이 초기화. 리스트 안에 리스트로.             
        
            for j in range(self._numCities): #tsp30.txt 이걸 표로 봐
                dx = self._locations[i][0] - self._locations[j][0]
                dy = self._locations[i][1] - self._locations[j][1]
                d = round(math.sqrt(dx**2 + dy**2),1) #제곱의 루트 math.sqrt. 소수첫째자리까지 반올림.
                row.append(d)        
            table.append(row)   
        return table # A symmetric matrix of pairwise distances

    def randomInit(self):   # Return a random initial tour
        n = self._numCities
        #n = self.setVariables[0]
        
        init = list(range(n))
        random.shuffle(init)
        return init

    def evaluate(self, current): ###
    ## Calculate the tour cost of 'current'
    ## 'current' is a list of city ids
        self._numEval += 1 
        n = self._numCities #도시수
        table = self._distanceTables
        cost = 0
       
        for i in range(n-1):
            locFrom = current[i] #현재, 랜덤으로 섞인 table들의 거리 계산을 위해 좌표
            locTo = current[i+1] 
            cost += table[locFrom][locTo] #2d테이블 거리들 다 더해
        cost += table[current[n-1]][current[0]]    
        return cost
    
    def mutants(self, current): # Apply inversion
        n = self._numCities
        neighbors = []
        count = 0
        triedPairs = []
        while count <= n:  # Pick two random loci for inversion
            i, j = sorted([random.randrange(n) for _ in range(2)])
            if i < j and [i, j] not in triedPairs:
                triedPairs.append([i, j])
                curCopy = self.inversion(current, i, j)
                count += 1
                neighbors.append(curCopy)
        return neighbors
    
    def inversion(self, current, i, j):  # Perform inversion
        curCopy = current[:]
        while i < j:
            curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
            i += 1
            j -= 1
        return curCopy
    
    def randomMutant(self, current): # Apply inversion
        while True:
            i, j = sorted([random.randrange(self._numCities[0])
                           for _ in range(2)])
            if i < j:
                curCopy = self.inversion(current, i, j)
                break
        return curCopy
    
    def describeProblem(self):
        print()
        n = self._numCities
        print("Number of cities:", n)
        print("City locations:")
        self._locations = self._numCities
        for i in range(n):
            print("{0:>12}".format(str(self._locations[i])), end = '')
            if i % 5 == 4:
                print()   
        
    def report(self):
        print()
        print("Best order of visits:")
        self.tenPerRow()       # Print 10 cities per row
        print("Minimum tour cost: {0:,}".format(round(self._value)))
        Problem.report(self)
       
    def tenPerRow(self):
        for i in range(len(self._solution)):
            print("{0:>5}".format(self._solution[i]), end='')
            if i % 10 == 9:
                print()

        
# 문제가 주어지면 적절한 알고리즘을 이용하는 게 핵심이다. (TSP, Numeric)
# 공통 요소 : solutuon, value, numEval
# 차이점
# Numeric : expression(함수), domain(범위), delta
# TSP : numCities(도시수), location(위치), distanceTables(거리)