#2.2.1
import pandas as pd

def read_loan_data(file_path):
    """
    Read loan data from CSV file with specified parameters
    
    Parameters:
    file_path (str): Path to the CSV file
    
    Returns:
    pandas.DataFrame: DataFrame containing the loan data
    """
    # Read CSV file into DataFrame
    df = pd.read_csv(file_path)
    
    # Verify column names match expected format
    expected_columns = [
        'loan_amnt', 'term', 'int_rate', 'emp_length', 'home_ownership',
        'annual_inc', 'purpose', 'addr_state', 'dti', 'delinq_2yrs',
        'revol_util', 'total_acc', 'bad_loan', 'longest_credit_line',
        'verification_status'
    ]
    
    # Basic data validation
    if not all(col in df.columns for col in expected_columns):
        raise ValueError("CSV file does not contain all required columns")
    
    # Return the DataFrame
    return df

# Example usage
try:
    # Read the CSV file
    loan_data = read_loan_data('csv_Data_Loan.csv')
    
    # Display first few rows and basic information
    print("First few rows of the data:")
    print(loan_data.head())
    
    print("\nDataset information:")
    print(loan_data.info())
    
    print("\nBasic statistics:")
    print(loan_data.describe())

except FileNotFoundError:
    print("Error: CSV file not found")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
#2.2.2
import pandas as pd

try:
    # Đọc file CSV - thêm encoding để tránh lỗi đọc file
    df = pd.read_csv('Data_Loan.csv', encoding='utf-8')
    
    # Định nghĩa các cột số
    df_number = df[[
        'loan_amnt',
        'int_rate',
        'emp_length', 
        'annual_inc',
        'dti',
        'delinq_2yrs',
        'revol_util',
        'total_acc',
        'bad_loan',
        'longest_credit_line'
    ]]
    
    # Định nghĩa các cột object
    df_object = df[[
        'term',
        'home_ownership',
        'purpose',
        'addr_state',
        'verification_status'
    ]]
    
    # In kết quả
    print("=== 5 dòng đầu của df_number ===")
    print(df_number.head())
    print("\n=== 5 dòng đầu của df_object ===")
    print(df_object.head())

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'Data_Loan.csv'. Hãy kiểm tra lại tên file và vị trí file.")
except pd.errors.EmptyDataError:
    print("Lỗi: File CSV trống.")
except Exception as e:
    print(f"Lỗi không xác định: {str(e)}")
    
#2.3
import pandas as pd

try:
    # Đọc file Excel
    df = pd.read_excel('movies.xlsx', engine='openpyxl')
    
    # Hiển thị thông tin cơ bản về DataFrame
    print("=== Thông tin cơ bản về dữ liệu ===")
    print(df.info())
    
    print("\n=== 5 dòng đầu tiên của dữ liệu ===")
    print(df.head())
    
    # Hiển thị số lượng phim theo từng năm
    print("\n=== Số lượng phim theo năm ===")
    print(df['Year'].value_counts().sort_index())
    
    # Hiển thị số lượng phim theo quốc gia
    print("\n=== Số lượng phim theo quốc gia ===")
    print(df['Country'].value_counts())
    
    # Hiển thị số lượng phim theo Content Rating
    print("\n=== Số lượng phim theo Content Rating ===")
    print(df['Content Rating'].value_counts())

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file Excel. Hãy kiểm tra lại tên file và vị trí file.")
except Exception as e:
    print(f"Lỗi không xác định: {str(e)}")
    
#2.4
import pandas as pd

try:
    # Đọc dữ liệu từ tệp JSON vào DataFrame
    data_json = pd.read_json('json_Data_flights.json')

    # Hiển thị 5 dòng đầu tiên của DataFrame
    print("=== 5 dòng đầu tiên của dữ liệu ===")
    print(data_json.head())

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file JSON. Hãy kiểm tra lại tên file và vị trí file.")
except ValueError as e:
    print(f"Lỗi định dạng tệp JSON: {str(e)}")
except Exception as e:
    print(f"Lỗi không xác định: {str(e)}")
    
#2.5
import requests
import pandas as pd

