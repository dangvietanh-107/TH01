#bai1
import numpy as np
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = 12
array_random =np.random.randint(0, 101, size=(n,n))
print(array_random)
print("kieu du lieu trong mang array_random",array_random.dtype)
print("kich thuoc trong mang array_random",array_random.shape)
print("so phan tu co trong mang array_random",array_random.size)
print("so chieu trong mang array_random",array_random.ndim)


#bai 2
import numpy as np
def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
n= 12
array_random =np.random.randint(0, 101, size=(n,n))
print(array_random)
print("kieu du lieu trong mang array_random",array_random.dtype)
print("kich thuoc trong mang array_random",array_random.shape)
print("so phan tu co trong mang array_random",array_random.size)
print("so chieu trong mang array_random",array_random.ndim)

v_chinh = np.diagonal(array_random)
print("vector cac ptu nam tren duong cheo chinh:", v_chinh)
v_phu = np.diagonal(np.fliplr(array_random))
print("vector cac ptu nam tren duong cheo phu:", v_phu)

#bai3
import numpy as np

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = 12  
array_random = np.random.randint(0, 101, size=(n,n))
print("Ma trận ngẫu nhiên:")
print(array_random)

print("Kiểu dữ liệu trong mảng array_random:", array_random.dtype)
print("Kích thước trong mảng array_random:", array_random.shape)
print("Số phần tử có trong mảng array_random:", array_random.size)
print("Số chiều trong mảng array_random:", array_random.ndim)

while True:
    try:
        x = int(input("Nhập số nguyên x (0 < x < 100): "))
        if 0 < x < 100:
            break
        else:
            print("Vui lòng nhập số trong khoảng (0, 100).")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")

# Đếm số phần tử
equal_to_x = np.sum(array_random == x)
greater_than_x = np.sum(array_random > x)
less_than_x = np.sum(array_random < x)

# Hiển thị kết quả
print(f"Số phần tử bằng {x}: {equal_to_x}")
print(f"Số phần tử lớn hơn {x}: {greater_than_x}")
print(f"Số phần tử nhỏ hơn {x}: {less_than_x}")