# 리스트 []

# 지하철 칸별로 10명 , 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10,20,30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇번째 칸에 타고잇는가?
print(subway.index("조세호")) # 1번에 위치

# 하하씨가 다음 정류장에서 다음칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석과 조세호사이에 넣어라

subway.insert(1, "정형돈")
print(subway)

# 지하철에있는 사람을 한명씩 뒤에서 꺼냄

# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇명있는지 확인

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능

num_list = [5,2,3,4,1]
num_list.sort()
print(num_list)


# 순서 뒤집기 가능

num_list.reverse()
print(num_list)

# 모두 지우기

num_list.clear()
print(num_list)


# 다양한 자료형 함께 사용
num_list = [2,3,43,2,3]
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

############### 사전 ###############
print("#################### 사전 ################")

cabinet = {3:"유재석", 100:"김태호"}  # key-value
print(cabinet)
# 값 가져오기 방법 1
print(cabinet[3])
print(cabinet[100])

# 값 가져오기 방법 2
print(cabinet.get(3))
print(cabinet.get(5))
print(cabinet.get(5, "사용가능"))

print(3 in cabinet) # 3키가 캐비넷에 있느냐

# 키가 정수가 아니라 str도 가능

cabinet = {"A-3":"유재석", "B-100" : "김태호"}

print(cabinet["A-3"])
print(cabinet.get("A-3"))

# 새 손님
print(cabinet)

cabinet["A-3"] = "김종국"
cabinet["C-29"] = "조세호"
print(cabinet)

# 간 손님

del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())
# value 들만 출력
print(cabinet.values())
# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)

############### 튜플 ###############
print("#################### 튜플 ################")

#변경되지않는 목록을 이용할때 튜플 사용

menu = ("돈까스", "치즈까스")
print(menu)
print(menu[0])
print(menu[1])


name = "김종국"
age = 20
hobby = "코딩"
print(name,age,hobby)

# 튜플 사용하는 예제
(name , age , hobby) = ("김종국", 20 ,"코딩")

############### 세트 ###############
print("#################### 세트 ################")

# 집합 (set)
# 중복 안됨 , 순서 없음

my_set = {1,2,3,4,5}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (자바 파이썬 둘다 가능한 사람)
print(java & python)
print(java.intersection(python))

# 합집합 (java 도 할수있거나 python도 할수있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할줄알지만 python은 할줄모르는 개발자)
print(java - python)
print(java.difference(python))

# python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java를 잊었어요
java.remove("김태호")
