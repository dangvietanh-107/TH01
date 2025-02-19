import sys
import mysql.connector
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QTabWidget
from Home_ui import Ui_Dialog
from Customer import CustomerApp
from History import HistoryApp
from Hoadon import HoadonApp
from Home import HomeApp
from KhuyenMai import KhuyenMaiApp


class HouseApp(QTabWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setCurrentIndex(0)
        
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="test1"
            )
            self.cursor = self.db.cursor()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Lỗi Kết Nối", f"Không thể kết nối đến database: {err}")
            sys.exit(1)    
        self.ui.btnkq.clicked.connect(self.calculate_statistics)
        self.ui.btnlogout.clicked.connect(self.logout)
        
    
    def calculate_statistics(self):
        """Tính toán doanh thu, số sản phẩm, số khách hàng và số mã khuyến mãi"""
        try:
            start_date = self.ui.datestart_4.date().toString("yyyy-MM-dd")
            end_date = self.ui.dateend_4.date().toString("yyyy-MM-dd")
            
            if start_date > end_date:
                QMessageBox.warning(self, "Lỗi", "Ngày bắt đầu không thể lớn hơn ngày kết thúc!")
                return
            
            # Tính tổng doanh thu
            self.cursor.execute("SELECT SUM(TongTien) FROM HOADON WHERE DATE(NgayLap) BETWEEN %s AND %s", (start_date, end_date))
            revenue = self.cursor.fetchone()[0] or 0
            self.ui.label_92.setText(f"{revenue:,.0f} VND")
            
            # Tính số lượng sản phẩm đã bán
            self.cursor.execute("SELECT SUM(SoLuong) FROM CHITIETHOADON WHERE MaHD IN (SELECT MaHD FROM HOADON WHERE DATE(NgayLap) BETWEEN %s AND %s)", (start_date, end_date))
            total_products = self.cursor.fetchone()[0] or 0
            self.ui.label_96.setText(str(total_products))
            
            # Tính tổng số khách hàng
            self.cursor.execute("SELECT COUNT(DISTINCT MaKH) FROM CHITIETHOADON WHERE MaHD IN (SELECT MaHD FROM HOADON WHERE DATE(NgayLap) BETWEEN %s AND %s)", (start_date, end_date))
            total_customers = self.cursor.fetchone()[0] or 0
            self.ui.label_97.setText(str(total_customers))
            
            # Tính tổng số mã khuyến mãi đã sử dụng
            self.cursor.execute("SELECT COUNT(DISTINCT MaKM) FROM CHITIETHOADON WHERE MaKM IS NOT NULL AND MaHD IN (SELECT MaHD FROM HOADON WHERE DATE(NgayLap) BETWEEN %s AND %s)", (start_date, end_date))
            total_discounts = self.cursor.fetchone()[0] or 0
            self.ui.label_98.setText(str(total_discounts))
            
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Có lỗi xảy ra khi tính toán: {str(e)}")
    def logout(self):
        """Hiển thị hộp thoại xác nhận đăng xuất và quay về trang đăng nhập"""
        reply = QMessageBox.question(self, "Xác nhận", "Bạn có muốn đăng xuất?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            from login import LoginApp  # Import tại đây để tránh lỗi vòng lặp
            self.close()
            self.login_window = LoginApp()
            self.login_window.show()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HouseApp()
    window.show()
    sys.exit(app.exec())
