def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return  balance - money

    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money): #저녁에 출금하면 수수료
    commission = 100
    return commission, balance - money - commission # 튜플형식으로 보내기


balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance,500)
print("수수료 : {0}이며 잔액은 {1}원 입니다.".format(commission, balance))


# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
#           .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")


############## 기본 값 #############
# 같은 학교 같은 학년 같은 반 같은 수업

def profile(name, age = 17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
          .format(name, age, main_lang))

profile("유재석")
profile("김태호")


############# 키워드 값 ##############

profile(age = 18, main_lang="123", name="강동현")

def profile2(name, age, *language) :
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
    for lang in language:
        print(lang, end=" ")
        print()
profile2("유재석", 20, "Python", "Java", "C", "C++","C#")
profile2("김태호", 25, "Kotlin", "Swift","","","")

# 지역변수 , 전역변수

gun = 10

def checkpoint(soldirers):
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldirers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 :{0}".format(gun))
checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))


# Quiz

def std_weight(height, gender):

    if gender == "M":
        print("키 "+ str(height) + "m 남자의 표준 체중은 " \
            + str(round(height*height*22, 2))+ "kg 입니다.")
    else:
        print("키 " + str(height) + " 여의 표준 체중은 " \
              + str(round(height * height * 21)) + "kg 입니다.")


std_weight(1.83, "M")