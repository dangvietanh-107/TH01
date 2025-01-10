#bai17
from datetime import datetime

class Person:
    def __init__(self, name, yearold, height, weight):
     self.name = name
     self.yearold = yearold
     self.height = height
     self.weight = weight
    def greeting(self):
     nam_hien_tai = datetime.now().year
     tuoi = nam_hien_tai - self.yearold
     return f"Chào bạn {self.name}, năm nay bạn {tuoi} tuổi!"
    def bmi_show(self):
     bmi = self.weight / (self.height**2)
     if bmi < 18.5:
        print("underweight")
     elif 18.5< bmi < 24.9:
        print("normal")
     elif 25< bmi < 29.9:
        print("overweight")
     else:
        print("obese")  
     return f"Chỉ số BMI của bạn là: {bmi}"


p1 = Person("dang viet anh", 2004, 1.65, 65)
print(p1.greeting())
print(p1.bmi_show())

#bai2
def max_min(url):
   try:
      with open(url,"r") as f:
         numbers =[float(num) for num in f.read().split()]
      return numbers
   except Exception as e:
      raise ValueError("loi file", e )
def writenumbers(url, numbers):
   try:
      with open(url, 'w') as f:
         f.write("".join(map(str,numbers)))
   except Exception as e:
      raise ValueError("loi file", e)
def swap(numbers):
   if  not numbers:
      return numbers
   max_value = max(numbers)
   min_value = min(numbers)
   max_index = numbers.index(max_value)
   min_index = numbers.index(min_value)
    
    # Đổi chỗ
   numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]
   return numbers

input_file="text.txt"
output_file="text2.txt"
try:
   numbers =max_min(input_file)
   update_numbers=swap(numbers)
   writenumbers(output_file, update_numbers)

except Exception as e:
   str(e)



