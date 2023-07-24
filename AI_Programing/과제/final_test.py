import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

def measure(func):
    """
        decorator function
        logging을 이용해 x값, y값, 계산값 을 출력할 수 있는 기능을 추가
    """
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        logging.info(f"?????? = {self.data[args[0]][1]}, y = {self.data[args[0]][2]}: {result}")
        return result
    return wrapper


class Evaluator:
    def __init__(self, filename):
        """
            filename에 주어진 경로에서 읽기 전용으로 csv 파일을 읽어서
            각 줄에 있는 수식과 변수 값을 저장

            csv 파일은 수식,x값,y값 으로 구성되어 있음
            ex) equations.txt
            10*x + 2*y,2,5
            0.5*x - 1.8*y,7,3
        """
        with open(filename, 'r') as file:
            lines = file.readlines()
            self.data = [line.strip().split(',') for line in lines]
    @measure
    def solve(self, idx):
        """
            idx 번째 수식을 계산한 값을 반환

            ex)
            solve(1) 은 equations.txt 의 0.5*x - 1.8*y가
            x=7, y=3일 때 값을 계산하여 반환

            solve 내부에는 logging이나 print 사용하지 말 것
        """
        equation, x, y = self.data[idx] ### 식
        x, y = float(x), float(y)
        return eval(equation)
        
def main():
    evaluator = Evaluator('과제/equations.txt')
    assert np.allclose(evaluator.solve(0), 30)
    assert np.allclose(evaluator.solve(1), -1.9)

main()
