"""Módulo TableManagement, se encarga de manejar todas las tablas"""

from PyQt5 import QtWidgets, QtCore
import Files
import Format


class TableManagement(QtWidgets.QTableWidget):
    """
    Clase TableManagement, hereda de QTableWidget, con la diferencia de que carga
    los archivos, en parte, es una imlpementación gráfica del módulo Files.
    Tiene las siguientes propiedades:
    _format: Para manejar el formato, ver módulos Format, Files, TableManagement.
    selectedEntries: Las entradas seleccionadas de la tabla.
    filters: En el caso de modifyPlaylist y newPlaylist, solo se desea mostrar
            los elementos de la Main_list que no están en la playlist abierta.
    mainList: Mainlist (ver Files.Mainlist)

    """
    def __init__(self, _format, parent=None, filters=()):
        """
        :param _format: ver Format.
        :param parent: del tipo QWidget
        :param filters: Iterable de objetos de Format
        """
        super().__init__(parent)

        self.selectedEntries = []
        self._format = _format
        self.filters = filters
        self.mainList = Files.MainList(_format)
        self.SetupUi()
        self.LoadList()
    
    def SetupUi(self):
        """
        Inicializa correctametne la cabecera y sus labels, incluyendo
        algunas característica clave como:
          setSortingEnabled: Para que la tabla se pueda ordenar por columnas
          setEditTriggers: Para que no sea modificable de ninguna forma
        Además, modifica el aspecto de la cabecera dependiendo del formato.
        """
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
        """
        Carga la lista de la mainList en la tabla.
        Por cuestiones de la librería (ver documentación de Qt for Python) no es
        conveniente agregar elementos cuando el ordenamiento está activado, por eso se
        desactiva y se vuelve a activar.
        """
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
        """
        Retorna el elemento seleccionado de la tabla en la forma de un objeto de Format
        (ya sea de la clase Music, Pictures o Videos)
        """
        row = self.currentRow()
        elem = {"name": self.item(row, 0).text(),
                "author": self.item(row, 1).text(),
                "album": self.item(row, 2).text(),
                "year": self.item(row, 3).text(),
                "type": self.item(row, 4).text()}

        return self.constructor(elem["name"], elem["author"], elem["album"], elem["year"], elem["type"], "")

    def UpdateSelectedEntries(self):
        """
        Función interna necesaria para actualizar la lista de los elementos seleccionados
        """
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
        """Acutaliza el formato y vuelve a cargar la lsita principal"""
        self._format = newFormat
        self.mainList = Files.MainList(newFormat)
        self.LoadList()

    def UpdatePlaylist(self, newFormat, newPlaylist):
        """Ifual que su homónimo para Main_list, solo que para playlists"""
        self._format = newFormat
        self.mainList = Files.Playlist(newFormat, newPlaylist)
        self.LoadList()
