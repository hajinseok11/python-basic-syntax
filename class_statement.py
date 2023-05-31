# 클래스의 사용
# 1) 같은 기능의 함수의 집합
# 2) 객체를 만들기 위해 사용

# 사칙연산 함수가 있을 때, 같은 기능을 하므로
# Calculator라는 클래스에 모아둘 수 있다.
# 명명규칙: 일반적으로 클래스는 대문자 알파벳으로 시작
# 변수명, 함수명은 소문자로 시작 -> camelcase
# 함수의 집합으로서의 클래스 -> 일반적이지 않은 형태
# class Calculator:
#     def plus(a,b):
#         return a+b
#     def minus(a,b):
#         return a-b
#     def multiply(a,b):
#         return a*b
#     def divide(a,b):
#         return a/b
# print(Calculator.plus(10,20))
# 위 클래스의 문제점은 클래스 내에서 누적된 값을 변수로 갖고있지 않다.
# class Calculator:
#     result = 0
#     # 클래스 변수 접근가능 방법1: 클래스명.변수
#     # 방법2 : classmethod 데코레이터 사용
#     # class내에 선언된 함수는 메서드라 부른다.
#     @classmethod
#     def plus(cls,a):
#         cls.result += a
#     def minus(a):
#         Calculator.result -= a
#     def multiply(a):
#         Calculator.result *= a
#     def divide(a):
#         Calculator.result /= a
# print(Calculator.result)
# Calculator.plus(10)
# print(Calculator.result)
# Calculator.minus(5)
# print(Calculator.result)


# 객체란 클래스의 복제본, 인스턴스라 부르기도 한다.
# 객체의 사용이유
# 클래스의 중복제거 : 변수와 함수의 재활용의 어려움 해결
# 객체 형식의 클래스의 기본구조
class Calculator:
    # 객체가 생성될 때 init은 가장먼저 실행
    # 생성자는 객체가 생성될 때 객체변수를 초기화(최초 setting) 하는 역할
    # result와 self.result는 다른 값이다.
    def __init__(self,result):
        self.result = result     # 1000 등으로 설정 가능
    # 객체를 만들 때 메서드 내의 첫번째 매개변수는 객체를 의미한다.
    def plus(self,a):
        self.result += a
    def minus(self,a):
        self.result -= a
    def multiply(self,a):
        self.result *= a
    def divide(self,a):
        self.result /= a

# 클래스생성시 매개변수를 통해 초기값 세팅가능
aCompany = Calculator(1000)
print(aCompany.result)
bCompany = Calculator(2000)
print(bCompany.result)

# Person이라는 클래스를 만든다.
# 생성자로 이름(name), 나이(age), 성별(gender), email을 받는다.
# 현재시간 출력하는 파이썬 함수
# import datetime
# print(datetime.datetime.now())      # 가입일도 출력 가능
# class Person:
#     def __init__(self,name,age,gender,email):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.email = email
#     def register(self):
#         self.myInfo = self.name +" ", self.age +" ", self.gender +" ", self.email
# p1 = Person('홍길동','19','남','hong@naver.com')
# p2 = Person('홍길동2','29','남','hong@naver.com')
# p1.register()
# p2.register()
# print(p1.myInfo)
# print(p2.myInfo)

# 클래스의 상속 
# 부모클래스에서의 기능을 자식클래스에서 물려받는 것
# class 자식클래스명(부모클래스명) 이런 형식으로 선언
class Calculator:
    def __init__(self):
        self.result = 0    
    def plus(self,a):
        self.result += a
    def minus(self,a):
        self.result -= a
    def multiply(self,a):
        self.result *= a

# Calculator 상속 후 divide메서드 추가
class CalculatorChild(Calculator):
    def divide(self,a):
        self.result/=a
    # 부모한테 있는 기능을 재선언하게 되면, 부모의 기능보다
    # 자식의 기능이 우선하게 되고, 이를 overriding이라 한다.
    def multiply(self,a):
        self.result *= (a+1)
    def printCalObject(self):
        return self.result
if __name__ == "__main__":
    cc1 = CalculatorChild()
    cc1.plus(100)
    print(cc1.result)
# print함수가 속해있는 클래스는 object클래스를 상속받고있다.
# 그런데, object클래스 안에는 list, dict같은 파이썬에서 자주
# 사용되는 객체값을 value형식으로 출력해주는 함수가 내장되어있다.


