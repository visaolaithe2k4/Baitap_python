#Tìm số nhỏ nhất
n = int(input("Nhập số phần tử: "))

a = []

for i in range(n):
    x = int(input("Nhập số: "))
    a.append(x)

minn = min(a)

print("Số nhỏ nhất:", minn)