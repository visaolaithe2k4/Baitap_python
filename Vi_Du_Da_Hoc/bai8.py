x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
z = int(input("Nhập z: "))

tich = x * y * z

so_chu_so = len(str(tich))

chu_so_lon_nhat = 0
for ch in str(tich):
    if int(ch) > chu_so_lon_nhat:
        chu_so_lon_nhat = int(ch)

print("Tích x * y * z =", tich)
print("Tích có", so_chu_so, "chữ số")
print("Chữ số lớn nhất là:", chu_so_lon_nhat)