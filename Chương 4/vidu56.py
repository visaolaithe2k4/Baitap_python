#Nhập dãy số và tính tổng
n = int(input("Nhập số phần tử: "))

a = []

for i in range(1, n + 1):
    x = int(input("Nhập số: "))
    a.append(x)

tong = sum(a)

print("Danh sách:", a)
print("Tổng =", tong)
