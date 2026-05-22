#Tính trung bình cộng
n = int(input("Nhập n: "))

a = []

for i in range(n):
    x = int(input("Nhập số: "))
    a.append(x)

tb = sum(a) / n

print("Trung bình cộng =", tb)