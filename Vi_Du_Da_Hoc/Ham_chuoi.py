lst = [1,2]
lst  += ['one', 'tow']
print(lst)

lst = list('KTER') *2
print(lst)

lst = list([1,2]) *2
print(lst)

#thay đổi nội dung list


#hàm len() ;: trả về số phần tử list

list1 =[123,'abc','xyz']
list2 = ['java','python','php']
print("độ dài list 1 :", len(list1)) 
print("độ dài list 2 :", len(list2)) 

#hàm max: trả về phần tử có giá trị lớn nhất trong list 
#cú pháp : max(list)
list1 = ['123','abc','xyz','def']
list2 = [222,333,111]
print("phần tử có giá trị lớn nhất:", max(list1)) 
print("phần tử có giá trị lớn nhất:", max(list2)) 
print("phần tử có giá trị lớn nhất:", min(list2)) 


#Hàm xử lý list : chuyển đổi 1 tuple thành list
#hàm list : list(seq)
aTuple = ('123','abc','xyz','def')
aList = list(aTuple)
print("Cac phan tu cua Tuple la :", aTuple)
print("Cac phan tu cua List la :", aList)


#phương thức append() : thêm cuối danh sách
# cú pháp : list.append(obj)

Pist1 = ['java','python','c++']
print(" Phan tu cua list truoc khi them",Pist1)
Pist1.append('php')
print(" Phan tu cua list sau khi them",Pist1)

#phương thức count() : đếm đối tượng xuất hiện bao nhiêu lần
# cú pháp : list.count(obj)

p1 = ['java','python','c++','python','python']
print(' số lần xuất hiện chữ python là', p1.count('python'))
print(' số lần xuất hiện chữ java là', p1.count('java'))

#phương thức extend() : thêm các nội dung của seq vào cuối list 
# cú pháp : list.extend(seq)

a1 = ['java','python','c++']
a2 = ['c++','spl','html']
a1.extend(a2);
print('List sau khi được mở rộng mà: ', a1)

#phương thức index() : trả về vị trí của obj xuất hiện
# cú pháp : list.index(obj)
a3 = ['java','python','c++']
print('chỉ mục của python là :',a3.index('python'))

#phương thức insert() : trả về vị trí của obj xuất hiện
# cú pháp : list.insert(obj)

a4  = ['java','python','c++','php','spl']
a4.insert(3,'androi')
print('list sau khi được chèn :' ,a4)

#pop() : xóa phần tử chỉ mục index ra khỏi danh sách
# list.pop()

b1 = ['java','python','c++','php','spl']
b1.pop() #xóa phần tử cuối
print(b1)
b1.pop(2) #xóa phần tử vị trí 2

#phương thức remove() : xóa đối tượng ra khoi list
# cú pháp : list.remove(obj)
c1 = ['java','python','c++','php','spl']
c1.remove('c++')
print("danh sách mới :",c1)

#hàm del cũng là xóa 
fruits = [ 'tao', 'cam','quyt','man','xoai']
del fruits[0]
print(fruits)

#phương thức reverse() : hàm đảo ngược
# cú pháp : list.rverse()

d1 =['java','python','c++','php','spl']
d1.reverse();
print("List bi dao nguoc",d1)

#phương thức clear() : xóa toàn bộ phần tử
# cú pháp : list.clear()
traicay = [ 'tao', 'cam','quyt','man','xoai']
traicay.clear()
print(traicay);

#phương thức sort() : sắp xếp theo tăng dần hoặc giảm dần, sẽ phụ thuộc vào reverse , TRUE là tăng dần
#False là tăng dần
#Nếu bỏ qua, các phần tử của list đươc sắp xếp theo tăng dần
# cú pháp : list.sort([reverse])

#hàm list chứa ma trận
matran = [[1,2,3],[4,5,6]]
print(matran)


#nhập vào một chuỗi số tách nhau bởi dấu ",". chuyển chuỗi đó thành danh sách số nguyên in ra ma trận 1 chiều
s = input("Nhập các số, cách nhau bởi dấu phẩy: ")
#chuyển thành list số nguyên
lst = eval("[" + s.replace(" ",",") + "]")
print("Ma trận 1 chiều:",lst)


# Bộ Tuple
#