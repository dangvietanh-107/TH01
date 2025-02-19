import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QVBoxLayout, QPushButton, QInputDialog, QListWidgetItem
from Home_ui import Ui_Dialog
from connection import get_connection

class HoadonApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Kết nối MySQL
        self.db = get_connection()
        if not self.db:
            sys.exit(1)
        self.cursor = self.db.cursor()
        
        # Load dữ liệu
        self.load_products()
        
        # Kết nối các sự kiện
        self.ui.pushButton.clicked.connect(self.process_payment)
        self.ui.textEditkm.textChanged.connect(self.calculate_total)  # Gọi khi nhập mã khuyến mãi
        
        # Thêm chức năng sửa/xóa sản phẩm
        self.ui.listWidget_8.itemDoubleClicked.connect(self.edit_product)
    
    def load_products(self):
        """Hiển thị sản phẩm dạng button với khoảng cách hợp lý."""
        self.cursor.execute("SELECT MaSP, TenSP, Gia FROM SANPHAM")
        products = self.cursor.fetchall()
        layout = QVBoxLayout(self.ui.scrollAreaWidgetContents)

        for masp, tensp, gia in products:
            btn = QPushButton(f"{tensp}")
            btn.setFixedSize(150, 50)  # Nhỏ hơn để gần nhau hơn
            btn.setStyleSheet("background-color: #f0f0f0; border: 1px solid black; font-size: 12px;")
            btn.clicked.connect(lambda checked, m=masp, t=tensp, g=gia: self.select_product(m, t, g))
            layout.addWidget(btn)
    
    def select_product(self, masp, tensp, gia):
        """Chọn số lượng khi bấm vào sản phẩm."""
        quantity, ok = QInputDialog.getInt(self, "Nhập số lượng", f"Số lượng cho {tensp}:", 1, 1, 100)
        if ok:
            total_price = gia * quantity
            item_text = f"{tensp} - SL: {quantity} - Giá: {total_price} VND"
            self.ui.listWidget_8.addItem(QListWidgetItem(item_text))
            self.calculate_total()
    
    def calculate_total(self):
        """Tính tổng tiền hóa đơn và áp dụng giảm giá ngay khi nhập mã."""
        total = 0
        for index in range(self.ui.listWidget_8.count()):
            item_text = self.ui.listWidget_8.item(index).text()
            total += int(float(item_text.split("- Giá: ")[1].split(" VND")[0]))
        
        discount_code = self.ui.textEditkm.toPlainText().strip()
        
        if discount_code:
            if len(discount_code) < 3:  # Đợi đến khi nhập đủ 3 ký tự mới kiểm tra
                self.ui.label_99.setText(f"{total:.2f} VND")  # Giữ nguyên tổng tiền
                return
            self.cursor.execute("SELECT GiamGia FROM KHUYENMAI WHERE MaKM = %s", (discount_code,))
            discount = self.cursor.fetchone()
            if discount:
                discount_percent = discount[0]
                total_after_discount = total - (total * discount_percent / 100)
                self.ui.label_99.setText(f"{total_after_discount:.2f} VND")  # Cập nhật tổng tiền sau giảm giá
            else:
                QMessageBox.warning(self, "Lỗi", "Mã khuyến mãi không hợp lệ!")
                self.ui.textEditkm.clear()  # Xóa mã không hợp lệ
                self.ui.label_99.setText(f"{total:.2f} VND")  # Hiển thị lại tổng tiền gốc
                return
        else:
            self.ui.label_99.setText(f"{total:.2f} VND")  # Nếu không có mã KM, hiển thị tổng tiền gốc
        
    
    def process_payment(self):
        """Xử lý thanh toán và cập nhật database."""
        customer_id = self.ui.textEditkh.toPlainText().strip()
        if not customer_id.isdigit():
            QMessageBox.warning(self, "Lỗi", "Mã khách hàng không hợp lệ!")
            return
        discount_code = self.ui.textEditkm.toPlainText().strip()
        if discount_code:
            self.cursor.execute("SELECT GiamGia FROM KHUYENMAI WHERE MaKM = %s", (discount_code,))
            discount = self.cursor.fetchone()
            if not discount: 
                QMessageBox.warning(self, "Lỗi", "Mã khuyến mãi không hợp lệ! Vui lòng kiểm tra lại.")
                self.ui.textEditkm.clear()
                return
        confirm = QMessageBox.question(self, "Xác nhận", "Bạn có muốn thanh toán không?",QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            total_price = float(self.ui.label_99.text().split(" VND")[0])
            self.cursor.execute("INSERT INTO HOADON (TongTien) VALUES (%s)", (total_price,))
            self.db.commit()
            ma_hd = self.cursor.lastrowid
            
            for index in range(self.ui.listWidget_8.count()):
                item_text = self.ui.listWidget_8.item(index).text()
                product_name, quantity, price = item_text.split(" - ")
                quantity = int(quantity.split(": ")[1])
                price = float(price.split(": ")[1].split(" VND")[0])
                
                self.cursor.execute("SELECT MaSP FROM SANPHAM WHERE TenSP = %s", (product_name,))
                ma_sp = self.cursor.fetchone()[0]
                
                discount_code = self.ui.textEditkm.toPlainText().strip() if self.ui.textEditkm.toPlainText().strip() else None
                
                self.cursor.execute("INSERT INTO CHITIETHOADON (MaHD, MaSP, MaKH, SoLuong, MaKM, ThanhTien) VALUES (%s, %s, %s, %s, %s, %s)",
                                    (ma_hd, ma_sp, customer_id, quantity, discount_code, price))
                
                self.cursor.execute("UPDATE SANPHAM SET SoLuong = SoLuong - %s WHERE MaSP = %s", (quantity, ma_sp))
                self.cursor.execute("SELECT SoLuong FROM SANPHAM WHERE MaSP = %s", (ma_sp,))
                remaining_quantity = self.cursor.fetchone()[0]
                if remaining_quantity == 0:
                    QMessageBox.information(self, "Thông báo", f"Sản phẩm {product_name} đã hết hàng.")
                
            self.db.commit()
            QMessageBox.information(self, "Thành công", "Thanh toán thành công!")
            self.clear_data()
    
    def edit_product(self, item):
        """Sửa hoặc xóa sản phẩm trong danh sách."""
        options = ["Sửa số lượng", "Xóa sản phẩm"]
        choice, ok = QInputDialog.getItem(self, "Chỉnh sửa sản phẩm", "Chọn hành động:", options, 0, False)
        if ok:
            if choice == "Sửa số lượng":
                new_quantity, ok = QInputDialog.getInt(self, "Nhập số lượng mới", "Số lượng:", 1, 1, 100)
                if ok:
                    product_name = item.text().split(" - ")[0]
                    self.cursor.execute("SELECT Gia FROM SANPHAM WHERE TenSP = %s", (product_name,))
                    price = self.cursor.fetchone()[0]
                    new_price = new_quantity * price
                    item.setText(f"{product_name} - SL: {new_quantity} - Giá: {new_price} VND")
                    self.calculate_total()
            else:
                self.ui.listWidget_8.takeItem(self.ui.listWidget_8.row(item))
                self.calculate_total()
    
    def clear_data(self):
        """Xóa toàn bộ dữ liệu sau khi thanh toán."""
        self.ui.listWidget_8.clear()
        self.ui.label_99.setText("0 VND")
        self.ui.textEditkh.clear()
        self.ui.textEditkm.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HoadonApp()
    window.show()
    sys.exit(app.exec())