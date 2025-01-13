#vd40
print("diem cao nhat cua lop",diem_2a.max)
print("diem thap nhat cua lop",diem_2a.min)

for i in range(0,diem_2a.shape[0]):
    print("diem cao nhat cua hoc sinh",i,"la",diem_2a[i].max())
    print("diem thap nhat cua hoc sinh",i,"la",diem_2a[i].min())
for i in range (0,diem_2a.shape[1]):
    print("diem cao nhat cua mon hoc",i,"la",diem_2a[:,i].max())
    print("diem thap nhat cua mon hoc",i,"la",diem_2a[:,i].min())
#vd41
print("tong tat ca cac diem trong cua lop 2a:",diem_2a.sum())

for i in range(0,diem_2a.shape[1]):
    print("tong diem cac mon cua hoc sinh",i,":",diem_2a[:,i].sum())
#vd43
print("diem tb cua lop 2a:",diem_2a.mean())

for i in range(0,diem_2a.shape[1]):
    print("diem tb cua mon hoc",i,":",diem_2a[:,i].mean())

mean_2a = diem_2a.mean(axis=0)
for i in range(0,mean_2a.size):
    print("diem tb cua hoc sinh",i,":",mean_2a[i])
#vd44
a=diem_2a[1,:15]

print("mang a ban dau",a)
print("so ptu trong mang a",a.size)
print("mang a da sap xep",np.sort(a,))
print("gia tri trung binh mean:",np.mean(a))
print("gtri tb median",np.median(a))

#vd45
from scipy import stats as sp
for i in range(0,diem_2a.shape[0]):
    a = sp.mode(diem_2a[i,:])
    print("mon",i,": diem xuat hien nhieu nhat:",a[0],"so lan:",a[1])
    print(type(a))
#vd46
for i in range(0,diem_2a.shape[1]):
    print("do chenh diem cua hoc sinh",i,":",diem_2a[:,i].max()-diem_2a[:,i].min())

#vd47
a = np.array([a0,1,1,9,12,1,9,12,10])
print("ptu cua mang a:",a)
print("gtri tb:",a.mean())
print("do lech chuan",a.std())


b= np.array([7,7,8,7,8,7,7,7,7])
print("ptu cua mang b:",b)
print("gtri tb:",b.mean())
print("do lech chuan",b.std())