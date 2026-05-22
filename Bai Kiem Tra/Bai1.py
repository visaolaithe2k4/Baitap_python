n = int(input("Nhap so phan tu n: "))
ds = []  
for i in range(n):
    so = float(input("Nhap so: "))
    ds.append(so)
tong = 0
dem = 0
for so in ds:
    if so > 0 and so < 1000:
        tong = tong + so
        dem = dem + 1
if dem > 0:
    tbc = tong / dem
    print("Trung binh cong =", tbc)
else:
    print("Khong co so nao thoa man")