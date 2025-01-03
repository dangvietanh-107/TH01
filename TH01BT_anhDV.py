# bai 1
N = int(input("Nhập số kẹo của cô (N): "))
M = int(input("Nhập số học sinh trong lớp (M): "))
if M != 0:
    keo_moi_hoc_sinh = N // M
    keo_con_lai = N % M

    print(f"Mỗi học sinh nhận được {keo_moi_hoc_sinh} cái kẹo.")
    print(f"Cô còn lại {keo_con_lai} cái kẹo.")
else:
    print("Số học sinh phải lớn hơn 0!")



#bai 2
ho_ten = input("Nhập họ tên: ")
nam_sinh = int(input("Nhập năm sinh: "))
from datetime import datetime
nam_hien_tai = datetime.now().year
tuoi = nam_hien_tai - nam_sinh
print(f"Bạn \"{ho_ten.upper()}\" năm nay {tuoi} tuổi!")



#bai 3
x = int(input("Nhập vào số tháng x: "))
so_tho_ban_dau = 2  
so_tho_sau_x_thang = so_tho_ban_dau * (2 ** x)
print(f"Trong rừng có: {so_tho_sau_x_thang} con thỏ")


#bai 4
van_ban = "Nước Việt Nam là một, dân tộc Việt Nam là một. Sông có thể cạn núi có thể mòn, song chân lý ấy không bao giờ thay đổi. (HỒ CHÍ MINH, 1890 – 1969)"

so_ky_tu = len(van_ban)
print(f"Số ký tự trong đoạn văn: {so_ky_tu}")
tim_kiem_1 = "hồ chí minh" in van_ban.lower()
tim_kiem_2 = "non sông" in van_ban.lower()
print(f"Đoạn văn có chứa 'hồ chí minh': {tim_kiem_1}")
print(f"Đoạn văn có chứa 'non sông': {tim_kiem_2}")
cau = van_ban.split(".")
print("Các câu trong đoạn văn:")
for i, c in enumerate(cau, 1):
    print(f"Câu {i}: {c.strip()}")

co_ky_tu_dac_biet = any(not char.isalnum() and not char.isspace() for char in van_ban)
print(f"Đoạn văn có ký tự đặc biệt: {co_ky_tu_dac_biet}")

van_ban_thay_the = van_ban.replace("Việt Nam", "VIỆTNAM")
print("Đoạn văn sau khi thay thế:")
print(van_ban_thay_the)


#bai 5
diem_thi = ["A", "B", "C", "F", "B", "A", "D", "F", "C", "B"]
so_sinh_vien = len(diem_thi)
print(f"Số sinh viên trong lớp: {so_sinh_vien}")
so_sinh_vien_hoc_lai = diem_thi.count("F")
print(f"Số sinh viên phải học lại môn này (điểm F): {so_sinh_vien_hoc_lai}")
so_sinh_vien_diem_cao = sum(1 for diem in diem_thi if diem in ["A", "B"])
print(f"Số sinh viên có điểm từ B trở lên: {so_sinh_vien_diem_cao}")
diem_thi_moi = diem_thi[1:-1]
print(f"Bảng điểm mới sau khi loại bỏ sinh viên đầu tiên và cuối cùng: {diem_thi_moi}")
