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
        Graphite.resize(1433, 724)
        icon = QIcon()
        icon.addFile(u"assets/Graphite.png", QSize(), QIcon.Normal, QIcon.Off)
        Graphite.setWindowIcon(icon)
        Graphite.setStyleSheet(u"QToolTip { color: #ffffff; background-color: #000000; border: 1px solid black; }\n"
"")
        Graphite.setIconSize(QSize(50, 50))
        self.open_file = QAction(Graphite)
        self.open_file.setObjectName(u"open_file")
        self.save = QAction(Graphite)
        self.save.setObjectName(u"save")
        self.save_as = QAction(Graphite)
        self.save_as.setObjectName(u"save_as")
        self.exit_app = QAction(Graphite)
        self.exit_app.setObjectName(u"exit_app")
        self.exit_app.setMenuRole(QAction.NoRole)
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
        self.expo_as = QAction(Graphite)
        self.expo_as.setObjectName(u"expo_as")
        self.expo = QAction(Graphite)
        self.expo.setObjectName(u"expo")
        self.new_work_sheet = QAction(Graphite)
        self.new_work_sheet.setObjectName(u"new_work_sheet")
        self.actionfilters = QAction(Graphite)
        self.actionfilters.setObjectName(u"actionfilters")
        self.actionfilters.setCheckable(False)
        self.actiondata_manipulation = QAction(Graphite)
        self.actiondata_manipulation.setObjectName(u"actiondata_manipulation")
        self.actionfx = QAction(Graphite)
        self.actionfx.setObjectName(u"actionfx")
        self.actiontest = QAction(Graphite)
        self.actiontest.setObjectName(u"actiontest")
        self.mainLayout = QWidget(Graphite)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setMinimumSize(QSize(1200, 642))
        self.mainLayout.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.gridLayout = QGridLayout(self.mainLayout)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.main = QStackedWidget(self.mainLayout)
        self.main.setObjectName(u"main")
        self.Page1 = QWidget()
        self.Page1.setObjectName(u"Page1")
        self.verticalLayout = QVBoxLayout(self.Page1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame1 = QFrame(self.Page1)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setMinimumSize(QSize(0, 160))
        self.frame1.setMaximumSize(QSize(16777215, 160))
        self.frame1.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.frame1.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.frame1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame1)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(250, 0))
        self.frame.setMaximumSize(QSize(300, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame { \n"
"	border: none;\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.open_btn = QPushButton(self.frame_2)
        self.open_btn.setObjectName(u"open_btn")
        self.open_btn.setMinimumSize(QSize(0, 32))
        self.open_btn.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"ProFontWindows Nerd Font Propo"])
        font.setPointSize(12)
        font.setBold(True)
        self.open_btn.setFont(font)
        self.open_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_btn.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 0.5);\n"
"}\n"
"QPushButton {\n"
"    color: white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"assets/upload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_btn.setIcon(icon1)
        self.open_btn.setIconSize(QSize(28, 28))

        self.verticalLayout_4.addWidget(self.open_btn)

        self.save_btn = QPushButton(self.frame_2)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(0, 32))
        self.save_btn.setMaximumSize(QSize(16777215, 16777215))
        self.save_btn.setFont(font)
        self.save_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_btn.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 0.5);\n"
"}\n"
"QPushButton {\n"
"    color: white;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"assets/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_btn.setIcon(icon2)
        self.save_btn.setIconSize(QSize(28, 28))

        self.verticalLayout_4.addWidget(self.save_btn)

        self.export_btn = QPushButton(self.frame_2)
        self.export_btn.setObjectName(u"export_btn")
        self.export_btn.setMinimumSize(QSize(0, 32))
        self.export_btn.setMaximumSize(QSize(16777215, 16777215))
        self.export_btn.setFont(font)
        self.export_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.export_btn.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 0.5);\n"
"}\n"
"QPushButton {\n"
"    color: white;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"assets/export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.export_btn.setIcon(icon3)
        self.export_btn.setIconSize(QSize(28, 28))

        self.verticalLayout_4.addWidget(self.export_btn)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame { \n"
"	border: none;\n"
"}")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.describe = QPushButton(self.frame_3)
        self.describe.setObjectName(u"describe")
        self.describe.setMinimumSize(QSize(0, 32))
        self.describe.setMaximumSize(QSize(16777215, 16777215))
        self.describe.setFont(font)
        self.describe.setCursor(QCursor(Qt.PointingHandCursor))
        self.describe.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 0.5);\n"
"}\n"
"QPushButton {\n"
"    color: white;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"assets/hypothesis.png", QSize(), QIcon.Normal, QIcon.Off)
        self.describe.setIcon(icon4)
        self.describe.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.describe)

        self.custom_button = QPushButton(self.frame_3)
        self.custom_button.setObjectName(u"custom_button")
        self.custom_button.setMinimumSize(QSize(0, 32))
        self.custom_button.setMaximumSize(QSize(16777215, 16777215))
        self.custom_button.setFont(font)
        self.custom_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.custom_button.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 0.5);\n"
"}\n"
"QPushButton {\n"
"    color: white;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"assets/pen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.custom_button.setIcon(icon5)
        self.custom_button.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.custom_button)

        self.worksheet = QPushButton(self.frame_3)
        self.worksheet.setObjectName(u"worksheet")
        self.worksheet.setMinimumSize(QSize(0, 32))
        self.worksheet.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"ProFontWindows Nerd Font Propo"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.worksheet.setFont(font1)
        self.worksheet.setCursor(QCursor(Qt.PointingHandCursor))
        self.worksheet.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 0.5);\n"
