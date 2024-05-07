# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interpolation.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(720, 480)
        Dialog.setMinimumSize(QSize(720, 480))
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.image = QVBoxLayout()
        self.image.setObjectName(u"image")

        self.verticalLayout_2.addLayout(self.image)

        self.horizontalFrame = QFrame(Dialog)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(0, 60))
        self.horizontalFrame.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.spacer)

        self.cancel = QPushButton(self.horizontalFrame)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout.addWidget(self.cancel)

        self.plot = QPushButton(self.horizontalFrame)
        self.plot.setObjectName(u"plot")

        self.horizontalLayout.addWidget(self.plot)


        self.verticalLayout_2.addWidget(self.horizontalFrame)

        self.verticalLayout_2.setStretch(0, 9)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.plot.setText(QCoreApplication.translate("Dialog", u"Plot", None))
    # retranslateUi

