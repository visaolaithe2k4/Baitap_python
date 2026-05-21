n = int(input("Nhập số phần tử n: "))
arr = []

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(x)

with open("dulieu.txt", "w", encoding="utf-8") as f:
    for x in arr:
        f.write(str(x) + " ")

print("Đã ghi dữ liệu vào file dulieu.txt")

doi_tuong_file.readlines