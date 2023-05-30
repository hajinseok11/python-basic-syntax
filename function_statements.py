a = 100
# 특정한 input값이 있을 때,
# 해당 값을 복잡한 로직을 통해서 연산을 한다고 가정하자.
# 그런데, 해당 연산은 매우 빈번하게 사용이 된다고 가정하자.
result = (((a + 10) * 20) / 10 ) ** 2
print(result)
b = 200
result2 = (((a + 10) * 20) / 10 ) ** 2
print(result)
# 복잡한 로직의 연산을 함수화 시켜서 재사용 할 수 있게 해보자.
# input값이 있어도 되고, 없어도 된다.
# return 값이 있어도 되고, 없어도 된다.
def MyFunc(myinput):
    calc = (((myinput + 10) * 20) / 10 ) ** 2
    return calc
# 정의된 함수를 호출할 때는 함수명(input)의 형태로 호출하게 된다.


# 함수 직접 구현해보기. 함수명은 myPlusFunc
# 함수의 로직은 사용자의 input을 받아 input값의 누적합을 더하는 함수
# 예를 들어 100을 입력하면 1+2+3+...+100
def myPlusFunc(num1):
    sum = 0
    for i in range(num1+1):
        sum += i
    return sum
result = myPlusFunc(10)
result2 = myPlusFunc(100)
print(result)
print(result2)

# input값 2개를 받아 두 값을 더한 뒤 *2만큼 하여 return 하는 함수를 만들어보자
# 그리고, 해당 함수를 호출하여 호출된 결과값을 result에 답아 출력해보자
def plusmulti(input1,input2):
    answer = (input1+input2)*2
    return answer
result = plusmulti(10,20)
print(result)

# list의 index함수를 쓰지않고 for문 또는 while문을 통해 숫자 9가 몇번째 index에 있는 값인지
# print 해보자
lista = [1,4,6,9]
for a in range(len(lista)):
    if lista[a] == 9:
        print(a)
        break       # 앞의 값을 먼저 출력하는 index 함수이기 때문에 break 필요

# 위의 for문을 활용하여 myindex라는 이름의 함수를 만들고자 한다.
# input값이 2개, print는 함수 내에서 하지 않고 
# return에 값을 담는다.
lista = [1,4,6,9]
def myindex(input1,input2):
    result = -1
    for a in range(len(input1)):
        if lista[a] == input2:
            result = a
            # break할 필요없이 바로 return해도 된다.
            # return하게 되면 함수전체가 강제 종료된다.
    return result
r1 = myindex(lista,9)
print(r1)

# 원의 넓이를 구하는 함수 만들기
# result = circleSize(num1)
# print("원의 넓이:" + str(result))

# 내가 작성한 답
# num1 = int(input('반지름의 길이를 입력하세요'))
# def circleSize(num1):
#     size = (num1**2)*3.14
#     return size
# print("원의넓이:"+ str(circleSize(num1)))

def circleSize(myInput):
    result = myInput **2 *3.14
    return result
num1 = int(input('반지름의 길이를 입력하세요'))
result = circleSize(num1)
print('원의넓이:'+str(result))

# 입력값이 없는 함수
# hello 출력하기
def hello1():
    print("hello1 python!")
def hello2():
    result = ("hello2 python!")
    return result
hello1()
print(hello2())

# 입력값이 정해져 있지 않고 mulitple한 함수
# 입력값의 개수가 정해져있지 않고 multiple한 함수 => *사용
def sum(*args):
    total = 0
    for i in args:
        total += i
    return total
totalValue = sum(1,2,3,4,5)
print(totalValue)

# 2개 이상의 리턴값이 있는 경우 :  tuple형태로 데이터 return
def cal(a,b):
    result1 = a+b
    result2 = a-b
    result3 = a*b
    return result1, result2, result3
calValue = cal(1,2)
# 계산한 첫번째 결과값은 xx, 두번째 결과값은 yy, 세번째 결과값은 zz
print(f'계산한 첫번째 결과값:{calValue[0]}, 두번째 결과값:{calValue[1]},세번째 결과값:{calValue[0]}')

# 함수에서 default 값 미리 세팅하기
def cal(a,b,c = 'plus'):    # default 값(기본값) 'plus'로 세팅된 것. 값을 주면 덮어 씌어짐
    if c =='plus':
        result = a+b
    elif c == 'minus':
        result = a-b
    elif c == 'multiply':
        result = a*b
    return result
