#bai2.2 slide 50
import numpy as np

path = "diemlop2a.txt"
diem_2a = np.loadtxt(path, delimiter=",", dtype=np.int32)
print(diem_2a)

for i in range(diem_2a.shape[0]):
    print("DTB cua tung mon hoc", i, ":", diem_2a[i, :].mean())

diem_tb = diem_2a.mean(axis=1)
diem_cao= np.argmax(diem_tb)
print("Mon hoc co diem tb cao nhat:", diem_cao, ":", diem_tb[diem_cao])
print("bang diem day du cua mon hoc:", diem_cao, ":", diem_2a.T[diem_cao])
diem_tb = diem_2a.mean(axis=1)
diem_thap= np.argmin(diem_tb)
print("Mon hoc co diem TB thap nhat:", diem_thap, ":", diem_tb[diem_thap])
print("bang diem day du cua mon hoc:", diem_thap, ":", diem_2a.T[diem_thap])

#bai2.1 slide 49
import numpy as np

path = "diemlop2a.txt"
diem_2a = np.loadtxt(path, delimiter=",", dtype=np.int32)
print(diem_2a)

for i in range(diem_2a.shape[1]):
    print("DTB cua tung HS", i, ":", diem_2a[:, i].mean())

diem_tb = diem_2a.mean(axis=0)
diem_cao= np.argmax(diem_tb)
print("HS co diem tb cao nhat:", diem_cao, ":", diem_tb[diem_cao])
print("bang diem day du cua hs:", diem_cao, ":", diem_2a.T[diem_cao])

diem_tb = diem_2a.mean(axis=0)
diem_thap= np.argmin(diem_tb)
print("HS co diem TB thap nhat:", diem_thap, ":", diem_tb[diem_thap])
print("bang diem day du cua hs:", diem_thap, ":", diem_2a.T[diem_thap])

#bai2.3
import numpy as np

path = "diemlop2a.txt"
diem_2a = np.loadtxt(path, delimiter=",", dtype=np.int32)
print(diem_2a)

std_devs = np.std(diem_2a, axis=1)

sv_diem_dongdeu = np.argmin(std_devs)
print("Sinh vien co diem dong deu nhat:", sv_diem_dongdeu , diem_2a[sv_diem_dongdeu ])

sv_diem_chechlech = np.argmax(std_devs)
print("Sinh vien co diem cac mon lech nhat trong lop:", sv_diem_chechlech, diem_2a[sv_diem_chechlech])

do_lech_mon = np.std(diem_2a, axis=0)

mon_dong_deu= np.argmin(do_lech_mon )
print("Mon hoc co diem dong deu nhat:", mon_dong_deu)

mon_chenh_lech = np.argmax(do_lech_mon )
print("Mon hoc co diem chenh lech nhat:", mon_chenh_lech)

#bai slide 61
import numpy as np
try:
    # Thay đổi delimiter nếu dữ liệu không cách nhau bằng khoảng trắng
    data_numpy = np.loadtxt('text.txt')

    # Lấy thông tin của mảng numpy
    shape = data_numpy.shape
    ndim = data_numpy.ndim
    dtype = data_numpy.dtype
    size = data_numpy.size

    # In ra thông tin
    print("Kích thước của mảng (shape):", shape)
    print("Số chiều của mảng (ndim):", ndim)
    print("Kiểu dữ liệu của mảng (dtype):", dtype)
    print("Số phần tử trong mảng (size):", size)

except Exception as e:
    print("Có lỗi xảy ra khi đọc file hoặc xử lý dữ liệu:", e)
