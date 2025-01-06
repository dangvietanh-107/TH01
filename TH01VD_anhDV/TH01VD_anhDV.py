#vd20
print("Hello world!")

#vd21
name = input("nhap ten:")
print("Hello", name)

#vd23
a = 0
A = 0
for i in range(1,6):
    print(i)
    a= a + 1
    print("gia tri cua bien a =", a)
    print("--------------------------------------------------------")
    for i in range (1,6,2):
        print(i)
        A =A +1

        print("gia tri cua bien A =", A)

#vd24
a = 9
b = 5

c = a + b
d = a - b
e = a * b
f = a / b
print("tong a + b =", c)
print("hieu a - b =", d)
print("tich a * b =", e)
print("thuong a / b =", f)

#vd38
A = int(input("so a:"))
B = int(input("so b:"))
C = int(input("so c:"))
a= A + B 
print (a)
b = a + C
print (b)
c = A + B + C
print (c)

#vd46
a = int(input("nhap so a:"))
b = int(input("nhap so b:"))

print("tong a + b =", a + b)
print("hieu a - b =", a - b)
print("tich a * b =", a*b)
print("thuong a / b =", a/b)
print("thuong nguyen a // b =", a//b)
print("thuong du a % b = ", a%b)
print("mu a**b =", a**b)

#vd47
x = 5
y = 3.14
z= "hello"
n =[1,2,3]
b = True
print("---------------")
print(type(x))
print(type(y))
print(type(z))
print(type(n))
print(type(b))

#vd52
st = "hello sinh vien eaut"
x = "hello" in st
y = "python" in st
print ("ket qua kiem tra hello", x)
print ("ket qua kiem tra python", y)


#vd62
hoc_sinh=["dang viet anh","nguyen hong van","dang duc huy"]
print(hoc_sinh)
diem =["A+","B+","C+"]
print(diem)
list_so=[1,2,4,5,7,8,-6,56]
print(list_so)
person_info =["dang viet anh", 21, "nam dinh", 1.75]
print(person_info)
list_rong=[]
print(list_rong)

#vd63
print= ("hoc sinh vi tri so 2",hoc_sinh[2])
print= ("diem cua hoc sinh vi tri so 1",diem[1])
print =("ho ten",person_info[0],"---chieu cao", person_info[3])
print =(list_so[2:1])

#vd65
list_a =[1,2,4,6,8]
list_b =[3,5,7,9]
list_c = list_a + list_b
print =("list c",list_c)
print =( list_c,  "co so phan tu",len(list_c))

#vd66
print =(list_c)
bol_0 = 0 in list_c
print =("phan tu 0 co thuoc list c?",bol_0)
bol_9 = 9 in list_c
print =("phan tu 9 co thuoc list c?",bol_9)

#vd67
print =("danh sach ban dau",list_c)
list_c.append(10)
print =("danh sach sau khi them 10",list_c)
list_c.insert(3,9)
print =("danh sach sau khi them 9 vao vi tri 3",list_c)
#vd69
print=("danh sach ban dau",list_c)

list_c.pop()
print=("danh sach sau khi xoa phan tu cuoi cung",list_c)
del list_c[3]
print=("danh sach sau khi xoa phan tu vi tri 3",list_c)
list_c.remove(0)
print=("danh sach sau khi xoa phan tu 0",list_c)

#vd70
print=("danh sach ban dau",list_c)
print=( "so 8 xuat hien",list_c.count(8))
print=( "so 0 xuat hien",list_c.count(0))

#vd71
      #so,chuoi
a = 10
b = a
b = 5
print('Giá trị của biến a:', a)
print('Giá trị của biến b:', b)
      #danhsach 
ds_a = [4, 5, 8, 9]
ds_b = ds_a
ds_b[1] = 10
print('Biến ds_a:', ds_a)
print('Biến ds_b:', ds_b)
#vd72
ds_a = [4, 5, 8, 9]
ds_b = ds_a.copy()
ds_b[1] = 10
print('Biến ds_a:', ds_a)
print('Biến ds_b:', ds_b)
#vd73
x = True
y = False
z = 5 > 8
w = 12 == 12

print('Kiểu dữ liệu của biến x:', type(x), ', Giá trị: ', x)
print('Kiểu dữ liệu của biến y:', type(y), ', Giá trị: ', y)
print('Kiểu dữ liệu của biến z:', type(z), ', Giá trị: ', z)
print('Kiểu dữ liệu của biến w:', type(w), ', Giá trị: ', w)