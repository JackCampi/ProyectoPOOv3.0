"""Functionality of the metadata dialog, it works either for add an element
    or for modify an element"""

from PyQt5 import QtWidgets, uic


class Dialog(QtWidgets.QDialog):
    def __init__(self, _format, modify=False):
        super().__init__()
        uic.loadUi(r"gui\dialogs\metadata.ui", self)

        self.setPath.clicked.connect(self.click)

        self._format = _format
        self.path = ""
        self.__setup(_format, modify)

    def __setup(self, _format, modify):
        if modify:
            self.setWindowTitle("Modificar")

        if _format == "pictures":
            self.author.setText("Protagonista:")

    def click(self):
        selectedFile = self.selectFilePath()
        if selectedFile != "":
            self.pathLabel.setText("*Archivo seleccionado*")
            self.pathLabel.setStyleSheet('color: green')
            self.path = selectedFile

    def selectFilePath(self):
        fileDialog = SelectFileDialog(self._format)
        selectedFile = [""]
        fileDialog.show()
        if fileDialog.exec_():
            selectedFile = fileDialog.selectedFiles()
        return selectedFile[0]

    def items(self):
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
    def __init__(self, _format):
        super().__init__()
        self._format = self.__setFileDialogFormat(_format)
        self._filter = self.__setFileDialogFilter(_format)
        self.setWindowTitle(f"Seleccionar {self._format}")
        self.setNameFilter(self._filter)

    @staticmethod
    def __setFileDialogFormat(_format):
        if _format == "music":
            return "canción"
        elif _format == "pictures":
            return "foto"
        elif _format == "videos":
            return "video"

    @staticmethod
    def __setFileDialogFilter(_format):
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
