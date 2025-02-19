import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem, QFileDialog, QListWidgetItem
from PyQt6.QtCore import Qt
from Home_ui import Ui_Dialog
from connection import get_connection

class HistoryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.db = get_connection()
        if not self.db:
            sys.exit(1)
        
        self.cursor = self.db.cursor()
            
        self.ui.btnresult.clicked.connect(self.filter_invoice_history)
        self.ui.listWidget_2.itemClicked.connect(self.show_invoice_details)
        self.ui.btnfile.clicked.connect(self.export_to_excel)
    
    def filter_invoice_history(self):
        try:
            start_date = self.ui.datestart.date().toString("yyyy-MM-dd")
            end_date = self.ui.dateend.date().toString("yyyy-MM-dd")
            
            if start_date > end_date:
                QMessageBox.warning(self, "Lỗi", "Ngày bắt đầu không thể lớn hơn ngày kết thúc!")
                return
            
            query = """
                SELECT MaHD, DATE(NgayLap), TongTien 
                FROM HOADON 
                WHERE DATE(NgayLap) BETWEEN %s AND %s 
                ORDER BY NgayLap DESC;
            """
            self.cursor.execute(query, (start_date, end_date))
            invoices = self.cursor.fetchall()
            
            self.ui.listWidget_2.clear()
            
            if not invoices:
                QMessageBox.information(self, "Thông báo", "Không có hóa đơn nào trong khoảng thời gian này.")
                return
            
            for invoice in invoices:
                MaHD, NgayLap, TongTien = invoice
                self.ui.listWidget_2.addItem(f"Hóa đơn {MaHD} - {NgayLap} - {TongTien:,.0f} VND")
                
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Có lỗi xảy ra khi lọc hóa đơn: {str(e)}")
    
    def show_invoice_details(self, item):
        try:
            MaHD = item.text().split(" - ")[0].split()[-1]
            
            query = """
                SELECT 
                    CHITIETHOADON.MaSP,
                    SANPHAM.TenSP,
                    CHITIETHOADON.SoLuong,
                    CHITIETHOADON.MaKM,
                    CHITIETHOADON.ThanhTien
                FROM CHITIETHOADON
                JOIN SANPHAM ON CHITIETHOADON.MaSP = SANPHAM.MaSP
                WHERE CHITIETHOADON.MaHD = %s;
            """
            self.cursor.execute(query, (MaHD,))
            details = self.cursor.fetchall()
            
            self.ui.listWidget_2.clear()
            
            if not details:
                QMessageBox.information(self, "Thông báo", "Không tìm thấy chi tiết hóa đơn!")
                return
            
            for record in details:
                self.ui.listWidget_2.addItem(" | ".join(str(value) for value in record))
            
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Có lỗi xảy ra khi hiển thị chi tiết: {str(e)}")
    
    def export_to_excel(self):
        try:
            items = [self.ui.listWidget_2.item(i).text().split(" | ") for i in range(self.ui.listWidget_2.count())]
            
            if not items:
                QMessageBox.warning(self, "Lỗi", "Không có dữ liệu để xuất!")
                return
            
            df = pd.DataFrame(items, columns=["Mã SP", "Tên Sản Phẩm", "Số Lượng", "Mã KM", "Thành Tiền"])
            
            file_path, _ = QFileDialog.getSaveFileName(self, "Lưu file", "", "Excel Files (*.xlsx);;All Files (*)")
            
            if file_path:
                df.to_excel(file_path, index=False)
                QMessageBox.information(self, "Thành công", "Xuất file Excel thành công!")
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Có lỗi khi xuất file: {str(e)}")
    
    def closeEvent(self, event):
        try:
            if hasattr(self, 'cursor'):
                self.cursor.close()
            if hasattr(self, 'db'):
                self.db.close()
        except Exception as e:
            print(f"Lỗi khi đóng kết nối: {str(e)}")
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HistoryApp()
    window.show()
    sys.exit(app.exec())