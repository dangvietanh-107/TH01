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