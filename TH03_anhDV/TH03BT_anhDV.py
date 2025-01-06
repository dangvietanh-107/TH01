#bai15a
from datetime import datetime

def greeting(ho_ten,nam_sinh):
    nam_hien_tai = datetime.now().year
    tuoi = nam_hien_tai - nam_sinh
    return f"Chào bạn {ho_ten}, năm nay bạn {tuoi} tuổi!"
ho_ten = input("Nhập họ tên: ")
nam_sinh = int(input("Nhập năm sinh: "))
print(greeting(ho_ten,nam_sinh))

#bai15b
def thong_tin_tho(x):
    so_tho_ban_dau = 2  
    so_tho_sau_x_thang = so_tho_ban_dau * (2 ** x)
    return f"Trong rừng có: {so_tho_sau_x_thang} con thỏ"
x = int(input("Nhập vào số tháng x: "))
print(thong_tin_tho(x))

#bai15c
def count_mark():
    diem_thi = ["A", "B", "C", "F", "B", "A", "D", "F", "C", "B"]
    so_sinh_vien = len(diem_thi)
    so_sinh_vien_hoc_lai = diem_thi.count("F")
    so_sinh_vien_diem_cao = sum(1 for diem in diem_thi if diem in ["A", "B"])
    return f"Số sinh viên trong lớp: {so_sinh_vien}\nSố sinh viên phải học lại môn này (điểm F): {so_sinh_vien_hoc_lai}\nSố sinh viên có điểm cao (A, B): {so_sinh_vien_diem_cao}"
print(count_mark())

#bai15d
def bmi_show():
    can_nang = float(input("Nhập cân nặng (kg): "))
    chieu_cao = float(input("Nhập chiều cao (m): "))
    bmi = can_nang / (chieu_cao**2)
    if bmi < 18.5:
        print("underweight")
    elif 18.5< bmi < 24.9:
        print("normal")
    elif 25< bmi < 29.9:
        print("overweight")
    else:
        print("obese")
    
    return f"Chỉ số BMI của bạn là: {bmi}"
print(bmi_show())

#bai15e
def cal_point():
    list_diem = [8.6, 9.1, 7.5, 8.1, 9.5]
    list_chu = {"A": 3.7, "A+": 4.0, "B": 3.0, "B+": 3.5, "A+": 4.0}
    list_chu2 = [3.7, 4.0, 3.0, 3.5, 4.0]
    so_ky_tu = len(list_chu)
    return f"Tổng số môn học: {so_ky_tu}\nĐiểm hệ 10: {sum(list_diem)/5}\nĐiểm hệ chữ: {sum(list_chu2)/5}"
print(cal_point())

#bai15f
def list_prime():
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    list_so = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    so_nguyen_to = [so for so in list_so if is_prime(so)]
    return f"Các số nguyên tố trong list: {so_nguyen_to}"
print(list_prime())



    

