from PyQt5 import QtWidgets, uic
import TableManagement


class Dialog(QtWidgets.QDialog):
    def __init__(self, _format):
        super().__init__()
        uic.loadUi("newPlaylist.ui", self)
        self._format = _format
        self.tableWidget = TableManagement.TableManagement(_format, self)
        self.tableWidget.setGeometry(20, 110, 561, 321)

    def Items(self):
        self.tableWidget.UpdateSelectedEntries()
        items = {"playlistName": self.playlistName.text(), "selectedEntries": self.tableWidget.selectedEntries}
        return items
