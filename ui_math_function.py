# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'math_function.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDialog, QDoubleSpinBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(320, 160)
        Dialog.setMaximumSize(QSize(320, 160))
        Dialog.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.func_lab = QLabel(Dialog)
        self.func_lab.setObjectName(u"func_lab")
        self.func_lab.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout.addWidget(self.func_lab)

        self.function = QLineEdit(Dialog)
        self.function.setObjectName(u"function")

        self.verticalLayout.addWidget(self.function)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.range_lab = QLabel(Dialog)
        self.range_lab.setObjectName(u"range_lab")

        self.horizontalLayout.addWidget(self.range_lab)

        self.starter = QSpinBox(Dialog)
        self.starter.setObjectName(u"starter")
        self.starter.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.starter.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.starter.setMinimum(-999999999)
        self.starter.setMaximum(999999999)
        self.starter.setValue(-100)

        self.horizontalLayout.addWidget(self.starter)

        self.end = QSpinBox(Dialog)
        self.end.setObjectName(u"end")
        self.end.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.end.setMinimum(-999999999)
        self.end.setMaximum(999999999)
        self.end.setValue(100)

        self.horizontalLayout.addWidget(self.end)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.step_lab = QLabel(Dialog)
        self.step_lab.setObjectName(u"step_lab")

        self.horizontalLayout_3.addWidget(self.step_lab)

        self.step = QDoubleSpinBox(Dialog)
        self.step.setObjectName(u"step")
        self.step.setDecimals(6)
        self.step.setMinimum(0.000001000000000)
        self.step.setMaximum(9999999.000000000000000)
        self.step.setValue(1.000000000000000)

        self.horizontalLayout_3.addWidget(self.step)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.cancel = QPushButton(Dialog)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout_2.addWidget(self.cancel)

        self.plot_btn = QPushButton(Dialog)
        self.plot_btn.setObjectName(u"plot_btn")

        self.horizontalLayout_2.addWidget(self.plot_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(4, 1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.func_lab.setText(QCoreApplication.translate("Dialog", u"function :", None))
        self.range_lab.setText(QCoreApplication.translate("Dialog", u"range :", None))
        self.step_lab.setText(QCoreApplication.translate("Dialog", u"step :", None))
        self.cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.plot_btn.setText(QCoreApplication.translate("Dialog", u"Plot", None))
    # retranslateUi

