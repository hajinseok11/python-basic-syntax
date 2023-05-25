# 파일명: dictionary.py
# tuple
# tuple은 변경불가능한 자료형으로써, ()를 통해 표현
t1 = (1,2,'a','b')
print(t1)
# 인덱싱, 슬라이싱 둘 다 리스트와 동일하게 허용
print(t1[0])
# 삭제, 변경 불가
# del t1[0]
print(t1)
# 튜플을 사용하는 이유는 개발자가 해당 자료를 수정하지 못하도록
# 강제적으로 지정한 것.
# 리스트에 비해 메모리 효율적


# dictionary
dic1 = {'이름':'홍길동','나이':25,'성별':'남'}
# 자료구조는 key와 value로 이루어져있다.
# 영어사전에서 단어와 뜻으로 이루어져있는 것에서 유래
# 다른 language의 map 또는 hashmap과 유사한 자료형
# json이라는 자료형태와도 유사하다

# dictionary의 특징 1
# key는 중복이 불가 
# value는 다른 key에도 존재할 수 있다 (중복 가능).
dic1 = {'이름':'홍길동','나이':25,'성별':'남','성별':'여'}
result = {'1':80,'2':90,'3':100,'4':10}
print(result)
print(dic1) # 해시함수를 사용하여 같은 key값에는 값을 덮어버림 -> 중복시 앞의 것 삭제

# dictionary의 기본호출 방식은 변수명[key], 변수명.get(key)
print(dic1['나이'])
print(dic1.get('나이'))

# 리스트는 a = [value,...] 
# 딕셔너리는 a = {key:value,...} 튜플은 a = (value,...)
# 딕셔너리와 튜플은 a[index], 딕셔너리는 a[key]

# dictionary의 특징 2
# key와 value로 이루어져 있다보니, 순서가 의미가 없다. index로 접근 불가
# key를 가지고 value 검색할 때 해시함수를 통해 index를 찾다보니
# 매우 빠른 속도를 보장한다.
dic1 = {'이름':'홍길동','나이':25,'성별':'남','성별':'여'}
# key:value 추가
dic1['신분'] = '학생'
print(dic1)

# 딕셔너리에서 키를 이용한 key:value 삭제
del dic1['성별']
print(dic1)

# 딕셔너리에서 key 목록만을 뽑아낼 때
# iterable한 상태로 data가 뽑아져 나오므로 for문 사용가능
keyList = dic1.keys()
print(keyList)
# 위의 keyList에서 각각의 값을 출력해보자.
for k in keyList:
    print(k)
    # key값을 출력해주는 for문 안에서 value도 같이 출력
    print(dic1[k])
# value 목록을 뽑아낼 때는 .values()를 사용
valuelist = dic1.values()
for v in valuelist:
    print(v)

# 위의 for문을 활용해서, key가 담긴 list를 만들고, value가 담긴 list를 만들어 출력
tempList1 = []
tempList2 = []
for k in keyList:
    tempList1.append(k)
    tempList2.append(dic1[k])
print(tempList1)
print(tempList2)

# 딕셔너리의 확장 : update 함수
dic1 = {"a":1,"b":2,"c":3}
dic2 = {"a":2,"d":4,"f":5}
dic1.update(dic2)
print(dic1)


# 딕셔너리로 변환해서 출력
lista = ['A','A','B','O','O','AB','AB']
dicta = {}
# dict에 'A':2를 어떻게 세팅하지?
for a in lista:
    if a not in dicta.keys():
        dicta[a] = 1
    else:
        dicta[a] += 1
print(dicta)    # {'A': 2, 'B': 1, 'O': 2, 'AB': 2}

# 방법2
if a not in dicta.keys():
    dicta[a] = lista.count(a)
print(dicta)    # {'A': 2, 'B': 1, 'O': 2, 'AB': 2}
