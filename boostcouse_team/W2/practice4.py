#나이와 현금 또는 카드를 입력하면 버스 요금이 출력되는 버스 요금 계산기를 만들어봅시다

import random
age = random.randint(1,100)
payment_type =["카드", "현금"]
type = random.choice(payment_type)
def bus_fare(age,type):
    if type == "카드":
        if age < 8:
            fare = "무료"
        if age >= 8 and age < 14:
            fare = "450원"
        if age >= 14 and age < 20:
            fare = "720원"
        if age >= 20 and age <75:
            fare = "1200원"
        else:
            fare = "무료"
    if type == "현금":
        if age < 8:
            fare = "무료"
        if age >= 8 and age < 14:
            fare = "450원"
        if age >= 14 and age < 20:
            fare = "1000원"
        if age >= 20 and age <75:
            fare = "1300원"
        else:
            fare = "무료"
    statement = "나이: %d세"%age + " "+"지불 유형:%s"%type+", "+"버스 요금: "+fare
    return statement
print(bus_fare(age,type))

