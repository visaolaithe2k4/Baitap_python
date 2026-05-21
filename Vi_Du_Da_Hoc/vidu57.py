#Tìm số lớn nhất trong dãy
n = int(input("Nhập số phần tử: "))

a = []

for i in range(n):
    x = int(input("Nhập số: "))
    a.append(x)

maxx = max(a)

print("Dãy số:", a)
print("Số lớn nhất:", maxx)