# list란 변수마다 값을 할당에서 사용하기에는 관리에 어려움이 있으므로
# 한 변수에 값을 집합시켜 놓은 것.
a = "a"
b = "b"
c = "c"
# 하나의 변수로 여러개의 데이터를 관리
# list의 경우에 []대괄호를 사용하여 데이터를 집합
lista = ["a","b", "c","d","e","f","g"]
# list안의 각각의 값에 접근할 때에는 index를 사용
print(lista[0])
print(lista[1])
print(lista[2])
# 여러개의 데이터를 범위를 지정해서 가져오고 싶을 때는 slicing 사용
# 슬라이싱의 결과값은 같은 list로 출력
# 0~5 번째까지 출력한 결과물의 type 출력
print(lista[0:5])
print(type(lista[0:5]))

# 문자열은 메모리 내부적으로 list와 유사한 자료구조
# 문자열은 값을 추가하거나 수정할 수가 없다.
# list는 값의 추가, 삭제, 수정이 가능한 구조를 가지고 있다.

# number 변수에 리스트 [1,2,3]을 저장하여 출력, 리스트 [1,2,3]의 1과 3을 더하여 출력
# list안에 list의 값을 조회하는 방법
list_ex1 = ['a','b','c',[1,2,3]]
number = list_ex1[3]
print(number[0]+number[2])
print(list_ex1[3][0]+list_ex1[3][2])

# 리스트 더하기
# list를 2개 선언하고 만들어서, 2개를 더해서 하나의 리스트로 만들어보자 그리고 출력
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
print(list1+list2)
print(3*(list1+list2))

# 리스트 길이구하기 (len)
print(len(list1))

# 리스트 값 수정하기 
# -> 1개의 값만 바꿀 땐 1개의 값으로
# -> 여러 값을 바꿀 땐 다른 리스트로 대체
lista = [1,3,5,7,9]
lista[1] = 4
print(lista)
lista[2] = [5,5,5]
print(lista)

# 리스트 요소 개수 세기 (count)
lista = ['1','2','3','4','1','1','3']
print(lista.count('1'))

# 리스트 요소 삭제하기 
# del 변수[index]
lista = ['1','2','3','4','1','1','3']
del lista[3]
print(lista)
# remove(값)
lista = ['1','2','3','4','1','1','3']
lista.remove('1')
print(lista)

# 특정한 값을 모두 제거하려면 어떻게 해야할까?
# del, for range
lista = [1,9,4,9,5,7,8,9]
count = 0
for a in range(0,len(lista)):
    if lista[a-count] == 9:
        del lista[a-count]
        count = count + 1
print(lista)
# remove
lista = [1,9,4,9,5,7,8,9]
for a in range(0,len(lista)):
    if 9 in lista:
        lista.remove(9)
    else:
        break
print(lista)

# list append : 리스트 맨 뒤로 추가
lista = [1,3,5,7]
# 9, 10을 append 이용해서 추가
lista.append(9)
lista.append(10)
print(lista)
# list insert : index를 지정하여 추가 가능
# lista.index(2,"abc") 추가 후 출력
lista.insert(2,"abc")
print(lista)
# list extend : iterable객체를 list에 추가할 때 사용
# extend 는 각 요소를 꺼내어 맨 뒤에 추가
listb = [10,20,30]
# lista.append(listb)
lista.extend(listb)
print(lista)

# list의 정렬은 sort()함수 사용
# sort()는 오름차순 정렬
# reverse=True 옵션을 주면 내림차순 정렬
numa = [1,5,6,524,75,34,86,5,35]
numa.sort()     
print(numa)

chlist = ['bread','john','abc']
chlist.sort()
print(chlist)

# list 뒤집기 : reverse()
chlist.reverse()
print(chlist)

# 리스트 위치반환: index()
lista = ["김돌쇠","김갑돌","김갑순","김철수"]
print(lista.index("김철수"))

# 마지막 요소 끄집어내기(pop)
# remove and return last value
lista.pop()
lastValue = lista.pop()
print(lastValue)

# 문자 리스트를 문자열로 만들기
# 문자열을 문자 리스트로 만들기
lista = ["hello","world","python"]
st2 = "".join(lista)
print(st2)
# 문자열을 문자 리스트로 만들기
sta = "hello world python"
mySta1 = list(sta)
mySta2 = sta.split()
print(mySta2)

my_string = 'bread'
# 방법 1 : list로 변환 후 reverse
# stList = list(my_string)
# stList.reverse()
# answer = "".join(stList)
# print(answer)

# 방법 2 : slicing
answer = my_string [::-1]
# 방법 3 : reversed(문자열)
answer = "".join(reversed(my_string))
print(answer)

# 최대값 구하기 (for 문 만을 사용)
lista = [100,20,30,5,90]
# 위 리스트의 최대값, 최소값을 정렬함수, 최대값 함수 사용x 구하기
maxa = lista[0]
mina = lista[0]
for i in lista:
    if maxa < i:
        maxa = i
    if mina > i :
        mina = i
print(maxa)
print(mina)

# 방법 2 # max min
maxA = max(lista)
minA = min(lista)

# 방법 3 # sort
lista.sort()
minA = lista[0]
maxA = lista[len(lista)-1]
maxA = lista[-1]
print(minA)
print(maxA)

