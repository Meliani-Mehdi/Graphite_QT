# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'describe.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 0, 2, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.zip_name = QLineEdit(Dialog)
        self.zip_name.setObjectName(u"zip_name")

        self.horizontalLayout_3.addWidget(self.zip_name)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.localpath = QLineEdit(Dialog)
        self.localpath.setObjectName(u"localpath")
        self.localpath.setReadOnly(True)

        self.horizontalLayout.addWidget(self.localpath)

        self.local = QPushButton(Dialog)
        self.local.setObjectName(u"local")
        self.local.setMinimumSize(QSize(45, 45))
        self.local.setMaximumSize(QSize(45, 45))
        icon = QIcon()
        icon.addFile(u"assets/fold.png", QSize(), QIcon.Normal, QIcon.Off)
        self.local.setIcon(icon)
        self.local.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.local)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalFrame = QFrame(Dialog)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.cancel = QPushButton(self.horizontalFrame)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout_2.addWidget(self.cancel)

        self.save = QPushButton(self.horizontalFrame)
        self.save.setObjectName(u"save")

        self.horizontalLayout_2.addWidget(self.save)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2.setStretch(0, 1)

        self.verticalLayout.addWidget(self.horizontalFrame)

        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"zip name: ", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Output location:", None))
        self.localpath.setText("")
        self.local.setText("")
        self.cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.save.setText(QCoreApplication.translate("Dialog", u"Save", None))
    # retranslateUi

