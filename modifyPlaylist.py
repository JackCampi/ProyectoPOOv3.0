from PyQt5 import QtWidgets, uic
import TableManagement


class Dialog(QtWidgets.QDialog):
    def __init__(self, _format, oldName):
        super().__init__()
        uic.loadUi("modifyPlaylist.ui", self)

        self._format = _format
        self.oldName.setText(oldName)
        self.tableWidget = TableManagement.TableManagement(_format, oldName)
        self.tableWidget.setGeometry(20, 130, 561, 301)
