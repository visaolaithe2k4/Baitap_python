m = int(input("Nhap m: "))
n = int(input("Nhap n: "))
tong = 0
so_tam = n
while so_tam > 0:
    tong += so_tam % 10
    so_tam //= 10
print("Tong cac chu so cua n =", tong)
if m % tong == 0:
    print("m chia het cho tong cac chu so cua n")
else:
    print("m khong chia het cho tong cac chu so cua n")