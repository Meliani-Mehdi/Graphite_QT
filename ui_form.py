# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QMainWindow, QMenu, QMenuBar, QScrollArea,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

class Ui_Graphite(object):
    def setupUi(self, Graphite):
        if not Graphite.objectName():
            Graphite.setObjectName(u"Graphite")
        Graphite.resize(1200, 673)
        icon = QIcon()
        icon.addFile(u"assets/Graphite.png", QSize(), QIcon.Normal, QIcon.Off)
        Graphite.setWindowIcon(icon)
        Graphite.setIconSize(QSize(50, 50))
        self.actionNew = QAction(Graphite)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(Graphite)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(Graphite)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_as = QAction(Graphite)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionOpen_recent = QAction(Graphite)
        self.actionOpen_recent.setObjectName(u"actionOpen_recent")
        self.actionExit = QAction(Graphite)
        self.actionExit.setObjectName(u"actionExit")
        self.actionpref = QAction(Graphite)
        self.actionpref.setObjectName(u"actionpref")
        self.actionSettings = QAction(Graphite)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionAbout = QAction(Graphite)
        self.actionAbout.setObjectName(u"actionAbout")
        self.mainLayout = QWidget(Graphite)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setMinimumSize(QSize(1200, 642))
        self.mainLayout.setStyleSheet(u"background-color: rgb(255, 120, 0);")
        self.gridLayout = QGridLayout(self.mainLayout)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.mainLayout)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 160))
        self.frame.setMaximumSize(QSize(16777215, 160))
        self.frame.setStyleSheet(u"background-color: rgb(94, 92, 100);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.mainLayout)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(250, 0))
        self.frame_2.setMaximumSize(QSize(250, 16777215))
        self.frame_2.setStyleSheet(u"background-color: rgb(51, 209, 122);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget = QTabWidget(self.mainLayout)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        self.scrollArea = QScrollArea(self.mainLayout)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(160, 0))
        self.scrollArea.setMaximumSize(QSize(160, 16777215))
        self.scrollArea.setStyleSheet(u"background-color: rgb(145, 65, 172);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 150, 468))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(150, 0))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(150, 16777215))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        Graphite.setCentralWidget(self.mainLayout)
        self.menubar = QMenuBar(Graphite)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 31))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        Graphite.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_recent)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionpref)
        self.menuEdit.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(Graphite)

        QMetaObject.connectSlotsByName(Graphite)
    # setupUi

    def retranslateUi(self, Graphite):
        Graphite.setWindowTitle(QCoreApplication.translate("Graphite", u"Graphite", None))
        self.actionNew.setText(QCoreApplication.translate("Graphite", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("Graphite", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("Graphite", u"Save", None))
        self.actionSave_as.setText(QCoreApplication.translate("Graphite", u"Save as ...", None))
        self.actionOpen_recent.setText(QCoreApplication.translate("Graphite", u"Open recent", None))
        self.actionExit.setText(QCoreApplication.translate("Graphite", u"Exit", None))
        self.actionpref.setText(QCoreApplication.translate("Graphite", u"pref", None))
        self.actionSettings.setText(QCoreApplication.translate("Graphite", u"Settings", None))
        self.actionAbout.setText(QCoreApplication.translate("Graphite", u"About", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Graphite", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Graphite", u"Tab 2", None))
        self.menuFile.setTitle(QCoreApplication.translate("Graphite", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("Graphite", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Graphite", u"Help", None))
    # retranslateUi

