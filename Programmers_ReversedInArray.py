#자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
#n	    return
#12345	[5,4,3,2,1]
#https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = []
    n=str(n)
    n = reversed(n)
    for x in n:
        answer.append(int(x))
    return answer

