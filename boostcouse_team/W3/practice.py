#Q1. 숫자를 입력 받고 그 숫자의 구구단을 출력하는 함수를 만들어 봅시다. 다만 아래의 조건을 만족해 주세요.
#조건 1: 홀 수 번째만 출력하기
#조건 2: 값이 50이하인 것만 출력하기

number = int()
def solution(number):
    print("몇 단? : %d"%number)
    print("%d단"%number)
    for i in range(1,10):
        if i%2 ==1 and number*i <= 50:
            print('%d'%number,'X',i, '=',number*i)
print(solution(number))
