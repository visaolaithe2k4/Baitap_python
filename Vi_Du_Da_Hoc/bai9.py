a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

tong = a + b + c

dem_chan = 0

for ch in str(tong):
    if int(ch) % 2 == 0:
        dem_chan += 1

print("Tổng a + b + c =", tong)
print("Trong tổng có", dem_chan, "chữ số chẵn")