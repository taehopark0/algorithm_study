#https://programmers.co.kr/learn/courses/30/lessons/68935
#자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
#n	    result
#45	    7
#125	229

def solution(n):
    list = []
    answer =[]
    while True:
        n, rest = divmod(n, 3)
        list.append(rest)

        if n == 0:
            break
    list = reversed(list)
    for k, v in enumerate(list):
        answer.append(v*(3**k))
    value = sum(answer)
    return value