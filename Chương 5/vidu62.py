#Kiểm tra số nguyên tố bằng hàm
def nguyento(n):

    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


x = int(input("Nhập số: "))

if nguyento(x):
    print(x, "là số nguyên tố")
else:
    print(x, "không là số nguyên tố")