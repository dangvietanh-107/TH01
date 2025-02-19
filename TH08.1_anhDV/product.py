import sys
import mysql.connector
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QMessageBox

class ProductApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản lý Sản Phẩm")
        self.setGeometry(300, 300, 800, 700)

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test1"
        )
        self.cursor = self.db.cursor()

        self.layout = QVBoxLayout()
        
        self.table = QTableWidget()
        self.layout.addWidget(self.table)
        
        self.btn_load = QPushButton("Load Data")
        self.btn_load.clicked.connect(self.load_data)
        self.layout.addWidget(self.btn_load)
        
        self.input_id = QLineEdit()
        self.input_id.setPlaceholderText("Mã Sản Phẩm")
        self.layout.addWidget(self.input_id)
        
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Tên Sản Phẩm")
        self.layout.addWidget(self.input_name)
        
        self.input_brand = QLineEdit()
        self.input_brand.setPlaceholderText("Hãng Sản Xuất")
        self.layout.addWidget(self.input_brand)
        
        self.input_price = QLineEdit()
        self.input_price.setPlaceholderText("Giá")
        self.layout.addWidget(self.input_price)
        
        self.input_quantity = QLineEdit()
        self.input_quantity.setPlaceholderText("Số Lượng")
        self.layout.addWidget(self.input_quantity)
        
        self.input_description = QLineEdit()
        self.input_description.setPlaceholderText("Mô Tả")
        self.layout.addWidget(self.input_description)
        
        self.input_camera = QLineEdit()
        self.input_camera.setPlaceholderText("Camera")
        self.layout.addWidget(self.input_camera)
        
        self.input_battery = QLineEdit()
        self.input_battery.setPlaceholderText("Pin")
        self.layout.addWidget(self.input_battery)
        
        self.input_ram = QLineEdit()
        self.input_ram.setPlaceholderText("RAM")
        self.layout.addWidget(self.input_ram)
        
        self.btn_add = QPushButton("Thêm Sản Phẩm")
        self.btn_add.clicked.connect(self.add_product)
        self.layout.addWidget(self.btn_add)
        
        self.btn_update = QPushButton("Sửa Sản Phẩm")
        self.btn_update.clicked.connect(self.update_product)
        self.layout.addWidget(self.btn_update)
        
        self.btn_delete = QPushButton("Xóa Sản Phẩm")
        self.btn_delete.clicked.connect(self.delete_product)
        self.layout.addWidget(self.btn_delete)

        self.setLayout(self.layout)

    def load_data(self):
        self.cursor.execute("SELECT * FROM SANPHAM")
        rows = self.cursor.fetchall()
        self.table.setRowCount(len(rows))
        self.table.setColumnCount(len(rows[0]))
        self.table.setHorizontalHeaderLabels(["Mã SP", "Tên SP", "Hãng SX", "Giá", "Số Lượng", "Mô Tả", "Camera", "Pin", "RAM"])
        for row_index, row_data in enumerate(rows):
            for col_index, col_data in enumerate(row_data):
                self.table.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
    
    def add_product(self):
        name = self.input_name.text()
        brand = self.input_brand.text()
        price = self.input_price.text()
        quantity = self.input_quantity.text()
        description = self.input_description.text()
        camera = self.input_camera.text()
        battery = self.input_battery.text()
        ram = self.input_ram.text()
        
        if name and brand and price and quantity:
            self.cursor.execute("INSERT INTO SANPHAM (TenSP, HangSX, Gia, SoLuong, MoTa, Camera, Pin, RAM) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (name, brand, price, quantity, description, camera, battery, ram))
            self.db.commit()
            self.load_data()
            self.clear_inputs()
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đủ thông tin")
    
    def update_product(self):
        product_id = self.input_id.text()
        name = self.input_name.text()
        brand = self.input_brand.text()
        price = self.input_price.text()
        quantity = self.input_quantity.text()
        description = self.input_description.text()
        camera = self.input_camera.text()
        battery = self.input_battery.text()
        ram = self.input_ram.text()
        
        if product_id and name and brand and price and quantity:
            self.cursor.execute("UPDATE SANPHAM SET TenSP=%s, HangSX=%s, Gia=%s, SoLuong=%s, MoTa=%s, Camera=%s, Pin=%s, RAM=%s WHERE MaSP=%s", (name, brand, price, quantity, description, camera, battery, ram, product_id))
            self.db.commit()
            self.load_data()
            self.clear_inputs()
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đủ thông tin")
    
    def delete_product(self):
        product_id = self.input_id.text()
        if product_id:
            self.cursor.execute("DELETE FROM SANPHAM WHERE MaSP=%s", (product_id,))
            self.db.commit()
            self.load_data()
            self.clear_inputs()
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập Mã Sản Phẩm")
    
    def clear_inputs(self):
        self.input_id.clear()
        self.input_name.clear()
        self.input_brand.clear()
        self.input_price.clear()
        self.input_quantity.clear()
        self.input_description.clear()
        self.input_camera.clear()
        self.input_battery.clear()
        self.input_ram.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductApp()
    window.show()
    sys.exit(app.exec())
