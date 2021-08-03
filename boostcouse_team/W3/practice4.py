#Q4. 2개의 숫자를 입력하여 그 사이에 소수가 몇 개인지 출력하는 함수를 만들어 봅시다.
#소수: 1과 자기 자신만을 약수로 가지는 수
#:작은_아래쪽_화살표: 출력 예시

import random
import math
n = random.randint(1,101)
m = random.randint(n,1000)
new_list = []

def count_prime_number(n,m):
    def isPrime(x):
        if x ==1:
            return False
        for i in range(2,int(math.sqrt(x))+1):
            if x%i==0:
                return False
        return True
    variables = [x for x in range(n,m+1)]
    for variable in variables:
        if isPrime(variable) == True:
            new_list.append(variable)
    return len(new_list)
print(count_prime_number(n,m))
