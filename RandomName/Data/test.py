from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog
from PyQt5.QtCore import QFile


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        openFile = QAction('打开', self)
        openFile.triggered.connect(self.file_open)
        self.toolbar = self.addToolBar('！！！')
        self.toolbar.addAction(openFile)

    def file_open(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")
        if fileName:
            with open(fileName, 'r') as file:
                print(file.read())


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
