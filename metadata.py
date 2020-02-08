"""Funcionalidad de la ventana de diálogo para ingresar los datos de los elementos,
    sirve para añadir y también para modificar."""

from PyQt5 import QtWidgets, uic


class Dialog(QtWidgets.QDialog):
    """
    Clase Dialog del módulo metadata, (parámetros en el __init__)
    Tiene las siguientes propiedades
    _format: Para manejar el formato, ver módulo Format
    path: vacío por defecto, cambia en caso de que se quiera agregar una ubicación para reproducir el elemento
    """
    def __init__(self, _format, modify=False):
        """
        :param _format: (str) puede ser "music", "videos", o "pictures".
        :param modify: (bool) se encarga de decidir si la interfaz se va a usar para añadir
            o para modificar, por defecto está en añadir.
        """
        super().__init__()
        uic.loadUi(r"metadata.ui", self)

        self.setPath.clicked.connect(self.click)

        self._format = _format
        self.path = ""
        self.__setup(_format, modify)

    def __setup(self, _format, modify):
        """
        Cambios menores en la interfaz, dependiendo del formato y de la modalidad (añadir/modificar)
        Función interna, se llama desde el instanciador.
        """
        if modify:
            self.setWindowTitle("Modificar")
        if _format == "music":
            self.author.setText("Artista:")
            pass
        elif _format == "pictures":
            self.type.setText("Tipo:")

    def click(self):
        """
        Se encarga de modificar la interfaz y cambiar la propiedad path si el usuario
        decide seleccionar un archivo de ubicación.
        """
        selectedFile = self.selectFilePath()
        if selectedFile != "":
            self.pathLabel.setText("*Archivo seleccionado*")
            self.pathLabel.setStyleSheet('color: green')
            self.path = selectedFile

    def selectFilePath(self):
        """
        No está en uso.
        """
        fileDialog = SelectFileDialog(self._format)
        selectedFile = [""]
        fileDialog.show()
        if fileDialog.exec_():
            selectedFile = fileDialog.selectedFiles()
        return selectedFile[0]

    def items(self):
        """
        Retorna la información ingresada por el usuario en formade diccionario.
        """
        items = {
            "name": self.nameInput.text(),
            "author": self.authorInput.text(),
            "album": self.albumInput.text(),
            "year": self.yearInput.text(),
            "type": self.typeInput.text(),
            "path": self.path
        }
        return items


class SelectFileDialog(QtWidgets.QFileDialog):
    """
    Esta clase entra en funcionamiento cuando el ussuario decide escoger una ubicación
    para poder reproducir archivos.
    Tiene las siguientes propiedades:
    _format: Para manejar el formato, ver módulos Format, Files, TableManagement
    _filter: Decide si lo que se busca son canciones, fotos, o videos.
    """
    def __init__(self, _format):
        super().__init__()
        self._format = self.__setFileDialogFormat(_format)
        self._filter = self.__setFileDialogFilter(_format)
        self.setWindowTitle(f"Seleccionar {self._format}")
        self.setNameFilter(self._filter)

    @staticmethod
    def __setFileDialogFormat(_format):
        """
        Cambia la propiedad format, esto función existe para mostrar en español
        el formato del dialogo para la ubicación, pues originalmente estaría en inglés
        """
        if _format == "music":
            return "canción"
        elif _format == "pictures":
            return "foto"
        elif _format == "videos":
            return "video"

    @staticmethod
    def __setFileDialogFilter(_format):
        """
        Se encarga de ajustar el filtro deseado.
        """
        if _format == "music":
            return "Canciones (*.mp3)"
        elif _format == "pictures":
            return "Imágenes (*.png *jpg)"
        elif _format == "videos":
            return "Videos (*.mp4 *.mkv)"


if __name__ == "__main__":
    import sys
    _format = "pictures"
    app = QtWidgets.QApplication(sys.argv)
    dialog = Dialog(_format)
    dialog.show()
    sys.exit(app.exec_())
