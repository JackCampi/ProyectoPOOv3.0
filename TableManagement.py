"""Módulo TableManagement, se encarga de manejar todas las tablas"""

from PyQt5 import QtWidgets, QtCore
import Files
import Format


class TableManagement(QtWidgets.QTableWidget):
    """
    Clase TableManagement, hereda de QTableWidget, con la diferencia de que carga
    los archivos, en parte, es una imlpementación gráfica del módulo Files.
    """
    def __init__(self, _format, parent=None, filters=()):
        super().__init__(parent)

        self.selectedEntries = []
        self._format = _format
        self.filters = filters
        self.mainList = Files.MainList(_format)
        self.SetupUi()
        self.LoadList()
    
    def SetupUi(self):
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.setSortingEnabled(True)
        self.setRowCount(0)
        self.setColumnCount(6)
        self.setGridStyle(QtCore.Qt.SolidLine)
        self.setCornerButtonEnabled(True)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(5, item)
        self.horizontalHeader().setVisible(True)
        self.horizontalHeader().setCascadingSectionResizes(False)
        self.horizontalHeader().setDefaultSectionSize(119)
        self.verticalHeader().setVisible(False)

        if self._format == "music":
            self.constructor = Format.Music
            labels = ["Nombre", "Artista", "Álbum", "Año", "Género", "Reproducible"]
        elif self._format == "pictures":
            self.constructor = Format.Pictures
            labels = ["Nombre", "Autor", "Álbum", "Año", "Tipo", "Reproducible"]
        elif self._format == "videos":
            self.constructor = Format.Videos
            labels = ["Nombre", "Autor", "Álbum", "Año", "Género", "Reproducible"]
        self.setHorizontalHeaderLabels(labels)

    def LoadList(self):
        self.setSortingEnabled(False)
        self.clearContents()
        self.setRowCount(0)

        if len(self.filters) > 0:
            listToLoad = [i for i in self.mainList.list if i not in self.filters]
        else:
            listToLoad = self.mainList.list

        for elem in listToLoad:
            n = self.rowCount()
            self.setRowCount(n + 1)
            self.setItem(n, 0, QtWidgets.QTableWidgetItem(elem.getName()))
            self.setItem(n, 1, QtWidgets.QTableWidgetItem(elem.getAuthor()))
            self.setItem(n, 2, QtWidgets.QTableWidgetItem(elem.getAlbum()))
            self.setItem(n, 3, QtWidgets.QTableWidgetItem(elem.getYear()))
            self.setItem(n, 4, QtWidgets.QTableWidgetItem(elem.getType()))
            self.setItem(n, 5, QtWidgets.QTableWidgetItem(elem.getPlayable()))

        self.setSortingEnabled(True)

    def getElement(self):
        row = self.currentRow()
        elem = {"name": self.item(row, 0).text(),
                "author": self.item(row, 1).text(),
                "album": self.item(row, 2).text(),
                "year": self.item(row, 3).text(),
                "type": self.item(row, 4).text()}

        return self.constructor(elem["name"], elem["author"], elem["album"], elem["year"], elem["type"], "")

    def UpdateSelectedEntries(self):
        for row in range(self.rowCount()):
            item = self.item(row, 0)
            if item.isSelected():
                elem = {"name": self.item(row, 0).text(),
                        "author": self.item(row, 1).text(),
                        "album": self.item(row, 2).text(),
                        "year": self.item(row, 3).text(),
                        "type": self.item(row, 4).text()}
                self.selectedEntries.append(elem)

    def Update(self, newFormat):
        self._format = newFormat
        self.mainList = Files.MainList(newFormat)
        self.LoadList()

    def UpdatePlaylist(self, newFormat, newPlaylist):
        self._format = newFormat
        self.mainList = Files.Playlist(newFormat, newPlaylist)
        self.LoadList()
