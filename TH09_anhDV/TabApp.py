from PyQt6 import QtWidgets
from tab import Ui_Dialog  # Giao diện chính

from Hoadon import HoadonApp
from Home import HomeApp
from Customer import CustomerApp
from KhuyenMai import KhuyenMaiApp
from History import HistoryApp
from login import LoginApp  # Import trang đăng nhập

class TabApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Kết nối các nút với các trang tương ứng
        self.ui.btnhome.clicked.connect(self.open_house)
        self.ui.btnhd.clicked.connect(self.open_hoadon)
        self.ui.btnsp.clicked.connect(self.open_home)
        self.ui.btnkh.clicked.connect(self.open_customer)
        self.ui.btnkm.clicked.connect(self.open_khuyenmai)
        self.ui.btnls.clicked.connect(self.open_history)
        self.ui.btndx.clicked.connect(self.logout)

        # Biến lưu cửa sổ con đang mở
        self.current_window = None

    def open_house(self):
        from House import HouseApp
        self.open_window(HouseApp)

    def open_hoadon(self):
        from Hoadon import HoadonApp
        self.open_window(HoadonApp)

    def open_home(self):
        from Home import HomeApp
        self.open_window(HomeApp)

    def open_customer(self):
        from Customer import CustomerApp
        self.open_window(CustomerApp)

    def open_khuyenmai(self):
        from KhuyenMai import KhuyenMaiApp
        self.open_window(KhuyenMaiApp)

    def open_history(self):
        from History import HistoryApp
        self.open_window(HistoryApp)

    def logout(self):
        """Hiển thị hộp thoại xác nhận đăng xuất"""
        reply = QtWidgets.QMessageBox.question(
            self, "Xác nhận", "Bạn có muốn đăng xuất?", 
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )

        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            self.close()
            self.login_window = LoginApp()  # Quay lại màn hình đăng nhập
            self.login_window.show()

    def closeEvent(self, event):
        """Khi đóng cửa sổ con, quay về TabApp"""
        self.show()  # Đảm bảo TabApp luôn hiện lại khi đóng cửa sổ con
        event.accept()

    def open_window(self, window_class):
        """Đóng cửa sổ hiện tại và mở cửa sổ mới"""
        if self.current_window:
            self.current_window.close()  # Đóng cửa sổ trước đó

    # Tạo cửa sổ mới
        self.current_window = window_class()
    
    # Gắn sự kiện closeEvent vào cửa sổ con
        self.current_window.closeEvent = self.child_closed_event  

        self.current_window.show()

    # Ẩn TabApp
        self.hide()

    def child_closed_event(self, event):
         """Khi cửa sổ con bị đóng, hiển thị lại TabApp"""
         self.show()
         self.current_window = None
         event.accept()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = TabApp()
    window.show()
    sys.exit(app.exec())