# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customize_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(350, 400)
        Dialog.setMinimumSize(QSize(350, 400))
        Dialog.setMaximumSize(QSize(350, 400))
        icon = QIcon()
        icon.addFile(u"assets/Graphite.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.yLab = QLabel(Dialog)
        self.yLab.setObjectName(u"yLab")

        self.gridLayout.addWidget(self.yLab, 2, 0, 1, 1)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 50))
        self.frame.setMaximumSize(QSize(280, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancel_btn = QPushButton(self.frame)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout.addWidget(self.cancel_btn)

        self.apply_btn = QPushButton(self.frame)
        self.apply_btn.setObjectName(u"apply_btn")

        self.horizontalLayout.addWidget(self.apply_btn)


        self.gridLayout.addWidget(self.frame, 6, 3, 1, 1)

        self.title_lab = QLabel(Dialog)
        self.title_lab.setObjectName(u"title_lab")

        self.gridLayout.addWidget(self.title_lab, 0, 0, 1, 1)

        self.lagend_lab = QLabel(Dialog)
        self.lagend_lab.setObjectName(u"lagend_lab")

        self.gridLayout.addWidget(self.lagend_lab, 3, 0, 1, 1)

        self.graph_title = QPlainTextEdit(Dialog)
        self.graph_title.setObjectName(u"graph_title")
        self.graph_title.setMinimumSize(QSize(0, 33))
        self.graph_title.setMaximumSize(QSize(16777215, 33))
        self.graph_title.setAcceptDrops(True)
        self.graph_title.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graph_title.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graph_title.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.gridLayout.addWidget(self.graph_title, 0, 1, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 6, 0, 1, 1)

        self.xLabel = QPlainTextEdit(Dialog)
        self.xLabel.setObjectName(u"xLabel")
        self.xLabel.setMinimumSize(QSize(0, 33))
        self.xLabel.setMaximumSize(QSize(16777215, 33))
        self.xLabel.setAcceptDrops(True)
        self.xLabel.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.xLabel.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.xLabel.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.gridLayout.addWidget(self.xLabel, 1, 1, 1, 3)

        self.yLabel = QPlainTextEdit(Dialog)
        self.yLabel.setObjectName(u"yLabel")
        self.yLabel.setMinimumSize(QSize(0, 33))
        self.yLabel.setMaximumSize(QSize(16777215, 33))
        self.yLabel.setAcceptDrops(True)
        self.yLabel.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.yLabel.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.yLabel.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.gridLayout.addWidget(self.yLabel, 2, 1, 1, 3)

        self.xLab = QLabel(Dialog)
        self.xLab.setObjectName(u"xLab")

        self.gridLayout.addWidget(self.xLab, 1, 0, 1, 1)

        self.lagend = QCheckBox(Dialog)
        self.lagend.setObjectName(u"lagend")

        self.gridLayout.addWidget(self.lagend, 3, 1, 1, 1)

        self.real_lab = QLabel(Dialog)
        self.real_lab.setObjectName(u"real_lab")
        self.real_lab.setMinimumSize(QSize(80, 0))
        self.real_lab.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.real_lab, 4, 0, 1, 1)

        self.real = QCheckBox(Dialog)
        self.real.setObjectName(u"real")

        self.gridLayout.addWidget(self.real, 4, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Graph settings", None))
        self.yLab.setText(QCoreApplication.translate("Dialog", u"Y Label :", None))
        self.cancel_btn.setText(QCoreApplication.translate("Dialog", u"cancel", None))
        self.apply_btn.setText(QCoreApplication.translate("Dialog", u"apply", None))
        self.title_lab.setText(QCoreApplication.translate("Dialog", u"Title :", None))
        self.lagend_lab.setText(QCoreApplication.translate("Dialog", u"Lagend :", None))
        self.xLab.setText(QCoreApplication.translate("Dialog", u"X Label :", None))
        self.lagend.setText("")
        self.real_lab.setText(QCoreApplication.translate("Dialog", u"real time :", None))
        self.real.setText("")
    # retranslateUi

