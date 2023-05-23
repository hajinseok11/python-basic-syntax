# 문자열 포맷팅이란 문자열 중간에 특정 문자(또는 숫자 등)를 삽입하는 방식.
# %s : 문자열, %d : 정수, %f : 실수
a = "I studied %s %d times" % ("python", 2)
print(a)

# 포맷팅을 왜 쓰는가? 
# 1) 문자열을 직접 삽입하면 1회성으로 coding할 수 밖에 없지만, 포맷팅은 변수값을 삽입할 수 있다.
# 2) 따옴표를 여러번 안닫아도 된다.

language = input("좋아하는 언어를 입력하세요")
times = input("그 언어를 몇번이나 공부하셨나요")
a = "I studied %s very hard %d times" %(language,int(times))
print(a)

# # 아래와 같이 코딩하면 따옴표로 열고 닫고를 너무 많이해서 귀찮다.
# a = "I studied" + language + "very hard" + str(times) + "times"
# print(a)

# my age is %d, and weight is %f kg
age = int(input("나이가 몇살이신가요?"))
weight = float(input("몸무게가 몇 킬로그램이신가요?"))
print("my age is %d, and weight is %.2f kg" % (age,weight))