# 더하기한 값 출력 
# 마이너스한 값 출력 
# 곱하기한 값 출력 
print(cal(3,5,'plus'))
print(cal(3,5,'minus'))
print(cal(3,5,'multiply'))

# 매개변수의 순서를 안맞추고도 원하는 매개변수의 자리에 값을 넣어
# 함수를 호출하는 방법
def whoAreYou(name,age,gender):
    print(f"제이름은 {name}이고, 나이는{age}, 성별은 {gender}입니다.")
whoAreYou(age = 19, name = '홍길동', gender = '남자')

# 파이썬에서 default 값 세팅하는 대표적인 예시가 print함수
# print 2개를 사용해서 줄바꿈 없이 hello world 라고 출력이 되도록 만들어보자
print('hello', end = ' ')
print('world')

# 지역변수와 전역변수
# 지역변수 : 함수 내에서의 변수, 함수 내에서만 유효
# 전역변수 : 함수 밖에서의 변수, 함수 내에서도 인식가능
a = 100
def sum(a,b):
    # 여기서 a의 값은? 100 or 10?
    # 전역변수인 a = 100보다, 함수 내에서 선언한 a = 10 우선적으로 인식
    result = a+b
    return result
result = sum(10,20)
print(result)   # 함수 내의 result 라는 변수는 함수 밖에서는 인식불가
print(a)        # result 프린트 할 수 있었던 것은 함수 내에서 어떤 값을 return해줬기 때문


lista  = [10,20,30,40]
# for 문 마다 같은 변수를 사용하는 것은 전역변수이기는 하지만,
# 재할당을 해서 사용하는 것이므로 reset되기 때문에 문제되지 않는다.
for a in range(len(lista)):
    print(a)
for a in range(len(lista)):
    print(a)
print(a)

# 이중 for문을 사용할 때는 문제가 될 여지가 있다.
# 다중 for문을 쓸 때는 상위의 for문의 변수를 잃어버리게 되므로, 다른 변수명 사용.
for a in range(len(lista)):
    for b in range(len(lista)):
        print(a)
        print(b)

# 함수 내에서 전역변수에 영향을 끼치는 방법 : global
# 기본적으로 함수 내에서 함수 밖의 전역변수를 수정할 수 없다.
# 그 이유는 저장되는 메모리 위치가 다르기 때문에
result = 0
def sum (a):
    global result
    result += a
    return result
value = sum(10)
print(value)

# 객체는 힙 메모리 영역에 저장되는데, 함수 내에서도 접근하여 추가/수정이 가능하다.
# 스택영역에 있는 지역변수는 함수가 끝나면 휘발되지만, 힙메모리는 휘발되지 않는다.
lista = [2,3,4]
def appendTest(input1, input2):
    input1.append(input2)
appendTest(lista,5)
print(lista)

# 만약에 지역변수가 함수호출이 끝난뒤에도 남아있다면 어떻게 될까?
# 함수에서 사용하는 지역변수가 계속 메모리에 남아있으면,
# 메모리 낭비 뿐만 아니라 다른 함수에서 해당 변수명을 사용할 수 없는 불편함이 있다.
# def test1(result):
#     result += 10
#     return result
# def test2():
#     result += 100
#     return result
# a = test1(20)
# b = test2()

# 아래 선택정렬을 함수화 시켜서 활용해보기
# def mySort(lista)
# print(lista)
def mySort(numlist):
    for a in range(len(lista)-1):
        # 두번째 for문은 비교의대상이 되는 index를 의미
        for b in range(a+1,len(lista)):
            if lista[a] > lista[b]:
                # 자리 change
                # lista[a],list[b] = lista[b],lista[a]
                temp = lista[a]
                lista[a] = lista[b]
                lista[b] = temp
lista = [5,1,2,3,6]
# lista.sort()
# list.sort(lista)
mySort(lista)
print(lista)

# lista에 listb를 담으면, 객체의 주소가 복사가 되게 된다.
# 그래서 listb가 lista와 동일한 주소, 동일한 데이터를 갖게된다.
lista = [5,1,2]
listb = lista
# 주소 출력하는 함수 : id
print(id(lista))
print(id(listb))
# lista와 값은 같되, 동일한 메모리 주소가 아니게 할당하고 싶으면 copy함수 사용
import copy
# 얕은 복사 즉, 객체안의 객체의 값은 (메모리) 주소로 복사가된다.
# 깊은 복사는 copy.deepcopy를 사용하여 객체의 객체도 모두 value로 복사.
listb = copy.copy(lista)
print(id(listb))
print(listb)

lista[0] = lista[1]
lista[1] = lista[0]
print(lista)
