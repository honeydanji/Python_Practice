from numeric01 import * #이렇게 하면 한방에 다 들여오니 numeric.createProblem() 이런식으로 다 안바꿔도된다.

def main():
    # Create an instance of numerical optimization problem
    p = createProblem()   # 'p': (expr, domain)
    # Call the search algorithm
    solution, minimum = firstChoice(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)

def firstChoice(p):
    current = randomInit(p)   # 'current' is a list of values
    valueC = evaluate(current, p)
    i = 0
    while i < LIMIT_STUCK: #랜덤하게 일단 1개 썩세스 선택 하고, 좋아지기만 하면 업데이트
        successor = randomMutant(current, p)
        valueS = evaluate(successor, p)
        if valueS < valueC: #얘는 주변에 1개 선택. 좋아지면. 즉 작아지면 좋아지는 방향. 그럼 업데이트
            current = successor
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    return current, valueC

def randomMutant(current, p): ### #딱 1개만 뽑아내는거. steepest ascent의 mutant는 모든 후보들 다 뽑아내는거;
    i = random.randint(0, len(current)-1) #steepest ascent 후보들 중에 하나 랜덤 뽑는다 생각해~ current가 5가 나올테니 인덱스로 적용시키기 위해 -1
    if random.uniform(0,1)>0.5: #1/2확률보다 크면
        d = DELTA
    else:
        d = -DELTA    
#    d = random.uniform(-DELTA, DELTA) #이건 내가 한겅    
    return mutate(current, i, d, p) # Return a random successor


def displaySetting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print()
    print("Mutation step size:", DELTA)
main()