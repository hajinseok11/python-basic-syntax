# if문의 기본 문법
# else는 optional(선택적) 요소
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


