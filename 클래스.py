# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(self.name))

    def move(self, location):
        print("지상 유닛 이동")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린", 40 ,1 ,5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


class Tank(AttackUnit):

    seize_developed = False # 시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self,"탱크", 150 ,1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        # 현재 시즈모드가 아닐 때
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드 일때
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False



class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("공중 유닛 이동")
        self.fly(self.name, location)


class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80 , 20 , 5)
        self.clocked = False


    def clocking(self):

        if self.clocked == True:
            print("{0} : 클로밍 모드를 해제합니다..".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹을 합니다.".format(self.name))
            self.clocked = True


def game_start():
    print("[알림] 게임을 시작합니다")
def game_over():
    print("Player : gg")
    print("Player 님이 게임에서 퇴장하셨습니다.")

# 실제 게임 진행

game_start()

m1= Marine()
m2= Marine()
m3= Marine()


t1 = Tank()
t2 = Tank()

w1 = Wraith()

# 유닛 일괄관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동

for unit in attack_units:
    unit.move("11시")

#탱크 시즈모드 개발

Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발 완료")

# 공격 모드 준비 (시즈모드 , 클라킹, 마린 스팀팩)

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격

for unit in attack_units:
    unit.attack("1시")

# 전군 피해
from random import *
for unit in attack_units:
    unit.damaged(randint(5,21)) # 공격은 랜덤으로 받음


game_over()


# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self,name, hp, 0)
#         super().__init__(name, hp, 0)
#         self.location = location

# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
#
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
# def game_over():
#     pass
# game_start()
# game_over()

# 벌쳐
# virture = AttackUnit("벌쳐", 80 , 10 , 20)
# battlecruiser = FlyableAttackUnit("배틀 크루져", 500, 25, 3)
#
# virture.move("11시")
# battlecruiser.move("3")

# 발키리
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# 파이어뱃 :" 공격 유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50,16)
# firebat1.attack("5시")
#
# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# marine1= Unit("마린", 40 ,5) # 마린과 탱크는 유닛클래스의 인스턴스
# marine2= Unit("마린", 40 ,5)
# tank = Unit("탱크", 150, 35)
#
# # 레이스 : 공중 유닛, 비행기 ,클로킹 (상대방에게 보이지않음)
#
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름  : {0}, 공격력 {1}".format(wraith1.name, wraith1.damage))
#
# # 마인드 컨트롤 : 상대방 유닛을 내것으로 만드는 것(빼앗음)
#
# wraith2 = Unit("레이스", 80 ,5)
# wraith2.clocking = True # 클래스 밖에서 해당 클래스의 원하는 변수에대해서 확장가능 ( 해당 객체에만 적용)
#
# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))




