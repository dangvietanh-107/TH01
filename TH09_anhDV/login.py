from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from connection import get_connection
from login_ui import Ui_Dialog  # Tách file UI ra `login_ui.py`

class LoginApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Kết nối các nút với phương thức
        self.ui.login.clicked.connect(self.login_user)
        self.ui.register_2.clicked.connect(self.goto_register)
        self.ui.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def login_user(self):
        username = self.ui.username.toPlainText().strip()
        password = self.ui.password.text().strip()

        # Kiểm tra nhập liệu
        if not username or not password:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        # Kết nối database
        conn = get_connection()
        if not conn:
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối đến database!")
            return

        try:
            cursor = conn.cursor()
            # Kiểm tra username và password trong database
            cursor.execute("SELECT * FROM DANGNHAP WHERE TenDangNhap = %s AND MatKhau = %s", (username, password))
            user = cursor.fetchone()

            if user:
                QMessageBox.information(self, "Thành công", "Đăng nhập thành công!")
                self.goto_home()
            else:
                QMessageBox.warning(self, "Lỗi", "Tên đăng nhập hoặc mật khẩu không chính xác!")

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi đăng nhập: {e}")

        finally:
            cursor.close()
            conn.close()

    def goto_register(self):
        from Register import RegisterApp  # Import trang đăng ký
        self.close()
        self.register_window = RegisterApp()
        self.register_window.show()

    def goto_home(self):
        from TabApp import TabApp  # Mở giao diện chính thay vì HouseApp
        self.hide()
        self.tab_window = TabApp()
        self.tab_window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec())
