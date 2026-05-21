#Ví dụ tìm max của 3 số
a = float(input("Nhập số thứ 1: "))
b = float(input("Nhập số thứ 2: "))
c = float(input("Nhập số thứ 3: "))

max_value = a

if b > max_value:
    max_value = b

if c > max_value:
    max_value = c

print("Số lớn nhất là:", max_value)