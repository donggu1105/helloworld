# try:
#
#     print("나누기 전용 계산기입니다.")
#
#     nums = []
#
#     nums.append(int(input("첫번째 숫자를 입력하세요 :")))
#     nums.append(int(input("두번째 숫자를 입력하세요 :")))
#     nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0],nums[1], nums[2]))
#
# except ValueError:
#     print("에러!")
# except ZeroDivisionError as err:
#     print(err)
# except:
#     print("알수없는 에러가 발생")

# 직접정의하는 에러

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

#
# try :
#     print("한 자리 숫자 나누기 전용 계산기")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("두번째 숫자를 입력하세요 : "))
#
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0} , {1}".format(num1,num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#         print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")
#
# except BigNumberError as err:
#         print("에러가 발생했습니다. 한자리 숫자만 입력하세요.")
#         print(err)
#
# finally:
#     print("계산기를 이용해주셔서 감사합니다.")
class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

chicken = 10
waiting = 1

try:
    while(True):
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))

        if order < 1:
            raise ValueError

        if order > chicken:
            print("재고 부족")
            raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
            break
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order

except ValueError:
        print("잘못된 값을 입력했습니다.")
except SoldOutError :
        pass
