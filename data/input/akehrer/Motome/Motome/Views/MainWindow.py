# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\Motome\Views\MainWindow.ui'
#
# Created: Tue May 20 17:11:02 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        font = QtGui.QFont()
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/resources/logo_320x320.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setContentsMargins(5, 5, 11, 5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frameOmniSettings = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameOmniSettings.sizePolicy().hasHeightForWidth())
        self.frameOmniSettings.setSizePolicy(sizePolicy)
        self.frameOmniSettings.setObjectName("frameOmniSettings")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frameOmniSettings)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.omniBar = QtGui.QLineEdit(self.frameOmniSettings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.omniBar.sizePolicy().hasHeightForWidth())
        self.omniBar.setSizePolicy(sizePolicy)
        self.omniBar.setMaxLength(65535)
        self.omniBar.setFrame(False)
        self.omniBar.setObjectName("omniBar")
        self.horizontalLayout.addWidget(self.omniBar)
        self.btnSettings = QtGui.QPushButton(self.frameOmniSettings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.btnSettings.sizePolicy().hasHeightForWidth())
        self.btnSettings.setSizePolicy(sizePolicy)
        self.btnSettings.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/resources/gear_32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSettings.setIcon(icon1)
        self.btnSettings.setFlat(True)
        self.btnSettings.setObjectName("btnSettings")
        self.horizontalLayout.addWidget(self.btnSettings)
        self.verticalLayout_5.addWidget(self.frameOmniSettings)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setContentsMargins(11, -1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.historyLabel = QtGui.QLabel(self.layoutWidget)
        self.historyLabel.setText("")
        self.historyLabel.setTextFormat(QtCore.Qt.RichText)
        self.historyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.historyLabel.setWordWrap(True)
        self.historyLabel.setObjectName("historyLabel")
        self.verticalLayout_3.addWidget(self.historyLabel)
        self.toolBox = QtGui.QStackedWidget(self.splitter)
        self.toolBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet("")
        self.toolBox.setObjectName("toolBox")
        self.tabEditor = QtGui.QWidget()
        self.tabEditor.setObjectName("tabEditor")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabEditor)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.tabEditor)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.toolBox.addWidget(self.tabEditor)
        self.tabPreview = QtGui.QWidget()
        self.tabPreview.setObjectName("tabPreview")
        self.verticalLayout = QtGui.QVBoxLayout(self.tabPreview)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.notePreview = QtGui.QTextBrowser(self.tabPreview)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notePreview.sizePolicy().hasHeightForWidth())
        self.notePreview.setSizePolicy(sizePolicy)
        self.notePreview.setFrameShape(QtGui.QFrame.NoFrame)
        self.notePreview.setOpenExternalLinks(False)
        self.notePreview.setOpenLinks(False)
        self.notePreview.setObjectName("notePreview")
        self.verticalLayout.addWidget(self.notePreview)
        self.toolBox.addWidget(self.tabPreview)
        self.tabDiff = QtGui.QWidget()
        self.tabDiff.setObjectName("tabDiff")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabDiff)
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.noteDiff = QtGui.QTextBrowser(self.tabDiff)
        self.noteDiff.setFrameShape(QtGui.QFrame.NoFrame)
        self.noteDiff.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.noteDiff.setObjectName("noteDiff")
        self.verticalLayout_4.addWidget(self.noteDiff)
        self.toolBox.addWidget(self.tabDiff)
        self.verticalLayout_5.addWidget(self.splitter)
        self.frameHistory = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameHistory.sizePolicy().hasHeightForWidth())
        self.frameHistory.setSizePolicy(sizePolicy)
        self.frameHistory.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameHistory.setFrameShadow(QtGui.QFrame.Raised)
        self.frameHistory.setObjectName("frameHistory")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frameHistory)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.historySlider = QtGui.QSlider(self.frameHistory)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.historySlider.sizePolicy().hasHeightForWidth())
        self.historySlider.setSizePolicy(sizePolicy)
        self.historySlider.setMaximum(1)
        self.historySlider.setPageStep(1)
        self.historySlider.setProperty("value", 1)
        self.historySlider.setTracking(False)
        self.historySlider.setOrientation(QtCore.Qt.Horizontal)
        self.historySlider.setInvertedAppearance(False)
        self.historySlider.setInvertedControls(False)
        self.historySlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.historySlider.setTickInterval(1)
        self.historySlider.setObjectName("historySlider")
        self.horizontalLayout_4.addWidget(self.historySlider)
        self.btnPrevDate = QtGui.QPushButton(self.frameHistory)
        self.btnPrevDate.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/resources/date_previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPrevDate.setIcon(icon2)
        self.btnPrevDate.setFlat(True)
        self.btnPrevDate.setObjectName("btnPrevDate")
        self.horizontalLayout_4.addWidget(self.btnPrevDate)
        self.btnNextDate = QtGui.QPushButton(self.frameHistory)
        self.btnNextDate.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/resources/date_next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNextDate.setIcon(icon3)
        self.btnNextDate.setFlat(True)
        self.btnNextDate.setObjectName("btnNextDate")
        self.horizontalLayout_4.addWidget(self.btnNextDate)
        self.verticalLayout_5.addWidget(self.frameHistory)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QObject.connect(self.historySlider, QtCore.SIGNAL("valueChanged(int)"), MainWindow.load_old_note)
        QtCore.QObject.connect(self.btnPrevDate, QtCore.SIGNAL("clicked()"), MainWindow.click_older_date)
        QtCore.QObject.connect(self.btnNextDate, QtCore.SIGNAL("clicked()"), MainWindow.click_newer_date)
        QtCore.QObject.connect(self.omniBar, QtCore.SIGNAL("textChanged(QString)"), MainWindow.start_search)
        QtCore.QObject.connect(self.btnSettings, QtCore.SIGNAL("clicked()"), MainWindow.load_settings)
        QtCore.QObject.connect(self.omniBar, QtCore.SIGNAL("returnPressed()"), MainWindow.new_note)
        QtCore.QObject.connect(self.historyLabel, QtCore.SIGNAL("linkActivated(QString)"), MainWindow.toggle_history_bar_view)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.omniBar, self.toolBox)
        MainWindow.setTabOrder(self.toolBox, self.btnPrevDate)
        MainWindow.setTabOrder(self.btnPrevDate, self.btnNextDate)
        MainWindow.setTabOrder(self.btnNextDate, self.historySlider)
        MainWindow.setTabOrder(self.historySlider, self.btnSettings)
        MainWindow.setTabOrder(self.btnSettings, self.noteDiff)
        MainWindow.setTabOrder(self.noteDiff, self.notePreview)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.omniBar.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Search... Press Enter to create a new note with your seach as the title", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSettings.setToolTip(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Tags: ", None, QtGui.QApplication.UnicodeUTF8))
        self.historySlider.setToolTip(QtGui.QApplication.translate("MainWindow", "Current", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPrevDate.setToolTip(QtGui.QApplication.translate("MainWindow", "Older", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNextDate.setToolTip(QtGui.QApplication.translate("MainWindow", "Newer", None, QtGui.QApplication.UnicodeUTF8))

import MainWindow_rc
