from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox, QTableView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from connection import get_connection
from Home_ui import Ui_Dialog  # Import giao diện từ Home_ui.py
from Customer import CustomerApp  # Import trang khách hàng

class HomeApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Kết nối các nút với phương thức
        self.ui.btnadd.clicked.connect(self.add_product)
        self.ui.btnedit.clicked.connect(self.edit_product)
        self.ui.btndel.clicked.connect(self.delete_product)
        self.ui.btntk.clicked.connect(self.search_product)

        # Khởi tạo model cho QTableView
        self.model = QStandardItemModel()
        self.ui.tableView_2.setModel(self.model)

        # Tải dữ liệu sản phẩm khi mở giao diện
        self.load_products()

    def load_products(self):
        """Tải danh sách sản phẩm lên QTableView"""
        conn = get_connection()
        if not conn:
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối đến database!")
            return
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM SANPHAM")
            rows = cursor.fetchall()

            # Đặt tiêu đề cột
            self.model.clear()
            self.model.setHorizontalHeaderLabels(["Mã SP", "Tên SP", "Hãng SX", "Giá", "Số Lượng", "Mô Tả", "Camera", "Pin", "RAM"])

            for row in rows:
                items = [QStandardItem(str(value)) for value in row]
                self.model.appendRow(items)

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi tải dữ liệu: {e}")
        finally:
            cursor.close()
            conn.close()

    def add_product(self):
        """Thêm sản phẩm mới vào database"""
        name = self.ui.tensp.toPlainText().strip()
        brand = self.ui.hangsx.toPlainText().strip()
        price = self.ui.gia.toPlainText().strip()
        quantity = self.ui.soluong.toPlainText().strip()
        description = self.ui.mota.toPlainText().strip()
        camera = self.ui.camera.toPlainText().strip()
        battery = self.ui.pin.toPlainText().strip()
        ram = self.ui.ram.toPlainText().strip()

        if not name or not brand or not price or not quantity:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin bắt buộc!")
            return

        conn = get_connection()
        if not conn:
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối đến database!")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO SANPHAM (TenSP, HangSX, Gia, SoLuong, MoTa, Camera, Pin, RAM) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                           (name, brand, price, quantity, description, camera, battery, ram))
            conn.commit()

            QMessageBox.information(self, "Thành công", "Thêm sản phẩm thành công!")
            self.clear_inputs()
            self.load_products()

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi thêm sản phẩm: {e}")

        finally:
            cursor.close()
            conn.close()

    def edit_product(self):
        """Chỉnh sửa sản phẩm dựa vào Mã sản phẩm"""
        product_id = self.ui.masp.toPlainText().strip()
        name = self.ui.tensp.toPlainText().strip()
        brand = self.ui.hangsx.toPlainText().strip()
        price = self.ui.gia.toPlainText().strip()
        quantity = self.ui.soluong.toPlainText().strip()
        description = self.ui.mota.toPlainText().strip()
        camera = self.ui.camera.toPlainText().strip()
        battery = self.ui.pin.toPlainText().strip()
        ram = self.ui.ram.toPlainText().strip()

        if not product_id or not name or not brand or not price or not quantity:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        conn = get_connection()
        if not conn:
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối đến database!")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE SANPHAM SET TenSP=%s, HangSX=%s, Gia=%s, SoLuong=%s, MoTa=%s, Camera=%s, Pin=%s, RAM=%s WHERE MaSP=%s",
                           (name, brand, price, quantity, description, camera, battery, ram, product_id))
            conn.commit()

            QMessageBox.information(self, "Thành công", "Cập nhật sản phẩm thành công!")
            self.clear_inputs()
            self.load_products()

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi cập nhật sản phẩm: {e}")

        finally:
            cursor.close()
            conn.close()

    def delete_product(self):
        """Xóa sản phẩm dựa vào Mã sản phẩm"""
        product_id = self.ui.masp.toPlainText().strip()

        if not product_id:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập Mã sản phẩm để xóa!")
            return

        conn = get_connection()
        if not conn:
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối đến database!")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM SANPHAM WHERE MaSP = %s", (product_id,))
            conn.commit()

            QMessageBox.information(self, "Thành công", "Xóa sản phẩm thành công!")
            self.clear_inputs()
            self.load_products()

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi xóa sản phẩm: {e}")

        finally:
            cursor.close()
            conn.close()

    def search_product(self):
        """Tìm kiếm sản phẩm theo Mã SP hoặc Tên SP"""
        search_text = self.ui.timkiem.toPlainText().strip()

        if not search_text:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập từ khóa tìm kiếm!")
            return

        conn = get_connection()
        if not conn:
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối đến database!")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM SANPHAM WHERE MaSP = %s OR TenSP LIKE %s", (search_text, f"%{search_text}%"))
            rows = cursor.fetchall()

            self.model.clear()
            self.model.setHorizontalHeaderLabels(["Mã SP", "Tên SP", "Hãng SX", "Giá", "Số Lượng", "Mô Tả", "Camera", "Pin", "RAM"])

            for row in rows:
                items = [QStandardItem(str(value)) for value in row]
                self.model.appendRow(items)

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi tìm kiếm sản phẩm: {e}")

        finally:
            cursor.close()
            conn.close()

    def clear_inputs(self):
        """Xóa nội dung của các ô nhập liệu"""
        self.ui.masp.clear()
        self.ui.tensp.clear()
        self.ui.hangsx.clear()
        self.ui.gia.clear()
        self.ui.soluong.clear()
        self.ui.mota.clear()
        self.ui.camera.clear()
        self.ui.pin.clear()
        self.ui.ram.clear()
        self.ui.timkiem.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = HomeApp()
    window.show()
    sys.exit(app.exec())
