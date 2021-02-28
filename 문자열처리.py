#슬라이싱
jumin = "990120-1234567"

print("성별 : "+ jumin[7])
print("몇년생 : "+ jumin[0:2]) # 0 ~ 2 직전까지 (하나 더해야함) 기억
print("월정보 :" + jumin[2:4])
print("일 정보 : "+ jumin[4:6])

print("생년월일 : "+ jumin[:6]) # 처음부터 6 직전까지
print("뒤에 일곱자리 : "+ jumin[7:]) # 7부터 끝까
print("뒤부터 세기 : "+ jumin[-7:]) # 뒤로부터세기 -7부터 끝까지


#문자열 처리함수
print("########## 문자열 처리함수 ############")

python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper()) # 몇번째 자리 대문자
print(len(python)) # 길이반환
print(python.replace("Python", "Java")) # 문자 찾은뒤 새로운 문자열로 대체


index = python.index("n")
print(index) # "?" 안에 든거 index알려줌
index = python.index("n", index + 1) # index+1이 시작위치 => 그 뒤로나오는 n을 찾는다
print(index)

print(python.find("n")) # 찾아서 인덱스 반환
print(python.find("Java")) # 없으면 -1 반환
# print(python.index("Java")) # 하면 오류

#문자열 포맷
print("########## 문자열 포맷 ############")

print("a" + "b")
print("a", "b")

#방법 1
print("나는 %d살입니다."  % 20) #정수만
print("나는 %s을 좋아해요" % "파이썬") # str
print("Apple 은 %c로 시작해요" % "A") # character

# %s 는 정수던 문자열이던 상관 X
print("나는 %s살입니다." % 20)
# 두개 이상
print("나는 %s색과 %s색을 좋아해요." %("파랑", "빨강"))


#방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파랑", "빨강"))
print("나는 {0}색과 {1}색을 좋아해요".format("파랑", "빨강"))
print("나는 {1}색과 {0}색을 좋아해요".format("파랑", "빨강"))

#방법 3
print("나는 {age}살이며 , {color}색을 좋아해요".format(age = 20, color = "빨강"))


#방법 4
age = 20
color = "빨강"
print(f"나는 {age}살이며 , {color}색을 좋아해요!!!!") # 변수로 저장된 값을 사용할수있음