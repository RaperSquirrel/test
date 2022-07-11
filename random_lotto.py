pass_cord = input("생년월일 8자리를 입력해 주십시오...")

Age = int(pass_cord[:4])

from random import*

if Age <= 2002 : 
    print("복권 구매가 가능한 나이입니다.")
    print("복권번호를 추첨하겠습니다")
    print(str(randrange(1, 99)))
    print(str(randrange(1, 99))) 
    print(str(randrange(1, 99)))
    print(str(randrange(1, 99)))
    print(str(randrange(1, 99)))
    print(str(randrange(1, 99)))
    print("보너스 번호는",str(randrange(0, 99)) ,"입니다.")

elif Age > 2003 : print("미성년자는 복권 구매가 불가능 합니다.")

input()






