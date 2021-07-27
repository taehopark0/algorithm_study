#Q1. 컴퓨터와 함께하는 가위바위보 게임을 만들어봅시다!
#조건1 : 함수의 인자로는 나의 가위바위보 선택이 들어감
#          (0, 1 ,2 혹은 "가위", "바위", "보" 로 입력할 수 있습니다. - 총 6가지 방법으로 넣을 수 있음)
#조건2 : 누가 무엇을 냈고, 누가 승리 했는지 출력이 되어야 함

import random
choice_dic ={"가위":0, "바위":1, "보":2}
choice_list = [0,1,2,"가위","바위","보"]
me= random.choice(choice_list)
you= random.choice(choice_list)

def solution(me,you):
    #숫자 연산을 위해 정수값으로
    if type(me)==str:
        me = choice_dic[me]
    if type(you) == str:
        you = choice_dic[you]
    #딕셔너리 키, 값 뒤집
    choice_dic_rvs = dict(zip(choice_dic.values(),choice_dic.keys()))
    #결과 비교
    if you - me == 1 or you-me ==-2:
        you = choice_dic_rvs[you]
        me= choice_dic_rvs[me]
        statement = 'me:%s'%me +' '+ 'you:%s'%you +' '+ "you가 이겼다"
    if me - you == 1 or me - you == -2:
        you = choice_dic_rvs[you]
        me = choice_dic_rvs[me]
        statement = 'me:%s'%me +' '+ 'you:%s'%you +' '+ "me가 이겼다"
    if me == you:
        you = choice_dic_rvs[you]
        me = choice_dic_rvs[me]
        statement = 'me:%s'%me +' '+ 'you:%s'%you+' '+ "비겼다"
    return statement
print(solution(me,you))