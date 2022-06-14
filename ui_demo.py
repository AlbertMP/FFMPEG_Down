# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demo.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(634, 239)
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.m3u8Link = QLineEdit(self.centralwidget)
        self.m3u8Link.setObjectName(u"m3u8Link")

        self.gridLayout.addWidget(self.m3u8Link, 1, 1, 1, 3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.download = QPushButton(self.centralwidget)
        self.download.setObjectName(u"download")

        self.gridLayout.addWidget(self.download, 4, 3, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.fileName = QLineEdit(self.centralwidget)
        self.fileName.setObjectName(u"fileName")

        self.gridLayout.addWidget(self.fileName, 2, 1, 1, 1)

        self.selecDirectory = QPushButton(self.centralwidget)
        self.selecDirectory.setObjectName(u"selecDirectory")

        self.gridLayout.addWidget(self.selecDirectory, 2, 3, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.status = QLabel(self.centralwidget)
        self.status.setObjectName(u"status")

        self.gridLayout.addWidget(self.status, 3, 1, 1, 3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)


        self.formLayout.setLayout(0, QFormLayout.SpanningRole, self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 634, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FFMPEG DOWNLOADER", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"File Name:", None))
        self.download.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"FFMPEG Downloader", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.selecDirectory.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"M3U8 Link:", None))
        self.status.setText(QCoreApplication.translate("MainWindow", u"Unknown", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u".mp4", None))
    # retranslateUi

