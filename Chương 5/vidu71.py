#Viết chương trình nhập vào một dãy số thực x1, x2, …, xn (0 < n < 100), sau đó tìm trung bình cộng các phần tử âm trong dãy mà giá trị nằm trong khoảng (-1000, -10).
n = int(input("Nhập số phần tử n: "))

a = []

for i in range(n):

    x = float(input("Nhập số: "))
    a.append(x)

tong = 0
dem = 0

for i in a:

    if i < -10 and i > -1000:

        tong = tong + i
        dem = dem + 1

if dem > 0:

    tbc = tong / dem

    print("Trung bình cộng =", tbc)

else:

    print("Không có số phù hợp")