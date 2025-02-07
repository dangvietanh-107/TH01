#11
import pandas as pd

# Đường dẫn đến file CSV
path = 'Data_Excersice\CSV\Data_CSV.csv'

# Đọc dữ liệu từ file CSV
data = pd.read_csv(path)

# Hiển thị thông tin về dữ liệu
data.info()

#13
import pandas as pd

# Đường dẫn đến file CSV
path = 'Data_Excersice\CSV\Data_CSV.csv'  # Bạn cần thay đổi đường dẫn này nếu file CSV ở vị trí khác

# Đọc dữ liệu từ file CSV và thiết lập cột 'Personal' làm index
data1 = pd.read_csv(path, index_col=0)  # index_col=0 nghĩa là cột đầu tiên (Personal) được chọn làm index

# Hiển thị thông tin về DataFrame data1
data1.info()

# Hiển thị 5 dòng dữ liệu đầu tiên
data1.head()

#14
import pandas as pd

# Đường dẫn đến file CSV
path = 'Data_Excersice\CSV\Data_CSV.csv'  # Bạn cần thay đổi đường dẫn này nếu file CSV ở vị trí khác

# Đọc dữ liệu từ file CSV, giới hạn số hàng và cột
data2 = pd.read_csv(path, nrows=100, usecols=['Height_cm', 'Weight_kg'])

# Hiển thị thông tin về DataFrame data2
data2.info()

# Hiển thị 5 dòng dữ liệu đầu tiên
data2.head()

#21
import pandas as pd

# Đường dẫn đến file Excel
path_excel = 'Data_Excersice\Data_Excel.xlsx'

# Đọc dữ liệu từ file Excel
data_ex = pd.read_excel(path_excel)

# Hiển thị thông tin về DataFrame data_ex
data_ex.info()

# Hiển thị 5 dòng dữ liệu đầu tiên
data_ex.head()

#23
import pandas as pd

# Đường dẫn đến file Excel
path_excel = 'Data_Excersice\Data_Excel.xlsx'  # Bạn cần thay đổi đường dẫn này nếu file Excel ở vị trí khác

# Đọc dữ liệu từ file Excel với các tùy chọn
data_ex1 = pd.read_excel(path_excel, 
                         sheet_name=0,  # Chọn sheet đầu tiên (sheet có chỉ số 0)
                         usecols=[1, 6, 7, 8, 9, 10],  # Chọn các cột theo chỉ số (0 là cột đầu tiên)
                         index_col=0)  # Chọn cột đầu tiên làm index

# Hiển thị thông tin về DataFrame data_ex1
data_ex1.info()

# Hiển thị 5 dòng dữ liệu đầu tiên
data_ex1.head()

#24
import pandas as pd

# Đường dẫn đến file Excel
path_excel = 'Data_Excersice\Data_Excel.xlsx'  # Bạn cần thay đổi đường dẫn này nếu file Excel ở vị trí khác

# Đọc dữ liệu từ file Excel với các tùy chọn
data_ex3 = pd.read_excel(path_excel, 
                         sheet_name='4080130_02',  # Chọn sheet có tên là '4080130_02'
                         skiprows=9)  # Bỏ qua 9 hàng đầu tiên

# Hiển thị thông tin về DataFrame data_ex3
data_ex3.info()

# Hiển thị 5 dòng dữ liệu đầu tiên
data_ex3.head()

#25
import pandas as pd

# Đường dẫn đến file Excel
path_excel = 'Data_Excersice\Data_Excel.xlsx'  # Bạn cần thay đổi đường dẫn này nếu file Excel ở vị trí khác

# Đọc dữ liệu từ file Excel với tùy chọn không dùng header
data_ex4 = pd.read_excel(path_excel, 
                         sheet_name='4080130_03',  # Chọn sheet có tên là '4080130_03'
                         header=None)  # Không sử dụng dòng đầu tiên làm header

# Hiển thị thông tin về DataFrame data_ex4
data_ex4.info()

# Hiển thị 5 dòng dữ liệu đầu tiên
data_ex4.head()

#26
import pandas as pd

# Đường dẫn đến file Excel
path_excel = 'Data_Excersice\Data_Excel.xlsx'  # Bạn cần thay đổi đường dẫn này nếu file Excel ở vị trí khác

# Đọc dữ liệu từ file Excel với các tùy chọn
data_ex41 = pd.read_excel(path_excel, 
                         sheet_name='4080130_03',  # Chọn sheet có tên là '4080130_03'
                         header=None,  # Không sử dụng dòng đầu tiên làm header
                         usecols=[1, 6, 7, 8, 9, 10],  # Chọn các cột theo chỉ số (0 là cột đầu tiên)
                         names=['Mã SV', 'A', 'B1', 'B2', 'C1', 'C2'],  # Đặt tên cột
                         index_col=0)  # Chọn cột đầu tiên làm index

# Hiển thị thông tin về DataFrame data_ex41
data_ex41.info()

# Hiển thị 5 dòng dữ liệu đầu tiên
data_ex41.head()

#31
import pandas as pd

# Đường dẫn đến file JSON
path_json = 'Data_Excersice\json_Data_product.json'

# Đọc dữ liệu từ file JSON vào biến DataFrame
data_json = pd.read_json(path_json)

# Hiển thị DataFrame
data_json

import pandas as pd

# Đường dẫn đến file JSON
path_json = 'Data_Excersice\json_Data_product.json'

# Đọc dữ liệu từ file Json vào biển DataFrame
# Sử dụng tham số orient='index'
data_json1 = pd.read_json(path_json, orient='index')

# Hiển thị DataFrame
data_json1

#32
# Hoặc Sử dụng thư viện json làm việc với dữ liệu json
import json

