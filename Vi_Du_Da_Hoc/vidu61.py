#Ghi dãy số vào file
f = open("dayso.txt", "w", encoding="utf-8")

n = int(input("Nhập số phần tử: "))

for i in range(n):
    x = input("Nhập số: ")
    f.write(x + "\n")

f.close()

print("Đã ghi file")