import datetime

# 1
print("Hello World")
# 2
print("Mary\'s cosmetics")
# 3 x (소수점 둘째짜리까지 표현하기)
digit = 3.141592
print("%.2f" % digit)
print("%.4f" % digit)
# 4
# first = input("첫번째 숫자를 입력하세요")
# second = input("두번째 숫자를 입력하세요")
# print(int(first) + int(second))
# 5
# str = input("출력하고싶은 문자열을 입력하세요")
# count = input("몇번 반복할겁니까?")
# for i in range(int(count)):
#     print(str)
# 6
# string1 = "720"
# int1= 100
# print(type(int(string1)))
# print(type(str(int1)))
# #7
# a = input()
# b = input()
#
# print("덧셈 : a + b = {}".format(int(a)+int(b)))
# print("빼기 : a + b = {}".format(int(a)-int(b)))
# print("곱하기 : a + b = {}".format(int(a)*int(b)))
# print("나누기 : a + b = {}".format(int(a)/int(b)))
# 8
# a = input("첫번째 숫자를 입력하세요")
# b = input("두번쨰 숫자를 입력하세요")
# print("a의 b승은 {}".format(int(a)**int(b)))
# # 11
# a = int(input("첫번쨰 숫자를 입력하세요"))
# b = int(input("두번쨰 숫자를 입력하세요"))
#
# print("{0} / {1} = {2:0.2f}".format(a, b, a/b))

names = ["보라", "영희", "철수"]
nums = [15, 20, 49]

for name, num in zip(names, nums):
    print(f"Hi I am {name}, and also {num}")

x = 10
y = 3

print(f"x + y = {x+y} | x / y = {x/y}")

date = datetime.datetime.now()
print(f"{date:%Y-%m-%d} is on a {date:%A}")