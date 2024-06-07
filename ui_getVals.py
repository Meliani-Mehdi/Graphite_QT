# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'getVals.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(373, 204)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.xStart = QLineEdit(Dialog)
        self.xStart.setObjectName(u"xStart")

        self.horizontalLayout_2.addWidget(self.xStart)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.xEnd = QLineEdit(Dialog)
        self.xEnd.setObjectName(u"xEnd")

        self.horizontalLayout_2.addWidget(self.xEnd)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.yStart = QLineEdit(Dialog)
        self.yStart.setObjectName(u"yStart")

        self.horizontalLayout_4.addWidget(self.yStart)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.yEnd = QLineEdit(Dialog)
        self.yEnd.setObjectName(u"yEnd")

        self.horizontalLayout_4.addWidget(self.yEnd)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancel = QPushButton(Dialog)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout.addWidget(self.cancel)

        self.skip = QPushButton(Dialog)
        self.skip.setObjectName(u"skip")

        self.horizontalLayout.addWidget(self.skip)

        self.apply = QPushButton(Dialog)
        self.apply.setObjectName(u"apply")

        self.horizontalLayout.addWidget(self.apply)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Give the X and Y Range Values", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"X Start :", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"X End :", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Y Start :", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Y End :", None))
        self.cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.skip.setText(QCoreApplication.translate("Dialog", u"Skip", None))
        self.apply.setText(QCoreApplication.translate("Dialog", u"Apply", None))
    # retranslateUi

