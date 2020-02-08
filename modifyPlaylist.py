"""Módulo modifyPLaylist, se encarga de la interfaza de usuario y funcionalidad
    necesaria para modificar listas de reproducción"""

from PyQt5 import QtWidgets, uic
import TableManagement
import Files


class Dialog(QtWidgets.QDialog):
    """
    Clase Dialog del módulo modifyPlaylist, la instancia de TableManagement (ver TableManagement)
    en esta ventana de diálogo permite la selección múltiple, a diferencia de la versión original.

    Al modificar las playlists, se pueden agregar elementos y cambiar el nombre de la playlist.
    Esta clase es una implementación gráfica del módulo Files.

    Tiene las siguientes propiedades:
    _format: Para manejar el formato, ver módulos Format, Files, TableManagement
    oldName: El nombre original de la lista de reproducción que se está modificando.
    tableWidget: instancia de TableManagement (ver TableManegement).
    """
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
        """
        Retorna en un diccionario el nuevo nombre de la lista de reproducción*
        y las nuevas entradas a agregar, las llaves del diccionario son "newName" y "selectedEntries"

        *Si el usuario no ingresa nada será la cadena vacía.
         Por seguridad se recomienda usar únicamente ASCII
        """
        self.tableWidget.UpdateSelectedEntries()
        items = {"newName": self.newName.text(),
                 "selectedEntries": self.tableWidget.selectedEntries}
        return items
