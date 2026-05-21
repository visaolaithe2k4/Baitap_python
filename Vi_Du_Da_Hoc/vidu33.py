#Ví dụ đọc file và tính tổng ma trận
f = open("e:\\matran.txt", "r")

ma = []

for dong in f.readlines():
    ma.append(dong.split())

print(ma)

s = 0

for subma in ma:
    for j in subma:
        s = s + float(j)

print("Tổng ma trận =", s)

f.close()
