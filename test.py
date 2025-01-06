def bmi_show():
    can_nang = float(input("Nhập cân nặng (kg): "))
    chieu_cao = float(input("Nhập chiều cao (m): "))
    bmi = can_nang / (chieu_cao ** 2)
    if bmi < 18.5:
        print("underweight")
    elif 18.5< bmi < 24.9:
        print("normal")
    elif 25< bmi < 29.9:
        print("overweight")
    else:
        print("obese")
    
    return f"Chỉ số BMI của bạn là: {bmi}"
print(bmi_show())