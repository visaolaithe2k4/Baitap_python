# Đọc file
f = open("input.txt", "r", encoding="utf-8")
noi_dung = f.read()
f.close()

out_so = ""
out_chu = ""

# Duyệt từng ký tự
for ky_tu in noi_dung:
    if ky_tu.isdigit():
        out_so += ky_tu
    elif ky_tu.isalpha():
        out_chu += ky_tu

# Ghi file số
f = open("output_so.txt", "w", encoding="utf-8")
f.write(out_so)
f.close()

# Ghi file chữ
f = open("output_chu.txt", "w", encoding="utf-8")
f.write(out_chu)
f.close()

print("Đã tạo 2 file: output_so.txt và output_chu.txt")