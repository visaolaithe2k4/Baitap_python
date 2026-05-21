a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
s = a + b
print("Tong =", s)
max_digit = 0
while s > 0:
    digit = s % 10
    if digit > max_digit:
        max_digit = digit
    s //= 10
print("Chu so lon nhat trong tong la:", max_digit)