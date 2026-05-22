#Đếm số nguyên tố nhỏ hơn n
n = int(input("n = "))

s = 0

for i in range(1, n):
    ktra = 0

    for j in range(2, i):
        if i % j == 0:
            ktra = 1

    if ktra == 0:
        s = s + i

print("Tổng các số nguyên tố là:", s)