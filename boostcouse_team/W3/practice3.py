#Q3. 2개의 숫자를 입력하여 그 사이에 짝수만 출력하는 함수를 만들어 봅시다. 그리고 중앙값도 함께 출력 해봅시다.
# (단, 중앙값이 짝수가 아닐 경우에는 중앙값은 출력을 하지 않고, 짝수인 수만 출력한다)
#중앙값: 정중앙에 있는 값
#특정 두 숫자 사이의 수들을 리스트로 만드는 법
import random
import numpy as np
n = random.randint(1,101)
m = random.randint(n,1000)
numbers = [ i for i in range(n,m+1)] # range(시작 숫자, 끝 숫자 + 1)
new_list =[]
def solution(numbers):
    for number in numbers:
        if number%2 == 0:
            new_list.append(str(number)+' '+'짝수')
    if np.median(numbers)%2 ==0:
        md= np.median(numbers)
        print(md)
        if len(new_list)%2 == 0:
            new_list.insert(len(new_list)/2,str(md)+' '+'중앙값')
        else:
            new_list.insert((len(new_list)-1)/2, str(md) + ' ' + '중앙값')
    return new_list
print(solution(numbers))


