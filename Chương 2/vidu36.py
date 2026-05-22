#Ví dụ nhập chiều dài và chiều rộng hình chữ nhật
from math import *

chieu_dai = int(input("Chiều dài hình chữ nhật: "))
chieu_rong = int(input("Chiều rộng hình chữ nhật: "))

print("Diện tích hình chữ nhật là:",
      chieu_dai * chieu_rong)

chu_vi = (chieu_dai + chieu_rong) * 2

print("Chu vi hình chữ nhật là:",
      chu_vi)