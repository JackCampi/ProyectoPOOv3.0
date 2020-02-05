from PyQt5 import QtWidgets, uic
import TableManagement


class Dialog(QtWidgets.QDialog):
    def __init__(self, _format, name):
        super().__init__()
        uic.loadUi("modifyPlaylist.ui", self)

        self._format = _format
        #self.playlistName.setText(name)
        self.tableWidget = TableManagement.TableManagement(_format, name)
        self.tableWidget.setGeometry(20, 30, 531, 21)
