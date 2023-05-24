# for 문의 기본구조
# for 변수 in 반복가능한 자료형(iterable)
#   실행문
lista = [1,2,3,4,5,6,7,8,9,10]
for a in lista:
    # a = 1, a = 2, a = 3, a = 4  .....
    print(a)

# range 문법 : range(x,y) x이상 y미만
for a in range(1,101):
    print(a)