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
    QHeaderView, QMainWindow, QMenu, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTabWidget, QTreeView, QVBoxLayout, QWidget)

class Ui_Graphite(object):
    def setupUi(self, Graphite):
        if not Graphite.objectName():
            Graphite.setObjectName(u"Graphite")
        Graphite.resize(1200, 673)
        icon = QIcon()
        icon.addFile(u"assets/Graphite.png", QSize(), QIcon.Normal, QIcon.Off)
        Graphite.setWindowIcon(icon)
        Graphite.setIconSize(QSize(50, 50))
        self.new_file = QAction(Graphite)
        self.new_file.setObjectName(u"new_file")
        self.open_file = QAction(Graphite)
        self.open_file.setObjectName(u"open_file")
        self.save = QAction(Graphite)
        self.save.setObjectName(u"save")
        self.save_as = QAction(Graphite)
        self.save_as.setObjectName(u"save_as")
        self.open_recent = QAction(Graphite)
        self.open_recent.setObjectName(u"open_recent")
        self.exit_app = QAction(Graphite)
        self.exit_app.setObjectName(u"exit_app")
        self.exit_app.setMenuRole(QAction.QuitRole)
        self.actionpref = QAction(Graphite)
        self.actionpref.setObjectName(u"actionpref")
        self.settings = QAction(Graphite)
        self.settings.setObjectName(u"settings")
        self.about = QAction(Graphite)
        self.about.setObjectName(u"about")
        self.mainLayout = QWidget(Graphite)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setMinimumSize(QSize(1200, 642))
        self.mainLayout.setStyleSheet(u"background-color: rgb(255, 120, 0);")
        self.gridLayout = QGridLayout(self.mainLayout)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame1 = QFrame(self.mainLayout)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setMinimumSize(QSize(0, 160))
        self.frame1.setMaximumSize(QSize(16777215, 160))
        self.frame1.setStyleSheet(u"background-color: rgb(94, 92, 100);")
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame2 = QVBoxLayout()
        self.frame2.setSpacing(0)
        self.frame2.setObjectName(u"frame2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(16)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.pushButton = QPushButton(self.mainLayout)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(32, 32))
        self.pushButton.setMaximumSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.pushButton)


        self.frame2.addLayout(self.verticalLayout_4)

        self.treeView = QTreeView(self.mainLayout)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setMinimumSize(QSize(250, 0))
        self.treeView.setMaximumSize(QSize(250, 16777215))

        self.frame2.addWidget(self.treeView)


        self.horizontalLayout.addLayout(self.frame2)

        self.Tab_graph = QHBoxLayout()
        self.Tab_graph.setObjectName(u"Tab_graph")
        self.graphTab = QTabWidget(self.mainLayout)
        self.graphTab.setObjectName(u"graphTab")
        self.graphTab.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.graphTab.setTabsClosable(True)

        self.Tab_graph.addWidget(self.graphTab)


        self.horizontalLayout.addLayout(self.Tab_graph)

        self.graphTypes = QScrollArea(self.mainLayout)
        self.graphTypes.setObjectName(u"graphTypes")
        self.graphTypes.setMinimumSize(QSize(130, 0))
        self.graphTypes.setMaximumSize(QSize(130, 16777215))
        self.graphTypes.setWidgetResizable(True)
        self.typeButtons = QWidget()
        self.typeButtons.setObjectName(u"typeButtons")
        self.typeButtons.setGeometry(QRect(0, 0, 114, 664))
        self.typeButtons.setStyleSheet(u"\n"
"background-color: rgb(23, 23, 23);")
        self.verticalLayout_3 = QVBoxLayout(self.typeButtons)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.plot = QPushButton(self.typeButtons)
        self.plot.setObjectName(u"plot")
        self.plot.setMinimumSize(QSize(110, 110))
        self.plot.setMaximumSize(QSize(110, 110))
        icon1 = QIcon()
        icon1.addFile(u"assets/plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.plot.setIcon(icon1)
        self.plot.setIconSize(QSize(120, 120))

        self.verticalLayout_3.addWidget(self.plot)

        self.histogram = QPushButton(self.typeButtons)
        self.histogram.setObjectName(u"histogram")
        self.histogram.setMinimumSize(QSize(110, 110))
        self.histogram.setMaximumSize(QSize(110, 110))
        icon2 = QIcon()
        icon2.addFile(u"assets/Bar-Chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.histogram.setIcon(icon2)
        self.histogram.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.histogram)

        self.piechart = QPushButton(self.typeButtons)
        self.piechart.setObjectName(u"piechart")
        self.piechart.setMinimumSize(QSize(110, 110))
        self.piechart.setMaximumSize(QSize(110, 110))
        icon3 = QIcon()
        icon3.addFile(u"assets/Pie-Chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.piechart.setIcon(icon3)
        self.piechart.setIconSize(QSize(110, 110))

        self.verticalLayout_3.addWidget(self.piechart, 0, Qt.AlignTop)

        self.pushButton_4 = QPushButton(self.typeButtons)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(110, 110))
        self.pushButton_4.setMaximumSize(QSize(110, 110))
        self.pushButton_4.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.pushButton_4, 0, Qt.AlignTop)

        self.pushButton_6 = QPushButton(self.typeButtons)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(110, 110))
        self.pushButton_6.setMaximumSize(QSize(110, 110))
        self.pushButton_6.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.pushButton_6, 0, Qt.AlignTop)

        self.pushButton_5 = QPushButton(self.typeButtons)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(110, 110))
        self.pushButton_5.setMaximumSize(QSize(110, 110))
        self.pushButton_5.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.pushButton_5, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.graphTypes.setWidget(self.typeButtons)
        self.plot.raise_()
        self.histogram.raise_()
        self.piechart.raise_()
        self.pushButton_6.raise_()
        self.pushButton_5.raise_()
        self.pushButton_4.raise_()

        self.horizontalLayout.addWidget(self.graphTypes)


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
        self.menuFile.addAction(self.new_file)
        self.menuFile.addAction(self.open_file)
        self.menuFile.addAction(self.save)
        self.menuFile.addAction(self.save_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.open_recent)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.exit_app)
        self.menuEdit.addAction(self.actionpref)
        self.menuEdit.addAction(self.settings)
        self.menuHelp.addAction(self.about)

        self.retranslateUi(Graphite)

        self.graphTab.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Graphite)
    # setupUi

    def retranslateUi(self, Graphite):
        Graphite.setWindowTitle(QCoreApplication.translate("Graphite", u"Graphite", None))
        self.new_file.setText(QCoreApplication.translate("Graphite", u"New", None))
