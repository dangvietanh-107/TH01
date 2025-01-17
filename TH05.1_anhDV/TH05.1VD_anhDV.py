import numpy as np #slide 5
vector_a =np.array([5,8,9,2,6,4,8,5,2,4],dtype=np.int16)
print(vector_a)
print("so phan tu cua vector:",vector_a.size)
matrix_a = vector_a.reshape((3,4))
print("reshape ve matrix :3x4")
print(matrix_a)
print("so phan tu cua matrix:",matrix_a.size)
print("reshape ve matrix :2x6")
matrix_b = vector_a.reshape((2,6))
print(matrix_b)
print("so phan tu cua matrix_b:",matrix_b.size)

#slide 7
a1_2d =np.array([(1,2,3,4),(5,6,7,8),(9,10,11,12)])
print("matrix",a1_2d)
print("a,ravel by row (default order=\"C\")")
print(a1_2d.ravel())
print("\n b, ravel by column (order=\"F\")")
print(a1_2d.ravel(order="F"))

#slide 9
x= np.arange(0,6)
print(x)
x1,x2 =np.split(x,2)
print(x1,x2)

x= np.arange(1,10)
print(x)
x1,x2,x3 =np.split(x,[2,6])
print(x1,x2,x3)

#slide 11
A2 =np.flip(A,0)
A2=np.flipud(A)
print("lat ma tran theo hang: \n",A2)

A1 =np.flip(A,1)
A1=np.fliplr(A)
print("lat ma tran theo cot: \n",A1)

#slide 16
x=np.arange(8)
print("x  =",x)
print("x+5=",x+5)
print("x-5=",x-5)
print("x*2=",x*2)
print("x/2=",x/2)
print("x//2=",x//2)
print("-x=", -x)
print("x**3=",x**3)
print("x%2=",x%2)

#pp  numpy
print("x  =",x)
print("x+5=",np.add(x,5))
print("x-5=",np.subtract(x,5))
print("x*2=",np.multiply(x,2))
print("x/2=",np.divide(x,2))
print("x//2=",np.floor_divide(x,2))
print("-x=", np.negative(x))
print("x**3=",np.power(x,3))
print("x%2=",np.mod(x,2))

#slide 17
x= np.array([-2,-1,0,1,2])
print(x)
print(np.abs(x))
print(np.absolute(x))

#silde 19
x = np.array([1,2,3])
print("x=",x)
print("e^x=",np.exp(x))
print("2^x=",np.exp2(x))
print("3^x=",np.power(3,x))

x = np.array([1,2,3,100])
print("x=",x)
print("ln(x)=",np.log(x))
print("log2(x)=",np.log2(x))
print("log10(x)=",np.log10(x))

#silde 20
arr =np.array([20.8999,67.8989,54.43409])
print("arr=",arr)
print("round(arr)=",np.round(arr,1))#lam tron toi so dau dau ,
print("round(arr)=",np.round(arr,2))
print(np.floor(arr))#lam tron xuong so nguyen gan nhat
print(np.ceil(arr))#lam tron len so nguyen gan nhat
print(np.trunc(arr))#lam tron ve phan nguyen


#silde 23
a= np.random.randint(1,33,15)
print("vector ban dau:\n",a)
a_sort = np.sort(a)
b_sort = np.flip(a_sort)
b_sort = -np.sort(-a)
print("vector sau khi sap xep tang dan:\n",a_sort)
print("vector sau khi sap xep giam dan:\n",b_sort)

#silde 25
#sap xep theo hang axis=0]
a_sort1 =np.sort(A,axis=0)
print("ma tran 1\n",a_sort1)

a_sort2 =np.sort(A,axis=1)
print("ma tran 2\n",a_sort2)

#chuyen thanh vector va sap xep cac phan tu tang dan theo hang
v_sort = np.sort(A,axis=None)
print("vector sau khi sap xep tang dan theo hang\n",v_sort)

a_sort3 = np.sort(A,axis=None).reshape(A.shape[0],A.shape[1])
print("ma tran 3\n",a_sort3)

#slide 28
x = np.array([17,2,55,1,6,5,8,9,5,1,32,6,8])
#tim kiem cac phan tu co gia tri ==1
t1=np.where(x==1)
print("1. so phan tu thoa man dieu kien = 1:",t1[0].size)
#tim kiem cac phan tu co gia trij >10
t2=np.where(x>10)
print(t2)
print("2. so phan tu thoa man dieu kien>10",t2[0].size)
#tim kiem cac phan tu co gia trij [5,12]
t3=np.where((x>=5)&(x<=12))
print(t3)
print("3. so phan tu thoa man dieu kien [5,12]",t3[0].size)

#silde29
arr =np.array([(1,2,3,4,5,4),(7,3,5,6,5,7,4,5)])
#tim kiem phan tu >4
x = np.where(arr >4)
print("ma tran a:\n",arr)
print(x)
print("so phan tu thoa man dieu kien >4",x[0].size)