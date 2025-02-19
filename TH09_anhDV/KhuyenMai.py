from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox, QTableView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from connection import get_connection
from Home_ui import Ui_Dialog  # Import giao diện từ Home_ui.py

class KhuyenMaiApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Kết nối các nút với phương thức
        self.ui.btnadd_4.clicked.connect(self.add_promotion)
        self.ui.btnedit_4.clicked.connect(self.edit_promotion)
        self.ui.btndel_4.clicked.connect(self.delete_promotion)
        self.ui.btntk_4.clicked.connect(self.search_promotion)

        # Khởi tạo model cho QTableView
        self.model = QStandardItemModel()
        self.ui.tableView_6.setModel(self.model)

        # Tải dữ liệu khuyến mãi khi mở giao diện
        self.load_promotions()

    def load_promotions(self):
        """Tải danh sách khuyến mãi lên QTableView"""
        conn = get_connection()
        if not conn:
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối đến database!")
            return
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM KHUYENMAI")
            rows = cursor.fetchall()

            # Đặt tiêu đề cột
            self.model.clear()
            self.model.setHorizontalHeaderLabels(["Mã KM", "Nội Dung", "Giảm Giá"])

            for row in rows:
                items = [QStandardItem(str(value)) for value in row]
                self.model.appendRow(items)

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi tải dữ liệu: {e}")
        finally:
            cursor.close()
            conn.close()

    def add_promotion(self):
        """Thêm khuyến mãi mới vào database"""
        makm = self.ui.makm.toPlainText().strip()
        noidung = self.ui.noidung.toPlainText().strip()
        giamgia = self.ui.giamgia.toPlainText().strip()

        if not makm or not noidung or not giamgia:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        if not giamgia.isdigit():
            QMessageBox.warning(self, "Lỗi", "Giảm giá phải là số!")
            return

        conn = get_connection()
        if not conn:
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối đến database!")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO KHUYENMAI (MaKM, NoiDung, GiamGia) VALUES (%s, %s, %s)",
                           (makm, noidung, giamgia))
            conn.commit()

            QMessageBox.information(self, "Thành công", "Thêm khuyến mãi thành công!")
            self.clear_inputs()
            self.load_promotions()

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi thêm khuyến mãi: {e}")

        finally:
            cursor.close()
            conn.close()

    def edit_promotion(self):
        """Chỉnh sửa khuyến mãi dựa vào Mã KM"""
        makm = self.ui.makm.toPlainText().strip()
        noidung = self.ui.noidung.toPlainText().strip()
        giamgia = self.ui.giamgia.toPlainText().strip()

        if not makm or not noidung or not giamgia:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        if not giamgia.isdigit():
            QMessageBox.warning(self, "Lỗi", "Giảm giá phải là số!")
            return

        conn = get_connection()
        if not conn:
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối đến database!")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE KHUYENMAI SET NoiDung=%s, GiamGia=%s WHERE MaKM=%s",
                           (noidung, giamgia, makm))
            conn.commit()

            QMessageBox.information(self, "Thành công", "Cập nhật khuyến mãi thành công!")
            self.clear_inputs()
            self.load_promotions()

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi cập nhật khuyến mãi: {e}")

        finally:
            cursor.close()
            conn.close()

    def delete_promotion(self):
        """Xóa khuyến mãi dựa vào Mã KM"""
        makm = self.ui.makm.toPlainText().strip()

        if not makm:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập Mã khuyến mãi để xóa!")
            return

        conn = get_connection()
        if not conn:
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối đến database!")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM KHUYENMAI WHERE MaKM = %s", (makm,))
            conn.commit()

            QMessageBox.information(self, "Thành công", "Xóa khuyến mãi thành công!")
            self.clear_inputs()
            self.load_promotions()

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi xóa khuyến mãi: {e}")

        finally:
            cursor.close()
            conn.close()

    def search_promotion(self):
        """Tìm kiếm khuyến mãi theo Mã KM hoặc Nội Dung"""
        search_text = self.ui.timkiem_4.toPlainText().strip()

        if not search_text:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập từ khóa tìm kiếm!")
            return

        conn = get_connection()
        if not conn:
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối đến database!")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM KHUYENMAI WHERE MaKM = %s OR NoiDung LIKE %s", (search_text, f"%{search_text}%"))
            rows = cursor.fetchall()

            self.model.clear()
            self.model.setHorizontalHeaderLabels(["Mã KM", "Nội Dung", "Giảm Giá"])

            for row in rows:
                items = [QStandardItem(str(value)) for value in row]
                self.model.appendRow(items)

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi tìm kiếm khuyến mãi: {e}")

        finally:
            cursor.close()
            conn.close()

    def clear_inputs(self):
        """Xóa nội dung của các ô nhập liệu"""
        self.ui.makm.clear()
        self.ui.noidung.clear()
        self.ui.giamgia.clear()
        self.ui.timkiem_4.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = KhuyenMaiApp()
    window.show()
    sys.exit(app.exec())
