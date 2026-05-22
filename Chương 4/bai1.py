# Viết chương trình đọc tệp input.txt/dat bao gồm mỗi dòng là 1 số tự nhiên, chương trinh này
# sẽ đưa ra kq ở output.txt
# bao gồm n dòng mỗi dòng lần lượt là các ước số nguyên tố khác nhau

import os

def uoc_nguyen_to_khac_nhau(n):
    uoc = []

    if n % 2 == 0:
        uoc.append(2)
        while n % 2 == 0:
            n //= 2

    i = 3
    while i * i <= n:
        if n % i == 0:
            uoc.append(i)
            while n % i == 0:
                n //= i
        i += 2

    if n > 2:
        uoc.append(n)

    return uoc


# Lấy đúng thư mục chứa file bai1.py
thu_muc_hien_tai = os.path.dirname(os.path.abspath(__file__))

input_path = os.path.join(thu_muc_hien_tai, "input.txt")
output_path = os.path.join(thu_muc_hien_tai, "output.txt")

with open(input_path, "r", encoding="utf-8") as f_in, open(output_path, "w", encoding="utf-8") as f_out:
    for line in f_in:
        line = line.strip()
        if line:  # bỏ qua dòng trống
            n = int(line)
            kq = uoc_nguyen_to_khac_nhau(n)
            f_out.write(" ".join(map(str, kq)) + "\n")

print("Đã ghi kết quả vào output.txt")