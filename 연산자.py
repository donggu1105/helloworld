#숫자처리함수
from math import *

print(ceil(3.5)) # 4
print(floor(3.3)) # 3
print(round(3.7)) # 4

#랜덤함수
print("##### 랜덤함수 ######")
from random import *

print(random()) # 0부터 1미만의 임의의 수
print(random() * 10) # 0부터 10 미만
print(int(random() * 10)) # 10 미만 정수만
print(int(random() * 10) + 1) # 10이하 정수만
print(randint(1,10))