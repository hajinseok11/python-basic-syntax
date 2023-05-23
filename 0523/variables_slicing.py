# 문자열의 슬라이싱
# 슬라이싱이란 문자열을 잘라내는 것을 의미
# 대상변수[x:y] : x이상 y 미만의 index를 가진 문자열을 잘라낸다
a = 'python is fun'
# python만 잘라내서 b에 담아 출력해주세요
b = a[0:6]
print(b)
# x, y 자리에 값이 없으면 처음부터 또는 끝까지를 의미
# 6 번째 문자부터 끝까지 잘라내서 변수 b에 담아 출력
b = a[6:]
print(b)

# a[x:y:z] 여기에서 z는 z-1 개씩 건너뛰고
# 2번째 이상 7번째 미만 문자열 중에 1개씩 건너뛰고 b에 담아 출력
b = a[2:7:2]
print(b)

A = '20220505children\'s_day'
date = A[0:8]
day = A[8:]
print(date)
print(day)