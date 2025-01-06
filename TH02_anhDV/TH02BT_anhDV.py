#bai 6
# Nhập vào một ký tự
ky_tu = input("Nhập vào một ký tự chữ cái bất kỳ: ").lower()
if ky_tu.isalpha() and len(ky_tu) == 1:  
    if ky_tu in "aeiou": 
        print(f"Ký tự '{ky_tu}' là nguyên âm.")
    else:
        print(f"Ký tự '{ky_tu}' là phụ âm.")
else:
    print("Vui lòng nhập một ký tự chữ cái hợp lệ.")
#bai 7
can_nang=input("Nhập cân nặng của bạn(kg):")
can_nang=float(can_nang)
chieu_cao=input("Nhập chiều cao của bạn(m):")
chieu_cao=float(chieu_cao)
bmi=can_nang/(chieu_cao**2)
if bmi < 18.5:
    print("underweight")
elif 18.5< bmi < 24.9:
    print("normal")
elif 25< bmi < 29.9:
    print("overweight")
else:
    print("obese")


#bai 8
thang_sinh=input("Nhập tháng sinh của bạn:")
thang_sinh=int(thang_sinh)
if 1<=thang_sinh<=12:
    if 1<=thang_sinh<=3:
        print("Mùa xuân")
    elif 4<=thang_sinh<=6:
        print("Mùa hạ")
    elif 7<=thang_sinh<=9:
        print("Mùa thu")
    elif 10<=thang_sinh<=12:
        print("Mùa đông")
else:
    print("Vui lòng nhập tháng sinh hợp lệ")

#bai 9
bang_cuuchuong = int(input("Nhập vào bảng cửu chương bạn muốn in: "))
if bang_cuuchuong < 1 or bang_cuuchuong > 10:
    print("Vui lòng nhập số từ 1 đến 10.")
else :
    for i in range(1, 11):
      print(f"{bang_cuuchuong} x {i} = {bang_cuuchuong * i}")

#bai10
list_diem =[8.6, 9.1, 7.5, 8.1, 9.5]
list_chu={"A":3.7,"A+":4.0,"B":3.0,"B+":3.5,"A+":4.0}
list_chu2 =[3.7, 4.0, 3.0, 3.5, 4.0]
print("--------diem trung binh------")
so_ky_tu = len(list_chu)
print(f"Tong so mon hoc: {so_ky_tu}")
print("điểm hệ 10",sum(list_diem)/5 )
print("điểm hệ chữ",sum(list_chu2)/5 )

#bai11
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Nhập số N từ người dùng
try:
    N = int(input("Nhập vào số tự nhiên N: "))
    if is_prime(N):
        print(f"{N} là số nguyên tố.")
    else:
        print(f"{N} không phải là số nguyên tố.")
except ValueError:
    print("Vui lòng nhập một số tự nhiên hợp lệ.")

#bai12
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Nhập số N từ người dùng
try:
    N = int(input("Nhập vào một số tự nhiên N: "))
    if N < 2:
        print("Không có số nguyên tố nào trong khoảng này.")
    else:
        print(f"Các số nguyên tố từ 2 tới {N} là:")
        primes = [i for i in range(2, N + 1) if is_prime(i)]
        print(primes)
except ValueError:
    print("Vui lòng nhập một số tự nhiên hợp lệ.")

#bai13
# Nhập số N từ người dùng
try:
    N = int(input("Nhập vào một số tự nhiên N (N > 0): "))
    if N <= 0:
        print("Vui lòng nhập một số lớn hơn 0.")
    else:
        binary_representation = bin(N)[2:]  # Sử dụng bin() để chuyển sang nhị phân và bỏ tiền tố '0b'
        print(f"Số {N} trong hệ nhị phân là: {binary_representation}")
except ValueError:
    print("Vui lòng nhập một số tự nhiên hợp lệ.")

#bai14
# Khởi tạo danh sách chiều cao của sinh viên (đơn vị: m)
student_heights = [1.55, 1.68, 1.72, 1.60, 1.65, 1.58, 1.75, 1.80, 1.62, 1.70]

# 1. Hiển thị chiều cao cao nhất và thấp nhất
max_height = max(student_heights)
min_height = min(student_heights)
print(f"Chiều cao cao nhất: {max_height} m")
print(f"Chiều cao thấp nhất: {min_height} m")

# 2. Tính chiều cao trung bình
mean_height = sum(student_heights) / len(student_heights)
print(f"Chiều cao trung bình: {mean_height:.2f} m")

# 3. Số lượng sinh viên có chiều cao lớn hơn hoặc bằng trung bình
above_mean_count = sum(1 for height in student_heights if height >= mean_height)
print(f"Số lượng sinh viên có chiều cao >= chiều cao trung bình: {above_mean_count}")

