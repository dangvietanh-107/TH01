import re
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QMessageBox
from connection import get_connection
from Register_ui import Ui_Dialog  # Tách file UI ra thành `Register_ui.py`

class RegisterApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # Kết nối các nút với phương thức
        self.ui.register_2.clicked.connect(self.register_user)
        self.ui.login.clicked.connect(self.goto_login)
        self.ui.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def register_user(self):
        username = self.ui.username.toPlainText().strip()
        password = self.ui.password.text().strip()
        email = self.ui.email.toPlainText().strip()

        # Kiểm tra nhập liệu
        if not username or not password or not email:
            QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin!")
            return
        
        # Kiểm tra độ dài tên đăng nhập
        if len(username) < 6:
            QMessageBox.warning(self, "Lỗi", "Tên đăng nhập phải có ít nhất 6 ký tự!")
            return
        
        # Kiểm tra định dạng email
        email_pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
        if not re.match(email_pattern, email):
            QMessageBox.warning(self, "Lỗi", "Email không hợp lệ! Hãy nhập email có đuôi @gmail.com")
            return

        # Kết nối cơ sở dữ liệu
        conn = get_connection()
        if not conn:
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối đến database!")
            return

        try:
            cursor = conn.cursor()
            # Kiểm tra xem tài khoản đã tồn tại chưa
            cursor.execute("SELECT * FROM DANGNHAP WHERE TenDangNhap = %s OR Email = %s", (username, email))
            if cursor.fetchone():
                QMessageBox.warning(self, "Lỗi", "Tên đăng nhập hoặc Email đã tồn tại!")
                return
            
            # Thêm tài khoản mới vào bảng
            cursor.execute("INSERT INTO DANGNHAP (TenDangNhap, MatKhau, Email) VALUES (%s, %s, %s)",
                           (username, password, email))
            conn.commit()

            # Hiển thị thông báo thành công
            QMessageBox.information(self, "Thành công", "Đăng ký tài khoản thành công!")

            # Xóa nội dung các ô nhập liệu
            self.ui.username.clear()
            self.ui.password.clear()
            self.ui.email.clear()
        
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi đăng ký: {e}")

        finally:
            cursor.close()
            conn.close()

    def goto_login(self):
        from login import LoginApp  # Import trang đăng nhập
        self.close()
        self.login_window = LoginApp()
        self.login_window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = RegisterApp()
    window.show()
    sys.exit(app.exec())
