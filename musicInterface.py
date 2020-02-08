# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musicInterface.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class MusicWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 350)
        MainWindow.setMinimumSize(QtCore.QSize(530, 350))
        MainWindow.setMaximumSize(QtCore.QSize(530, 350))
        MainWindow.setBaseSize(QtCore.QSize(530, 350))
        MainWindow.setStyleSheet("font: 8pt \"Comic Sans MS\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BackgroundMusicLabel = QtWidgets.QLabel(self.centralwidget)
        self.BackgroundMusicLabel.setEnabled(False)
        self.BackgroundMusicLabel.setGeometry(QtCore.QRect(-1, -1, 532, 352))
        self.BackgroundMusicLabel.setStyleSheet("background-image: url(:/MusicBackground/musicBackgroundImage.png);")
        self.BackgroundMusicLabel.setText("")
        self.BackgroundMusicLabel.setObjectName("BackgroundMusicLabel")
        self.songSlider = QtWidgets.QSlider(self.centralwidget)
        self.songSlider.setEnabled(True)
        self.songSlider.setGeometry(QtCore.QRect(300, 250, 211, 16))
        self.songSlider.setOrientation(QtCore.Qt.Horizontal)
        self.songSlider.setObjectName("songSlider")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(300, 270, 211, 40))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.ButtonsLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.ButtonsLayout.setContentsMargins(0, 0, 0, 0)
        self.ButtonsLayout.setObjectName("ButtonsLayout")
        self.previousSongButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.previousSongButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/PreviousButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previousSongButton.setIcon(icon)
        self.previousSongButton.setIconSize(QtCore.QSize(30, 30))
        self.previousSongButton.setFlat(True)
        self.previousSongButton.setObjectName("previousSongButton")
        self.ButtonsLayout.addWidget(self.previousSongButton)
        self.PSMusicButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.PSMusicButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/PlayStopButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PSMusicButton.setIcon(icon1)
        self.PSMusicButton.setIconSize(QtCore.QSize(30, 30))
        self.PSMusicButton.setFlat(True)
        self.PSMusicButton.setObjectName("PSMusicButton")
        self.ButtonsLayout.addWidget(self.PSMusicButton)
        self.nextSongButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.nextSongButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/NextButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextSongButton.setIcon(icon2)
        self.nextSongButton.setIconSize(QtCore.QSize(30, 30))
        self.nextSongButton.setFlat(True)
        self.nextSongButton.setObjectName("nextSongButton")
        self.ButtonsLayout.addWidget(self.nextSongButton)
        self.songAuthorLabel = QtWidgets.QLabel(self.centralwidget)
        self.songAuthorLabel.setGeometry(QtCore.QRect(290, 220, 231, 17))
        self.songAuthorLabel.setStyleSheet("font: 75 08pt \"Comic Sans MS\";\n"
"color: rgb(188, 188, 188);\n"
"")
        self.songAuthorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.songAuthorLabel.setObjectName("songAuthorLabel")
        self.songNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.songNameLabel.setGeometry(QtCore.QRect(290, 180, 231, 23))
        self.songNameLabel.setStyleSheet("font: 75 12pt \"Comic Sans MS\";\n"
"color: rgb(250, 250, 250);")
        self.songNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.songNameLabel.setObjectName("songNameLabel")
        self.songAlbumLabel = QtWidgets.QLabel(self.centralwidget)
        self.songAlbumLabel.setGeometry(QtCore.QRect(290, 200, 231, 20))
        self.songAlbumLabel.setStyleSheet("font: 75 08pt \"Comic Sans MS\";\n"
"color: rgb(188, 188, 188);\n"
"")
        self.songAlbumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.songAlbumLabel.setObjectName("songAlbumLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reproductor"))
        self.songAuthorLabel.setText(_translate("MainWindow", "SongAuthor"))
        self.songNameLabel.setText(_translate("MainWindow", "SongName"))
        self.songAlbumLabel.setText(_translate("MainWindow", "SongAlbum"))
from Icons import Background_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
