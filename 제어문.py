# weather = input("오늘 날씨는 어때요?")
# # if 조건:
# #     실행 명령문
#
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요없어요")


# temp = int(input("기온은 어떄요?"))
#
# if 30 <= temp:
#     print("너무 더워요 나가지마세요")
# elif 10 <= temp or temp > 30:
#     print("괜찮은 날씨에요")


##### 반복문 ######

for waiting_no in [0,1,5,6,4]:
    print("대기번호 : {0}".format(waiting_no))

for wait_no in range(1,6): # start - end
    print("내가만듬 : {0}".format(wait_no))

startbucks = ["아이어맨", "그루트", "토르"]

for customer in startbucks:
    print("{0} 손님 커피가 준비되었습니다.".format(customer))


#### while ####

customer = "토르"
index = 5

while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

#
# customer = "아이언맨"
# index = 1
# while True :
#     print("{0}, 커피가 준비 되었습니다. 호출 {1}회.".format(customer, index))
#     index += 1
#
# customer = "토르"
# person = "Unknown"
#
# while person != customer :
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")


#### continue / break #######

absent = [2,5] # 결석
no_book = [7] # 책 안가져옴
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("{0}야 너때문에 오늘 수업은 여기까지다 오늘 좀 혼나자".format(student))
        break
    else:
        print("{0}야 책을 읽어봐".format(student))


#### 한줄 for #####

# 출석번호가 1, 2, 3, 4 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1,2,3,4,5]
students = [i+100 for i in students]
print(students)

# 학생이름을 길이로 변환

students = ["Iron man", "Thor", "I am groot"]
students = [len(student) for student in students]
print(students)

students = ["joey", "brad", "alice", "jihyeon"]
students = [student.upper() for student in students]
print(students)


##### Quiz
from random import *

cnt = 0 # 총 탑승 승객
for i in range(1,51): # 1 ~ 50 이라는 수 (승객)
    time = randrange(5, 51) # 5분 ~ 50분 소요시간
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 () (소요시간 : {1}분)".format(i,time))
        cnt += 1
    else:
        print("[X] {0}번째 손님 () (소요시간 : {1}분)".format(i,time))


print("총 탑슴승객수 :"+str(cnt))