from PyQt5 import QtWidgets, QtCore
import Files
import Format


class TableManagement(QtWidgets.QTableWidget):
    def __init__(self, _format, parent=None):
        super().__init__(parent)

        self._format = _format
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
        elif self._format == "pictures":
            self.constructor = Format.Pictures
        elif self._format == "videos":
            self.constructor = Format.Videos

    def LoadList(self):
        self.setSortingEnabled(False)
        self.clearContents()
        self.setRowCount(0)
        for elem in self.mainList.list:
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

    def __updateSelectedEntries(self):
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

    def Items(self):
        self.__updateSelectedEntries()
        items = {"newName": self.newName.text(), "selectedEntries": self.selectedEntries}
        return items
