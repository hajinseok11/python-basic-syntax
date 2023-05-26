# While 문의 기본구조:
# while 조건식: # 조건식이 참인 경우 반복 => 무한반복이 기본 전제
#     실행문
# a = 10
# while a > 5:
#     print("참입니다")

# 조건을 체크 후 True면 실행문을 1회 실행시키고,
# 다시 조건을 체크하러 돌아온다. 그리고 True이면 또 다시 실행.
# 그러다, 조건이 False되면 while문 종료
# a = 0
# while a < 5 :
#     print(str(a) + '번반복')
#     a += 1

# # 1~1000까지 프린트 되도록 출력
# a = 0
# while a <1000:
#     a += 1
#     print(a)
# # 1~1000까지의 합 출력
# a = 1
# sum = 0
# while a <= 1000:
#     sum+=a
#     a += 1
# print(sum)

# While문에서 반복을 진행하다가 break를 만나면 반복문 종료
# 1) if 문을 써서 특정 조건에 break
# a = 1
# sum = 0
# while True:
#     sum+=a
#     if a == 1000:
#         break 
#     a += 1
# print(sum)

# continue : 이 구문을 만나면, 다시 반복문 조건으로 이동
# 하단에 불필요한 로직을 수행하지 않고 다시 조건으로 이동할 수 있게 해준다.
# 아래와 같은 코드에서 hello는 무한출력
# a = 0
# while a < 1000:
#     print("Hello")
#     continue
#     a += 1

# 2) 1~1000중에 홀수만 더해서 출력 # 250500
# continue : 이 구문을 만나면, 다시 반복문 조건으로 이동
# a = 0
# sum = 0
# while a < 1000:
#     a+=1
#     if a % 2 == 0:
#         continue
#     sum += a
#         # continue문을 활용해서 coding
# print(sum)


# 1. 사용자한테 리스트 크기를 입력(3)
# 2. 리스트 크기 만큼 값을 입력받는것.(3번반복)
# => 10
# => 20
# => 30
# while True:
#     listSize = int(input("리스트의 크기를 입력해주세요"))
#     if listSize > 10:
#         print('다시 입력해주세요')
#         continue
#     a = 0
#     lista = []
#     while a < listSize:
#         listValue = input("리스트의 값을 입력해주세요")
#         lista.append(listValue)
#         a += 1
#     print(lista)

# 로또 번호 생성기
# 랜덤의 값을 추출하는 파이썬 라이브러리 => random
import random
# print(random.randint(1,45))
# 리스트의 크기가  6개인 리스트를 만들어서, 오늘의 로또번호를 만들어보자.
a = 0
lista = []
while a < 6 :
    randNum = random.randint(1,45)
    lista.append(randNum)
    a += 1
print(lista)


# for 문의 기본구조
# for 변수 in 반복가능한 자료형(iterable)
#   실행문
# lista = [1,2,3,4,5,6,7,8,9,10]
# for a in lista:
#     # a = 1, a = 2, a = 3, a = 4  .....
#     print(a)

# range 문법 : range(x,y) x이상 y미만
# for a in range(1,101):
#     print(a)

# range의 의미 iterable 객체
v1 = list(range(1,10))
print(v1)

# range(x,y) : x이상 y미만의 숫자를 담은 객체
# range(y) : 0이상 y 미만의 숫자를 담은 객체
v1 = list(range(10,20)) # 10, 11, ...., 19
# for a in 리스트를 써서 v1의 값을 모두 출력
for a in v1:
    print(a)
# for a in range를 써서 v1[index]의 형태로 v1의 값을 모두 출력

for b in range(len(v1)):
    print(v1[b])

# for a in 리스트 구문으로는 원본리스트 데이터를 변경할 수 없다.
lista = [10,20,30,40,50,60,70,80,90,100]
lista[5] = 100
for a in lista:
    a = 100     # 이런 방식으로는 원본의 lista의 값을 변경할 수 없다.

# 직접 리스트의 index로 접근해야지 원본을 바꿀 수 있다.
for a in range(len(lista)):
    lista[a] = 100
print(lista)

# 리스트를 만드는 방법중에 리스트 컴프리헨션이라는 방법이 있다.
# 리스트에 0~9 까지를 담는 방법
# 방법1
lista = [0,1,2,3,4,5,6,7,8,9]
# 방법2
lista = list(range(10))
# 방법3
lista = []
for a in range(10):
    if a % 2 !=0:
        lista.append(a*2)

# 방법4     # 리스트 컴프리헨션
# 장점 : 간결하다
lista = [a*2 for a in range(10) if a % 2 !=0]
print(lista)

