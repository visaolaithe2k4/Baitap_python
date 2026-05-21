#Ví dụ module math
import math

def can_bac_hai(x):
    return math.sqrt(x)

def binh_phuong(x):
    return x ** 2

def chu_vi_hcn(a, b):
    return (a + b) * 2


print("Căn bậc hai của 25:",
      can_bac_hai(25))

print("Bình phương của 6:",
      binh_phuong(6))

print("Chu vi hình chữ nhật:",
      chu_vi_hcn(4, 5))