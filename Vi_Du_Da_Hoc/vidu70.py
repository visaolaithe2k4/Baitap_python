#Viết chương trình nhập vào 2 số nguyên dương m và n, sau đó tính tổng (m+n) và tìm ra chữ số lớn nhất trong tổng đó.
m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

tong = m + n

print("Tổng =", tong)

maxx = 0
tam = tong

while tam > 0:

    so = tam % 10

    if so > maxx:
        maxx = so

    tam = tam // 10

print("Chữ số lớn nhất là:", maxx)