# Đường dẫn đến file JSON
path_json = 'Data_Excersice\json_Data_product.json'  # Bạn cần thay đổi đường dẫn này nếu file JSON ở vị trí khác

with open(path_json, 'r') as myfile:
    data = myfile.read()

# Đọc dữ liệu vào biến obj
obj = json.loads(data)

# Kiểm tra kiểu dữ liệu của obj
print(type(obj))  # Kết quả sẽ là <class 'dict'>

# Lấy giá trị của key = 'Product'
print(obj['Product'])

# Lấy giá trị của key = 'Price'
print(obj['Price'])

#38
# Lấy dữ liệu tỷ lệ hối đoái
import pandas as pd
import requests as rq

# url api
url_api = 'http://api.exchangeratesapi.io/v1/latest?access_key=06a81a333abfe2ac294f7bc88bac1ec9'

# Lấy dữ liệu theo url_api
result_money = rq.get(url_api)

# check status của request
print(result_money.status_code)  # Kết quả là 200 nếu thành công

# Chuyển đổi dữ liệu sang kiểu string
data_text = result_money.text

# Chuyển đổi dữ liệu sang kiểu json
data_json = result_money.json()

print('Text: ', data_text)
print('--------------------------------------------------')
print('Json:', data_json)

# Chuyển đổi dữ liệu json sang kiểu DataFrame
df = pd.DataFrame(data_json)
print(df.head(10))

#39
# Truyền tham số cho url

# Lấy tỷ giá của một số ngoại tệ:
# 1. GBP (Bảng Anh)
# 2. JPY (Yên Nhật)
# 3. MYR (Ringgit Malaysia)
# 4. THB (Bạt Thái Lan)
# 5. KRW (Won - Hàn Quốc)
# 6. VND (Việt Nam Đồng)

import pandas as pd
import requests as rq

# url api
url_api = 'http://api.exchangeratesapi.io/v1/latest?access_key=06a81a333abfe2ac294f7bc88bac1ec9'

result_money1 = rq.get(url_api, params={'symbols': 'USD, JPY, THB, VND, MYR, GBP, KRW'})

data_json1 = result_money1.json()

df1 = pd.DataFrame(data_json1)

print(df1.head(10))

#45
# Truyền tham số cho url

# Lấy tỷ giá của một số ngoại tệ:
# 1. GBP (Bảng Anh)
# 2. JPY (Yên Nhật)
# 3. MYR (Ringgit Malaysia)
# 4. THB (Bạt Thái Lan)
# 5. KRW (Won - Hàn Quốc)
# 6. VND (Việt Nam Đồng)

import pandas as pd
import requests as rq

# url api
url_api = 'http://api.exchangeratesapi.io/v1/latest?access_key=06a81a333abfe2ac294f7bc88bac1ec9'

result_money1 = rq.get(url_api, params={'symbols': 'USD, JPY, THB, VND, MYR, GBP, KRW'})

data_json1 = result_money1.json()

df1 = pd.DataFrame(data_json1)

print(df1.head(10))

#46
# Lấy dữ liệu chuyển vào các biến kiểu list
dt_time, dt_rain, dt_t2m, dt_tm, dt_tx = [], [], [], [], []

for i in data_mg:
    dt_time.append(str(i['Time']))
    dt_rain.append(i['Rain'])
    dt_t2m.append(i['T2m'])
    dt_tm.append(i['Tm'])
    dt_tx.append(i['Tx'])

# Kết hợp các biến list lại
ziplist_water = list(zip(dt_time, dt_rain, dt_t2m, dt_tm, dt_tx))

# Chuyển về dữ liệu DataFrame
import pandas as pd

df = pd.DataFrame(ziplist_water,
                  columns=['Time', 'Rain', 'T2m', 'Tm', 'Tx'],
                  index=None)

# Hiển thị 5 dòng dữ liệu đầu tiên
print(df.head())

# Hiển thị thông tin về DataFrame
df.info()

#51

#52
# Đọc tập dữ liệu Boston House Prices
import sklearn.datasets as datask

X, y = datask.load_boston(return_X_y=True)

print(type(X))
print('Kích thước dữ liệu đầu vào (features):', X.shape)
print('Kích thước dữ liệu đầu ra (target):', y.shape)

#54
# Đọc tập dữ liệu Iris Dataset
import sklearn.datasets as datask

X_iris, y_iris = datask.load_iris(return_X_y=True)

print(type(X_iris))
print('Kích thước dữ liệu đầu vào (features):', X_iris.shape)
print('Kích thước dữ liệu đầu ra (target):', y_iris.shape)

print('Bộ dữ liệu 1)', X_iris[1,:], '--',y_iris[1])
print('Bộ dữ liệu 55)', X_iris[55,:], '--',y_iris[55])
print('Bộ dữ liệu 111)', X_iris[111,:], '--',y_iris[111])

#60
# load module datasets trong thư viện sklearn
import sklearn.datasets as datask

# Tạo dữ liệu mẫu cho bài toán PHÂN LỚP
# Với 200 mẫu, đầu vào 5 thuộc tính, phân thành 2 lớp
X_features, y_target = datask.make_classification(n_samples=200,
                                                 n_features=5,
                                                 n_classes=2)

print(X_features[:10, :])
print(y_target[:10])
#61
# Load module datasets from sklearn library
import sklearn.datasets as datask

# Create sample data for REGRESSION task
X_features, y_target, coeff = datask.make_regression(n_samples=200,
                                                    n_features=5,
                                                    n_informative=3,
                                                    n_targets=1,
                                                    noise=0.0,
                                                    coef=True,
                                                    random_state=1)

print(X_features[:10, :])
print(y_target[:10])
