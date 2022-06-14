from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
# PySide6-uic demo.ui -o ui_demo.py
from ui_demo import Ui_MainWindow
import applescript


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.band()
        self.show()

    def band(self):
        self.ui.download.clicked.connect(self.handle_click)
        # self.ui.selecDirectory.clicked.connect(self.open_file)

    def handle_click(self):
        m3u8Link = self.ui.m3u8Link.text()
        fileName = self.ui.fileName.text()

        # Make sure ffmpeg has been installed system wide before use terminal command
        path = self.open_file()
        if path != '':
            command = "do script \"ffmpeg -i '" + m3u8Link + "' " + path + "/" + fileName + ".mp4\""
            applescript.tell.app("Terminal", command)
            self.ui.status.setText("No specific directory.")
        else:
            command = "do script \"ffmpeg -i '" + m3u8Link + "' " + fileName + ".mp4\""
            applescript.tell.app("Terminal", command)


    def open_file(self):
        # open file
        # fileName = QFileDialog.getOpenFileName(self, 'Open a file', '', 'All Files (*.*)')
        return QFileDialog.getExistingDirectory(self)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()

    app.exec()
