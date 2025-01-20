import numpy as np #slide 39
a = np.array([(1,3,1,4),(3,9,5,15),(0,2,1,1),(0,4,2,3)])
print("ma tran:\n",a)
det_a=np.linalg.det(a)
print("det_a=",det_a)

b=np.array([(1,3,1,4),(3,9,5,15),(0,2,1,1),(0,4,2,3)])
print("ma tran:\n",b)
det_b=np.linalg.det(b)

#slide 42
d_A1=A.diagonal(1)
print(d_A1)

d_A1=A.diagonal(0)
print(d_A1)

d_A1=A.diagonal(-4)
print(d_A1)
#slide44
d_A1 =np.triu(A,2)
print(d_A1)

d_A1 =np.triu(A,-3)
print(d_A1)
#slide45
trace_A=A.trace()
print("trace of matrix A:\n",trace_A)

trace_A=A.diagonal().sum
print("trace of matrix A", trace_A) 

#slide53
equa_ab =np.equa(a,b)
print(equa_ab)
#slide54
sum_ab=np.add(a,b)
print(sum_ab)

sub_ab =np.subtract(a,b)
print(sub_ab)

#slide55
multi_ac=np.dot(a,c)
print(multi_ac)


vector_a=np.random.randint(1,20,10)
vector_b=np.random.randint(1,20,10)
vector_ab=vector_a@vector_b
print("vectora",vector_a)
print("vectorb",vector_b)
print("vectorab",vector_ab)

#slide61
A=np.array([(1,3,1,4),(3,9,5,15),(0,2,1,1),(0,4,2,3)])
A_T=A.T
print("ma tran a",A)
print("ma tran chuyen vi",A_T)

B=np.array([(1,3,1,4),(3,9,5,15),(0,2,1,1),(0,4,2,3)])
B_T=B.T
print("ma tran a",B)
print("ma tran chuyen vi",B_T)
