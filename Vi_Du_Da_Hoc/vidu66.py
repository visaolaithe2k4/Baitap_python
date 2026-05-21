#Tính giai thừa
n = int(input("Nhập n: "))

gt = 1

for i in range(1, n + 1):
    gt = gt * i

print("Giai thừa =", gt)