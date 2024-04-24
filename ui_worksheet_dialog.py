# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'worksheet_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        if not Dialog2.objectName():
            Dialog2.setObjectName(u"Dialog2")
        Dialog2.resize(758, 672)
        Dialog2.setMinimumSize(QSize(400, 500))
        Dialog2.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(Dialog2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tableWidget)

        self.plotwork = QPushButton(Dialog2)
        self.plotwork.setObjectName(u"plotwork")

        self.verticalLayout.addWidget(self.plotwork)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addwork_2 = QPushButton(Dialog2)
        self.addwork_2.setObjectName(u"addwork_2")

        self.horizontalLayout.addWidget(self.addwork_2)

        self.remcol = QPushButton(Dialog2)
        self.remcol.setObjectName(u"remcol")

        self.horizontalLayout.addWidget(self.remcol)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.addwork = QPushButton(Dialog2)
        self.addwork.setObjectName(u"addwork")

        self.horizontalLayout_3.addWidget(self.addwork)

        self.remrow = QPushButton(Dialog2)
        self.remrow.setObjectName(u"remrow")

        self.horizontalLayout_3.addWidget(self.remrow)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Dialog2)

        QMetaObject.connectSlotsByName(Dialog2)
    # setupUi

    def retranslateUi(self, Dialog2):
        Dialog2.setWindowTitle(QCoreApplication.translate("Dialog2", u"Dialog", None))
        self.plotwork.setText(QCoreApplication.translate("Dialog2", u"plot", None))
        self.addwork_2.setText(QCoreApplication.translate("Dialog2", u"add column", None))
        self.remcol.setText(QCoreApplication.translate("Dialog2", u"remove column", None))
        self.addwork.setText(QCoreApplication.translate("Dialog2", u"add row", None))
        self.remrow.setText(QCoreApplication.translate("Dialog2", u"remove row", None))
    # retranslateUi