"}\n"
"QPushButton {\n"
"    color: white;\n"
"}\n"
"\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"assets/formula.png", QSize(), QIcon.Normal, QIcon.Off)
        self.worksheet.setIcon(icon6)
        self.worksheet.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.worksheet)


        self.horizontalLayout_4.addWidget(self.frame_3)


        self.horizontalLayout_3.addWidget(self.frame)

        self.mode_frames = QTabWidget(self.frame1)
        self.mode_frames.setObjectName(u"mode_frames")
        self.mode_frames.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: black; /* Optional: Change the text color if needed */\n"
"    border: 1px solid black; /* Optional: Add a border */\n"
"    padding: 5px; /* Optional: Add some padding for better appearance */\n"
"    border-radius: 5px; /* Optional: Add rounded corners */\n"
"}\n"
"\n"
"/* Optional: Change the background color on hover */\n"
"QPushButton:hover {\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"/* Optional: Change the background color when the button is pressed */\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}\n"
"")
        self.mode_framesPage3 = QWidget()
        self.mode_framesPage3.setObjectName(u"mode_framesPage3")
        self.verticalLayout_9 = QVBoxLayout(self.mode_framesPage3)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.mode_framesPage3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 2491, 114))
        self.horizontalLayout_7 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.power = QPushButton(self.scrollAreaWidgetContents_2)
        self.power.setObjectName(u"power")
        self.power.setMinimumSize(QSize(95, 95))
        self.power.setMaximumSize(QSize(95, 95))
        icon7 = QIcon()
        icon7.addFile(u"assets/buttons/algo/power_fit_plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.power.setIcon(icon7)
        self.power.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.power)

        self.quadraple = QPushButton(self.scrollAreaWidgetContents_2)
        self.quadraple.setObjectName(u"quadraple")
        self.quadraple.setMinimumSize(QSize(95, 95))
        self.quadraple.setMaximumSize(QSize(95, 95))
        self.quadraple.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.quadraple)

        self.cubic = QPushButton(self.scrollAreaWidgetContents_2)
        self.cubic.setObjectName(u"cubic")
        self.cubic.setMinimumSize(QSize(95, 95))
        icon8 = QIcon()
        icon8.addFile(u"assets/buttons/algo/cubic_fit_plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cubic.setIcon(icon8)
        self.cubic.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.cubic)

        self.log = QPushButton(self.scrollAreaWidgetContents_2)
        self.log.setObjectName(u"log")
        self.log.setMinimumSize(QSize(95, 95))
        self.log.setMaximumSize(QSize(95, 95))
        self.log.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.log)

        self.linear = QPushButton(self.scrollAreaWidgetContents_2)
        self.linear.setObjectName(u"linear")
        self.linear.setMinimumSize(QSize(95, 95))
        icon9 = QIcon()
        icon9.addFile(u"assets/buttons/algo/linear_fit_plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.linear.setIcon(icon9)
        self.linear.setIconSize(QSize(95, 95))

        self.horizontalLayout_7.addWidget(self.linear)

        self.logi = QPushButton(self.scrollAreaWidgetContents_2)
        self.logi.setObjectName(u"logi")
        self.logi.setMinimumSize(QSize(95, 95))
        self.logi.setMaximumSize(QSize(95, 95))
        self.logi.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.logi)

        self.fourier = QPushButton(self.scrollAreaWidgetContents_2)
        self.fourier.setObjectName(u"fourier")
        self.fourier.setMinimumSize(QSize(95, 95))
        icon10 = QIcon()
        icon10.addFile(u"assets/buttons/algo/fourier_fit_plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fourier.setIcon(icon10)
        self.fourier.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.fourier)

        self.weibull = QPushButton(self.scrollAreaWidgetContents_2)
        self.weibull.setObjectName(u"weibull")
        self.weibull.setMinimumSize(QSize(95, 95))
        self.weibull.setMaximumSize(QSize(95, 95))
        self.weibull.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.weibull)

        self.sine = QPushButton(self.scrollAreaWidgetContents_2)
        self.sine.setObjectName(u"sine")
        self.sine.setMinimumSize(QSize(95, 95))
        icon11 = QIcon()
        icon11.addFile(u"assets/buttons/algo/sine_fit_plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sine.setIcon(icon11)
        self.sine.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.sine)

        self.hill = QPushButton(self.scrollAreaWidgetContents_2)
        self.hill.setObjectName(u"hill")
        self.hill.setMinimumSize(QSize(95, 95))
        self.hill.setMaximumSize(QSize(95, 95))
        self.hill.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.hill)

        self.Polynome = QPushButton(self.scrollAreaWidgetContents_2)
        self.Polynome.setObjectName(u"Polynome")
        self.Polynome.setMinimumSize(QSize(95, 95))
        icon12 = QIcon()
        icon12.addFile(u"assets/buttons/algo/polynomial_fit_plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Polynome.setIcon(icon12)
        self.Polynome.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.Polynome)

        self.expof = QPushButton(self.scrollAreaWidgetContents_2)
        self.expof.setObjectName(u"expof")
        self.expof.setMinimumSize(QSize(95, 95))
        self.expof.setMaximumSize(QSize(95, 95))
        self.expof.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.expof)

        self.cosine = QPushButton(self.scrollAreaWidgetContents_2)
        self.cosine.setObjectName(u"cosine")
        self.cosine.setMinimumSize(QSize(95, 95))
        self.cosine.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.cosine)

        self.gompertz = QPushButton(self.scrollAreaWidgetContents_2)
        self.gompertz.setObjectName(u"gompertz")
        self.gompertz.setMinimumSize(QSize(95, 95))
        self.gompertz.setMaximumSize(QSize(95, 95))
        self.gompertz.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.gompertz)

        self.Gaussian = QPushButton(self.scrollAreaWidgetContents_2)
        self.Gaussian.setObjectName(u"Gaussian")
        self.Gaussian.setMinimumSize(QSize(95, 95))
        self.Gaussian.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.Gaussian)

        self.dexpof = QPushButton(self.scrollAreaWidgetContents_2)
        self.dexpof.setObjectName(u"dexpof")
        self.dexpof.setMinimumSize(QSize(95, 95))
        self.dexpof.setMaximumSize(QSize(95, 95))
        self.dexpof.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.dexpof)

        self.lorenzian = QPushButton(self.scrollAreaWidgetContents_2)
        self.lorenzian.setObjectName(u"lorenzian")
        self.lorenzian.setMinimumSize(QSize(95, 95))
        self.lorenzian.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.lorenzian)

        self.texpof = QPushButton(self.scrollAreaWidgetContents_2)
        self.texpof.setObjectName(u"texpof")
        self.texpof.setMinimumSize(QSize(95, 95))
        self.texpof.setMaximumSize(QSize(95, 95))
        self.texpof.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.texpof)

        self.voigt = QPushButton(self.scrollAreaWidgetContents_2)
        self.voigt.setObjectName(u"voigt")
        self.voigt.setMinimumSize(QSize(95, 95))
        self.voigt.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.voigt)

        self.spline = QPushButton(self.scrollAreaWidgetContents_2)
        self.spline.setObjectName(u"spline")
        self.spline.setMinimumSize(QSize(95, 95))
        self.spline.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.spline)

        self.lowess_2 = QPushButton(self.scrollAreaWidgetContents_2)
        self.lowess_2.setObjectName(u"lowess_2")
        self.lowess_2.setMinimumSize(QSize(95, 95))
        self.lowess_2.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.lowess_2)

        self.sav = QPushButton(self.scrollAreaWidgetContents_2)
        self.sav.setObjectName(u"sav")
        self.sav.setMinimumSize(QSize(95, 95))
        self.sav.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.sav)

        self.mac = QPushButton(self.scrollAreaWidgetContents_2)
        self.mac.setObjectName(u"mac")
        self.mac.setMinimumSize(QSize(95, 95))
        self.mac.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.mac)

        self.segmoidal = QPushButton(self.scrollAreaWidgetContents_2)
        self.segmoidal.setObjectName(u"segmoidal")
        self.segmoidal.setMinimumSize(QSize(95, 95))
        self.segmoidal.setIconSize(QSize(80, 80))

        self.horizontalLayout_7.addWidget(self.segmoidal)

        self.horizontalSpacer_5 = QSpacerItem(93, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 93, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_9.addWidget(self.scrollArea_2)

        self.mode_frames.addTab(self.mode_framesPage3, "")
        self.mode_framesPage4 = QWidget()
        self.mode_framesPage4.setObjectName(u"mode_framesPage4")
        self.mode_framesPage4.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.mode_framesPage4)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.mode_framesPage4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1222, 114))
        self.horizontalLayout_6 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.lowpass = QPushButton(self.scrollAreaWidgetContents)
        self.lowpass.setObjectName(u"lowpass")
        self.lowpass.setMinimumSize(QSize(95, 95))
        self.lowpass.setMaximumSize(QSize(95, 95))
        self.lowpass.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u"assets/buttons/algo/lowpass_filter_plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lowpass.setIcon(icon13)
        self.lowpass.setIconSize(QSize(80, 80))

        self.horizontalLayout_6.addWidget(self.lowpass)

        self.bandpass = QPushButton(self.scrollAreaWidgetContents)
        self.bandpass.setObjectName(u"bandpass")
        self.bandpass.setMinimumSize(QSize(95, 95))
        self.bandpass.setMaximumSize(QSize(95, 95))
        self.bandpass.setCursor(QCursor(Qt.PointingHandCursor))
        self.bandpass.setStyleSheet(u"")
        icon14 = QIcon()
        icon14.addFile(u"assets/buttons/algo/bandpass_filter_plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bandpass.setIcon(icon14)
        self.bandpass.setIconSize(QSize(80, 80))

        self.horizontalLayout_6.addWidget(self.bandpass)

        self.highpass = QPushButton(self.scrollAreaWidgetContents)
        self.highpass.setObjectName(u"highpass")
        self.highpass.setMinimumSize(QSize(95, 95))
        self.highpass.setMaximumSize(QSize(95, 95))
        self.highpass.setCursor(QCursor(Qt.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u"assets/buttons/algo/highpass_filter_plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.highpass.setIcon(icon15)
        self.highpass.setIconSize(QSize(80, 80))

        self.horizontalLayout_6.addWidget(self.highpass)

        self.lowess = QPushButton(self.scrollAreaWidgetContents)
        self.lowess.setObjectName(u"lowess")
        self.lowess.setMinimumSize(QSize(95, 95))
        self.lowess.setMaximumSize(QSize(95, 95))
        self.lowess.setCursor(QCursor(Qt.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u"assets/buttons/algo/lowess_plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lowess.setIcon(icon16)
        self.lowess.setIconSize(QSize(80, 80))

        self.horizontalLayout_6.addWidget(self.lowess)

        self.boxcar = QPushButton(self.scrollAreaWidgetContents)
        self.boxcar.setObjectName(u"boxcar")
        self.boxcar.setMinimumSize(QSize(95, 95))
        self.boxcar.setMaximumSize(QSize(95, 95))
        self.boxcar.setCursor(QCursor(Qt.PointingHandCursor))
        self.boxcar.setStyleSheet(u"")
        icon17 = QIcon()
        icon17.addFile(u"assets/buttons/algo/boxcar_no_bg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boxcar.setIcon(icon17)
        self.boxcar.setIconSize(QSize(80, 80))

        self.horizontalLayout_6.addWidget(self.boxcar)

        self.sheb = QPushButton(self.scrollAreaWidgetContents)
        self.sheb.setObjectName(u"sheb")
        self.sheb.setMinimumSize(QSize(95, 95))
        self.sheb.setMaximumSize(QSize(95, 95))
        self.sheb.setCursor(QCursor(Qt.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u"assets/buttons/algo/chebyshev_plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sheb.setIcon(icon18)
        self.sheb.setIconSize(QSize(80, 80))

        self.horizontalLayout_6.addWidget(self.sheb)

        self.savi = QPushButton(self.scrollAreaWidgetContents)
        self.savi.setObjectName(u"savi")
        self.savi.setMinimumSize(QSize(95, 95))
        self.savi.setMaximumSize(QSize(95, 95))
        self.savi.setCursor(QCursor(Qt.PointingHandCursor))
        icon19 = QIcon()
        icon19.addFile(u"assets/buttons/algo/savgol_plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.savi.setIcon(icon19)
        self.savi.setIconSize(QSize(80, 80))

        self.horizontalLayout_6.addWidget(self.savi)

        self.move = QPushButton(self.scrollAreaWidgetContents)
        self.move.setObjectName(u"move")
        self.move.setMinimumSize(QSize(95, 95))
        self.move.setMaximumSize(QSize(95, 95))
        self.move.setCursor(QCursor(Qt.PointingHandCursor))
        icon20 = QIcon()
        icon20.addFile(u"assets/buttons/algo/moving_avg_plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.move.setIcon(icon20)
        self.move.setIconSize(QSize(80, 80))

        self.horizontalLayout_6.addWidget(self.move)

        self.butter = QPushButton(self.scrollAreaWidgetContents)
        self.butter.setObjectName(u"butter")
        self.butter.setMinimumSize(QSize(95, 95))
        self.butter.setMaximumSize(QSize(95, 95))
        self.butter.setCursor(QCursor(Qt.PointingHandCursor))
        icon21 = QIcon()
        icon21.addFile(u"assets/buttons/algo/butterworth_plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.butter.setIcon(icon21)
        self.butter.setIconSize(QSize(80, 80))

        self.horizontalLayout_6.addWidget(self.butter)

        self.median = QPushButton(self.scrollAreaWidgetContents)
        self.median.setObjectName(u"median")
        self.median.setMinimumSize(QSize(95, 95))
        self.median.setMaximumSize(QSize(95, 95))
        self.median.setCursor(QCursor(Qt.PointingHandCursor))
        icon22 = QIcon()
        icon22.addFile(u"assets/buttons/algo/median_filter_plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.median.setIcon(icon22)
        self.median.setIconSize(QSize(80, 80))

        self.horizontalLayout_6.addWidget(self.median)

        self.gaus = QPushButton(self.scrollAreaWidgetContents)
        self.gaus.setObjectName(u"gaus")
        self.gaus.setMinimumSize(QSize(95, 95))
        self.gaus.setMaximumSize(QSize(95, 95))
        self.gaus.setCursor(QCursor(Qt.PointingHandCursor))
        icon23 = QIcon()
        icon23.addFile(u"assets/buttons/algo/gaussian_filter_plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.gaus.setIcon(icon23)
        self.gaus.setIconSize(QSize(80, 80))

        self.horizontalLayout_6.addWidget(self.gaus)

        self.exponon = QPushButton(self.scrollAreaWidgetContents)
        self.exponon.setObjectName(u"exponon")
        self.exponon.setMinimumSize(QSize(95, 95))
        self.exponon.setMaximumSize(QSize(95, 95))
        self.exponon.setCursor(QCursor(Qt.PointingHandCursor))
        icon24 = QIcon()
        icon24.addFile(u"assets/buttons/algo/exponential_filter_plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exponon.setIcon(icon24)
        self.exponon.setIconSize(QSize(80, 80))

        self.horizontalLayout_6.addWidget(self.exponon)

        self.horizontalSpacer_2 = QSpacerItem(40, 93, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea)

        self.mode_frames.addTab(self.mode_framesPage4, "")

        self.horizontalLayout_3.addWidget(self.mode_frames)


        self.verticalLayout.addWidget(self.frame1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame2 = QVBoxLayout()
        self.frame2.setSpacing(0)
        self.frame2.setObjectName(u"frame2")
        self.tree_header = QWidget(self.Page1)
        self.tree_header.setObjectName(u"tree_header")
        self.tree_header.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.tree_header)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.folder_icon = QLabel(self.tree_header)
        self.folder_icon.setObjectName(u"folder_icon")
        self.folder_icon.setMaximumSize(QSize(30, 30))
        self.folder_icon.setPixmap(QPixmap(u"assets/fold.png"))
        self.folder_icon.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.folder_icon)

        self.project_lab = QLabel(self.tree_header)
        self.project_lab.setObjectName(u"project_lab")
        self.project_lab.setStyleSheet(u"font: 700 10pt \"ProFontWindows Nerd Font Propo\";\n"
"")

        self.horizontalLayout_2.addWidget(self.project_lab)

        self.lagend_select = QPushButton(self.tree_header)
        self.lagend_select.setObjectName(u"lagend_select")
        self.lagend_select.setMinimumSize(QSize(32, 32))
        self.lagend_select.setMaximumSize(QSize(32, 32))
        self.lagend_select.setCursor(QCursor(Qt.PointingHandCursor))
        icon25 = QIcon()
        icon25.addFile(u"assets/legend.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lagend_select.setIcon(icon25)
        self.lagend_select.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.lagend_select)

        self.fullscreen = QPushButton(self.tree_header)
        self.fullscreen.setObjectName(u"fullscreen")
        self.fullscreen.setMinimumSize(QSize(32, 32))
        self.fullscreen.setMaximumSize(QSize(32, 32))
        self.fullscreen.setCursor(QCursor(Qt.PointingHandCursor))
        icon26 = QIcon()
        icon26.addFile(u"assets/fullscreen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fullscreen.setIcon(icon26)
        self.fullscreen.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.fullscreen)

        self.focus = QPushButton(self.tree_header)
        self.focus.setObjectName(u"focus")
        self.focus.setMinimumSize(QSize(32, 32))
        self.focus.setMaximumSize(QSize(32, 32))
        self.focus.setCursor(QCursor(Qt.PointingHandCursor))
        icon27 = QIcon()
        icon27.addFile(u"assets/focus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.focus.setIcon(icon27)
        self.focus.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.focus)


        self.frame2.addWidget(self.tree_header)

        self.treeView = QTreeView(self.Page1)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setMinimumSize(QSize(250, 0))
        self.treeView.setMaximumSize(QSize(250, 16777215))

        self.frame2.addWidget(self.treeView)


        self.horizontalLayout.addLayout(self.frame2)

        self.Tab_graph = QHBoxLayout()
        self.Tab_graph.setObjectName(u"Tab_graph")
        self.graphTab = QTabWidget(self.Page1)
        self.graphTab.setObjectName(u"graphTab")
        self.graphTab.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.graphTab.setTabsClosable(True)
        self.graphTab.setMovable(True)

        self.Tab_graph.addWidget(self.graphTab)


        self.horizontalLayout.addLayout(self.Tab_graph)

        self.graphTypes = QScrollArea(self.Page1)
        self.graphTypes.setObjectName(u"graphTypes")
        self.graphTypes.setMinimumSize(QSize(130, 0))
        self.graphTypes.setMaximumSize(QSize(130, 16777215))
        self.graphTypes.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.graphTypes.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphTypes.setWidgetResizable(True)
        self.typeButtons = QWidget()
        self.typeButtons.setObjectName(u"typeButtons")
        self.typeButtons.setGeometry(QRect(0, 0, 114, 1434))
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
        icon28 = QIcon()
        icon28.addFile(u"assets/buttons/types/plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.plot.setIcon(icon28)
        self.plot.setIconSize(QSize(120, 120))

        self.verticalLayout_3.addWidget(self.plot)

        self.histogram = QPushButton(self.typeButtons)
        self.histogram.setObjectName(u"histogram")
        self.histogram.setMinimumSize(QSize(110, 110))
        self.histogram.setMaximumSize(QSize(110, 110))
        self.histogram.setCursor(QCursor(Qt.PointingHandCursor))
        icon29 = QIcon()
        icon29.addFile(u"assets/buttons/types/Bar-Chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.histogram.setIcon(icon29)
        self.histogram.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.histogram)

        self.piechart = QPushButton(self.typeButtons)
        self.piechart.setObjectName(u"piechart")
        self.piechart.setMinimumSize(QSize(110, 110))
        self.piechart.setMaximumSize(QSize(110, 110))
        self.piechart.setCursor(QCursor(Qt.PointingHandCursor))
        icon30 = QIcon()
        icon30.addFile(u"assets/buttons/types/Pie-Chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.piechart.setIcon(icon30)
        self.piechart.setIconSize(QSize(110, 110))

        self.verticalLayout_3.addWidget(self.piechart)

        self.scatterplot = QPushButton(self.typeButtons)
        self.scatterplot.setObjectName(u"scatterplot")
        self.scatterplot.setMinimumSize(QSize(110, 110))
        self.scatterplot.setMaximumSize(QSize(110, 110))
        self.scatterplot.setCursor(QCursor(Qt.PointingHandCursor))
        icon31 = QIcon()
        icon31.addFile(u"assets/buttons/types/scatter_plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.scatterplot.setIcon(icon31)
        self.scatterplot.setIconSize(QSize(110, 110))

        self.verticalLayout_3.addWidget(self.scatterplot)

        self.fill_between = QPushButton(self.typeButtons)
        self.fill_between.setObjectName(u"fill_between")
        self.fill_between.setMinimumSize(QSize(110, 110))
        self.fill_between.setMaximumSize(QSize(110, 110))
        self.fill_between.setCursor(QCursor(Qt.PointingHandCursor))
        icon32 = QIcon()
        icon32.addFile(u"assets/buttons/types/fill_between.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fill_between.setIcon(icon32)
        self.fill_between.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.fill_between)

        self.stackplot = QPushButton(self.typeButtons)
        self.stackplot.setObjectName(u"stackplot")
        self.stackplot.setMinimumSize(QSize(110, 110))
        self.stackplot.setMaximumSize(QSize(110, 110))
        self.stackplot.setCursor(QCursor(Qt.PointingHandCursor))
        icon33 = QIcon()
        icon33.addFile(u"assets/buttons/types/stackplot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stackplot.setIcon(icon33)
        self.stackplot.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.stackplot)

        self.contour = QPushButton(self.typeButtons)
        self.contour.setObjectName(u"contour")
        self.contour.setMinimumSize(QSize(110, 110))
        self.contour.setMaximumSize(QSize(110, 110))
        self.contour.setCursor(QCursor(Qt.PointingHandCursor))
        icon34 = QIcon()
        icon34.addFile(u"assets/buttons/types/contour.png", QSize(), QIcon.Normal, QIcon.Off)
        self.contour.setIcon(icon34)
        self.contour.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.contour)

        self.contourf = QPushButton(self.typeButtons)
        self.contourf.setObjectName(u"contourf")
        self.contourf.setMinimumSize(QSize(110, 110))
        self.contourf.setMaximumSize(QSize(110, 110))
        self.contourf.setCursor(QCursor(Qt.PointingHandCursor))
        icon35 = QIcon()
        icon35.addFile(u"assets/buttons/types/contourf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.contourf.setIcon(icon35)
        self.contourf.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.contourf)

        self.pushButton_10 = QPushButton(self.typeButtons)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(110, 110))
        self.pushButton_10.setMaximumSize(QSize(110, 110))
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        icon36 = QIcon()
        icon36.addFile(u"assets/buttons/types/imshow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon36)
        self.pushButton_10.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.pushButton_10)

        self.pushButton_9 = QPushButton(self.typeButtons)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(110, 110))
        self.pushButton_9.setMaximumSize(QSize(110, 110))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        icon37 = QIcon()
        icon37.addFile(u"assets/buttons/types/pcolormesh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon37)
        self.pushButton_9.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.typeButtons)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(110, 110))
        self.pushButton_8.setMaximumSize(QSize(110, 110))
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        icon38 = QIcon()
        icon38.addFile(u"assets/buttons/types/surface_3d.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon38)
        self.pushButton_8.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.typeButtons)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(110, 110))
        self.pushButton_7.setMaximumSize(QSize(110, 110))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        icon39 = QIcon()
        icon39.addFile(u"assets/buttons/types/trisurf3d.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon39)
        self.pushButton_7.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_5 = QPushButton(self.typeButtons)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(110, 110))
        self.pushButton_5.setMaximumSize(QSize(110, 110))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        icon40 = QIcon()
        icon40.addFile(u"assets/buttons/types/wire3d.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon40)
        self.pushButton_5.setIconSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.graphTypes.setWidget(self.typeButtons)
        self.plot.raise_()
        self.histogram.raise_()
        self.piechart.raise_()
        self.pushButton_5.raise_()
        self.fill_between.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.contourf.raise_()
        self.stackplot.raise_()
        self.contour.raise_()
        self.scatterplot.raise_()

        self.horizontalLayout.addWidget(self.graphTypes)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.main.addWidget(self.Page1)
        self.can = QWidget()
        self.can.setObjectName(u"can")
        self.verticalLayout_5 = QVBoxLayout(self.can)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.can_btns = QFrame(self.can)
        self.can_btns.setObjectName(u"can_btns")
        self.can_btns.setMinimumSize(QSize(0, 45))
        self.can_btns.setMaximumSize(QSize(16777215, 45))
        self.can_btns.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.can_btns)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.backM = QPushButton(self.can_btns)
        self.backM.setObjectName(u"backM")
        self.backM.setMinimumSize(QSize(40, 40))
        self.backM.setMaximumSize(QSize(40, 40))
        self.backM.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 0.5);\n"
"}")
        icon41 = QIcon()
        icon41.addFile(u"assets/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backM.setIcon(icon41)
        self.backM.setIconSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.backM)

        self.focus_2 = QPushButton(self.can_btns)
        self.focus_2.setObjectName(u"focus_2")
        self.focus_2.setMinimumSize(QSize(40, 40))
        self.focus_2.setMaximumSize(QSize(40, 40))
        self.focus_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.focus_2.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 0.5);\n"
"}")
        self.focus_2.setIcon(icon27)
        self.focus_2.setIconSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.focus_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addWidget(self.can_btns)

        self.canv = QFrame(self.can)
        self.canv.setObjectName(u"canv")
        self.canv.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_5.addWidget(self.canv)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 16)
        self.main.addWidget(self.can)

        self.gridLayout.addWidget(self.main, 0, 0, 1, 1)

        Graphite.setCentralWidget(self.mainLayout)
        self.menubar = QMenuBar(Graphite)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1433, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuNew = QMenu(self.menuFile)
        self.menuNew.setObjectName(u"menuNew")
        self.open_recent_path = QMenu(self.menuFile)
        self.open_recent_path.setObjectName(u"open_recent_path")
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
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.open_file)
        self.menuFile.addAction(self.open_folder)
        self.menuFile.addAction(self.save)
        self.menuFile.addAction(self.save_as)
        self.menuFile.addAction(self.expo)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.open_recent_path.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.exit_app)
        self.menuNew.addAction(self.new_work_sheet)
        self.menuNew.addAction(self.actionfx)
        self.menuEdit.addAction(self.actionpref)
        self.menuEdit.addAction(self.settings)
        self.menuHelp.addAction(self.about)
        self.menuMode.addAction(self.MathMode)
        self.menuMode.addAction(self.menuBiology.menuAction())
        self.menuMode.addAction(self.actiondata_manipulation)
        self.menuBiology.addAction(self.BchimieMode)
        self.menuBiology.addAction(self.actionfilters)

        self.retranslateUi(Graphite)

        self.main.setCurrentIndex(0)
        self.mode_frames.setCurrentIndex(0)
        self.graphTab.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Graphite)
    # setupUi

    def retranslateUi(self, Graphite):
        Graphite.setWindowTitle(QCoreApplication.translate("Graphite", u"Graphite", None))
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
        self.exit_app.setText(QCoreApplication.translate("Graphite", u"Exit", None))
        self.actionpref.setText(QCoreApplication.translate("Graphite", u"pref", None))
        self.settings.setText(QCoreApplication.translate("Graphite", u"Settings", None))
        self.about.setText(QCoreApplication.translate("Graphite", u"About", None))
        self.open_folder.setText(QCoreApplication.translate("Graphite", u"Open folder", None))
#if QT_CONFIG(shortcut)
        self.open_folder.setShortcut(QCoreApplication.translate("Graphite", u"Ctrl+Shift+O", None))
#endif // QT_CONFIG(shortcut)
        self.MathMode.setText(QCoreApplication.translate("Graphite", u"statistical analyse", None))
        self.BchimieMode.setText(QCoreApplication.translate("Graphite", u"fittings", None))
        self.actionWorksheet.setText(QCoreApplication.translate("Graphite", u"Worksheet", None))
        self.actionExel.setText(QCoreApplication.translate("Graphite", u"Exel", None))
        self.actiongraph.setText(QCoreApplication.translate("Graphite", u"graph", None))
        self.actionwoeksheet.setText(QCoreApplication.translate("Graphite", u"woeksheet", None))
        self.expo_as.setText(QCoreApplication.translate("Graphite", u"Export as ...", None))
        self.expo.setText(QCoreApplication.translate("Graphite", u"Export", None))
        self.new_work_sheet.setText(QCoreApplication.translate("Graphite", u"Work sheet", None))
#if QT_CONFIG(shortcut)
        self.new_work_sheet.setShortcut(QCoreApplication.translate("Graphite", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionfilters.setText(QCoreApplication.translate("Graphite", u"filters", None))
        self.actiondata_manipulation.setText(QCoreApplication.translate("Graphite", u"data manipulation", None))
        self.actionfx.setText(QCoreApplication.translate("Graphite", u"fx", None))
        self.actiontest.setText(QCoreApplication.translate("Graphite", u"test", None))
        self.open_btn.setText(QCoreApplication.translate("Graphite", u"Open", None))
        self.save_btn.setText(QCoreApplication.translate("Graphite", u" save", None))
        self.export_btn.setText(QCoreApplication.translate("Graphite", u"export", None))
        self.describe.setText(QCoreApplication.translate("Graphite", u"describe", None))
        self.custom_button.setText(QCoreApplication.translate("Graphite", u"Customize", None))
        self.worksheet.setText(QCoreApplication.translate("Graphite", u"worksheet", None))
#if QT_CONFIG(tooltip)
        self.power.setToolTip(QCoreApplication.translate("Graphite", u"power fit", None))
#endif // QT_CONFIG(tooltip)
        self.power.setText("")
        self.quadraple.setText(QCoreApplication.translate("Graphite", u"quadriple", None))
#if QT_CONFIG(tooltip)
        self.cubic.setToolTip(QCoreApplication.translate("Graphite", u"cubic", None))
#endif // QT_CONFIG(tooltip)
        self.cubic.setText("")
        self.log.setText(QCoreApplication.translate("Graphite", u"logarithm", None))
#if QT_CONFIG(tooltip)
        self.linear.setToolTip(QCoreApplication.translate("Graphite", u"linear", None))
#endif // QT_CONFIG(tooltip)
        self.linear.setText("")
        self.logi.setText(QCoreApplication.translate("Graphite", u"logistic", None))
#if QT_CONFIG(tooltip)
        self.fourier.setToolTip(QCoreApplication.translate("Graphite", u"fourier", None))
#endif // QT_CONFIG(tooltip)
        self.fourier.setText("")
        self.weibull.setText(QCoreApplication.translate("Graphite", u"weibull", None))
#if QT_CONFIG(tooltip)
        self.sine.setToolTip(QCoreApplication.translate("Graphite", u"sine", None))
#endif // QT_CONFIG(tooltip)
        self.sine.setText("")
        self.hill.setText(QCoreApplication.translate("Graphite", u"hill", None))
#if QT_CONFIG(tooltip)
        self.Polynome.setToolTip(QCoreApplication.translate("Graphite", u"polynome", None))
#endif // QT_CONFIG(tooltip)
        self.Polynome.setText("")
        self.expof.setText(QCoreApplication.translate("Graphite", u"expononcial", None))
        self.cosine.setText(QCoreApplication.translate("Graphite", u"cosine", None))
        self.gompertz.setText(QCoreApplication.translate("Graphite", u"gompertz", None))
        self.Gaussian.setText(QCoreApplication.translate("Graphite", u"Gaussian", None))
        self.dexpof.setText(QCoreApplication.translate("Graphite", u"dexpof", None))
        self.lorenzian.setText(QCoreApplication.translate("Graphite", u"lorenzian", None))
        self.texpof.setText(QCoreApplication.translate("Graphite", u"txpof", None))
        self.voigt.setText(QCoreApplication.translate("Graphite", u"voigt", None))
        self.spline.setText(QCoreApplication.translate("Graphite", u"spline", None))
        self.lowess_2.setText(QCoreApplication.translate("Graphite", u"lowess", None))
        self.sav.setText(QCoreApplication.translate("Graphite", u"Savitzky-Golay ", None))
        self.mac.setText(QCoreApplication.translate("Graphite", u"meichaelis-menten", None))
        self.segmoidal.setText(QCoreApplication.translate("Graphite", u"segmoidal", None))
        self.mode_frames.setTabText(self.mode_frames.indexOf(self.mode_framesPage3), QCoreApplication.translate("Graphite", u"Fittings", None))
#if QT_CONFIG(tooltip)
        self.lowpass.setToolTip(QCoreApplication.translate("Graphite", u"Lowpass", None))
#endif // QT_CONFIG(tooltip)
        self.lowpass.setText("")
#if QT_CONFIG(tooltip)
        self.bandpass.setToolTip(QCoreApplication.translate("Graphite", u"Bandpass", None))
#endif // QT_CONFIG(tooltip)
        self.bandpass.setText("")
#if QT_CONFIG(tooltip)
        self.highpass.setToolTip(QCoreApplication.translate("Graphite", u"Highpass", None))
#endif // QT_CONFIG(tooltip)
        self.highpass.setText("")
#if QT_CONFIG(tooltip)
        self.lowess.setToolTip(QCoreApplication.translate("Graphite", u"Lowess filter", None))
#endif // QT_CONFIG(tooltip)
        self.lowess.setText("")
#if QT_CONFIG(tooltip)
        self.boxcar.setToolTip(QCoreApplication.translate("Graphite", u"Boxcar function", None))
#endif // QT_CONFIG(tooltip)
        self.boxcar.setText("")
#if QT_CONFIG(tooltip)
        self.sheb.setToolTip(QCoreApplication.translate("Graphite", u"Chebyshev filter", None))
#endif // QT_CONFIG(tooltip)
        self.sheb.setText("")
#if QT_CONFIG(tooltip)
        self.savi.setToolTip(QCoreApplication.translate("Graphite", u"Savitzky-Golay filter", None))
#endif // QT_CONFIG(tooltip)
        self.savi.setText("")
#if QT_CONFIG(tooltip)
        self.move.setToolTip(QCoreApplication.translate("Graphite", u"Moving Average", None))
#endif // QT_CONFIG(tooltip)
        self.move.setText("")
#if QT_CONFIG(tooltip)
        self.butter.setToolTip(QCoreApplication.translate("Graphite", u"Butterworth filter", None))
#endif // QT_CONFIG(tooltip)
        self.butter.setText("")
#if QT_CONFIG(tooltip)
        self.median.setToolTip(QCoreApplication.translate("Graphite", u"Median", None))
#endif // QT_CONFIG(tooltip)
        self.median.setText("")
#if QT_CONFIG(tooltip)
        self.gaus.setToolTip(QCoreApplication.translate("Graphite", u"Gaussian", None))
#endif // QT_CONFIG(tooltip)
        self.gaus.setText("")
#if QT_CONFIG(tooltip)
        self.exponon.setToolTip(QCoreApplication.translate("Graphite", u"Exponential ", None))
#endif // QT_CONFIG(tooltip)
        self.exponon.setText("")
        self.mode_frames.setTabText(self.mode_frames.indexOf(self.mode_framesPage4), QCoreApplication.translate("Graphite", u"Filters", None))
        self.folder_icon.setText("")
        self.project_lab.setText(QCoreApplication.translate("Graphite", u" Project Tree", None))
        self.lagend_select.setText("")
        self.fullscreen.setText("")
#if QT_CONFIG(shortcut)
        self.fullscreen.setShortcut(QCoreApplication.translate("Graphite", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.focus.setText("")
#if QT_CONFIG(shortcut)
        self.focus.setShortcut(QCoreApplication.translate("Graphite", u"F", None))
#endif // QT_CONFIG(shortcut)
        self.plot.setText("")
        self.histogram.setText("")
        self.piechart.setText("")
        self.scatterplot.setText("")
        self.fill_between.setText("")
        self.stackplot.setText("")
        self.contour.setText("")
        self.contourf.setText("")
        self.pushButton_10.setText("")
        self.pushButton_9.setText("")
        self.pushButton_8.setText("")
        self.pushButton_7.setText("")
        self.pushButton_5.setText("")
        self.backM.setText("")
#if QT_CONFIG(shortcut)
        self.backM.setShortcut(QCoreApplication.translate("Graphite", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.focus_2.setText("")
#if QT_CONFIG(shortcut)
        self.focus_2.setShortcut(QCoreApplication.translate("Graphite", u"F", None))
#endif // QT_CONFIG(shortcut)
        self.menuFile.setTitle(QCoreApplication.translate("Graphite", u"File", None))
        self.menuNew.setTitle(QCoreApplication.translate("Graphite", u"New", None))
        self.open_recent_path.setTitle(QCoreApplication.translate("Graphite", u"Open recent", None))
        self.menuEdit.setTitle(QCoreApplication.translate("Graphite", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Graphite", u"Help", None))
        self.menuMode.setTitle(QCoreApplication.translate("Graphite", u"analyse", None))
        self.menuBiology.setTitle(QCoreApplication.translate("Graphite", u"plotting analyse", None))
    # retranslateUi

