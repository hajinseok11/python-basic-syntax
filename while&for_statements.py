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

# 한 반에 수학 점수가 60 이상 합격, 60 미만 불합격
lista = [90, 25, 67, 45,80]
# 위 list가 학생의 번호 순서대로 있을때 아래와 같이 출력하도록 코딩
# ex) 1번 학생은 합격 입니다.
# ex) 2번 학생은 불합격 입니다.
# num = 1
# for i in lista:
#     if i > 59:
#         print(' %d 번째 학생은 합격'%num)
#     else:
#         print(' %d 번째 학생은 불합격'%num)
#     num+=1

# for i in range(len(lista)):
#     if lista[a] > 59:
#         print(' %d 번째 학생은 합격'% (a+1))
#     else:
#         print(' %d 번째 학생은 불합격'% (a+1))
    
# for문과 break: for 문에서 break를 반드시 써야하는 상황
# 혈액형이 a형인 고객 선착순 1명만 찾는 상황
lista = ['b','b','ab','a','b','a']
# 출력결과 : 4번째 고객이 이벤트에 당첨되었습니다.
for a in range(len(lista)):
    if lista[a] == 'a':
        answer = a+1
        # break를 넣고 안넣고 결과값 차이 확인
        break
print(str(answer) + "번째 고객이 당첨되었습니다")

# # for문을 이용한 구구단
# # 5단 결과 출력
for i in range(1,10):
    print(f"5 X {i} = {5*i}")
# 구구단 몇단을 계산해드릴까요? -> 
# while True 사용
while True:
    num = int(input("구구단 몇단을 계산해드릴까요?"))    
    for i in range(1,10):
        print(f"{num} X {i} = {num*i}")
    break

# 2중 for문
# 구구단을 5단~9단까지 한꺼번에 출력
# 5X1 = 5
# ...
# 9X9 = 81
num = 5
while num < 10:
    for i in range(1,10):
        print(f"{num} X {i} = {num*i}")
        num += 1

for num in range(5,10):
    for a in range(1,10):
        print(f"{num} X {a} = {num*a}")


lista = [10,20,30,40]
# list[0]와 lista[1]의 자리를 바꾸려면?
# lista = [20,20,30,40]
lista [0]= lista[1]
lista [1]= lista[0]
# 위 방식은 0번째 값이 소멸됨
temp = lista[0]
lista[0] = lista[1]
lista[1] = temp
# 위 방법은 값을 잃어버리지 않음
# 파이썬에서 지원하고있는 문법
lista[0], lista[1] = lista[1], lista[0]

# for 문을 이용한 정렬 알고리즘
lista = [93,45,21,30,20,94,66,71,45]
# 위 리스트를 어떻게 오름차순 정렬 할 것인가?
# lista.sort()
# print(lista)
# 선택정렬 : 0번째 index부터 가장 작은 값을 채워나가는 방식
# 첫번째 for문은 채워나가야할 index를 의미
for a in range(len(lista)-1):
    # 두번째 for문은 비교의대상이 되는 index를 의미
    for b in range(a+1,len(lista)):
        if lista[a] > lista[b]:
            # 자리 change
            # lista[a],list[b] = lista[b],lista[a]
            temp = lista[a]
            lista[a] = lista[b]
            lista[b] = temp
print(lista)
# 버블정렬 방법도 있음 (생략)

# 프로그래머스 행렬의 덧셈
arr1 = [[1,2],[2,3],[2,3],[2,3],[2,3]]
arr2 = [[3,4],[5,6],[2,3],[2,3],[2,3]]
answer = []
for a in range(len(arr1)):
    temp = []
    for b in range(len(arr1[0])):
        temp.append(arr1[a][b]+arr2[a][b])
    answer.append(temp) 
print(answer)
