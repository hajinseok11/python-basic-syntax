a = 10
if (a > 5) | (a > 100):
    print('참입니다1')
if a > 5 | a > 100 :
    print('참입니다2')
# 비트연산이란 2진법의 숫자를 | (or), &(and), ^(xor) 등으로 
# CPU내부적으로 계산하는 방식
# ex)
# 1111 and 1000 => 1000     1 = True 0 = False
# 1111 or 1000 => 1111
print(10 or 1) # => 10 출력 / 비트 연산시 | 사용해야함

# and는 &와 같고 or는 |와 같고 not은 부정의 의미
# not True 는 False가 되고, not False는 True가 된다.

# 대입연산자
a = 10 
# a = a + 1 이렇게 표현해도 되고, a += 1 이렇게 표현해도 된다.
a += 1 
print(a)
# -=, /=, *=, 

# 비교연산자 중에 chaining (범위로 표현할 수 있다.)
# 5 < a < 100 이렇게 표현하거나 a > 5 and 100 < a
a = 10
if a > 5 and 100 < a:
    print('참입니다.')


# if문의 기본 문법
# else는 optional(선택적) 요소
# else 상단에 있는 if 또는 elif에 종속된다.
# elif도 마찬가지로 elif 상단에 if에 종속된다.
# 숫자를 입력받아서.
# 90이하면 예각입니다 출력
# 90이면 직각
# 91~179면 둔각
# ~중 하나만을 실행시키고자 할 때는 elif를 if 에 종속시켜 실행하면 실수가 없다.
# num1 = int(input('숫자를 입력해주세요'))
# if num1 < 90:
#     print('예각입니다.')
# elif num1 == 90:        # elif는 if에 종속적
#     print('직각입니다.')
# elif num1 < 180:
#     print('둔각입니다.')
# elif num1 == 180: # else를 써도되고, 안써도 된다.
#     print('직각입니다.')               


# if 참조건:
#     실행문
# else:
#     실행문
a=int(input("숫자를 입력해주세요"))
if a > 10:
    print("a는 10보다 큽니다")
else:
    print("a는 10보다 작습니다.")

TrueOrFalse = True
if TrueOrFalse:
    print("참입니다")
else:
    print("거짓입니다")

# 얼마를 가지고있습니까?를 변수에 담고
# 만약 30,000 이상이 있으면 '택시를 타고 가시오'출력
# 그렇지 않으면 '걸어가시오' 출력
money = int(input("얼마를 가지고 있습니까?"))
if money >= 30000:
    print('택시를 타고 가시오')
else:
    print('걸어가시오')

# if문 한줄로 쓰기
# 코드가 짧고 단순한 경우에 아래와 같이 한줄로 쓰는 것을 권장
# ';' 사용하여 두줄을 한줄로 표현 가능 권장x
a = 10
if a > 1 : print('a는 1보다 큽니다')

# 조건부표현식(삼항연산자) : 간단한 식으로 표현
# 먼저 if문의 실행문을 if 문 앞으로, : 필요없고,
a = 10
print('a는 10보다 큽니다.') if a >10 else print('a는 10보다 작습니다.')
# 실행문을 실행하기 위해 사용한다기 보다는,
# 참인경우에 어떤값, 거짓인 경우에 어떤 값을 쉽게 result에 담기 위해 사용
result = 'A는 10보다 큼' if a > 10 else 'A는 10보다 작음'
print(result)


lst = [1,2,3,4,5,6,7,8,9,10]
numInput = int(input('정수입력'))
if numInput in lst:
    print("입력하신 숫자는 존재합니다.")
else:
    print('리스트에 포함되지 않았습니다.')


wei = int(input('짐의 무게'))
fee = (wei // 10)*10000
if wei < 10:
    fee = 0
print('짐의 무게는 %d 이고, 수수료는 %d입니다.'%(wei,fee))
# f formating
print(f"짐의 무게는 {wei} 이고, 수수료는 {fee}입니다")


money = int(input('돈이 얼마 있으신가요?'))
dinner = input("배가 고프신가요? 네 or 아니오")
if money > 10000 and dinner == '네':
    print("저녁을 사먹으시오")
else:
    print('집에 가시오')

# a와 b가 같은지 비교하는 연사자 is
# 객체 타입의 경우에는 메모리 주소를 비교하고,
# 숫자, 문자, bool과 같은 기본타입의 경우 값을 비교한다.
# 숫자, 문자, bool같은 경우에는 데이터 pool을 만들어서, 재활용 한다.
# 그래서, 값을 비교할 때 메모리 주소가 아니라 데이터 pool에서 값을 직접 비교
a = 10
b = 10
if a is b:
    print('참입니다.')

a = [10,20]
a = [10,20]
if a is b:
    print("참입니다") # False

a = 10
b = 20
if a == b:
    # pass 시키는 것 (pass를 명시적으로 표현한 것)
    pass
else:
    print('두 값이 다릅니다.')

