#Viết chương trình nhập vào một dãy số nguyên x1, x2, …, xn (0 < n < 200), tính tổng các phần tử chẵn trong dãy, và kiểm tra xem tổng này có chia hết cho 7 và nhỏ hơn 200 hay không.
n = int(input("Nhập số phần tử n: "))

a = []

for i in range(n):

    x = int(input("Nhập số: "))
    a.append(x)

tong = 0

for i in a:

    if i % 2 == 0:

        tong = tong + i

print("Tổng các số chẵn =", tong)

if tong % 7 == 0 and tong < 200:

    print("Tổng chia hết cho 7 và nhỏ hơn 200")

else:

    print("Không thỏa điều kiện")