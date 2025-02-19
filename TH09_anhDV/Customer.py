from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox, QTableView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from connection import get_connection
from Home_ui import Ui_Dialog  # Import giao diện từ Home_ui.py

class CustomerApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Kết nối các nút với phương thức
        self.ui.btnadd_3.clicked.connect(self.add_customer)
        self.ui.btnedit_3.clicked.connect(self.edit_customer)
        self.ui.btndel_3.clicked.connect(self.delete_customer)
        self.ui.btntk_3.clicked.connect(self.search_customer)

        # Khởi tạo model cho QTableView
        self.model = QStandardItemModel()
        self.ui.tableView_5.setModel(self.model)

        # Tải dữ liệu khách hàng khi mở giao diện
        self.load_customers()

    def load_customers(self):
        """Tải danh sách khách hàng lên QTableView"""
        conn = get_connection()
        if not conn:
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối đến database!")
            return
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM KHACHHANG")
            rows = cursor.fetchall()

            # Đặt tiêu đề cột
            self.model.clear()
            self.model.setHorizontalHeaderLabels(["Mã KH", "Họ Tên", "SĐT", "Địa Chỉ", "Email", "Ngày ĐK"])

            for row in rows:
                items = [QStandardItem(str(value)) for value in row]
                self.model.appendRow(items)

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi tải dữ liệu: {e}")
        finally:
            cursor.close()
            conn.close()

    def add_customer(self):
        """Thêm khách hàng mới vào database"""
        name = self.ui.hotenkh.toPlainText().strip()
        phone = self.ui.sdt.toPlainText().strip()
        address = self.ui.diachi.toPlainText().strip()
        email = self.ui.email.toPlainText().strip()

        if not name or not phone or not email:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin bắt buộc!")
            return

        conn = get_connection()
        if not conn:
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối đến database!")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO KHACHHANG (HoTen, SDT, DiaChi, Email) VALUES (%s, %s, %s, %s)",
                           (name, phone, address, email))
            conn.commit()

            QMessageBox.information(self, "Thành công", "Thêm khách hàng thành công!")
            self.clear_inputs()
            self.load_customers()

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi thêm khách hàng: {e}")

        finally:
            cursor.close()
            conn.close()
    def on_tab_activated(self):
        # Xử lý khi tab được kích hoạt
        print("Home tab được kích hoạt")
        # Thêm code xử lý của bạn ở đây
    def edit_customer(self):
        """Chỉnh sửa khách hàng dựa vào Mã KH"""
        customer_id = self.ui.makh.toPlainText().strip()
        name = self.ui.hotenkh.toPlainText().strip()
        phone = self.ui.sdt.toPlainText().strip()
        address = self.ui.diachi.toPlainText().strip()
        email = self.ui.email.toPlainText().strip()

        if not customer_id or not name or not phone or not email:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        conn = get_connection()
        if not conn:
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối đến database!")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE KHACHHANG SET HoTen=%s, SDT=%s, DiaChi=%s, Email=%s WHERE MaKH=%s",
                           (name, phone, address, email, customer_id))
            conn.commit()

            QMessageBox.information(self, "Thành công", "Cập nhật khách hàng thành công!")
            self.clear_inputs()
            self.load_customers()

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi cập nhật khách hàng: {e}")

        finally:
            cursor.close()
            conn.close()

    def delete_customer(self):
        """Xóa khách hàng dựa vào Mã KH"""
        customer_id = self.ui.makh.toPlainText().strip()

        if not customer_id:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập Mã khách hàng để xóa!")
            return

        conn = get_connection()
        if not conn:
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối đến database!")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM KHACHHANG WHERE MaKH = %s", (customer_id,))
            conn.commit()

            QMessageBox.information(self, "Thành công", "Xóa khách hàng thành công!")
            self.clear_inputs()
            self.load_customers()

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi xóa khách hàng: {e}")

        finally:
            cursor.close()
            conn.close()

    def search_customer(self):
        """Tìm kiếm khách hàng theo Mã KH hoặc Họ tên"""
        search_text = self.ui.timkiem_3.toPlainText().strip()

        if not search_text:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập từ khóa tìm kiếm!")
            return

        conn = get_connection()
        if not conn:
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối đến database!")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM KHACHHANG WHERE MaKH = %s OR HoTen LIKE %s", (search_text, f"%{search_text}%"))
            rows = cursor.fetchall()

            self.model.clear()
            self.model.setHorizontalHeaderLabels(["Mã KH", "Họ Tên", "SĐT", "Địa Chỉ", "Email", "Ngày ĐK"])

            for row in rows:
                items = [QStandardItem(str(value)) for value in row]
                self.model.appendRow(items)

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi tìm kiếm khách hàng: {e}")

        finally:
            cursor.close()
            conn.close()

    def clear_inputs(self):
        """Xóa nội dung của các ô nhập liệu"""
        self.ui.makh.clear()
        self.ui.hotenkh.clear()
        self.ui.sdt.clear()
        self.ui.diachi.clear()
        self.ui.email.clear()
        self.ui.timkiem_3.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = CustomerApp()
    window.show()
    sys.exit(app.exec())
