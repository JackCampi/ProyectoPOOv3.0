from PyQt5 import QtWidgets, QtGui
import Files

class TableManagement(QtWidgets.QTableWidget):
    def __init__(self, _format, name):
        super().__init__()
        
        self._format = _format
        self.mainList = Files.MainList(_format)
        self.LoadList()
        self.SetupUi()
    
    def SetupUi(self):
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.setSortingEnabled(True)
        self.setRowCount(0)
        self.setColumnCount(6)
        
        if self._format == "pictures":
            labels = ["Nombre", "Protagonista", "Álbum", "Año", "Género", "Reproducible"]
        else:
            labels = ["Nombre", "Autor", "Álbum", "Año", "Género", "Reproducible"]
            self.setHorizontalHeaderLabels(labels)

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

    def Items(self):
        self.__updateSelectedEntries()
        items = {"newName": self.newName.text(), "selectedEntries": self.selectedEntries}
        return items