# URL của API
url = "http://api.plos.org/search"
params = {
    "q": "title:VIRUS",  # Tiêu đề có chứa từ "VIRUS"
    "fl": "id,eissn,author_display,abstract,title_display,score"  # Các trường cần lấy
}

# Gửi yêu cầu GET đến API
response = requests.get(url, params=params)

# Kiểm tra phản hồi từ API
if response.status_code == 200:
    # Parse dữ liệu JSON
    data = response.json()
    docs = data.get("response", {}).get("docs", [])
    
    # Tạo DataFrame từ dữ liệu
    df = pd.DataFrame(docs, columns=["id", "eissn", "author_display", "abstract", "title_display", "score"])
    
    # Lưu DataFrame ra file CSV
    df.to_csv("Paper.csv", index=False, encoding="utf-8")
    print("Dữ liệu đã được lưu vào file Paper.csv")
else:
    print(f"Lỗi khi gọi API: {response.status_code}")
    
#4.1
from pymongo import MongoClient
import pandas as pd

# Kết nối tới MongoDB
client = MongoClient("mongodb://localhost:27017/")  # URI đúng cho MongoDB
db = client["your_database_name"]  # Tên database
collection = db["LC_Meteorology"]  # Tên collection

# Truy vấn dữ liệu
query = {"Id": "LC"}
fields = {"_id": 0, "Time": 1, "Rain": 1, "T2m": 1}
cursor = collection.find(query, fields).sort("Time", -1).limit(1000)

# Kiểm tra có dữ liệu không
if len(list(cursor)) > 0:
    # Quay lại con trỏ nếu đã duyệt qua hết
    cursor.rewind()

    # Chuyển đổi dữ liệu sang DataFrame
    df_lc = pd.DataFrame(list(cursor))
    
    # Hiển thị thông tin DataFrame
    print(df_lc.info())
    print(df_lc.head(10))  # Hiển thị 10 dòng đầu tiên
else:
    print("Không có dữ liệu phù hợp với truy vấn.")
    
#4.2
import pymongo
import pandas as pd

# Kết nối đến MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Thay đổi nếu cần
db = client["your_database_name"]  # Thay đổi tên database của bạn
collection = db["LC_Stations"]

# Đọc toàn bộ dữ liệu từ Collection LC_Stations
data = list(collection.find({}, {"_id": 0}))  # Loại bỏ _id nếu không cần

# Chuyển dữ liệu thành DataFrame
df_station = pd.DataFrame(data)

# Hiển thị DataFrame
print(df_station)

#5.1
from sklearn.datasets import load_wine
import pandas as pd

# Tải dữ liệu Wine dataset
wine = load_wine()

# Đọc dữ liệu dưới dạng ndarray
X_ndarray = wine.data  # Biến đầu vào (features)
y_ndarray = wine.target  # Nhãn của các mẫu

# Chuyển đổi dữ liệu sang DataFrame
df_wine = pd.DataFrame(X_ndarray, columns=wine.feature_names)
df_wine["class"] = y_ndarray  # Thêm cột class

# Hiển thị một số mẫu rượu trong tập dữ liệu
print("Dữ liệu dưới dạng ndarray:")
print(X_ndarray[:5])  # Hiển thị 5 mẫu đầu tiên
print("\nDữ liệu dưới dạng DataFrame:")
print(df_wine.head())  # Hiển thị 5 dòng đầu tiên

#5.2
from sklearn.datasets import (
    fetch_olivetti_faces,
    fetch_20newsgroups,
    fetch_20newsgroups_vectorized,
    fetch_lfw_people,
    fetch_lfw_pairs,
    fetch_covtype,
    fetch_rcv1,
    fetch_kddcup99,
    fetch_california_housing
)
import numpy as np

def explore_dataset(dataset, name):
    """Hàm hiển thị thông tin cơ bản về dataset"""
    print(f"\n=== {name} ===")
    print(f"Kích thước dữ liệu: {dataset.data.shape}")
    if hasattr(dataset, 'target'):
        print(f"Kích thước nhãn: {dataset.target.shape}")
    if hasattr(dataset, 'target_names'):
        print(f"Các nhãn: {dataset.target_names}")
    print(f"Keys có sẵn trong dataset: {dataset.keys()}")
    print("-" * 50)

