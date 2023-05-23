# 문자열 관련 주요 함수
# count : 대상 문자열에 지정한 문자가 몇개가 있는지 출력하는 함수
a = "python"
print(a.count('o'))

# find : 대상 문자열에서 지정한 문자가 몇번째 index에 있는지 찾는 함수
# index : find와 같은 기능
print(a.find('o'))
print(a.index('o'))

# 없는 문자를 찾을 때는 -1 return
print(a.find('x'))

whatyouwant = input('아무런 문자나 입력해주세요')
search = input('찾고자하는 문자 1개만 입력해주세요')
result = whatyouwant.find(search)
if result == -1:
    print("찾고자 하는 값이 없습니다.")
else:
    print("요청하신 문자는 %d 번째에 있습니다." % result)

# 대소문자 변경 : upper / lower()
a = "hello"
print(a.upper())
b = "HELLO"
print(b.lower())

# 문자열 양쪽 공백을 없애는 함수 : strip()
a = "   hello world     "
print(a.strip())
myId = (input("id를 입력해주세요")).strip()   # abc@naver.com
myPw = input("비밀번호를 입력해주세요")
print("ID는 "+ myId+"이고"+ "비밀번호는"+myPw)

# 문자열 대체 : replace()
a = 'I studied python'
print(a.replace('python','java'))

# 공백을 기준으로 문자를 자르는 함수: split()
a = "I studied python"
b = a.split(" ")
print(b)

a = "I    studied    python"
b = a.split(" ")
c = a.split()
print(b)
print(c)

a = "I:studied:python"
b = a.split(":")
print(b)

x = int(input('x값 입력'))
y =2.5*pow(x,2)+3.3*x+6
print(y)

# word1 word2 word3
a = input('첫번째 문자를 입력해주세요')
b = input('첫번째 문자를 입력해주세요')
c = input('첫번째 문자를 입력해주세요')
abc = a[0] + b[0] + c[0]
print(abc)