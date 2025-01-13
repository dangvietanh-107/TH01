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
