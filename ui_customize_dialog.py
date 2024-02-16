# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customize_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 525)
        Dialog.setMinimumSize(QSize(600, 525))
        Dialog.setMaximumSize(QSize(600, 525))
        icon = QIcon()
        icon.addFile(u"assets/Graphite.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.yLab = QLabel(Dialog)
        self.yLab.setObjectName(u"yLab")

        self.gridLayout.addWidget(self.yLab, 2, 0, 1, 1)

        self.lagend_lab = QLabel(Dialog)
        self.lagend_lab.setObjectName(u"lagend_lab")

        self.gridLayout.addWidget(self.lagend_lab, 3, 0, 1, 1)

        self.xLab = QLabel(Dialog)
        self.xLab.setObjectName(u"xLab")

        self.gridLayout.addWidget(self.xLab, 1, 0, 1, 1)

        self.lagend = QCheckBox(Dialog)
        self.lagend.setObjectName(u"lagend")

        self.gridLayout.addWidget(self.lagend, 3, 2, 1, 1)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(580, 100))
        self.frame.setMaximumSize(QSize(580, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(340, 40, 241, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.gridLayout.addWidget(self.frame, 4, 0, 1, 4)

        self.title_lab = QLabel(Dialog)
        self.title_lab.setObjectName(u"title_lab")

        self.gridLayout.addWidget(self.title_lab, 0, 0, 1, 1)

        self.hs = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.hs, 3, 3, 1, 1)

        self.yLabel = QPlainTextEdit(Dialog)
        self.yLabel.setObjectName(u"yLabel")
        self.yLabel.setMinimumSize(QSize(0, 50))
        self.yLabel.setMaximumSize(QSize(16777215, 50))

        self.gridLayout.addWidget(self.yLabel, 2, 1, 1, 3)

        self.xLabel = QPlainTextEdit(Dialog)
        self.xLabel.setObjectName(u"xLabel")
        self.xLabel.setMinimumSize(QSize(0, 50))
        self.xLabel.setMaximumSize(QSize(16777215, 50))

        self.gridLayout.addWidget(self.xLabel, 1, 1, 1, 3)

        self.graph_title = QPlainTextEdit(Dialog)
        self.graph_title.setObjectName(u"graph_title")
        self.graph_title.setMinimumSize(QSize(0, 50))
        self.graph_title.setMaximumSize(QSize(16777215, 50))

        self.gridLayout.addWidget(self.graph_title, 0, 1, 1, 3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Graph settings", None))
        self.yLab.setText(QCoreApplication.translate("Dialog", u"Y Label :", None))
        self.lagend_lab.setText(QCoreApplication.translate("Dialog", u"Lagend :", None))
        self.xLab.setText(QCoreApplication.translate("Dialog", u"X Label :", None))
        self.lagend.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"apply", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"cancel", None))
        self.title_lab.setText(QCoreApplication.translate("Dialog", u"Title :", None))
    # retranslateUi

