from PyQt5 import QtWidgets, uic
import TableManagement


class Dialog(QtWidgets.QDialog):
    def __init__(self, _format, name):
        super().__init__()
        uic.loadUi("newPlaylist.ui", self)
        self._format = _format
        self.tableWidget = TableManagement.TableManagement(_format, name)
        self.tableWidget.setGeometry(20, 110, 561, 321)
        self.selectedEntries = []
