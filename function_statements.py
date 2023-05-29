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
    calc = (((myinput+ 10) * 20) / 10 ) ** 2
    return calc

# 정의된 함수를 호출할 때는 함수명(input)의 형태로 호출하게 된다.
result2 = MyFunc(200)

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
    return result
r1 = myindex(lista,9)
print(r1)

