# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'export.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(300, 400)
        Dialog.setStyleSheet(u"QFrame { \n"
"	border: none;\n"
"}\n"
"QLabel {\n"
"    color: black;\n"
"}")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 6, 0, 1, 3)

        self.horizontalFrame = QFrame(Dialog)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(0, 100))
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancel = QPushButton(self.horizontalFrame)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout.addWidget(self.cancel)

        self.expo = QPushButton(self.horizontalFrame)
        self.expo.setObjectName(u"expo")

        self.horizontalLayout.addWidget(self.expo)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 1)

        self.gridLayout.addWidget(self.horizontalFrame, 13, 0, 1, 3)

        self.format = QComboBox(Dialog)
        self.format.addItem("")
        self.format.addItem("")
        self.format.addItem("")
        self.format.addItem("")
        self.format.addItem("")
        self.format.addItem("")
        self.format.addItem("")
        self.format.addItem("")
        self.format.addItem("")
        self.format.addItem("")
        self.format.setObjectName(u"format")

        self.gridLayout.addWidget(self.format, 2, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 0, 1, 3)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 11, 0, 1, 3)

        self.dpi = QSpinBox(Dialog)
        self.dpi.setObjectName(u"dpi")
        self.dpi.setMinimum(1)
        self.dpi.setMaximum(600)
        self.dpi.setValue(300)

        self.gridLayout.addWidget(self.dpi, 5, 0, 1, 1)

        self.filename = QLineEdit(Dialog)
        self.filename.setObjectName(u"filename")

        self.gridLayout.addWidget(self.filename, 2, 0, 1, 2)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 3, 0, 1, 3)

        self.horizontalFrame1 = QFrame(Dialog)
        self.horizontalFrame1.setObjectName(u"horizontalFrame1")
        self.horizontalFrame1.setMinimumSize(QSize(0, 50))
        self.horizontalFrame1.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.location = QLineEdit(self.horizontalFrame1)
        self.location.setObjectName(u"location")
        self.location.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.location)

        self.file = QPushButton(self.horizontalFrame1)
        self.file.setObjectName(u"file")
        self.file.setMinimumSize(QSize(45, 45))
        self.file.setMaximumSize(QSize(45, 45))
        icon = QIcon()
        icon.addFile(u"assets/folders.png", QSize(), QIcon.Normal, QIcon.Off)
        self.file.setIcon(icon)
        self.file.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.file)


        self.gridLayout.addWidget(self.horizontalFrame1, 12, 0, 1, 3)

        self.padding = QSpinBox(Dialog)
        self.padding.setObjectName(u"padding")
        self.padding.setMaximum(500)

        self.gridLayout.addWidget(self.padding, 5, 1, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)

        self.transparent = QCheckBox(Dialog)
        self.transparent.setObjectName(u"transparent")
        self.transparent.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.transparent, 8, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(11, 3)

        self.retranslateUi(Dialog)

        self.format.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Format:", None))
        self.cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.expo.setText(QCoreApplication.translate("Dialog", u"Export", None))
        self.format.setItemText(0, QCoreApplication.translate("Dialog", u"eps", None))
        self.format.setItemText(1, QCoreApplication.translate("Dialog", u"jpg", None))
        self.format.setItemText(2, QCoreApplication.translate("Dialog", u"pdf", None))
        self.format.setItemText(3, QCoreApplication.translate("Dialog", u"pgf", None))
        self.format.setItemText(4, QCoreApplication.translate("Dialog", u"png", None))
        self.format.setItemText(5, QCoreApplication.translate("Dialog", u"ps", None))
        self.format.setItemText(6, QCoreApplication.translate("Dialog", u"raw", None))
        self.format.setItemText(7, QCoreApplication.translate("Dialog", u"svg", None))
        self.format.setItemText(8, QCoreApplication.translate("Dialog", u"tif", None))
        self.format.setItemText(9, QCoreApplication.translate("Dialog", u"webp", None))

        self.label_3.setText(QCoreApplication.translate("Dialog", u"dpi:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"File name:", None))
        self.location.setText("")
        self.file.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"padding:", None))
        self.transparent.setText(QCoreApplication.translate("Dialog", u"transparent", None))
    # retranslateUi

