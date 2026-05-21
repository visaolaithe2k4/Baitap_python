#Ví dụ tính tổng các số lẻ nhỏ hơn n
n = int(input("Nhập số tự nhiên n: "))

i = 1
tong = 0

while i < n:
    if i % 2 != 0:
        tong = tong + i

    i = i + 1

print("Tổng các số lẻ nhỏ hơn", n, "là:", tong)