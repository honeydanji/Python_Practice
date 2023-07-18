class Fraction:
    def __init__(self, numerator, denominator): ### 초기값
        self.numerator = numerator ### 분자
        self.denominator = denominator ### 분모
        
    def reduce(self):
        if self.denominator == 0:
            raise ZeroDivisionError
        gcd = self.greatest_common_divisor(self.numerator, self.denominator)
        
        return self.numerator // gcd, self.denominator // gcd

    ## 최대공약수 구하기
    @staticmethod        
    def greatest_common_divisor(m, n):
        
        ''' 
            @statocmethod : 1. 정적메서드 
                            2. self를 사용하지 않는다.
                            3. 단순 계산할 때 유용하다.(사칙연산)
                            4. 인스턴스 내부 수정이 필요없을 때 사용하자.                
        '''
         
        while n != 0:
            t = m % n
            (m, n) = (n, t)
        return abs(m)
    
    