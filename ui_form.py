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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTextEdit, QTreeView, QVBoxLayout, QWidget)

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
        self.open_folder = QAction(Graphite)
        self.open_folder.setObjectName(u"open_folder")
        self.mainLayout = QWidget(Graphite)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setMinimumSize(QSize(1200, 642))
        self.mainLayout.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.gridLayout = QGridLayout(self.mainLayout)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame1 = QFrame(self.mainLayout)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setMinimumSize(QSize(0, 160))
        self.frame1.setMaximumSize(QSize(16777215, 160))
        self.frame1.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.Mode_menu = QComboBox(self.frame1)
        self.Mode_menu.addItem("")
        self.Mode_menu.addItem("")
        self.Mode_menu.addItem("")
        self.Mode_menu.setObjectName(u"Mode_menu")
        self.Mode_menu.setGeometry(QRect(350, 120, 111, 31))
        self.Mode_menu.setStyleSheet(u"")
        self.mode_frames = QStackedWidget(self.frame1)
        self.mode_frames.setObjectName(u"mode_frames")
        self.mode_frames.setGeometry(QRect(470, 10, 321, 101))
        self.Math_page = QWidget()
        self.Math_page.setObjectName(u"Math_page")
        self.mode_frames.addWidget(self.Math_page)
        self.Eccomerce_page = QWidget()
        self.Eccomerce_page.setObjectName(u"Eccomerce_page")
        self.mode_frames.addWidget(self.Eccomerce_page)
        self.Biology_page = QWidget()
        self.Biology_page.setObjectName(u"Biology_page")
        self.mode_frames.addWidget(self.Biology_page)
        self.textEdit = QTextEdit(self.frame1)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(560, 120, 211, 31))
        self.label_2 = QLabel(self.frame1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(490, 120, 49, 31))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame2 = QVBoxLayout()
        self.frame2.setSpacing(0)
        self.frame2.setObjectName(u"frame2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.label = QLabel(self.mainLayout)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 10pt \"ProFontWindows Nerd Font Propo\";\n"
"rgb:(255, 255, 255);\n"
"")

        self.horizontalLayout_2.addWidget(self.label)

        self.pushButton = QPushButton(self.mainLayout)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(32, 32))
        self.pushButton.setMaximumSize(QSize(32, 32))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.mainLayout)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(32, 32))
        self.pushButton_3.setMaximumSize(QSize(32, 32))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.mainLayout)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(32, 32))
        self.pushButton_2.setMaximumSize(QSize(32, 32))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.frame2.addLayout(self.horizontalLayout_2)

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
        self.graphTab.setMovable(True)

        self.Tab_graph.addWidget(self.graphTab)


        self.horizontalLayout.addLayout(self.Tab_graph)

        self.graphTypes = QScrollArea(self.mainLayout)
        self.graphTypes.setObjectName(u"graphTypes")
        self.graphTypes.setMinimumSize(QSize(130, 0))
        self.graphTypes.setMaximumSize(QSize(130, 16777215))
        self.graphTypes.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.graphTypes.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphTypes.setWidgetResizable(True)
        self.typeButtons = QWidget()
        self.typeButtons.setObjectName(u"typeButtons")
        self.typeButtons.setGeometry(QRect(0, 0, 114, 1324))
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
        self.plot.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"assets/plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.plot.setIcon(icon1)
        self.plot.setIconSize(QSize(120, 120))

        self.verticalLayout_3.addWidget(self.plot)

        self.histogram = QPushButton(self.typeButtons)
        self.histogram.setObjectName(u"histogram")
        self.histogram.setMinimumSize(QSize(110, 110))
        self.histogram.setMaximumSize(QSize(110, 110))
        self.histogram.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"assets/Bar-Chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.histogram.setIcon(icon2)
        self.histogram.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.histogram)

        self.piechart = QPushButton(self.typeButtons)
        self.piechart.setObjectName(u"piechart")
        self.piechart.setMinimumSize(QSize(110, 110))
        self.piechart.setMaximumSize(QSize(110, 110))
        self.piechart.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"assets/Pie-Chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.piechart.setIcon(icon3)
        self.piechart.setIconSize(QSize(110, 110))

        self.verticalLayout_3.addWidget(self.piechart, 0, Qt.AlignTop)

        self.fill_between = QPushButton(self.typeButtons)
        self.fill_between.setObjectName(u"fill_between")
        self.fill_between.setMinimumSize(QSize(110, 110))
        self.fill_between.setMaximumSize(QSize(110, 110))
        self.fill_between.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"assets/fill_between.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fill_between.setIcon(icon4)
        self.fill_between.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.fill_between, 0, Qt.AlignTop)

        self.stackplot = QPushButton(self.typeButtons)
        self.stackplot.setObjectName(u"stackplot")
        self.stackplot.setMinimumSize(QSize(110, 110))
        self.stackplot.setMaximumSize(QSize(110, 110))
        self.stackplot.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"assets/stackplot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stackplot.setIcon(icon5)
        self.stackplot.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.stackplot)

        self.pushButton_11 = QPushButton(self.typeButtons)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(110, 110))
        self.pushButton_11.setMaximumSize(QSize(110, 110))
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_11.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.pushButton_11)

        self.pushButton_10 = QPushButton(self.typeButtons)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(110, 110))
        self.pushButton_10.setMaximumSize(QSize(110, 110))
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.pushButton_10)

        self.pushButton_9 = QPushButton(self.typeButtons)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(110, 110))
        self.pushButton_9.setMaximumSize(QSize(110, 110))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.pushButton_9)

        self.pushButton_6 = QPushButton(self.typeButtons)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(110, 110))
        self.pushButton_6.setMaximumSize(QSize(110, 110))
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_8 = QPushButton(self.typeButtons)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(110, 110))
        self.pushButton_8.setMaximumSize(QSize(110, 110))
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.typeButtons)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(110, 110))
        self.pushButton_7.setMaximumSize(QSize(110, 110))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_5 = QPushButton(self.typeButtons)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(110, 110))
        self.pushButton_5.setMaximumSize(QSize(110, 110))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.graphTypes.setWidget(self.typeButtons)
        self.plot.raise_()
        self.histogram.raise_()
        self.piechart.raise_()
        self.pushButton_6.raise_()
        self.pushButton_5.raise_()
        self.fill_between.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.pushButton_11.raise_()
        self.stackplot.raise_()

        self.horizontalLayout.addWidget(self.graphTypes)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        Graphite.setCentralWidget(self.mainLayout)
        self.menubar = QMenuBar(Graphite)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 22))
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
        self.menuFile.addAction(self.open_folder)
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

        self.mode_frames.setCurrentIndex(2)
        self.graphTab.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Graphite)
    # setupUi

    def retranslateUi(self, Graphite):
        Graphite.setWindowTitle(QCoreApplication.translate("Graphite", u"Graphite", None))
        self.new_file.setText(QCoreApplication.translate("Graphite", u"New", None))
