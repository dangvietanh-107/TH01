import numpy as np

path = "diemlop2a.txt"
diem_2a = np.loadtxt(path, delimiter=",", dtype=np.int32)
print(diem_2a)

# Calculate the standard deviation for each student
std_devs = np.std(diem_2a, axis=1)

# Find the student with the most consistent scores (lowest standard deviation)
sv_diem_dongdeu = np.argmin(std_devs)
print("Sinh vien co diem dong deu nhat:", sv_diem_dongdeu , diem_2a[sv_diem_dongdeu ])

# Find the student with the most varied scores (highest standard deviation)
sv_diem_chechlech = np.argmax(std_devs)
print("Sinh vien co diem cac mon lech nhat trong lop:", sv_diem_chechlech, diem_2a[sv_diem_chechlech])

# Calculate the standard deviation for each subject
do_lech_mon = np.std(diem_2a, axis=0)

# Find the subject with the most consistent scores (lowest standard deviation)
most_consistent_subject = np.argmin(do_lech_mon )
print("Mon hoc co diem dong deu nhat:", most_consistent_subject)

# Find the subject with the most varied scores (highest standard deviation)
most_varied_subject = np.argmax(do_lech_mon )
print("Mon hoc co diem chenh lech nhat:", most_varied_subject)
