#한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
#각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.
#제한사항
#numbers는 길이 1 이상 7 이하인 문자열입니다.
#numbers는 0~9까지 숫자만으로 이루어져 있습니다.
#"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
# 숫자로 만들어서 소수인지 아닌지 판별한다.
from itertools import permutations
import math, sys
numbers="011"

def solution(numbers):
    list_numbers=[x for x in numbers]
    permutations_list=[]
    answer=[]
    new=[]
    realanswer =[]
    def isPrime(x):
        if x ==1:
            return False
        for i in range(2,int(math.sqrt(x))+1):
            if x%i==0:
                return False
        return True
    for i in range(len(numbers)):
        permutations_list+=list(permutations(list_numbers,i+1))
    answer =list(map(''.join,permutations_list))
    for x in answer:
        if x.startswith('0') == True:
            x=x.replace('0','')
            new.append(x)
            if x == '':
                new.remove(x)
        else:
            new.append(x)
    for x in list(set(new)):
        if isPrime(int(x)) == True:
            realanswer.append(x)
    return len(realanswer)
print(solution(numbers))
