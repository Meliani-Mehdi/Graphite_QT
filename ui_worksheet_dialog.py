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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDialog, QHeaderView,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        if not Dialog2.objectName():
            Dialog2.setObjectName(u"Dialog2")
        Dialog2.resize(347, 530)
        Dialog2.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(Dialog2)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QSize(331, 16777215))
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setRowCount(10)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(159)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tableWidget)

        self.plotwork = QPushButton(Dialog2)
        self.plotwork.setObjectName(u"plotwork")

        self.verticalLayout.addWidget(self.plotwork)

        self.remcol = QPushButton(Dialog2)
        self.remcol.setObjectName(u"remcol")

        self.verticalLayout.addWidget(self.remcol)

        self.addwork_2 = QPushButton(Dialog2)
        self.addwork_2.setObjectName(u"addwork_2")

        self.verticalLayout.addWidget(self.addwork_2)

        self.remrow = QPushButton(Dialog2)
        self.remrow.setObjectName(u"remrow")

        self.verticalLayout.addWidget(self.remrow)

        self.addwork = QPushButton(Dialog2)
        self.addwork.setObjectName(u"addwork")

        self.verticalLayout.addWidget(self.addwork)


        self.retranslateUi(Dialog2)

        QMetaObject.connectSlotsByName(Dialog2)
    # setupUi

    def retranslateUi(self, Dialog2):
        Dialog2.setWindowTitle(QCoreApplication.translate("Dialog2", u"Dialog", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog2", u"X", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog2", u"Y (graph 1)", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.plotwork.setText(QCoreApplication.translate("Dialog2", u"plot", None))
        self.remcol.setText(QCoreApplication.translate("Dialog2", u"remove column", None))
        self.addwork_2.setText(QCoreApplication.translate("Dialog2", u"add column", None))
        self.remrow.setText(QCoreApplication.translate("Dialog2", u"remove row", None))
        self.addwork.setText(QCoreApplication.translate("Dialog2", u"add row", None))
    # retranslateUi

