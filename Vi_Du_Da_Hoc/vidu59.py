#Đếm số chẵn trong dãy
n = int(input("Nhập n: "))
a = []
for i in range(n):
    x = int(input("Nhập số: "))
    a.append(x)
dem = 0
for i in a:
    if i % 2 == 0:
        dem = dem + 1
print("Có", dem, "số chẵn")