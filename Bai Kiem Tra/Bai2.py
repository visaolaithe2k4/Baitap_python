n = int(input("Nhap n: "))
tong = 0
while n > 0:
    tong += n % 10
    n //= 10
if tong % 3 == 0:
    print("Tong cac chu so chia het cho 3")
else:
    print("Tong cac chu so khong chia het cho 3")