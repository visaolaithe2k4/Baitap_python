n = int(input("Nhap n: "))
tich = 1
while n > 0:
    tich *= n % 10
    n //= 10
if tich % 2 == 0 and tich > 20:
    print("Tich cac chu so la so chan va lon hon 20")
else:
    print("Khong thoa man")