#Trang 13
import numpy as np
a1 = np.arange(1,30+1)
print(a1)

print('-------------------------------------------------------')
vector_a_le = a1[a1%2==1]
print("\nVector a_le:")
print(vector_a_le)

vector_a_chan = a1[a1%2==0]
print("\nVector a_chan:")
print(vector_a_chan)

vector_a_3 = a1[a1%3==0]
print("\nVector a_3: ")
print(vector_a_3)

#Trang 31
import numpy as np

# Function to clean and convert string data to numeric array
def clean_data(data_str):
    # Remove brackets and split by spaces
    data = data_str.strip('[]').split()
    # Convert to float array
    return np.array([float(x) for x in data])

# Sample data from the file (in real implementation, this would be read from file)
with open('Data_BMI.txt', 'r') as file:
    # Đọc dòng dữ liệu chiều cao
    height_data = file.readline()
    # Đọc dòng dữ liệu cân nặng
    weight_data = file.readline()
# Convert string data to numpy arrays
v_height = clean_data(height_data)
v_weight = clean_data(weight_data)

print("Vector chiều cao (v_height):")
print(v_height)
print("\nĐộ dài vector chiều cao:", len(v_height))

print("\nVector cân nặng (v_weight):")
print(v_weight)
print("\nĐộ dài vector cân nặng:", len(v_weight))

#Trang 33
import numpy as np

# Cách 1: Sử dụng np.loadtxt()
v_height = np.loadtxt('data_BMI.txt')
v_height_m = v_height / 100

# Tính bình phương các giá trị
v_height_m2 = np.power(v_height_m, 2)

print("Vector v_height_m2:")
print(v_height_m2)

# In ra một số thông tin kiểm tra
print("\nSố phần tử:", len(v_height_m2))
print("Giá trị nhỏ nhất:", np.min(v_height_m2))
print("Giá trị lớn nhất:", np.max(v_height_m2))
print("Giá trị trung bình:", np.mean(v_height_m2))

#Trang 34
import numpy as np

# Giả sử đã có v_weight và v_height_m2 từ các bước trước
def calculate_bmi(weight, height_m2):
    """
    Tính BMI từ cân nặng và chiều cao bình phương
    weight: cân nặng (kg)
    height_m2: chiều cao bình phương (m²)
    """
    bmi = weight / height_m2
    # Làm tròn đến 1 số sau dấu chấm
    return np.round(bmi, 1)

# Tính BMI cho từng người
v_bmi = calculate_bmi(v_weight, v_height_m2)

print("Chỉ số BMI của 17 người:")
print(v_bmi)

# In một số thống kê cơ bản
print("\nThống kê BMI:")
print(f"Giá trị nhỏ nhất: {np.min(v_bmi)}")
print(f"Giá trị lớn nhất: {np.max(v_bmi)}")
print(f"Giá trị trung bình: {np.mean(v_bmi):.1f}")
print(f"Số lượng người: {len(v_bmi)}")

# Kiểm tra phân phối BMI theo các ngưỡng chuẩn
print("\nPhân loại BMI:")
print(f"Số người gầy (BMI < 18.5): {np.sum(v_bmi < 18.5)}")
print(f"Số người bình thường (18.5 ≤ BMI < 25): {np.sum((v_bmi >= 18.5) & (v_bmi < 25))}")
print(f"Số người thừa cân (BMI ≥ 25): {np.sum(v_bmi >= 25)}")

#Trang 36
import numpy as np

def classify_bmi_counts(v_bmi):
    """
    Phân loại và đếm số người theo các mức BMI
    """
    # Định nghĩa các ngưỡng phân loại và đảm bảo không có khoảng trống
    underweight = np.sum(v_bmi < 18.5)
    normal = np.sum((v_bmi >= 18.5) & (v_bmi < 25.0))
    overweight = np.sum((v_bmi >= 25.0) & (v_bmi < 30.0))
    obese = np.sum((v_bmi >= 30.0) & (v_bmi < 35.0))
    extremely_obese = np.sum(v_bmi >= 35.0)
    
    # Tính tổng
    calculated_total = underweight + normal + overweight + obese + extremely_obese
    total = len(v_bmi)
    
    # In kết quả theo định dạng yêu cầu
    print(f"Tổng số: {total}")
    print("-" * 25)
    print(f"1. Underweight    : {underweight}")
    print(f"2. Normal         : {normal}")
    print(f"3. Overweight     : {overweight}")
    print(f"4. Obese          : {obese}")
    print(f"5. Extremely Obese: {extremely_obese}")
    print(f"\nKiểm tra tổng: {calculated_total}")
    
    # Kiểm tra tổng với thông báo chi tiết
    if total != calculated_total:
        print(f"\nCảnh báo: Có {total - calculated_total} giá trị không được phân loại!")
        print("Kiểm tra các giá trị BMI nằm ngoài khoảng phân loại:")
        print(v_bmi[(v_bmi < 0) | (np.isnan(v_bmi))])
    
    return {
        "Underweight": underweight,
        "Normal": normal,
        "Overweight": overweight,
        "Obese": obese,
        "Extremely Obese": extremely_obese,
        "Total": total,
        "Calculated Total": calculated_total
    }

# Thực hiện phân loại và in kết quả
bmi_stats = classify_bmi_counts(v_bmi)