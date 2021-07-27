#학생 이름과 점수를 입력하면 학점을 출력하는 학점 변환기를 만들어 봅시다.
#이름과 점수, 학점 모두 출력하도록 해봅니다.
grade_dict ={"A+": [x for x in range(95,101)], "A": [x for x in range(90,95)], "B+":[x for x in range(85,90)],
             "B":[x for x in range(80,85)],"C+":[x for x in range(75,80)],"C":[x for x in range(70,75)]
             ,"D+":[x for x in range(65,70)],"D":[x for x in range(60,65)],
             "F":[x for x in range(0,60)]}
#grade_dict_rvs = dict(zip(grade_dict.values(),grade_dict.keys()))
value_list = [values for values in grade_dict.values()]
key_list = [keys for keys in grade_dict.keys()]

grade = 95
name = "jake"
def grader(name,grade):
    for i in range(len(value_list)):
        if grade in value_list[i]:
            grade_alphabetic = key_list[i]
    statement = "학생 이름: %s"%name+ " " + "점수: %d점"%grade +" "+ "학점: %s"%grade_alphabetic
    return statement
print(grader(name,grade))
