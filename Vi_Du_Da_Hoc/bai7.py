def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input("Nhập n: "))

while n <= 0 or n >= 100:
    n = int(input("Nhập lại n, điều kiện 0 < n < 100: "))

ds = []

for i in range(n):
    x = int(input(f"Nhập x{i + 1}: "))
    ds.append(x)

tong = 0

for x in ds:
    if la_so_nguyen_to(x):
        tong += x

print("Tổng các số nguyên tố trong dãy là:", tong)

if tong % 2 != 0 and tong > 50:
    print("Tổng là số lẻ và lớn hơn 50")
else:
    print("Tổng không phải là số lẻ và lớn hơn 50")