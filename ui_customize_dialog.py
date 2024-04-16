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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

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
        Dialog.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.title_lab = QLabel(Dialog)
        self.title_lab.setObjectName(u"title_lab")

        self.horizontalLayout_2.addWidget(self.title_lab)

        self.graph_title = QLineEdit(Dialog)
        self.graph_title.setObjectName(u"graph_title")

        self.horizontalLayout_2.addWidget(self.graph_title)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 9)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.xLab = QLabel(Dialog)
        self.xLab.setObjectName(u"xLab")

        self.horizontalLayout_3.addWidget(self.xLab)

        self.xLabel = QLineEdit(Dialog)
        self.xLabel.setObjectName(u"xLabel")

        self.horizontalLayout_3.addWidget(self.xLabel)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 9)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.yLab = QLabel(Dialog)
        self.yLab.setObjectName(u"yLab")

        self.horizontalLayout_4.addWidget(self.yLab)

        self.yLabel = QLineEdit(Dialog)
        self.yLabel.setObjectName(u"yLabel")

        self.horizontalLayout_4.addWidget(self.yLabel)

        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 9)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lagend_lab = QLabel(Dialog)
        self.lagend_lab.setObjectName(u"lagend_lab")

        self.horizontalLayout_5.addWidget(self.lagend_lab)

        self.lagend = QCheckBox(Dialog)
        self.lagend.setObjectName(u"lagend")

        self.horizontalLayout_5.addWidget(self.lagend)

        self.marker_lab = QLabel(Dialog)
        self.marker_lab.setObjectName(u"marker_lab")
        self.marker_lab.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.marker_lab)

        self.marker = QComboBox(Dialog)
        self.marker.addItem("")
        icon1 = QIcon()
        icon1.addFile(u"assets/markers/m00.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u"assets/markers/m01.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u"assets/markers/m02.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon3, "")
        icon4 = QIcon()
        icon4.addFile(u"assets/markers/m04.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon4, "")
        icon5 = QIcon()
        icon5.addFile(u"assets/markers/m03.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u"assets/markers/m06.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon6, "")
        icon7 = QIcon()
        icon7.addFile(u"assets/markers/m05.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon7, "")
        icon8 = QIcon()
        icon8.addFile(u"assets/markers/m08.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon8, "")
        icon9 = QIcon()
        icon9.addFile(u"assets/markers/m07.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon9, "")
        icon10 = QIcon()
        icon10.addFile(u"assets/markers/m10.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon10, "")
        icon11 = QIcon()
        icon11.addFile(u"assets/markers/m09.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon11, "")
        icon12 = QIcon()
        icon12.addFile(u"assets/markers/m11.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon12, "")
        icon13 = QIcon()
        icon13.addFile(u"assets/markers/m12.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon13, "")
        icon14 = QIcon()
        icon14.addFile(u"assets/markers/m13.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon14, "")
        icon15 = QIcon()
        icon15.addFile(u"assets/markers/m17.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon15, "")
        icon16 = QIcon()
        icon16.addFile(u"assets/markers/m23.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon16, "")
        icon17 = QIcon()
        icon17.addFile(u"assets/markers/m18.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon17, "")
        icon18 = QIcon()
        icon18.addFile(u"assets/markers/m24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon18, "")
        icon19 = QIcon()
        icon19.addFile(u"assets/markers/m14.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon19, "")
        icon20 = QIcon()
        icon20.addFile(u"assets/markers/m15.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon20, "")
        icon21 = QIcon()
        icon21.addFile(u"assets/markers/m19.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon21, "")
        icon22 = QIcon()
        icon22.addFile(u"assets/markers/m20.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon22, "")
        icon23 = QIcon()
        icon23.addFile(u"assets/markers/m21.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon23, "")
        icon24 = QIcon()
        icon24.addFile(u"assets/markers/m22.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon24, "")
        icon25 = QIcon()
        icon25.addFile(u"assets/markers/m27.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon25, "")
        icon26 = QIcon()
        icon26.addFile(u"assets/markers/m28.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon26, "")
        icon27 = QIcon()
        icon27.addFile(u"assets/markers/m26.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon27, "")
        icon28 = QIcon()
        icon28.addFile(u"assets/markers/m25.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon28, "")
        icon29 = QIcon()
        icon29.addFile(u"assets/markers/m31.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon29, "")
        icon30 = QIcon()
        icon30.addFile(u"assets/markers/m32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon30, "")
        icon31 = QIcon()
        icon31.addFile(u"assets/markers/m30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon31, "")
        icon32 = QIcon()
        icon32.addFile(u"assets/markers/m29.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marker.addItem(icon32, "")
        self.marker.setObjectName(u"marker")

        self.horizontalLayout_5.addWidget(self.marker)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.real_lab = QLabel(Dialog)
        self.real_lab.setObjectName(u"real_lab")
        self.real_lab.setMinimumSize(QSize(80, 0))
        self.real_lab.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_6.addWidget(self.real_lab)

        self.real = QCheckBox(Dialog)
        self.real.setObjectName(u"real")

        self.horizontalLayout_6.addWidget(self.real)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.cancel_btn = QPushButton(Dialog)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout_7.addWidget(self.cancel_btn)

        self.apply_btn = QPushButton(Dialog)
        self.apply_btn.setObjectName(u"apply_btn")

        self.horizontalLayout_7.addWidget(self.apply_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Graph settings", None))
        self.title_lab.setText(QCoreApplication.translate("Dialog", u"Title :", None))
        self.xLab.setText(QCoreApplication.translate("Dialog", u"X Label :", None))
        self.yLab.setText(QCoreApplication.translate("Dialog", u"Y Label :", None))
        self.lagend_lab.setText(QCoreApplication.translate("Dialog", u"Lagend :", None))
        self.lagend.setText("")
        self.marker_lab.setText(QCoreApplication.translate("Dialog", u"marker: ", None))
        self.marker.setItemText(0, QCoreApplication.translate("Dialog", u"None", None))
        self.marker.setItemText(1, QCoreApplication.translate("Dialog", u"point", None))
        self.marker.setItemText(2, QCoreApplication.translate("Dialog", u"pixel", None))
        self.marker.setItemText(3, QCoreApplication.translate("Dialog", u"circle", None))
        self.marker.setItemText(4, QCoreApplication.translate("Dialog", u"triangle up", None))
        self.marker.setItemText(5, QCoreApplication.translate("Dialog", u"triangle down", None))
        self.marker.setItemText(6, QCoreApplication.translate("Dialog", u"triangle right", None))
        self.marker.setItemText(7, QCoreApplication.translate("Dialog", u"triangle left", None))
        self.marker.setItemText(8, QCoreApplication.translate("Dialog", u"tri up", None))
        self.marker.setItemText(9, QCoreApplication.translate("Dialog", u"tri down", None))
        self.marker.setItemText(10, QCoreApplication.translate("Dialog", u"tri right", None))
        self.marker.setItemText(11, QCoreApplication.translate("Dialog", u"tri left", None))
        self.marker.setItemText(12, QCoreApplication.translate("Dialog", u"octagon", None))
        self.marker.setItemText(13, QCoreApplication.translate("Dialog", u"square", None))
        self.marker.setItemText(14, QCoreApplication.translate("Dialog", u"pentagon", None))
        self.marker.setItemText(15, QCoreApplication.translate("Dialog", u"plus", None))
        self.marker.setItemText(16, QCoreApplication.translate("Dialog", u"plus (filled)", None))
        self.marker.setItemText(17, QCoreApplication.translate("Dialog", u"X", None))
        self.marker.setItemText(18, QCoreApplication.translate("Dialog", u"X (filled)", None))
        self.marker.setItemText(19, QCoreApplication.translate("Dialog", u"star", None))
        self.marker.setItemText(20, QCoreApplication.translate("Dialog", u"hexagon", None))
        self.marker.setItemText(21, QCoreApplication.translate("Dialog", u"diamond", None))
        self.marker.setItemText(22, QCoreApplication.translate("Dialog", u"thin diamond", None))
        self.marker.setItemText(23, QCoreApplication.translate("Dialog", u"vertical line", None))
        self.marker.setItemText(24, QCoreApplication.translate("Dialog", u"horizantol line", None))
        self.marker.setItemText(25, QCoreApplication.translate("Dialog", u"tick up", None))
        self.marker.setItemText(26, QCoreApplication.translate("Dialog", u"tick down", None))
        self.marker.setItemText(27, QCoreApplication.translate("Dialog", u"tick right", None))
        self.marker.setItemText(28, QCoreApplication.translate("Dialog", u"tick left", None))
        self.marker.setItemText(29, QCoreApplication.translate("Dialog", u"caret up", None))
        self.marker.setItemText(30, QCoreApplication.translate("Dialog", u"caret down", None))
        self.marker.setItemText(31, QCoreApplication.translate("Dialog", u"caret right", None))
        self.marker.setItemText(32, QCoreApplication.translate("Dialog", u"caret left", None))

        self.real_lab.setText(QCoreApplication.translate("Dialog", u"real time :", None))
        self.real.setText("")
        self.cancel_btn.setText(QCoreApplication.translate("Dialog", u"cancel", None))
        self.apply_btn.setText(QCoreApplication.translate("Dialog", u"apply", None))
    # retranslateUi

