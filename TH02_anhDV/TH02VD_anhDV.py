#vd1

a =10
b = 8
print=("1.lớn hơn a >b:", a > b)
print=("2. Nhỏ hơn a < b:", a < b)
print+("3. Bằng a == b:", a == b)
print=("4. Lớn hơn hoặc bằng a >= b:", a >= b)
print=("5. Nhỏ hơn hoặc bằng a <= b:", a <= b)
print=("6. Khác a != b:", a != b)

#vd2
x =5
y =True
kt =(x>3) and (x<10)
kt2=(x>3) or (x<4)
kt3= not y
print("phép toán AND",kt)
print("phép toán OR", kt2)
print("phép toán NOT",kt3)

#vd3
# câu lệnh điều khiển
so_tien = input (" Nhập số tiền bạn có")
so_tien = int(so_tien)
if so_tien > 100:
    print("Bạn có thể mua một chiếc điện thoại")
else:
    print("Bạn không thể mua một chiếc điện thoại")

#vd4
num = 3
if num >0:
 print(num,"là số dương")
print("thông điệp này luôn được in")

num = -1
if num >0:
 print(num,"là số dương")
print("thông điệp này luôn được in")
#vd5
so_nguyen= input("Nhập số nguyên:")
so_nguyen = int(so_nguyen)
if so_nguyen % 2 == 0:
    print("Số chẵn")
else:
    print("Số lẻ")

#vd6
num = 3
if num >= 0:
    print(num, "là số dương")
else:
    print(num, "là số âm")

num = -1
if num >= 0:
    print(num, "là số dương")
else:
    print(num, "là số âm")

#vd7
so_nguyen= input("Nhập số nguyên:")
so_nguyen = int(so_nguyen)
if so_nguyen % 2 == 0:
    print("Số chẵn")
else:
    print("Số lẻ")

#vd8
gioi_tinh = input("Nhập giới tính, 0 =nam, 1= nữ:")
gioi_tinh = int(gioi_tinh)
if gioi_tinh == 0:
    print("Chào anh đep trai")
elif gioi_tinh == 1:
    print("Chào chị xinh gái")
else:
    print("Giới tính không hợp lệ")

#vd9
num = float(input("nhập một số:"))
if num >= 0:
    if num ==0:
        print("Số không")
    else:
        print("Số dương")
else:
    print("Số âm")

#vd10
n = int(input("Em sinh tháng mấy?"))
i=1
while (i<=n):
    print(i,"I love u")
    i=i+1
    print("----vietanh")

#vd11
n = int(input("em sinh tháng mấy?"))
i = 1
while (i<=n):
    print(i,"I love u")
    if (i==3):
        break
    i=i+1
print("----vietanh")
#vd12
n=20
i=1
while (i<=n):
    i=i+1
    if(i%3!=0):
        continue
    print(i)
print("----vietanh")
#vd13
while True:
    n = int(input("em sinh tháng mấy?"))
    if (1<=n<=12):
        break
    print("tháng không đúng, nhập lại")
    print("chào em cô gái tháng ",n)
#vd14
n=10
tich =1
tong =0 
for i in range(1, n+1):
    tich = tich*i
    tong = tong+i
print("10!+",tich)
print("10+=",tong)
#vd15
st = "eaut in my mind"
for i in st:
    print("ký tự: ",i)
st = "eaut in my mind"
dem =0
for i in st:
    if(i=="M"):
        dem = dem+1
        print("Số lần xuất hiện của M là:",dem)
#vd16
hoc_sinh=["dang viet anh","le van huy","le thi mai","le van nam"]
print("danh sách học sinh:")
tt =  1
for i in hoc_sinh:
    print(tt,")",i)
    tt=tt+1
#vd17
for i in range():
    print("i+",i)
for i in range(2,11,2):
    print("i+",i)
#vd18
for i in range(2,10):
    print("bang cuu chuong",i)
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
        print("-----")

