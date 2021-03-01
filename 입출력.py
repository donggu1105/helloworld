print("Python", "Java", "Javascript", sep=" vs ", end="?") # separator
print("무엇이 더 재밌을까요?") # end 한문장으로 출력하고 ?로 끝낸다
#
# import sys
# print("Python", "Java", file=sys.stdout) # 표준출력으로
# print("Python", "Java", file=sys.stderr) # 표준에어로 뽑음

scores = {"수학" : 0, "영어":50, "코딩":100}
for subject , score in scores.items():
    print(subject.ljust(8),score) # 왼쪽에 8개의 공간을 넣고 왼쪽정렬을 해라
    print(subject, str(score).rjust(4), sep=":")  # 오른쪽 정렬을 하는데 4칸의 공간을 확보


# 은행 대기순번표
for number in range(1,21):
    print("대기번호 : "+ str(number).zfill(3)) # 3칸의 공간을 확보하는데 빈공간은 0으로 채우기

# answer = input("정답을 입력하세요 : ")
# print("입력하신 값은 "+ answer + "입니다.")


######## 다양한 출력포맷 ########


# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일때는 +로 표시 , 음수일때는 -로 표시 (주식할때 보통 이렇게 표시)
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000))
# 3자리 마다 콤마를 찍어주기, +,- 부호도 붙이기
print("{0:+,}".format(100000000))
# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
#돈이 많으면 행복하니까 빈자리는 ^로 채워주기
print("{0:^<+30,}".format(10000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소주점 특정 자리수까지만 표시
print("{0:.3f}".format(5/3)) # 3자리까지표시 4자리에서 반올


########## 파일 입출력 #########
# score_file = open("score.txt", "w", encoding="utf8") # 파일이름 , 쓰기위한 목적으로 열겠다, 마지막으로 인코딩정보
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()


# score_file = open("score.txt", "a", encoding="utf8") # a 는 append 계속 이어쓰기하고싶어
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()


# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동, end=""는 한줄로 표시
# print(score_file.readline()) # 줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) # 줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) # 줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) # 줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
# score_file.close()

# line을 잘 모를때 while로 다뽑아오기
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
#
# score_file.close()


# 라인을 리스트로 받아서 출력하
# score_file = open("score.txt", "r", encoding="utf8")
#
# lines = score_file.readlines()
#
# for line in lines:
#     print(line, end="")
#
# score_file.close()



######## pickle ########
# 프로그램상에서 사용하고있는 데이터를 파일형태로 저장하는건데 그 파일을 누군가에 주면 그파일을 열어서(피클을 이용해서) 코드에서 또 사용가능

import  pickle
# profile_file = open("profile.pickle", "wb") # write binary 피클을 쓰기위해서는 항상 binary를 설정해줘야함
# profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()


# pickle에서 데이터 가져오기
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()


######### with ########

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))


# with open("study.txt", "w", encoding="utf8") as study_file:
#         study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())



## Quiz

# for week in range(1,51):
#     with open(str(week) +"주차 보고서", "w") as file:
#         file.write(str(week)+"주차 주간보고")
#         file.write("부서 :")
#         file.write("이름 :")
#         file.write("업무요약 :")