# 1. Olivetti faces dataset
faces = fetch_olivetti_faces()
explore_dataset(faces, "Olivetti Faces Dataset")

# 2. 20 Newsgroups dataset
newsgroups = fetch_20newsgroups()
explore_dataset(newsgroups, "20 Newsgroups Dataset")

# 3. 20 Newsgroups Vectorized
news_vectorized = fetch_20newsgroups_vectorized()
explore_dataset(news_vectorized, "20 Newsgroups Vectorized Dataset")

# 4. LFW People dataset
lfw_people = fetch_lfw_people(min_faces_per_person=70)
explore_dataset(lfw_people, "LFW People Dataset")

# 5. LFW Pairs dataset
lfw_pairs = fetch_lfw_pairs()
explore_dataset(lfw_pairs, "LFW Pairs Dataset")

# 6. Covertype dataset
covtype = fetch_covtype(data_home='data', random_state=42)
explore_dataset(covtype, "Covertype Dataset")

# 7. RCV1 dataset
rcv1 = fetch_rcv1(random_state=42)
explore_dataset(rcv1, "RCV1 Dataset")

# 8. KDD Cup 99 dataset
kddcup = fetch_kddcup99(random_state=42)
explore_dataset(kddcup, "KDD Cup 99 Dataset")

# 9. California Housing dataset
housing = fetch_california_housing()
explore_dataset(housing, "California Housing Dataset")

#6.1 
# Phần 1: Bài toán phân lớp với Decision Tree
import numpy as np
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier

# Tạo dataset cho bài toán phân lớp
print("=== Bài toán phân lớp ===")
X_clf, y_clf = make_classification(
    n_samples=1000,      # 1000 mẫu
    n_features=8,        # 8 đặc trưng
    n_classes=2,         # 2 lớp
    random_state=42      # Để kết quả có thể tái tạo lại được
)

# Tạo và huấn luyện mô hình Decision Tree
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_clf, y_clf)

# In kết quả
print(f"Kích thước dữ liệu: {X_clf.shape}")
print(f"Số lượng mẫu cho mỗi lớp: {np.bincount(y_clf)}")
print(f"Độ chính xác của mô hình: {dt_model.score(X_clf, y_clf):.4f}")

# Phần 2: Bài toán phân cụm và trực quan hóa
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

def create_cluster_dataset(cluster_std):
    # Tạo dataset
    X, y = make_blobs(
        n_samples=10000,     # 10000 mẫu
        n_features=2,        # 2 đặc trưng
        centers=5,           # 5 tâm cụm
        cluster_std=cluster_std,  # Độ phân tán của cụm
        random_state=42
    )
    
    # Vẽ biểu đồ scatter
    plt.figure(figsize=(10, 6))
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
    plt.colorbar()
    plt.title(f'Biểu đồ phân cụm (cluster_std={cluster_std})')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
    
    return X, y

print("\n=== Bài toán phân cụm ===")
# Tạo dataset với cluster_std = 0.5
X_cluster, y_cluster = create_cluster_dataset(0.5)
print(f"Kích thước dữ liệu phân cụm: {X_cluster.shape}")
print(f"Số lượng cụm: {len(np.unique(y_cluster))}")

# Thử nghiệm với các giá trị cluster_std khác nhau
print("\nThử nghiệm với các giá trị cluster_std khác nhau:")
std_values = [0.1, 0.3, 0.7, 1.0]
for std in std_values:
    print(f"\nTạo dataset với cluster_std = {std}")
    X, y = create_cluster_dataset(std)

print("\nNhận xét về ảnh hưởng của tham số cluster_std:")
print("1. cluster_std = 0.1: Các cụm rất tập trung, ranh giới rõ ràng")
print("2. cluster_std = 0.3: Các cụm vẫn tách biệt nhưng bắt đầu có sự phân tán")
print("3. cluster_std = 0.5: Các cụm phân tán vừa phải, vẫn có thể phân biệt được")
print("4. cluster_std = 0.7: Các cụm bắt đầu có sự chồng lấn")
print("5. cluster_std = 1.0: Các cụm chồng lấn nhiều, khó phân biệt ranh giới")