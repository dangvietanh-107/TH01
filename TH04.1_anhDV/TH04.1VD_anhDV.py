#vd13
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a)
print("loai du lieu a", type(a))
print("loai du lieu cua ptu trong mang a",a.dtype)
print("kich thuoc cua mang a",a.shape)
print("so phan tu cua mang a",a.size)
print("so chieu cua mang a",a.ndim)

#vd14
import numpy as np
b = np.array([(1, 3, 4, 5.0),(1, 2, 3, 3.5)])
print(b)
print("loai du lieu a", type(b))
print("kieu du lieu cua phan tu trong mang b",b.dtype)
print("kich thuoc cua mang b",b.shape)
print("so phan tu cua mang b",b.size)
print("so chieu cua mang b",b.ndim)

#vd15
import numpy as np
c = np.array([[(2,4,0,6),(4,7,5,6)],
              [(0,3,2,1),(9,4,5,6)],
              [(5,8,6,4),(1,4,6,8)]])
print(c)
print("phan tu dau tien cua mang c",c[0,0,0])
print("kieu du lieu cua phan tu trong mang c",c.dtype)
print("kich thuoc cua mang c",c.shape)
print("so phan tu cua mang c",c.size)
print("so chieu cua mang c",c.ndim)

#vd18
import numpy as np
array_zeros = np.zeros((5,3))
print("kieu du lieu trong mang az",array_zeros.dtype)
print("kich thuoc trong mang az",array_zeros.shape)
print("so phan tu co trong mang az",array_zeros.size)
print("so chieu trong mang az",array_zeros.ndim)

import numpy as np
array_one = np.ones((3, 5), dtype=np.int32)
print(array_one)
print("kieu du lieu trong mang azo",array_one.dtype)
print("kich thuoc trong mang azo",array_one.shape)
print("so phan tu co trong mang azo",array_one.size)
print("so chieu trong mang azo",array_one.ndim)

#vd19
import numpy as np
array_eye =np.eye(5)
print(array_eye)
print("kieu du lieu trong mang array_eye",array_eye.dtype)
print("kich thuoc trong mang array_eyeo",array_eye.shape)
print("so phan tu co trong mang array_eye",array_eye.size)
print("so chieu trong mang array_eye",array_eye.ndim)


#vd20
import numpy as np
array_random =np.random.random((7,5))
print(array_random)
print("kieu du lieu trong mang array_random",array_random.dtype)
print("kich thuoc trong mang array_random",array_random.shape)
print("so phan tu co trong mang array_random",array_random.size)
print("so chieu trong mang array_random",array_random.ndim)

#vd22
d = np.arange(1,15,2)
print("vectoe d:",d)
print("so phan tu cua vector d", d.size)
print("-----")
f =np.linspace(1,15,11)
print("vector f",f)
print("so phan tu cua vector f",f.size)

#vd25
import numpy as np
path = "text.txt"
diem_2a = np.loadtxt(path,delimiter=",",dtype=np.int)
print(diem_2a)
print("kieu du lieu trong mang diem_2a",diem_2a.dtype)
print("kich thuoc trong mang diem_2a",diem_2a.shape)
print("so phan tu co trong mang diem_2a",diem_2a.size)
print("so chieu trong mang diem_2a",diem_2a.ndim)

#vd28
a_float=np.linspace(0,15,11)
print(a_float)
print("kieu du lieu:",a_float)
a_int=a_float.astype(np.int16)
print(a_int)
print("di lieu sau khi chuyen",a_int.dtype)


a_str = a_int.astype(np.str)
print(a_str)
print("di lieu sau khi chuyen",a_str.dtype)

a_bol = a_int.astype(np.bool)
print(a_bol)
print("di lieu sau khi chuyen",a_bol.dtype)


#vd31
a = np.array([3,5,3,10,9,1,9,8,3,1])
print("cac phan tu cua vector a:\n",a)
print("ptu dau tien",a[0])
print("ptu thu 3",a[3])
print("ptu cuoi cung",a[-1])

print("3 ptu dau tien",a[:3])
print("tu ptu thu 5 toi het",a[5:])
print("tu phan tu thu 2 den ptu thu 6 cua vector",a[2:6])

#vd32
print("diem mon hoc dau tien, cua hoc sinh dau tien",diem_2a[0,0])
print("diem mon hoc thu 1, cua hoc sinh thu 3",diem_2a[1,3])
print("diem mon cuoi cung, cua hoc sinh cuoi cung",diem_2a[-1,-1])
print("-----")
print("bang diem lop 2a",diem_2a)

#vd33
diem_hs5=diem_2a[:,5]
print("diem cac mon hoc cua hoc sinh 5",diem_hs5)
diem_mon =diem_2a[-1,:]

diem5_hs10 = diem_2a[:5,:10]
print("bang diem 5 mon hoc dau tien cua 10 hoc sinh dau cua lop\n",diem5_hs10)


