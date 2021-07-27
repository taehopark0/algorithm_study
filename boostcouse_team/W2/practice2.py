#월급을 입력하면 연봉을 계산해주는 계산기를 만들어 봅시다. 세전 연봉과 세후 연봉을 함께 출력하도록 해봅니다.
#아래의 세율 표를 토대로 만들어주세요(단, 실제 세율과 다를 수 있습니다!)

mon_payment =300
def yearly_payment(mon_payment):
    if mon_payment*12 <= 1200:
        before = mon_payment*12
        after = mon_payment*12*(1-0.06)

    elif mon_payment*12 <= 4600:
        before = mon_payment * 12
        after = mon_payment * 12 * (1 - 0.15)

    elif mon_payment*12 <= 8800:
        before = mon_payment * 12
        after = mon_payment * 12 * (1 - 0.24)

    elif mon_payment*12 <= 15000:
        before = mon_payment * 12
        after = mon_payment * 12 * (1 - 0.35)

    elif mon_payment*12 <= 30000:
        before = mon_payment * 12
        after = mon_payment * 12 * (1 - 0.38)

    elif mon_payment*12 <= 50000:
        before = mon_payment * 12
        after = mon_payment * 12 * (1 - 0.4)

    else:
        before = mon_payment * 12
        after = mon_payment * 12 * (1 - 0.42)

    statement= "세전 연봉: %d 만원"%before+" "+"세후 연봉: %d만원"%after

    return statement
print(yearly_payment(mon_payment))