#if QT_CONFIG(shortcut)
        self.new_file.setShortcut(QCoreApplication.translate("Graphite", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.open_file.setText(QCoreApplication.translate("Graphite", u"Open", None))
#if QT_CONFIG(shortcut)
        self.open_file.setShortcut(QCoreApplication.translate("Graphite", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.save.setText(QCoreApplication.translate("Graphite", u"Save", None))
#if QT_CONFIG(shortcut)
        self.save.setShortcut(QCoreApplication.translate("Graphite", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.save_as.setText(QCoreApplication.translate("Graphite", u"Save as ...", None))
#if QT_CONFIG(shortcut)
        self.save_as.setShortcut(QCoreApplication.translate("Graphite", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.open_recent.setText(QCoreApplication.translate("Graphite", u"Open recent", None))
#if QT_CONFIG(shortcut)
        self.open_recent.setShortcut(QCoreApplication.translate("Graphite", u"Ctrl+Shift+O", None))
#endif // QT_CONFIG(shortcut)
        self.exit_app.setText(QCoreApplication.translate("Graphite", u"Exit", None))
        self.actionpref.setText(QCoreApplication.translate("Graphite", u"pref", None))
        self.settings.setText(QCoreApplication.translate("Graphite", u"Settings", None))
        self.about.setText(QCoreApplication.translate("Graphite", u"About", None))
        self.pushButton.setText("")
        self.plot.setText("")
        self.histogram.setText("")
        self.piechart.setText("")
        self.pushButton_4.setText("")
        self.pushButton_6.setText("")
        self.pushButton_5.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("Graphite", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("Graphite", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Graphite", u"Help", None))
    # retranslateUi

