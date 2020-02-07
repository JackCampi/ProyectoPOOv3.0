# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pictureInterface.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        MainWindow.setStyleSheet("font: 75 12pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(49, 49, 49);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pictureLabel = QtWidgets.QLabel(self.centralwidget)
        self.pictureLabel.setGeometry(QtCore.QRect(10, 10, 581, 361))
        self.pictureLabel.setText("")
        self.pictureLabel.setScaledContents(True)
        self.pictureLabel.setObjectName("pictureLabel")
        self.pictureNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.pictureNameLabel.setGeometry(QtCore.QRect(35, 433, 531, 16))
        self.pictureNameLabel.setScaledContents(False)
        self.pictureNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pictureNameLabel.setWordWrap(False)
        self.pictureNameLabel.setObjectName("pictureNameLabel")
        self.pictureAlbumLabel = QtWidgets.QLabel(self.centralwidget)
        self.pictureAlbumLabel.setGeometry(QtCore.QRect(35, 452, 531, 16))
        self.pictureAlbumLabel.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"color: rgb(185, 185, 185);")
        self.pictureAlbumLabel.setScaledContents(False)
        self.pictureAlbumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pictureAlbumLabel.setWordWrap(False)
        self.pictureAlbumLabel.setObjectName("pictureAlbumLabel")
        self.pictureAuthorLabel = QtWidgets.QLabel(self.centralwidget)
        self.pictureAuthorLabel.setGeometry(QtCore.QRect(35, 470, 531, 16))
        self.pictureAuthorLabel.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"color: rgb(185, 185, 185);")
        self.pictureAuthorLabel.setScaledContents(False)
        self.pictureAuthorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pictureAuthorLabel.setWordWrap(False)
        self.pictureAuthorLabel.setObjectName("pictureAuthorLabel")
        self.previousPictureButton = QtWidgets.QPushButton(self.centralwidget)
        self.previousPictureButton.setGeometry(QtCore.QRect(220, 390, 51, 23))
        self.previousPictureButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/PreviousButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previousPictureButton.setIcon(icon)
        self.previousPictureButton.setIconSize(QtCore.QSize(30, 30))
        self.previousPictureButton.setFlat(True)
        self.previousPictureButton.setObjectName("previousPictureButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(331, 390, 51, 23))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/NextButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pictureNameLabel.setText(_translate("MainWindow", "PictureName"))
        self.pictureAlbumLabel.setText(_translate("MainWindow", "PictureAlbum"))
        self.pictureAuthorLabel.setText(_translate("MainWindow", "PictureAuthor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
