# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UNALPlayMainWindow2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk
from tkinter import messagebox
import metadata
import addToPlaylist
import modifyPlaylist
import Format
import newPlaylist
import TableManagement
import Files

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self._format = "music"
        self.currentList = "Main_list"
        self.constructor = Format.Music
        self.mainList = Files.MainList(self._format)

        root = tk.Tk()
        root.withdraw()  # Para evitar la ventana random del tkinter

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("font: 10pt \"Comic Sans MS\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 530, 801, 74))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.formatLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.formatLayout.setContentsMargins(0, 0, 0, 0)
        self.formatLayout.setObjectName("formatLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formatLayout.addItem(spacerItem)
        self.musicFormatButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.musicFormatButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/musica_format2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.musicFormatButton.setIcon(icon)
        self.musicFormatButton.setIconSize(QtCore.QSize(80, 64))
        self.musicFormatButton.setFlat(True)
        self.musicFormatButton.setObjectName("musicFormatButton")
        self.formatLayout.addWidget(self.musicFormatButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formatLayout.addItem(spacerItem1)
        self.picturesFormatButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.picturesFormatButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/fotos_format2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.picturesFormatButton.setIcon(icon1)
        self.picturesFormatButton.setIconSize(QtCore.QSize(80, 64))
        self.picturesFormatButton.setFlat(True)
        self.picturesFormatButton.setObjectName("picturesFormatButton")
        self.formatLayout.addWidget(self.picturesFormatButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formatLayout.addItem(spacerItem2)
        self.VideoFormatButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.VideoFormatButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/video_format2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VideoFormatButton.setIcon(icon2)
        self.VideoFormatButton.setIconSize(QtCore.QSize(80, 64))
        self.VideoFormatButton.setFlat(True)
        self.VideoFormatButton.setObjectName("VideoFormatButton")
        self.formatLayout.addWidget(self.VideoFormatButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formatLayout.addItem(spacerItem3)
        self.appNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.appNameLabel.setGeometry(QtCore.QRect(250, 10, 311, 61))
        self.appNameLabel.setStyleSheet("font: 28pt \"Comic Sans MS\";")
        self.appNameLabel.setScaledContents(False)
        self.appNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.appNameLabel.setObjectName("appNameLabel")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(200, 80, 650, 42))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.toolsLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.toolsLayout.setContentsMargins(0, 0, 50, 0)
        self.toolsLayout.setSpacing(0)
        self.toolsLayout.setObjectName("toolsLayout")
        self.addButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.addButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/añadir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon3)
        self.addButton.setIconSize(QtCore.QSize(32, 32))
        self.addButton.setDefault(False)
        self.addButton.setFlat(True)
        self.addButton.setObjectName("addButton")
        self.toolsLayout.addWidget(self.addButton)
        self.modifyButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.modifyButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/modificar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.modifyButton.setIcon(icon4)
        self.modifyButton.setIconSize(QtCore.QSize(32, 32))
        self.modifyButton.setFlat(True)
        self.modifyButton.setObjectName("modifyButton")
        self.toolsLayout.addWidget(self.modifyButton)
        self.removeButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.removeButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icons/eliminar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeButton.setIcon(icon5)
        self.removeButton.setIconSize(QtCore.QSize(32, 32))
        self.removeButton.setFlat(True)
        self.removeButton.setObjectName("removeButton")
        self.toolsLayout.addWidget(self.removeButton)
        self.addPlaylistButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.addPlaylistButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icons/añadirPlaylist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addPlaylistButton.setIcon(icon6)
        self.addPlaylistButton.setIconSize(QtCore.QSize(32, 32))
        self.addPlaylistButton.setFlat(True)
        self.addPlaylistButton.setObjectName("addPlaylistButton")
        self.toolsLayout.addWidget(self.addPlaylistButton)
        self.removePlaylistButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.removePlaylistButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Icons/eliminarPlaylist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removePlaylistButton.setIcon(icon7)
        self.removePlaylistButton.setIconSize(QtCore.QSize(32, 32))
        self.removePlaylistButton.setFlat(True)
        self.removePlaylistButton.setObjectName("removePlaylistButton")
        self.toolsLayout.addWidget(self.removePlaylistButton)
        self.modifyPlaylistButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.modifyPlaylistButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Icons/añadirAPlaylist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.modifyPlaylistButton.setIcon(icon8)
        self.modifyPlaylistButton.setIconSize(QtCore.QSize(32, 32))
        self.modifyPlaylistButton.setFlat(True)
        self.modifyPlaylistButton.setObjectName("modifyPlaylistButton")
        self.toolsLayout.addWidget(self.modifyPlaylistButton)

        self.itemsTable = TableManagement.TableManagement(self._format, self.centralwidget)
        self.itemsTable.setGeometry(QtCore.QRect(199, 150, 601, 370))

        self.formatMenu = QtWidgets.QTreeWidget(self.centralwidget)
        self.formatMenu.setEnabled(True)
        self.formatMenu.setGeometry(QtCore.QRect(0, 80, 200, 440))
        self.formatMenu.setObjectName("formatMenu")
        item_0 = QtWidgets.QTreeWidgetItem(self.formatMenu)
        item_0 = QtWidgets.QTreeWidgetItem(self.formatMenu)
        self.searchBar = QtWidgets.QLineEdit(self.centralwidget)
        self.searchBar.setGeometry(QtCore.QRect(270, 125, 491, 20))
        self.searchBar.setObjectName("searchBar")
        self.searchLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchLabel.setGeometry(QtCore.QRect(211, 126, 61, 16))
        self.searchLabel.setObjectName("searchLabel")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(760, 120, 31, 31))
        self.searchButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Icons/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchButton.setIcon(icon9)
        self.searchButton.setIconSize(QtCore.QSize(15, 15))
        self.searchButton.setFlat(True)
        self.searchButton.setObjectName("searchButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.musicFormatButton.clicked.connect(self.changeToMusicFormat)
        self.picturesFormatButton.clicked.connect(self.changeToPicturesFormat)
        self.VideoFormatButton.clicked.connect(self.changeToVideosFormat)
        self.modifyPlaylistButton.clicked.connect(self.modifyPlaylistInterface)
        self.removePlaylistButton.clicked.connect(self.removePlaylist)
        self.addPlaylistButton.clicked.connect(self.addPlaylistInterface)
        self.removeButton.clicked.connect(self.removeElement)
        self.modifyButton.clicked.connect(self.modifyElementInterface)
        self.addButton.clicked.connect(self.elementInterface)
        self.formatMenu.itemSelectionChanged.connect(self.changeCurrentList)

        self.formatMenuUpdate()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def changeToMusicFormat(self):
        self._format = "music"
        self.currentList = "Main_list"
        self.constructor = Format.Music
        self.mainList = Files.MainList(self._format)

        self.formatMenu.headerItem().setText(0, "MÚSICA")
        self.formatMenu.topLevelItem(0).setText(0, "Mi Música")

        self.itemsTable.Update(self._format)

        item = self.itemsTable.horizontalHeaderItem(1)
        item.setText("Artista")
        item = self.itemsTable.horizontalHeaderItem(4)
        item.setText("Género")

        self.formatMenuUpdate()

    def changeToVideosFormat(self):
        self._format = "videos"
        self.currentList = "Main_list"
        self.constructor = Format.Videos
        self.mainList = Files.MainList(self._format)

        self.formatMenu.headerItem().setText(0, "VIDEOS")
        self.formatMenu.topLevelItem(0).setText(0, "Mis Videos")

        self.itemsTable.Update(self._format)

        item = self.itemsTable.horizontalHeaderItem(1)
        item.setText("Autor")
        item = self.itemsTable.horizontalHeaderItem(4)
        item.setText("Género")

        self.formatMenuUpdate()

    def changeToPicturesFormat(self):
        self._format = "pictures"
        self.currentList = "Main_list"
        self.constructor = Format.Pictures
        self.mainList = Files.MainList(self._format)

        self.formatMenu.headerItem().setText(0, "FOTOS")
        self.formatMenu.topLevelItem(0).setText(0, "Mis Fotos")

        self.itemsTable.Update(self._format)

        item = self.itemsTable.horizontalHeaderItem(1)
        item.setText("Autor")
        item = self.itemsTable.horizontalHeaderItem(4)
        item.setText("Tipo")

        self.formatMenuUpdate()

    def changeCurrentList(self):
        mainListItem = self.formatMenu.topLevelItem(0)  # devuelve un QTreeWidgetItem "mainList"
        playlistItem = self.formatMenu.topLevelItem(1)  # devuelve un QTreeWidgetItem "playlist"

        if mainListItem.isSelected():
            self.currentList = "Main_list"
            self.itemsTable.mainList = Files.MainList(self._format)
            self.itemsTable.Update(self._format)
        elif not playlistItem.isSelected():
            self.currentList = self.formatMenu.selectedItems()[0].text(0)
            self.itemsTable.UpdatePlaylist(self._format, self.currentList)

        self.itemsTable.LoadList()

    def formatMenuUpdate(self):
        self.playlistList = Files.PlaylistList(self._format)
        self.playlists = self.playlistList.GetPlaylists()
        playlistItem = self.formatMenu.topLevelItem(1)  # devuelve un QTreeWidgetItem "playlist"
        for i in playlistItem.takeChildren():
            del i
        for item in self.playlists:
            newItem = QtWidgets.QTreeWidgetItem(playlistItem)
            newItem.setText(0, item)
            #newItem.clicked.connect(self.itemsTableUpdate())  #Queda pendiente xd

    def itemsTableUpdate(self):
        pass
        #funcion creada por juan. Debe actualizar los datos de la tabla de los items

    def addPlaylistInterface(self):
        playlistDialog = newPlaylist.Dialog(self._format)
        playlistDialog.show()

        if playlistDialog.exec_() and playlistDialog.accepted:
            temp = playlistDialog.Items()
            name = temp["playlistName"]
            elems = []
            for i in temp["selectedEntries"]:
                elem = self.constructor(i["name"], i["author"], i["album"], i["year"], i["type"], "")
                elems.append(elem)

            playlist = Files.Playlist(self._format, name)
            for i in self.mainList.list:
                if i in elems:
                    playlist.AddEntry(i)

            self.formatMenuUpdate()  # Añadir al árbol

    def modifyPlaylistInterface(self):
        self._interface = addToPlaylist.Dialog(self._format, self.currentList) #hablar con juan acerca de addToPlaylist y modifyPlaylist
        self._interface.show()

    def removePlaylist(self):
        if self.currentList == "Main_list":
            messagebox.showinfo(message="No se puede eliminar la lista principal", title="Alerta")
            return
        self.answer = messagebox.askyesno(message="¿Desea eliminar {0}?".format(self.currentList),title="Alerta")
        self.playlistToRemove = Files.Playlist(self._format,self.currentList)
        if self.answer == True:
            self.playlistToRemove.DeletePlaylist()
        else:
            return
        self.formatMenuUpdate()
        mainListItem = self.formatMenu.topLevelItem(0)
        playlistItem = self.formatMenu.topLevelItem(1)
        mainListItem.setSelected(True)
        playlistItem.setSelected(False)
        self.changeCurrentList()

    def elementInterface(self):
        metadataDialog = metadata.Dialog(self._format,modify=False)
        metadataDialog.show()

        if metadataDialog.exec_() and metadataDialog.accepted:
            temp = metadataDialog.items()
            elem = self.constructor(temp["name"], temp["author"],
                                    temp["album"], temp["year"],
                                    temp["type"], temp["path"])
            self.itemsTable.mainList.AddEntry(elem)
            self.itemsTable.LoadList()

    def modifyElementInterface(self):
        if len(self.itemsTable.selectedItems()) == 0:
            messagebox.showinfo(message="Seleccione primero el elemento que desea modificar.", title="Alerta")
            return
        else:
            metadataDialog = metadata.Dialog(self._format, modify=True)
            metadataDialog.show()

            if metadataDialog.exec_() and metadataDialog.accepted:
                temp = metadataDialog.items()
                newElement = self.constructor(temp["name"], temp["author"],
                                        temp["album"], temp["year"],
                                        temp["type"], temp["path"])

                oldElement = self.itemsTable.getElement()
                self.itemsTable.mainList.ModifyList(newElement, oldElement)
                self.itemsTable.LoadList()

    def removeElement(self):
        if len(self.itemsTable.selectedItems()) == 0:
            messagebox.showinfo(message="Seleccione primero el elemento que desea eliminar.", title="Alerta")
            return
        else:
            oldElement = self.itemsTable.getElement()
            userIsSure = messagebox.askyesno(message="¿Desea eliminar {0}?".format(oldElement.getName()), title="Eliminar elemento")
            if userIsSure:
                self.itemsTable.mainList.DeleteEntry(oldElement)
                self.itemsTable.LoadList()
            else:
                return



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inicio"))
        self.appNameLabel.setText(_translate("MainWindow", "UNALPLAY"))
        self.modifyPlaylistButton.setWhatsThis(_translate("MainWindow", "eliminar playlist"))
        self.itemsTable.setSortingEnabled(True)
        item = self.itemsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.itemsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Artista"))
        item = self.itemsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Álbum"))
        item = self.itemsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Año"))
        item = self.itemsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Género"))
        item = self.itemsTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Reproducible"))
        self.formatMenu.headerItem().setText(0, _translate("MainWindow", "MÚSICA"))
        __sortingEnabled = self.formatMenu.isSortingEnabled()
        self.formatMenu.setSortingEnabled(False)
        self.formatMenu.topLevelItem(0).setText(0, _translate("MainWindow", "Mi Música"))
        self.formatMenu.topLevelItem(1).setText(0, _translate("MainWindow", "Playlists"))
        self.formatMenu.setSortingEnabled(__sortingEnabled)
        self.searchLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00004a;\">BUSCAR</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
