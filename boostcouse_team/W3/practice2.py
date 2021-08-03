#Q2. 가위바위보 업그레이드 버젼을 함수로 만들어 봅시다. 아래와 같은 조건을 만족해 주세요.
#조건 1: 게임을 몇 판을 진행할 것인지 입력을 받아주기
#조건 2: 0, 1, 2, "가위", "바위", "보" 이외에 다른 입력을 받으면 재입력 받기
#조건 3: 게임종료 후 나와 컴퓨터의 총 전적 출력하기
import random
choice_dic = {"가위": 0, "바위": 1, "보": 2}
choice_list = [0, 1, 2, "가위", "바위", "보"]
me = random.choice(choice_list)
you = random.choice(choice_list)
number = random.randint(1, 10)
# 숫자 연산을 위해 정수값으로

def solution(me,you,number):
    me_count = 0
    you_count =0
    draw_count = 0
    choice_dic_rvs = dict(zip(choice_dic.values(), choice_dic.keys()))
    #딕셔너리 키, 값 뒤집
    for i in range(1, number + 1):
        me = random.choice(choice_list)
        you = random.choice(choice_list)
        if type(me) == str:
            me = choice_dic[me]
        if type(you) == str:
            you = choice_dic[you]
        print("가위 바위 보 : " + str(i))
        #결과 비교
        if you - me == 1 or you-me ==-2:
            you = choice_dic_rvs[you]
            me= choice_dic_rvs[me]
            statement = str(i)+' '+ '번 째 판 you의 승리'
            you_count+=1
            print('나 : ' + me)
            print('you : ' + you)
            print(statement)
            you = choice_dic[you]
            me = choice_dic[me]
        if me - you == 1 or me - you == -2:
            you = choice_dic_rvs[you]
            me = choice_dic_rvs[me]
            statement = str(i) + ' ' + '번 째 판 me의 승리'
            print('나 : '+ me)
            print('you :' + you)
            print(statement)
            me_count+=1
            you = choice_dic[you]
            me = choice_dic[me]
        if me == you:
            you = choice_dic_rvs[you]
            me = choice_dic_rvs[me]
            statement = 'me:%s'%me +' '+ 'you:%s'%you+' '+ "비겼다"
            draw_count +=1
            print('나 : ' + me)
            print('you :' + you)
            print(statement)
            you = choice_dic[you]
            me = choice_dic[me]
    print('me의 전적 : %d'%me_count+'승'+' '+'%d'%draw_count+'무'+' '+'%d'%you_count+'패')
    print('you의 전적 : %d'%you_count+'승'+' '+'%d'%draw_count+'무'+' '+'%d'%me_count+'패')
print(solution(me,you,number))