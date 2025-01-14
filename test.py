import numpy as np
try:
    # Thay đổi delimiter nếu dữ liệu không cách nhau bằng khoảng trắng
    data_numpy = np.loadtxt('diemlop2a.txt')

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