#if QT_CONFIG(shortcut)
        self.new_file.setShortcut(QCoreApplication.translate("Graphite", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.open_file.setText(QCoreApplication.translate("Graphite", u"Open file", None))
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
        self.open_recent.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.exit_app.setText(QCoreApplication.translate("Graphite", u"Exit", None))
        self.actionpref.setText(QCoreApplication.translate("Graphite", u"pref", None))
        self.settings.setText(QCoreApplication.translate("Graphite", u"Settings", None))
        self.about.setText(QCoreApplication.translate("Graphite", u"About", None))
        self.open_folder.setText(QCoreApplication.translate("Graphite", u"Open folder", None))
#if QT_CONFIG(shortcut)
        self.open_folder.setShortcut(QCoreApplication.translate("Graphite", u"Ctrl+Shift+O", None))
#endif // QT_CONFIG(shortcut)
        self.Mode_menu.setItemText(0, QCoreApplication.translate("Graphite", u"Math", None))
        self.Mode_menu.setItemText(1, QCoreApplication.translate("Graphite", u"Biology", None))
        self.Mode_menu.setItemText(2, QCoreApplication.translate("Graphite", u"Eccomerce", None))

        self.textEdit.setHtml(QCoreApplication.translate("Graphite", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Graphite", u"<html><head/><body><p><span style=\" font-size:14pt;\">f(x)=</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Graphite", u"    Project Tree", None))
        self.pushButton.setText("")
        self.pushButton_3.setText("")
        self.pushButton_2.setText("")
        self.plot.setText("")
        self.histogram.setText("")
        self.piechart.setText("")
        self.fill_between.setText("")
        self.stackplot.setText("")
        self.pushButton_11.setText("")
        self.pushButton_10.setText("")
        self.pushButton_9.setText("")
        self.pushButton_6.setText("")
        self.pushButton_8.setText("")
        self.pushButton_7.setText("")
        self.pushButton_5.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("Graphite", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("Graphite", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Graphite", u"Help", None))
    # retranslateUi

