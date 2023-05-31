# 예외처리 : try except 구문
# 예외처리를 하는 이유는 프로그램 실행 중간에 예외가 발생하더라도
# 프로그램이 강제종료되지 않도록 하기 위해
# while True:
# #     # 분자를 입력해주세요   first
# #     # 분모를 입력해주세요   second
    
# #     # 사용자가 0으로 숫자를 나누게 되면 
# #     # division by zero 에러발생
# #     # 문제발생 가능성이 있는 곳에 try
#     try:
#         first = int(input("분자를 입력해주세요"))
#         second = int(input("분모를 입력해주세요"))
#         print(first/second)
# #     # 문제 발생했을 때 이후의 action except
#     except ZeroDivisionError as zd:
#         print(f"{zd}오류입니다.")
#     except ValueError as ve:
#         print(f"{ve}오류입니다")
#     except Exception:
#         print(f"{Exception}오류입니다.")
# #     # finally는 문제가 있든 없든 무조건 실행
#     finally:
#         print("결과를 확인해주세요")

# 에러 강제의 예시
# while True:
#     raise Exception
# 부모클래스 raise Exception (에러 강제)를 통해
# 자식클래스로 하여금 overriding 유도
class Bird:    
    def fly(self):
            raise Exception
class Eagle(Bird):
    def fly(self):
        print("fly fly")
    pass

eagle1 = Eagle()
eagle1.fly()

