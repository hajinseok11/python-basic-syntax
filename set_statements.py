# set은 집합(수학)이라고 부르기도 한다.
# set의 특성은 딕셔너리와 마찬가지로 index가 없고, 중복이 없다.
s1 = {'이름','나이','성별'}
# list의 중복을 제거하기 위해서 list를 가지고 set으로 형변환 시키는 방식 많이 사용
s1 = set(['이름','이름','나이','성별'])
# 집합의 개수 구하는 함수 : len
print(len(s1))
print(s1)
s2 = set('test')
print(s2)

# index로 접근 불가
# print(s1[0])

lista = ['A','A','A','B','B','AB','O']
setA = set(lista)
print(len(set(lista)))
# 이 반 학생들의 혈액형 종류는 총 몇개인가?
# A, B, AB, O -> 총 4개

# setA의 값을 하나씩 출력 하려면?
for a in setA:
    print(a)

# 합집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8])
# s3 = s1 | s2  프로그래밍에서 "|" 기호는 or(또는)를 의미한다.
s3 = s1.union(s2)
print(s3)

# 프로그래밍에서 &은 일반적으로 and(그리고)를 의미
# 앰퍼샌드라고 부른다.
s3 = s1 & s2
s3 = s1.intersection(s2)
print(s3)

# s2에서 s1을 뺀 차집합
# -, difference
print(s2-s1)
print(s2.difference(s1))

# 집합에서 값 추가 : add()
s1 = {1,2,3,4,5,6}
# 7을 추가한 다음에 s1출력
s1.add(7)
print(s1)

# 값 여러개 추가시 update함수 (딕셔너리와 동일)
s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
s1.update(s2)
print(s1)

# set값 삭제 시 remove,discard 함수 사용 
s1 = {1,2,3,4,5,6}
# discard: remove와 달리 삭제할 값이 존재하지 않아도 에러가 발생하지 않음
s1.remove(6)
s1.discard(5)
s1.discard(6)
print(s1)

# boolean (불형) 타입
# : in(또는 not in) 뒤에 iterable한 자료형이 나온다
# a in lista, a not in lista, a in dicta, a in seta

# 비어있는 값들은 거짓, 값이 들어있으면 참이다.
listA = [1,2,3]
while listA:
    print('참입니다.')
    listA.pop()
# 숫자 1은 참, 0은 거짓