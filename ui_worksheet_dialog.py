# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'worksheet_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        if not Dialog2.objectName():
            Dialog2.setObjectName(u"Dialog2")
        Dialog2.resize(400, 480)
        self.label = QLabel(Dialog2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 141, 21))
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Dialog2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 10, 141, 21))
        self.label_2.setLineWidth(1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.addwork = QPushButton(Dialog2)
        self.addwork.setObjectName(u"addwork")
        self.addwork.setGeometry(QRect(40, 420, 101, 41))
        self.plotwork = QPushButton(Dialog2)
        self.plotwork.setObjectName(u"plotwork")
        self.plotwork.setGeometry(QRect(190, 420, 101, 41))
        self.verticalLayoutWidget = QWidget(Dialog2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 60, 311, 311))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.retranslateUi(Dialog2)

        QMetaObject.connectSlotsByName(Dialog2)
    # setupUi

    def retranslateUi(self, Dialog2):
        Dialog2.setWindowTitle(QCoreApplication.translate("Dialog2", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog2", u"X", None))
        self.label_2.setText(QCoreApplication.translate("Dialog2", u"Y", None))
        self.addwork.setText(QCoreApplication.translate("Dialog2", u"add", None))
        self.plotwork.setText(QCoreApplication.translate("Dialog2", u"plot", None))
    # retranslateUi

