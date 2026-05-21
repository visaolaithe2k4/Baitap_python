# Viết chương trình nhập vào 2 số nguyên dương a và b, sau đó kiểm tra xem a có chia hết cho chữ số nhỏ nhất của b hay không.
# Ví dụ: a = 24, b = 582, chữ số nhỏ nhất của b là 2, và 24 chia hết cho 2
# Viết chương trình nhập vào 2 số nguyên dương m và n, sau đó tính tổng (a+b) và tìm ra chữ số lớn nhất trong tổng đó.

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

minn = 9
tam = b

while tam > 0:

    so = tam % 10

    if so < minn:
        minn = so

    tam = tam // 10

print("Chữ số nhỏ nhất của b là:", minn)

if minn != 0 and a % minn == 0:
    print(a, "chia hết cho", minn)
else:
    print(a, "không chia hết cho", minn)