#Ma trận 2 chiều
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

a = []

for i in range(m):

    row = []

    for j in range(n):

        x = int(input("Nhập phần tử: "))
        row.append(x)

    a.append(row)

print("Ma trận:")

for i in a:
    print(i)