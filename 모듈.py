# import theater_module
#
# theater_module.price(3)
# theater_module.price_morning(3)
# theater_module.price_soldier(5)

# import theater_module as mv
#
# mv.price(3)
# mv.price_morning(5)
# mv.price_soldier(2)

# from theater_module import *
#
# price(3)
# price_soldier(5)
# price_morning(4)

# 명시적으로 어떤 함수를 쓸지 결정가능
# from theater_module import price, price_morning
#
# price(3)
# price_morning(123)

# from theater_module import price_soldier as price
#
# price(3)

# import travel.thailand
#
# trip_to = travel.thailand.ThailandPackage()
#
# trip_to.detail()
#
from travel import vietnam
#
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import *
# from travel import *
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# import inspect
# import random
#
# print(inspect.getfile(random))
# print(inspect.getfile(vietnam))


# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


# dir : 어떤 객체를 넘겨줬을떄 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
import random
import pickle
print(dir(random))

list = [1,2,3]
print(dir(list))

name = "Joey"
print(dir(name))


# glob : 경로 내의 폴더 / 파일목록 조회

import glob

print(glob.glob("*.py")) # 확장자가 .py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os
# print(os.getcwd())
#
# folder = "sample.dir"
#
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print("폴더 삭제완료")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성했습니다.")

print(os.listdir())

import time # 시간관련함수

print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime

print("오늘 날짜는 ", datetime.date.today())


# timedelta :  두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은 ", today+td)


# Quiz

import byme

me = byme.Idid()
me.sign()