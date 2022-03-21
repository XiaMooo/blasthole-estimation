# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1728, 900)
        MainWindow.setMinimumSize(QSize(1500, 900))
        self.actionSubmenu_2 = QAction(MainWindow)
        self.actionSubmenu_2.setObjectName(u"actionSubmenu_2")
        self.actionSubmenu_2.setCheckable(True)
        self.actionSubmenu_3 = QAction(MainWindow)
        self.actionSubmenu_3.setObjectName(u"actionSubmenu_3")
        self.actionSUBSUB = QAction(MainWindow)
        self.actionSUBSUB.setObjectName(u"actionSUBSUB")
        self.actionSUBSUB_2 = QAction(MainWindow)
        self.actionSUBSUB_2.setObjectName(u"actionSUBSUB_2")
        self.actionSUBSUB_3 = QAction(MainWindow)
        self.actionSUBSUB_3.setObjectName(u"actionSUBSUB_3")
        self.actiondissabled = QAction(MainWindow)
        self.actiondissabled.setObjectName(u"actiondissabled")
        self.actiondissabled.setEnabled(False)
        self.actionSubmenu = QAction(MainWindow)
        self.actionSubmenu.setObjectName(u"actionSubmenu")
        self.actionSubmenu.setCheckable(True)
        self.actionSubmenu.setChecked(True)
        self.actionSubmenu_4 = QAction(MainWindow)
        self.actionSubmenu_4.setObjectName(u"actionSubmenu_4")
        self.actionSubmenu_4.setCheckable(True)
        self.actionSubmenu_5 = QAction(MainWindow)
        self.actionSubmenu_5.setObjectName(u"actionSubmenu_5")
        self.actionSubmenu_5.setCheckable(True)
        self.actionSubmenu_5.setEnabled(False)
        self.actionToolbar = QAction(MainWindow)
        self.actionToolbar.setObjectName(u"actionToolbar")
        self.actionSelected = QAction(MainWindow)
        self.actionSelected.setObjectName(u"actionSelected")
        self.actionSelected.setCheckable(True)
        self.actionSelected.setChecked(True)
        self.actionaction = QAction(MainWindow)
        self.actionaction.setObjectName(u"actionaction")
        self.actionaction2 = QAction(MainWindow)
        self.actionaction2.setObjectName(u"actionaction2")
        self.actionaction3 = QAction(MainWindow)
        self.actionaction3.setObjectName(u"actionaction3")
        self.action111 = QAction(MainWindow)
        self.action111.setObjectName(u"action111")
        self.action111.setCheckable(True)
        self.action222 = QAction(MainWindow)
        self.action222.setObjectName(u"action222")
        self.action222.setCheckable(True)
        self.action333 = QAction(MainWindow)
        self.action333.setObjectName(u"action333")
        self.action333.setCheckable(True)
        self.actionsubmenu = QAction(MainWindow)
        self.actionsubmenu.setObjectName(u"actionsubmenu")
        icon = QIcon()
        iconThemeName = u"document-new"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"C:/Users/qinyf/.designer/backup", QSize(), QIcon.Normal, QIcon.Off)
        
        self.actionsubmenu.setIcon(icon)
        self.actionsubmenu_2 = QAction(MainWindow)
        self.actionsubmenu_2.setObjectName(u"actionsubmenu_2")
        icon1 = QIcon()
        iconThemeName = u"folder"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u"C:/Users/qinyf/.designer/backup", QSize(), QIcon.Normal, QIcon.Off)
        
        self.actionsubmenu_2.setIcon(icon1)
        self.actionsubmenu_3 = QAction(MainWindow)
        self.actionsubmenu_3.setObjectName(u"actionsubmenu_3")
        icon2 = QIcon()
        iconThemeName = u"document-save-as"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u"C:/Users/qinyf/.designer/backup", QSize(), QIcon.Normal, QIcon.Off)
        
        self.actionsubmenu_3.setIcon(icon2)
        self.actionsubmenu_4 = QAction(MainWindow)
        self.actionsubmenu_4.setObjectName(u"actionsubmenu_4")
        icon3 = QIcon()
        iconThemeName = u"document-save"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u"C:/Users/qinyf/.designer/backup", QSize(), QIcon.Normal, QIcon.Off)
        
        self.actionsubmenu_4.setIcon(icon3)
        self.actionSave_all = QAction(MainWindow)
        self.actionSave_all.setObjectName(u"actionSave_all")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        icon4 = QIcon()
        iconThemeName = u"window-close"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u"C:/Users/qinyf/.designer/backup", QSize(), QIcon.Normal, QIcon.Off)
        
        self.actionClose.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_17 = QGridLayout(self.centralwidget)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.Panel = QWidget(self.centralwidget)
        self.Panel.setObjectName(u"Panel")
        self.Panel.setMinimumSize(QSize(400, 0))
        self.gridLayout_11 = QGridLayout(self.Panel)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.widget = QWidget(self.Panel)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonCamera = QPushButton(self.widget)
        self.buttonCamera.setObjectName(u"buttonCamera")
        self.buttonCamera.setMinimumSize(QSize(0, 80))
