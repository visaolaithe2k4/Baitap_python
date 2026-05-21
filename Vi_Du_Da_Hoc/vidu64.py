#Tính tổng ma trận
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

a = []

for i in range(m):

    row = []

    for j in range(n):

        x = int(input("Nhập phần tử: "))
        row.append(x)

    a.append(row)

tong = 0

for i in range(m):
    for j in range(n):
        tong = tong + a[i][j]

print("Tổng =", tong)