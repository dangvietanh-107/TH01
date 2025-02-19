import sys
import mysql.connector
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox

class LoginRegisterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Đăng nhập & Đăng ký")
        self.setGeometry(100, 100, 400, 300)
        
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test1"
        )
        self.cursor = self.db.cursor()
        
        self.layout = QVBoxLayout()
        
        self.label_user = QLabel("Tên Đăng Nhập:")
        self.layout.addWidget(self.label_user)
        self.input_user = QLineEdit()
        self.layout.addWidget(self.input_user)
        
        self.label_pass = QLabel("Mật Khẩu:")
        self.layout.addWidget(self.label_pass)
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.layout.addWidget(self.input_pass)
        
        self.label_email = QLabel("Email:")
        self.layout.addWidget(self.label_email)
        self.input_email = QLineEdit()
        self.layout.addWidget(self.input_email)
        
        self.btn_register = QPushButton("Đăng Ký")
        self.btn_register.clicked.connect(self.register_user)
        self.layout.addWidget(self.btn_register)
        
        self.btn_login = QPushButton("Đăng Nhập")
        self.btn_login.clicked.connect(self.login_user)
        self.layout.addWidget(self.btn_login)
        
        self.setLayout(self.layout)
    
    def register_user(self):
        username = self.input_user.text().strip()
        password = self.input_pass.text().strip()
        email = self.input_email.text().strip()
        
        if username and password and email:
            try:
                self.cursor.execute("INSERT INTO DANGNHAP (TenDangNhap, MatKhau, Email) VALUES (%s, %s, %s)", (username, password, email))
                self.db.commit()
                QMessageBox.information(self, "Thành công", "Đăng ký thành công!")
            except mysql.connector.IntegrityError:
                QMessageBox.warning(self, "Lỗi", "Tên đăng nhập hoặc email đã tồn tại!")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
    
    def login_user(self):
        username = self.input_user.text().strip()
        password = self.input_pass.text().strip()
        
        if username and password:
            self.cursor.execute("SELECT * FROM DANGNHAP WHERE TenDangNhap=%s AND MatKhau=%s", (username, password))
            user = self.cursor.fetchone()
            
            if user:
                QMessageBox.information(self, "Thành công", "Đăng nhập thành công!")
                self.open_product_page()
            else:
                QMessageBox.warning(self, "Lỗi", "Sai tên đăng nhập hoặc mật khẩu!")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
    
    def open_product_page(self):
        try:
            from product import ProductApp
            self.product_window = ProductApp()
            self.product_window.show()
            self.close()
        except ImportError:
            QMessageBox.critical(self, "Lỗi", "Không thể tải ProductApp. Hãy kiểm tra file product.py!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginRegisterApp()
    window.show()
    sys.exit(app.exec())
