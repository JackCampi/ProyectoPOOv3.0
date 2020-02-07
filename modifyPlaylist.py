from PyQt5 import QtWidgets, uic
import TableManagement
import Files


class Dialog(QtWidgets.QDialog):
    def __init__(self, _format, oldName):
        super().__init__()
        uic.loadUi("modifyPlaylist.ui", self)

        self._format = _format
        self.oldName.setText(oldName)
        playlist = Files.Playlist(_format, oldName)
        self.tableWidget = TableManagement.TableManagement(_format, self, playlist.list)
        self.tableWidget.setGeometry(20, 130, 561, 301)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

    def Items(self):
        self.tableWidget.UpdateSelectedEntries()
        items = {"newName": self.newName.text(),
                 "selectedEntries": self.tableWidget.selectedEntries}
        return items
