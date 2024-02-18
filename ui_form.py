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
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTreeView,
    QVBoxLayout, QWidget)

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
        self.MathMode = QAction(Graphite)
        self.MathMode.setObjectName(u"MathMode")
        self.BchimieMode = QAction(Graphite)
        self.BchimieMode.setObjectName(u"BchimieMode")
        self.actionWorksheet = QAction(Graphite)
        self.actionWorksheet.setObjectName(u"actionWorksheet")
        self.actionExel = QAction(Graphite)
        self.actionExel.setObjectName(u"actionExel")
        self.actiongraph = QAction(Graphite)
        self.actiongraph.setObjectName(u"actiongraph")
        self.actionwoeksheet = QAction(Graphite)
        self.actionwoeksheet.setObjectName(u"actionwoeksheet")
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
        self.horizontalLayout_3 = QHBoxLayout(self.frame1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame1)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(250, 0))
        self.frame.setMaximumSize(QSize(250, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_2)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(2)
        self.custom_button_2 = QPushButton(self.frame_3)
        self.custom_button_2.setObjectName(u"custom_button_2")
        self.custom_button_2.setMinimumSize(QSize(32, 32))
        self.custom_button_2.setMaximumSize(QSize(32, 32))

        self.gridLayout_2.addWidget(self.custom_button_2, 2, 0, 1, 1)

        self.custom_button_3 = QPushButton(self.frame_3)
        self.custom_button_3.setObjectName(u"custom_button_3")
        self.custom_button_3.setMinimumSize(QSize(32, 32))
        self.custom_button_3.setMaximumSize(QSize(32, 32))

        self.gridLayout_2.addWidget(self.custom_button_3, 2, 1, 1, 1)

        self.custom_button_6 = QPushButton(self.frame_3)
        self.custom_button_6.setObjectName(u"custom_button_6")
        self.custom_button_6.setMinimumSize(QSize(32, 32))
        self.custom_button_6.setMaximumSize(QSize(32, 32))

        self.gridLayout_2.addWidget(self.custom_button_6, 1, 2, 1, 1)

        self.custom_button_10 = QPushButton(self.frame_3)
        self.custom_button_10.setObjectName(u"custom_button_10")
        self.custom_button_10.setMinimumSize(QSize(32, 32))
        self.custom_button_10.setMaximumSize(QSize(32, 32))

        self.gridLayout_2.addWidget(self.custom_button_10, 1, 0, 1, 1)

        self.custom_button_4 = QPushButton(self.frame_3)
        self.custom_button_4.setObjectName(u"custom_button_4")
        self.custom_button_4.setMinimumSize(QSize(32, 32))
        self.custom_button_4.setMaximumSize(QSize(32, 32))

        self.gridLayout_2.addWidget(self.custom_button_4, 1, 1, 1, 1)

        self.custom_button = QPushButton(self.frame_3)
        self.custom_button.setObjectName(u"custom_button")
        self.custom_button.setMinimumSize(QSize(32, 32))
        self.custom_button.setMaximumSize(QSize(32, 32))
        icon1 = QIcon()
        icon1.addFile(u"assets/formula.png", QSize(), QIcon.Normal, QIcon.Off)
        self.custom_button.setIcon(icon1)
        self.custom_button.setIconSize(QSize(32, 32))

        self.gridLayout_2.addWidget(self.custom_button, 2, 2, 1, 1)

        self.custom_button_7 = QPushButton(self.frame_3)
        self.custom_button_7.setObjectName(u"custom_button_7")
        self.custom_button_7.setMinimumSize(QSize(32, 32))
        self.custom_button_7.setMaximumSize(QSize(32, 32))

        self.gridLayout_2.addWidget(self.custom_button_7, 0, 2, 1, 1)

        self.custom_button_8 = QPushButton(self.frame_3)
        self.custom_button_8.setObjectName(u"custom_button_8")
        self.custom_button_8.setMinimumSize(QSize(32, 32))
        self.custom_button_8.setMaximumSize(QSize(32, 32))

        self.gridLayout_2.addWidget(self.custom_button_8, 0, 1, 1, 1)

        self.custom_button_9 = QPushButton(self.frame_3)
        self.custom_button_9.setObjectName(u"custom_button_9")
        self.custom_button_9.setMinimumSize(QSize(32, 32))
        self.custom_button_9.setMaximumSize(QSize(32, 32))

        self.gridLayout_2.addWidget(self.custom_button_9, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_3)


        self.horizontalLayout_3.addWidget(self.frame)

        self.mode_frames = QStackedWidget(self.frame1)
        self.mode_frames.setObjectName(u"mode_frames")
        self.Math_page = QWidget()
        self.Math_page.setObjectName(u"Math_page")
        self.Math_page.setStyleSheet(u"background-color:rgb(0, 0, 127)")
        self.mode_frames.addWidget(self.Math_page)
        self.Eccomerce_page = QWidget()
        self.Eccomerce_page.setObjectName(u"Eccomerce_page")
        self.Eccomerce_page.setStyleSheet(u"background-color:rgb(85, 255, 0)")
        self.mode_frames.addWidget(self.Eccomerce_page)
        self.Biology_page = QWidget()
        self.Biology_page.setObjectName(u"Biology_page")
        self.Biology_page.setStyleSheet(u"background-color:rgb(255, 255, 0)")
        self.min_max = QPushButton(self.Biology_page)
        self.min_max.setObjectName(u"min_max")
        self.min_max.setGeometry(QRect(10, 10, 81, 41))
        self.min_max.setStyleSheet(u"background-color: rgb(255, 0, 0)")
        self.Polynome = QPushButton(self.Biology_page)
        self.Polynome.setObjectName(u"Polynome")
        self.Polynome.setGeometry(QRect(10, 73, 81, 41))
        self.mode_frames.addWidget(self.Biology_page)

        self.horizontalLayout_3.addWidget(self.mode_frames)


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
        self.folder_icon = QLabel(self.mainLayout)
        self.folder_icon.setObjectName(u"folder_icon")
        self.folder_icon.setMaximumSize(QSize(30, 30))
        self.folder_icon.setPixmap(QPixmap(u"assets/folders.png"))
        self.folder_icon.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.folder_icon)

        self.project_lab = QLabel(self.mainLayout)
        self.project_lab.setObjectName(u"project_lab")
        self.project_lab.setStyleSheet(u"font: 700 10pt \"ProFontWindows Nerd Font Propo\";\n"
"rgb:(255, 255, 255);\n"
"")

        self.horizontalLayout_2.addWidget(self.project_lab)

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
        icon2 = QIcon()
        icon2.addFile(u"assets/plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.plot.setIcon(icon2)
        self.plot.setIconSize(QSize(120, 120))

        self.verticalLayout_3.addWidget(self.plot)

        self.histogram = QPushButton(self.typeButtons)
        self.histogram.setObjectName(u"histogram")
        self.histogram.setMinimumSize(QSize(110, 110))
        self.histogram.setMaximumSize(QSize(110, 110))
        self.histogram.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"assets/Bar-Chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.histogram.setIcon(icon3)
        self.histogram.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.histogram)

        self.piechart = QPushButton(self.typeButtons)
        self.piechart.setObjectName(u"piechart")
        self.piechart.setMinimumSize(QSize(110, 110))
        self.piechart.setMaximumSize(QSize(110, 110))
        self.piechart.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"assets/Pie-Chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.piechart.setIcon(icon4)
        self.piechart.setIconSize(QSize(110, 110))

        self.verticalLayout_3.addWidget(self.piechart, 0, Qt.AlignTop)

        self.fill_between = QPushButton(self.typeButtons)
        self.fill_between.setObjectName(u"fill_between")
        self.fill_between.setMinimumSize(QSize(110, 110))
        self.fill_between.setMaximumSize(QSize(110, 110))
        self.fill_between.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"assets/fill_between.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fill_between.setIcon(icon5)
        self.fill_between.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.fill_between, 0, Qt.AlignTop)

        self.stackplot = QPushButton(self.typeButtons)
        self.stackplot.setObjectName(u"stackplot")
        self.stackplot.setMinimumSize(QSize(110, 110))
        self.stackplot.setMaximumSize(QSize(110, 110))
        self.stackplot.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u"assets/stackplot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stackplot.setIcon(icon6)
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
        self.menuMode = QMenu(self.menubar)
        self.menuMode.setObjectName(u"menuMode")
        self.menuBiology = QMenu(self.menuMode)
        self.menuBiology.setObjectName(u"menuBiology")
        Graphite.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.new_file)
        self.menuFile.addAction(self.open_file)
        self.menuFile.addAction(self.open_folder)
        self.menuFile.addAction(self.actionwoeksheet)
        self.menuFile.addAction(self.save)
        self.menuFile.addAction(self.save_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.open_recent)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.exit_app)
        self.menuEdit.addAction(self.actionpref)
        self.menuEdit.addAction(self.settings)
        self.menuHelp.addAction(self.about)
        self.menuMode.addAction(self.MathMode)
        self.menuMode.addAction(self.menuBiology.menuAction())
        self.menuBiology.addAction(self.BchimieMode)

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
        self.MathMode.setText(QCoreApplication.translate("Graphite", u"Math", None))
        self.BchimieMode.setText(QCoreApplication.translate("Graphite", u"Chimie", None))
        self.actionWorksheet.setText(QCoreApplication.translate("Graphite", u"Worksheet", None))
        self.actionExel.setText(QCoreApplication.translate("Graphite", u"Exel", None))
        self.actiongraph.setText(QCoreApplication.translate("Graphite", u"graph", None))
        self.actionwoeksheet.setText(QCoreApplication.translate("Graphite", u"woeksheet", None))
        self.custom_button_2.setText("")
        self.custom_button_3.setText("")
        self.custom_button_6.setText("")
        self.custom_button_10.setText("")
        self.custom_button_4.setText("")
        self.custom_button.setText("")
        self.custom_button_7.setText("")
        self.custom_button_8.setText("")
        self.custom_button_9.setText("")
        self.min_max.setText(QCoreApplication.translate("Graphite", u"find min max", None))
        self.Polynome.setText(QCoreApplication.translate("Graphite", u"polynome", None))
        self.folder_icon.setText("")
        self.project_lab.setText(QCoreApplication.translate("Graphite", u" Project Tree", None))
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
        self.menuMode.setTitle(QCoreApplication.translate("Graphite", u"Mode", None))
        self.menuBiology.setTitle(QCoreApplication.translate("Graphite", u"Biology", None))
    # retranslateUi