#if QT_CONFIG(tooltip)
        self.buttonCamera.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.buttonCamera.setCheckable(True)

        self.gridLayout.addWidget(self.buttonCamera, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.buttonCapture = QPushButton(self.widget)
        self.buttonCapture.setObjectName(u"buttonCapture")
        self.buttonCapture.setMinimumSize(QSize(0, 80))
        self.buttonCapture.setCheckable(True)

        self.gridLayout.addWidget(self.buttonCapture, 2, 0, 1, 1)

        self.buttonProcess = QPushButton(self.widget)
        self.buttonProcess.setObjectName(u"buttonProcess")
        self.buttonProcess.setMinimumSize(QSize(0, 80))
        self.buttonProcess.setCheckable(True)

        self.gridLayout.addWidget(self.buttonProcess, 4, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.buttonStart = QPushButton(self.widget)
        self.buttonStart.setObjectName(u"buttonStart")
        self.buttonStart.setMinimumSize(QSize(0, 80))

        self.horizontalLayout_14.addWidget(self.buttonStart)

        self.buttonStop = QPushButton(self.widget)
        self.buttonStop.setObjectName(u"buttonStop")
        self.buttonStop.setMinimumSize(QSize(0, 80))

        self.horizontalLayout_14.addWidget(self.buttonStop)


        self.gridLayout.addLayout(self.horizontalLayout_14, 6, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 5, 0, 1, 1)


        self.gridLayout_11.addWidget(self.widget, 0, 0, 1, 3)

        self.widget_2 = QWidget(self.Panel)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 9, -1, 9)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, -1, 5, -1)
        self.sourceChoose = QPushButton(self.widget_2)
        self.sourceChoose.setObjectName(u"sourceChoose")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceChoose.sizePolicy().hasHeightForWidth())
        self.sourceChoose.setSizePolicy(sizePolicy)
        self.sourceChoose.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.sourceChoose)

        self.editSource = QLineEdit(self.widget_2)
        self.editSource.setObjectName(u"editSource")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.editSource.sizePolicy().hasHeightForWidth())
        self.editSource.setSizePolicy(sizePolicy1)
        self.editSource.setMinimumSize(QSize(0, 40))
        self.editSource.setAlignment(Qt.AlignCenter)
        self.editSource.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.editSource)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, -1, 5, -1)
        self.modelChoose = QPushButton(self.widget_2)
        self.modelChoose.setObjectName(u"modelChoose")
        sizePolicy.setHeightForWidth(self.modelChoose.sizePolicy().hasHeightForWidth())
        self.modelChoose.setSizePolicy(sizePolicy)
        self.modelChoose.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.modelChoose)

        self.modelLabel = QLabel(self.widget_2)
        self.modelLabel.setObjectName(u"modelLabel")

        self.horizontalLayout.addWidget(self.modelLabel, 0, Qt.AlignHCenter)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, -1, 5, -1)
        self.yamlChoose = QPushButton(self.widget_2)
        self.yamlChoose.setObjectName(u"yamlChoose")
        sizePolicy.setHeightForWidth(self.yamlChoose.sizePolicy().hasHeightForWidth())
        self.yamlChoose.setSizePolicy(sizePolicy)
        self.yamlChoose.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.yamlChoose)

        self.Yaml = QLabel(self.widget_2)
        self.Yaml.setObjectName(u"Yaml")

        self.horizontalLayout_2.addWidget(self.Yaml, 0, Qt.AlignHCenter)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, -1, 5, -1)
        self.imgSize = QCheckBox(self.widget_2)
        self.imgSize.setObjectName(u"imgSize")
        sizePolicy.setHeightForWidth(self.imgSize.sizePolicy().hasHeightForWidth())
        self.imgSize.setSizePolicy(sizePolicy)
        self.imgSize.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_3.addWidget(self.imgSize)

        self.editSize = QLineEdit(self.widget_2)
        self.editSize.setObjectName(u"editSize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.editSize.sizePolicy().hasHeightForWidth())
        self.editSize.setSizePolicy(sizePolicy2)
        self.editSize.setMinimumSize(QSize(0, 40))
        self.editSize.setAlignment(Qt.AlignCenter)
        self.editSize.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.editSize)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, -1, -1, -1)
        self.noConf = QCheckBox(self.widget_2)
        self.noConf.setObjectName(u"noConf")
        sizePolicy.setHeightForWidth(self.noConf.sizePolicy().hasHeightForWidth())
        self.noConf.setSizePolicy(sizePolicy)
        self.noConf.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_4.addWidget(self.noConf)

        self.filter = QCheckBox(self.widget_2)
        self.filter.setObjectName(u"filter")
        self.filter.setMinimumSize(QSize(0, 40))
        self.filter.setChecked(True)

        self.horizontalLayout_4.addWidget(self.filter)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.confThresholdText = QLabel(self.widget_2)
        self.confThresholdText.setObjectName(u"confThresholdText")
        self.confThresholdText.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_11.addWidget(self.confThresholdText)

        self.horizontalSpacer = QSpacerItem(13, 40, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)

        self.valThreshold = QLabel(self.widget_2)
        self.valThreshold.setObjectName(u"valThreshold")
        self.valThreshold.setMinimumSize(QSize(0, 40))
        self.valThreshold.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.valThreshold)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.confSlider = QSlider(self.widget_2)
        self.confSlider.setObjectName(u"confSlider")
        sizePolicy1.setHeightForWidth(self.confSlider.sizePolicy().hasHeightForWidth())
        self.confSlider.setSizePolicy(sizePolicy1)
        self.confSlider.setMaximumSize(QSize(16777215, 100))
        self.confSlider.setMaximum(100)
        self.confSlider.setValue(25)
        self.confSlider.setSliderPosition(25)
        self.confSlider.setTracking(True)
        self.confSlider.setOrientation(Qt.Horizontal)
        self.confSlider.setInvertedControls(False)

        self.verticalLayout.addWidget(self.confSlider)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.IoUThresholdText = QLabel(self.widget_2)
        self.IoUThresholdText.setObjectName(u"IoUThresholdText")
        self.IoUThresholdText.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_18.addWidget(self.IoUThresholdText)

        self.horizontalSpacer_3 = QSpacerItem(13, 40, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_3)

        self.valIOUThreshold = QLabel(self.widget_2)
        self.valIOUThreshold.setObjectName(u"valIOUThreshold")
        self.valIOUThreshold.setMinimumSize(QSize(0, 40))
        self.valIOUThreshold.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.valIOUThreshold)


        self.verticalLayout.addLayout(self.horizontalLayout_18)

        self.IoUSlider = QSlider(self.widget_2)
        self.IoUSlider.setObjectName(u"IoUSlider")
        sizePolicy1.setHeightForWidth(self.IoUSlider.sizePolicy().hasHeightForWidth())
        self.IoUSlider.setSizePolicy(sizePolicy1)
        self.IoUSlider.setMinimumSize(QSize(0, 0))
        self.IoUSlider.setMaximum(100)
        self.IoUSlider.setValue(45)
        self.IoUSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.IoUSlider)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)
        self.verticalLayout.setStretch(8, 1)

        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 1)


        self.gridLayout_11.addWidget(self.widget_2, 1, 0, 1, 3)


        self.gridLayout_17.addWidget(self.Panel, 0, 0, 1, 1)

        self.View = QWidget(self.centralwidget)
        self.View.setObjectName(u"View")
        self.View.setMinimumSize(QSize(700, 0))
        self.gridLayout_22 = QGridLayout(self.View)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.ViweForm = QWidget(self.View)
        self.ViweForm.setObjectName(u"ViweForm")
        self.gridLayout_14 = QGridLayout(self.ViweForm)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.LayOuts = QVBoxLayout()
        self.LayOuts.setObjectName(u"LayOuts")
        self.CV = QLabel(self.ViweForm)
        self.CV.setObjectName(u"CV")
        self.CV.setAlignment(Qt.AlignCenter)

        self.LayOuts.addWidget(self.CV)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.LayOuts.addItem(self.verticalSpacer_5)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.paramsText = QLabel(self.ViweForm)
        self.paramsText.setObjectName(u"paramsText")
        self.paramsText.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.paramsText)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)

        self.params = QLabel(self.ViweForm)
        self.params.setObjectName(u"params")

        self.horizontalLayout_13.addWidget(self.params)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(2, 55)

        self.LayOuts.addLayout(self.horizontalLayout_13)

        self.LayOuts.setStretch(0, 100)

        self.gridLayout_14.addLayout(self.LayOuts, 0, 1, 1, 1)


        self.gridLayout_22.addWidget(self.ViweForm, 0, 0, 1, 1)


        self.gridLayout_17.addWidget(self.View, 0, 2, 4, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.buttonCamera.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Blast Hole Detector", None))
        self.actionSubmenu_2.setText(QCoreApplication.translate("MainWindow", u"Submenu", None))
        self.actionSubmenu_3.setText(QCoreApplication.translate("MainWindow", u"Submenu", None))
        self.actionSUBSUB.setText(QCoreApplication.translate("MainWindow", u"SUBSUB", None))
        self.actionSUBSUB_2.setText(QCoreApplication.translate("MainWindow", u"SUBSUB", None))
        self.actionSUBSUB_3.setText(QCoreApplication.translate("MainWindow", u"SUBSUB", None))
        self.actiondissabled.setText(QCoreApplication.translate("MainWindow", u"dissabled", None))
        self.actionSubmenu.setText(QCoreApplication.translate("MainWindow", u"Submenu", None))
        self.actionSubmenu_4.setText(QCoreApplication.translate("MainWindow", u"Submenu", None))
        self.actionSubmenu_5.setText(QCoreApplication.translate("MainWindow", u"Submenu", None))
        self.actionToolbar.setText(QCoreApplication.translate("MainWindow", u"Qt Material Theme", None))
#if QT_CONFIG(tooltip)
        self.actionToolbar.setToolTip(QCoreApplication.translate("MainWindow", u"Qt Material Theme", None))
#endif // QT_CONFIG(tooltip)
        self.actionSelected.setText(QCoreApplication.translate("MainWindow", u"Selected", None))
        self.actionaction.setText(QCoreApplication.translate("MainWindow", u"action", None))
        self.actionaction2.setText(QCoreApplication.translate("MainWindow", u"action2", None))
        self.actionaction3.setText(QCoreApplication.translate("MainWindow", u"action3", None))
        self.action111.setText(QCoreApplication.translate("MainWindow", u"111", None))
        self.action222.setText(QCoreApplication.translate("MainWindow", u"222", None))
        self.action333.setText(QCoreApplication.translate("MainWindow", u"333", None))
        self.actionsubmenu.setText(QCoreApplication.translate("MainWindow", u"New...", None))
        self.actionsubmenu_2.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
        self.actionsubmenu_3.setText(QCoreApplication.translate("MainWindow", u"Save as...", None))
        self.actionsubmenu_4.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_all.setText(QCoreApplication.translate("MainWindow", u"Save all", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.buttonCamera.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.buttonCapture.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.buttonProcess.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.buttonStart.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.buttonStop.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.sourceChoose.setText(QCoreApplication.translate("MainWindow", u"Source", None))
        self.editSource.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.modelChoose.setText(QCoreApplication.translate("MainWindow", u"Choose Model", None))
        self.modelLabel.setText(QCoreApplication.translate("MainWindow", u"best.pt", None))
        self.yamlChoose.setText(QCoreApplication.translate("MainWindow", u"Choose Data", None))
        self.Yaml.setText(QCoreApplication.translate("MainWindow", u"blastHole.yaml", None))
        self.imgSize.setText(QCoreApplication.translate("MainWindow", u"ImageSize", None))
        self.editSize.setText(QCoreApplication.translate("MainWindow", u"1280", None))
        self.noConf.setText(QCoreApplication.translate("MainWindow", u"--noconf", None))
        self.filter.setText(QCoreApplication.translate("MainWindow", u"--filter", None))
        self.confThresholdText.setText(QCoreApplication.translate("MainWindow", u"Confidence Threshold", None))
        self.valThreshold.setText(QCoreApplication.translate("MainWindow", u"25%", None))
        self.IoUThresholdText.setText(QCoreApplication.translate("MainWindow", u"IoU Threshold", None))
        self.valIOUThreshold.setText(QCoreApplication.translate("MainWindow", u"45%", None))
        self.CV.setText(QCoreApplication.translate("MainWindow", u"View Widget", None))
        self.paramsText.setText(QCoreApplication.translate("MainWindow", u"Params:", None))
        self.params.setText("")
    # retranslateUi

