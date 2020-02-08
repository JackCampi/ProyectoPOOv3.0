"""Módulo newPLaylist, se encarga de la interfaza de usuario y funcionalidad
    necesaria para hacer listas de reproducción"""

from PyQt5 import QtWidgets, uic
import TableManagement


class Dialog(QtWidgets.QDialog):
    """
    Clase Dialog del módulo modifyPlaylist, la instancia de TableManagement (ver TableManagement)
    en esta ventana de diálogo permite la selección múltiple, a diferencia de la versión original.

    Al hacer una nueva playlist, se le pueden ingresar elementos de la lista principal asociada
    directamente.

    Tiene las siguientes propiedades:
    _format: Para manejar el formato, ver módulos Format, Files, TableManagement
    tableWidget: instancia de TableManagement (ver TableManegement).
    """
    def __init__(self, _format):
        super().__init__()
        uic.loadUi("newPlaylist.ui", self)
        self._format = _format
        self.tableWidget = TableManagement.TableManagement(_format, self)
        self.tableWidget.setGeometry(20, 110, 561, 321)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

    def Items(self):
        """
        Retorna en un diccionario el nombre de la nueva lista de reproducción*
        y las entradas a agregar, las llaves del diccionario son "playlistName" y "selectedEntries"

        *Por seguridad se recomienda usar únicamente ASCII
        """
        self.tableWidget.UpdateSelectedEntries()
        items = {"playlistName": self.playlistName.text(), "selectedEntries": self.tableWidget.selectedEntries}
        return items
