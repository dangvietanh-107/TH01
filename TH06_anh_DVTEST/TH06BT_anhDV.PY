import pandas as pd

def read_loan_data(file_path='loan_data.xlsx'):
    try:
        # Đọc file Excel với pd.read_excel
        df = pd.read_excel(file_path, 
                         sheet_name=0,  # Đọc sheet đầu tiên
                         names=['loan_amnt', 'term', 'int_rate', 'emp_length_home_ownership',
                               'annual_inc', 'purpose', 'addr_state', 'dti', 
                               'delinq_2yrs', 'revol_util', 'total_acc', 'bad_loan',
                               'longest_credit_line', 'verification_status'])
        
        # Hiển thị thông tin cơ bản về DataFrame
        print("\nThông tin cơ bản về dữ liệu:")
        print(f"Số lượng bản ghi: {len(df)}")
        print(f"Số lượng cột: {len(df.columns)}")
        
        # Hiển thị 5 dòng đầu tiên của dữ liệu
        print("\n5 dòng đầu tiên của dữ liệu:")
        print(df.head())
        
        return df
        
    except FileNotFoundError:
        print(f"Không tìm thấy file {file_path}")
        return None
    except Exception as e:
        print(f"Có lỗi xảy ra: {str(e)}")
        return None

# Gọi hàm để đọc dữ liệu
df = read_loan_data()

# Nếu đọc dữ liệu thành công, thực hiện phân tích
if df is not None:
    print("\nThống kê cơ bản về dữ liệu số:")
    print(df.describe())

#18
import pandas as pd

def split_loan_data(file_path='loan_data.xlsx'):
    try:
        # Đọc file Excel
        df = pd.read_excel(file_path)
        
        # In ra tên các cột có trong DataFrame để kiểm tra
        print("Các cột có trong DataFrame:")
        print(df.columns.tolist())
        
        # Xác định các cột số và cột object dựa trên kiểu dữ liệu thực tế
        numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
        object_columns = df.select_dtypes(include=['object']).columns
        
        # Tạo hai DataFrame riêng biệt
        df_number = df[numeric_columns].copy()
        df_object = df[object_columns].copy()
        
        # Hiển thị 5 dòng đầu của df_number
        print("\n5 dòng đầu tiên của df_number:")
        print(df_number.head())
        
        # Hiển thị 5 dòng đầu của df_object
        print("\n5 dòng đầu tiên của df_object:")
        print(df_object.head())
        
        return df_number, df_object
        
    except FileNotFoundError:
        print(f"Không tìm thấy file {file_path}")
        return None, None
    except Exception as e:
        print(f"Có lỗi xảy ra: {str(e)}")
        return None, None

# Gọi hàm để đọc và tách dữ liệu
df_number, df_object = split_loan_data()

# Kiểm tra kết quả
if df_number is not None and df_object is not None:
    print("\nKích thước của df_number:", df_number.shape)
    print("Kích thước của df_object:", df_object.shape)