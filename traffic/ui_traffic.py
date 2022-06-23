from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from detect_traffic import Detect_Traffic
import sys
from PyQt5.QtGui import QPixmap, QFont


class Ui_MainWindow(QDialog):
    _file_name = None
    _dict_object = None
    _list_cls = ['./img_traffic/cam_nguoc_chieu.png', './img_traffic/cam_xe_tai.png',
                 './img_traffic/cam_re_trai.png', './img_traffic/cam_re_phai.png',
                 './img_traffic/cam_do_xe.png', './img_traffic/hieu_lenh.png',
                 './img_traffic/nguoi_di_bo.png',
                 './img_traffic/vong_xoay.png', './img_traffic/xe_bus.png']

    _list_label = ['cấm ngược chiều', 'cấm xe tải', 'cấm rẽ trái', 'cấm rẽ phải', 'cấm đỗ xe', 'hiệu lệnh',
                   'người đi bộ', 'vòng xoáy', 'xe bus']

    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(1023, 654)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1001, 631))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        space_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(space_item)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        space_item1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_5.addItem(space_item1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.horizontalLayout_6.setStretch(0, 7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.image_view = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.image_view.setFrameShape(QtWidgets.QFrame.Box)
        self.image_view.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_view.setLineWidth(5)
        self.image_view.setObjectName("image_view")
        self.horizontalLayout_7.addWidget(self.image_view)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.object_image = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.object_image.setFrameShape(QtWidgets.QFrame.Box)
        self.object_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.object_image.setLineWidth(2)
        self.object_image.setObjectName("object_image")
        self.horizontalLayout_8.addWidget(self.object_image)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_14.addWidget(self.label_6)
        self.object_index = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.object_index.setMinimum(1)
        self.object_index.setObjectName("object_index")
        self.horizontalLayout_14.addWidget(self.object_index)
        self.verticalLayout_9.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_15.addWidget(self.label_7)
        self.object_name = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.object_name.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.object_name.setFrameShadow(QtWidgets.QFrame.Plain)
        self.object_name.setLineWidth(3)
        self.object_name.setObjectName("object_name")
        self.horizontalLayout_15.addWidget(self.object_name)
        self.verticalLayout_9.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_8.addLayout(self.verticalLayout_9)
        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 6)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        space_item2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(space_item2)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_16.addWidget(self.label_9)
        self.path_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.path_name.setText("")
        self.path_name.setObjectName("path_name")
        self.horizontalLayout_16.addWidget(self.path_name)
        self.add_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout_16.addWidget(self.add_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout_16)
        space_item3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(space_item3)
        self.detect_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.detect_button.setEnabled(True)
        self.detect_button.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.detect_button.setStyleSheet("QpushButton{\n"
                                         "background-color: rgb(128, 60, 224);\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "background-color: rgb(193, 81, 241);\n"
                                         "}")
        self.detect_button.setIconSize(QtCore.QSize(30, 20))
        self.detect_button.setAutoExclusive(False)
        self.detect_button.setAutoDefault(False)
        self.detect_button.setDefault(True)
        self.detect_button.setFlat(False)
        self.detect_button.setObjectName("detect_button")
        self.detect_button.clicked.connect(self.detect_image)
        self.verticalLayout_7.addWidget(self.detect_button)
        space_item4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(space_item4)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_17.addWidget(self.label_4)
        self.object_number = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.object_number.setFrameShape(QtWidgets.QFrame.Box)
        self.object_number.setFrameShadow(QtWidgets.QFrame.Raised)
        self.object_number.setLineWidth(3)
        self.object_number.setObjectName("object_number")
        self.horizontalLayout_17.addWidget(self.object_number)
        self.verticalLayout_7.addLayout(self.horizontalLayout_17)
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_6.setStretch(0, 2)
        self.verticalLayout_6.setStretch(1, 5)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout_7.setStretch(0, 4)
        self.horizontalLayout_7.setStretch(1, 3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 6)
        main_window.setCentralWidget(self.centralwidget)
        self.set_attribute_for_widget(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def detect_image(self):
        weight_path = "weight_traffic.pt"
        detect_traffic = Detect_Traffic()
        detect_traffic.set_spec(self._file_name[0], weight_path)
        bgr_img, number_object, self._dict_object = detect_traffic.detect_image()
        height, width, channel = bgr_img.shape
        byte_per_line = 3 * width
        qt_img = QtGui.QImage(bgr_img.data, width, height, byte_per_line, QtGui.QImage.Format_RGB888).rgbSwapped()
        pixmap_image = QPixmap.fromImage(qt_img)
        pixmap_image1 = pixmap_image.scaled(self.image_view.width() - 35, self.image_view.height() - 35,
                                            Qt.IgnoreAspectRatio)
        self.image_view.setPixmap(pixmap_image1)
        self.image_view.setAlignment(Qt.AlignCenter)
        self.object_number.setFont(QFont('Arial', 20))
        self.object_number.setText(str(number_object))
        self.object_number.setAlignment(Qt.AlignCenter)
        self.object_index.setMaximum(number_object)
        self.object_index.valueChanged.connect(self.set_value_changed)
        if len(self._dict_object) != 0 and self._dict_object is not None:
            first_cls = self._dict_object.get(0)
            pixmap_image0 = QPixmap(self._list_cls[first_cls])
            pixmap_image0 = pixmap_image0.scaled(self.object_image.width() - 20, self.object_image.height() - 20,
                                                 Qt.IgnoreAspectRatio)
            self.object_image.setPixmap(pixmap_image0)
            self.object_image.setAlignment(Qt.AlignCenter)
            self.object_name.setText(self._list_label[first_cls])
            self.object_name.setAlignment(Qt.AlignCenter)

    def set_value_changed(self):
        current_value = self.object_index.value()
        print(current_value)
        if len(self._dict_object) != 0 and self._dict_object is not None:
            cls = self._dict_object.get(current_value - 1)
            pixmap_image0 = QPixmap(self._list_cls[cls])
            pixmap_image0 = pixmap_image0.scaled(self.object_image.width() - 20, self.object_image.height() - 20,
                                                 Qt.IgnoreAspectRatio)
            self.object_image.setPixmap(pixmap_image0)
            self.object_image.setAlignment(Qt.AlignCenter)
            self.object_name.setText(self._list_label[cls])
            self.object_name.setAlignment(Qt.AlignCenter)

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle('message')
        msg.setText('Error')
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def add_file_path(self):
        self._file_name = QFileDialog.getOpenFileName(parent=self, caption='Open file', directory='',
                                                      filter='Images (*.png, *.jpg)')
        self.path_name.setText(self._file_name[0])
        pixmap = QPixmap(self._file_name[0])
        pixmap1 = pixmap.scaled(self.image_view.width() - 35, self.image_view.height() - 35, Qt.IgnoreAspectRatio)
        self.image_view.setPixmap(pixmap1)
        self.image_view.setAlignment(Qt.AlignCenter)

    def set_attribute_for_widget(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; "
                                        "font-weight:600;\">HANOI UNIVERSITY OF SCIENCE AND "
                                        "TECHNOLOGY</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; "
                                        "font-weight:600;\">TRAFFIC DETECTION SYTEM</span></p></body></html>"))
        self.label.setText(
            _translate("MainWindow", "<html><head/><body><p><img src=\"bk_logo.png\"/></p></body></html>"))
        self.image_view.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">loading image...</p></body></html>"))
        self.object_image.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/>object...</p></body></html>"))
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; "
                                        "font-weight:600;\">ID:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; "
                                        "font-weight:600;\">NAME:</span></p></body></html>"))
        self.object_name.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-weight:600;\">PATH: "
                                        "</span></p></body></html>"))
        self.add_button.setText(_translate("MainWindow", "add"))
        self.add_button.clicked.connect(self.add_file_path)
        self.detect_button.setText(_translate("MainWindow", "DETECT"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; "
                                        "font-weight:600;\">Object number:</span></p></body></html>"))
        self.object_number.setText(_translate("MainWindow",
                                              "<html><head/><body><p align=\"center\"><span style=\" "
                                              "font-size:20pt;\">0</span></p></body></html>"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup_ui(main_window)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
