import sys
import mysql.connector
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from Home_ui import Ui_Dialog

class HistoryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Kết nối MySQL
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test1"
        )
        self.cursor = self.db.cursor()

        # Kết nối sự kiện
        self.ui.btnresult.clicked.connect(self.filter_invoice_history)

    def filter_invoice_history(self):
        """Lọc và hiển thị lịch sử hóa đơn theo ngày bắt đầu và kết thúc."""
        start_date = self.ui.datestart.date().toString("yyyy-MM-dd")
        end_date = self.ui.dateend.date().toString("yyyy-MM-dd")

        if start_date > end_date:
            QMessageBox.warning(self, "Lỗi", "Ngày bắt đầu không thể lớn hơn ngày kết thúc!")
            return

        query = """
            SELECT HOADON.MaHD, HOADON.NgayLap, HOADON.TongTien, COALESCE(CHITIETHOADON.MaKH, 'Không có') AS MaKH
            FROM HOADON
            LEFT JOIN CHITIETHOADON ON HOADON.MaHD = CHITIETHOADON.MaHD
            WHERE HOADON.NgayLap BETWEEN %s AND %s
            ORDER BY HOADON.NgayLap DESC;
        """
        
        self.cursor.execute(query, (start_date, end_date))
        data = self.cursor.fetchall()

        if not data:
            QMessageBox.information(self, "Thông báo", "Không có hóa đơn nào trong khoảng thời gian này.")
            self.ui.tableWidget.setRowCount(0)  # Xóa dữ liệu cũ nếu không có kết quả
            return
        
        # Cập nhật tableWidget
        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Mã HĐ", "Ngày Lập", "Mã KH", "Tổng Tiền"])

        for row, record in enumerate(data):
            for col, value in enumerate(record):
                self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(value)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HistoryApp()
    window.show()
    sys.exit(app.exec())
