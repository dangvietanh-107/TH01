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


#bai 2
def vcheo(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True