# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqt_vertical_tab_widget import VerticalTabWidget
from PyQt5 import QtWebEngineWidgets


class Ui_ClearMod_Window(object):
    def setupUi(self, ClearMod_Window):
        ClearMod_Window.setObjectName("ClearMod_Window")
        ClearMod_Window.resize(920, 705)
        ClearMod_Window.setMinimumSize(QtCore.QSize(920, 705))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icons/ClearMod.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ClearMod_Window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(ClearMod_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Interface_Widget = VerticalTabWidget()
        self.Interface_Widget.setTabPosition(QtWidgets.QTabWidget.West)
        self.Interface_Widget.setObjectName("Interface_Widget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 9, 443, 170))
        self.layoutWidget.setObjectName("layoutWidget")
        self.Start_layout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.Start_layout.setContentsMargins(0, 0, 0, 0)
        self.Start_layout.setObjectName("Start_layout")
        self.start_label = QtWidgets.QLabel(self.layoutWidget)
        self.start_label.setObjectName("start_label")
        self.Start_layout.addWidget(self.start_label)
        self.LighTheam_radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.LighTheam_radioButton.setChecked(True)
        self.LighTheam_radioButton.setObjectName("LighTheam_radioButton")
        self.Start_layout.addWidget(self.LighTheam_radioButton)
        self.DarkTheam_radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.DarkTheam_radioButton.setObjectName("DarkTheam_radioButton")
        self.Start_layout.addWidget(self.DarkTheam_radioButton)
        self.reboot_checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.reboot_checkBox.setObjectName("reboot_checkBox")
        self.Start_layout.addWidget(self.reboot_checkBox)
        self.Start_button = QtWidgets.QPushButton(self.layoutWidget)
        self.Start_button.setObjectName("Start_button")
        self.Start_layout.addWidget(self.Start_button)
        self.Interface_Widget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Data_box = QtWidgets.QGroupBox(self.tab_3)
        self.Data_box.setObjectName("Data_box")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.Data_box)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.data_labels_layout = QtWidgets.QVBoxLayout()
        self.data_labels_layout.setObjectName("data_labels_layout")
        self.Login_label = QtWidgets.QLabel(self.Data_box)
        self.Login_label.setObjectName("Login_label")
        self.data_labels_layout.addWidget(self.Login_label)
        self.Password_label = QtWidgets.QLabel(self.Data_box)
        self.Password_label.setObjectName("Password_label")
        self.data_labels_layout.addWidget(self.Password_label)
        self.Referal_label = QtWidgets.QLabel(self.Data_box)
        self.Referal_label.setObjectName("Referal_label")
        self.data_labels_layout.addWidget(self.Referal_label)
        self.horizontalLayout_4.addLayout(self.data_labels_layout)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Login_input = QtWidgets.QLineEdit(self.Data_box)
        self.Login_input.setMaxLength(12)
        self.Login_input.setObjectName("Login_input")
        self.verticalLayout_7.addWidget(self.Login_input)
        self.Password_input = QtWidgets.QLineEdit(self.Data_box)
        self.Password_input.setMaxLength(12)
        self.Password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password_input.setObjectName("Password_input")
        self.verticalLayout_7.addWidget(self.Password_input)
        self.Referal_input = QtWidgets.QLineEdit(self.Data_box)
        self.Referal_input.setMaxLength(12)
        self.Referal_input.setObjectName("Referal_input")
        self.verticalLayout_7.addWidget(self.Referal_input)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.gridLayout_6.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.ShowPassword_checkBox = QtWidgets.QCheckBox(self.Data_box)
        self.ShowPassword_checkBox.setObjectName("ShowPassword_checkBox")
        self.gridLayout_6.addWidget(self.ShowPassword_checkBox, 1, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.Data_box)
        self.UsersButtons_groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.UsersButtons_groupBox.setTitle("")
        self.UsersButtons_groupBox.setObjectName("UsersButtons_groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.UsersButtons_groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.UserGen_button = QtWidgets.QPushButton(self.UsersButtons_groupBox)
        self.UserGen_button.setObjectName("UserGen_button")
        self.horizontalLayout_5.addWidget(self.UserGen_button)
        self.ClearData_button = QtWidgets.QPushButton(self.UsersButtons_groupBox)
        self.ClearData_button.setObjectName("ClearData_button")
        self.horizontalLayout_5.addWidget(self.ClearData_button)
        self.verticalLayout_8.addWidget(self.UsersButtons_groupBox)
        self.Avatar_groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.Avatar_groupBox.setObjectName("Avatar_groupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.Avatar_groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.Avatar_widget = QtWidgets.QTabWidget(self.Avatar_groupBox)
        self.Avatar_widget.setObjectName("Avatar_widget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.LeftPublicAvatar_button = QtWidgets.QToolButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LeftPublicAvatar_button.sizePolicy().hasHeightForWidth())
        self.LeftPublicAvatar_button.setSizePolicy(sizePolicy)
        self.LeftPublicAvatar_button.setMinimumSize(QtCore.QSize(100, 0))
        self.LeftPublicAvatar_button.setArrowType(QtCore.Qt.LeftArrow)
        self.LeftPublicAvatar_button.setObjectName("LeftPublicAvatar_button")
        self.gridLayout_8.addWidget(self.LeftPublicAvatar_button, 0, 0, 1, 1)
        self.PublicAvatar_image = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PublicAvatar_image.sizePolicy().hasHeightForWidth())
        self.PublicAvatar_image.setSizePolicy(sizePolicy)
        self.PublicAvatar_image.setObjectName("PublicAvatar_image")
        self.gridLayout_8.addWidget(self.PublicAvatar_image, 0, 1, 1, 1)
        self.RightPublicAvatar_button = QtWidgets.QToolButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RightPublicAvatar_button.sizePolicy().hasHeightForWidth())
        self.RightPublicAvatar_button.setSizePolicy(sizePolicy)
        self.RightPublicAvatar_button.setMinimumSize(QtCore.QSize(100, 0))
        self.RightPublicAvatar_button.setArrowType(QtCore.Qt.RightArrow)
        self.RightPublicAvatar_button.setObjectName("RightPublicAvatar_button")
        self.gridLayout_8.addWidget(self.RightPublicAvatar_button, 0, 2, 1, 1)
        self.Avatar_widget.addTab(self.widget, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.LeftSecretAvatar_button = QtWidgets.QToolButton(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LeftSecretAvatar_button.sizePolicy().hasHeightForWidth())
        self.LeftSecretAvatar_button.setSizePolicy(sizePolicy)
        self.LeftSecretAvatar_button.setMinimumSize(QtCore.QSize(100, 0))
        self.LeftSecretAvatar_button.setArrowType(QtCore.Qt.LeftArrow)
        self.LeftSecretAvatar_button.setObjectName("LeftSecretAvatar_button")
        self.gridLayout_9.addWidget(self.LeftSecretAvatar_button, 0, 0, 1, 1)
        self.SecretAvatar_image = QtWidgets.QLabel(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SecretAvatar_image.sizePolicy().hasHeightForWidth())
        self.SecretAvatar_image.setSizePolicy(sizePolicy)
        self.SecretAvatar_image.setObjectName("SecretAvatar_image")
        self.gridLayout_9.addWidget(self.SecretAvatar_image, 0, 1, 1, 1)
        self.RightSecretAvatar_button = QtWidgets.QToolButton(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RightSecretAvatar_button.sizePolicy().hasHeightForWidth())
        self.RightSecretAvatar_button.setSizePolicy(sizePolicy)
        self.RightSecretAvatar_button.setMinimumSize(QtCore.QSize(100, 0))
        self.RightSecretAvatar_button.setArrowType(QtCore.Qt.RightArrow)
        self.RightSecretAvatar_button.setObjectName("RightSecretAvatar_button")
        self.gridLayout_9.addWidget(self.RightSecretAvatar_button, 0, 2, 1, 1)
        self.Avatar_widget.addTab(self.tab_5, "")
        self.gridLayout_7.addWidget(self.Avatar_widget, 0, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.Avatar_groupBox)
        self.RegButtons_groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.RegButtons_groupBox.setObjectName("RegButtons_groupBox")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.RegButtons_groupBox)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.CheckData_button = QtWidgets.QPushButton(self.RegButtons_groupBox)
        self.CheckData_button.setObjectName("CheckData_button")
        self.horizontalLayout_7.addWidget(self.CheckData_button)
        self.Reg_button = QtWidgets.QPushButton(self.RegButtons_groupBox)
        self.Reg_button.setObjectName("Reg_button")
        self.horizontalLayout_7.addWidget(self.Reg_button)
        self.verticalLayout_8.addWidget(self.RegButtons_groupBox)
        self.Message_label = QtWidgets.QLabel(self.tab_3)
        self.Message_label.setStyleSheet("color: rgb(170, 0, 0);")
        self.Message_label.setText("")
        self.Message_label.setObjectName("Message_label")
        self.verticalLayout_8.addWidget(self.Message_label)
        self.Interface_Widget.addTab(self.tab_3, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.widget1 = QtWidgets.QWidget(self.tab_6)
        self.widget1.setGeometry(QtCore.QRect(11, 2, 461, 217))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.Login_groupBox_1 = QtWidgets.QGroupBox(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Login_groupBox_1.sizePolicy().hasHeightForWidth())
        self.Login_groupBox_1.setSizePolicy(sizePolicy)
        self.Login_groupBox_1.setObjectName("Login_groupBox_1")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.Login_groupBox_1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.Login_label_2 = QtWidgets.QLabel(self.Login_groupBox_1)
        self.Login_label_2.setObjectName("Login_label_2")
        self.verticalLayout_9.addWidget(self.Login_label_2)
        self.Password_label_2 = QtWidgets.QLabel(self.Login_groupBox_1)
        self.Password_label_2.setObjectName("Password_label_2")
        self.verticalLayout_9.addWidget(self.Password_label_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.Login_input_2 = QtWidgets.QLineEdit(self.Login_groupBox_1)
        self.Login_input_2.setMaxLength(12)
        self.Login_input_2.setObjectName("Login_input_2")
        self.verticalLayout_10.addWidget(self.Login_input_2)
        self.Password_input_2 = QtWidgets.QLineEdit(self.Login_groupBox_1)
        self.Password_input_2.setMaxLength(12)
        self.Password_input_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password_input_2.setObjectName("Password_input_2")
        self.verticalLayout_10.addWidget(self.Password_input_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.verticalLayout_11.addLayout(self.horizontalLayout_6)
        self.ShowPassword2_checkBox = QtWidgets.QCheckBox(self.Login_groupBox_1)
        self.ShowPassword2_checkBox.setObjectName("ShowPassword2_checkBox")
        self.verticalLayout_11.addWidget(self.ShowPassword2_checkBox)
        self.verticalLayout_12.addWidget(self.Login_groupBox_1)
        self.Login_groupBox_2 = QtWidgets.QGroupBox(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Login_groupBox_2.sizePolicy().hasHeightForWidth())
        self.Login_groupBox_2.setSizePolicy(sizePolicy)
        self.Login_groupBox_2.setObjectName("Login_groupBox_2")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.Login_groupBox_2)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.UsersList_comboBox = QtWidgets.QComboBox(self.Login_groupBox_2)
        self.UsersList_comboBox.setObjectName("UsersList_comboBox")
        self.verticalLayout_18.addWidget(self.UsersList_comboBox)
        self.verticalLayout_12.addWidget(self.Login_groupBox_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.ClearData_button_2 = QtWidgets.QPushButton(self.widget1)
        self.ClearData_button_2.setObjectName("ClearData_button_2")
        self.horizontalLayout_9.addWidget(self.ClearData_button_2)
        self.Login_Button = QtWidgets.QPushButton(self.widget1)
        self.Login_Button.setObjectName("Login_Button")
        self.horizontalLayout_9.addWidget(self.Login_Button)
        self.verticalLayout_12.addLayout(self.horizontalLayout_9)
        self.LoginError_label = QtWidgets.QLabel(self.widget1)
        self.LoginError_label.setStyleSheet("color: red;")
        self.LoginError_label.setText("")
        self.LoginError_label.setObjectName("LoginError_label")
        self.verticalLayout_12.addWidget(self.LoginError_label)
        self.Interface_Widget.addTab(self.tab_6, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.System_groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.System_groupBox.setObjectName("System_groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.System_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.OS_label = QtWidgets.QLabel(self.System_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OS_label.sizePolicy().hasHeightForWidth())
        self.OS_label.setSizePolicy(sizePolicy)
        self.OS_label.setObjectName("OS_label")
        self.verticalLayout.addWidget(self.OS_label)
        self.MAC_label = QtWidgets.QLabel(self.System_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MAC_label.sizePolicy().hasHeightForWidth())
        self.MAC_label.setSizePolicy(sizePolicy)
        self.MAC_label.setObjectName("MAC_label")
        self.verticalLayout.addWidget(self.MAC_label)
        self.IP_label = QtWidgets.QLabel(self.System_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IP_label.sizePolicy().hasHeightForWidth())
        self.IP_label.setSizePolicy(sizePolicy)
        self.IP_label.setObjectName("IP_label")
        self.verticalLayout.addWidget(self.IP_label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.OSname_label = QtWidgets.QLabel(self.System_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OSname_label.sizePolicy().hasHeightForWidth())
        self.OSname_label.setSizePolicy(sizePolicy)
        self.OSname_label.setObjectName("OSname_label")
        self.verticalLayout_2.addWidget(self.OSname_label)
        self.MACadress_label = QtWidgets.QLabel(self.System_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MACadress_label.sizePolicy().hasHeightForWidth())
        self.MACadress_label.setSizePolicy(sizePolicy)
        self.MACadress_label.setObjectName("MACadress_label")
        self.verticalLayout_2.addWidget(self.MACadress_label)
        self.IParress_label = QtWidgets.QLabel(self.System_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IParress_label.sizePolicy().hasHeightForWidth())
        self.IParress_label.setSizePolicy(sizePolicy)
        self.IParress_label.setObjectName("IParress_label")
        self.verticalLayout_2.addWidget(self.IParress_label)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.ShowSystemData_checkBox = QtWidgets.QCheckBox(self.System_groupBox)
        self.ShowSystemData_checkBox.setChecked(True)
        self.ShowSystemData_checkBox.setObjectName("ShowSystemData_checkBox")
        self.gridLayout_2.addWidget(self.ShowSystemData_checkBox, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.System_groupBox, 0, 0, 1, 1)
        self.Launchers_groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.Launchers_groupBox.setObjectName("Launchers_groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Launchers_groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ClearMode_label = QtWidgets.QLabel(self.Launchers_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ClearMode_label.sizePolicy().hasHeightForWidth())
        self.ClearMode_label.setSizePolicy(sizePolicy)
        self.ClearMode_label.setObjectName("ClearMode_label")
        self.verticalLayout_3.addWidget(self.ClearMode_label)
        self.Shararam_label = QtWidgets.QLabel(self.Launchers_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Shararam_label.sizePolicy().hasHeightForWidth())
        self.Shararam_label.setSizePolicy(sizePolicy)
        self.Shararam_label.setObjectName("Shararam_label")
        self.verticalLayout_3.addWidget(self.Shararam_label)
        self.Private_label = QtWidgets.QLabel(self.Launchers_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Private_label.sizePolicy().hasHeightForWidth())
        self.Private_label.setSizePolicy(sizePolicy)
        self.Private_label.setObjectName("Private_label")
        self.verticalLayout_3.addWidget(self.Private_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ClearMode_value_label = QtWidgets.QLabel(self.Launchers_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ClearMode_value_label.sizePolicy().hasHeightForWidth())
        self.ClearMode_value_label.setSizePolicy(sizePolicy)
        self.ClearMode_value_label.setObjectName("ClearMode_value_label")
        self.verticalLayout_4.addWidget(self.ClearMode_value_label)
        self.Shararam_Value_label = QtWidgets.QLabel(self.Launchers_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Shararam_Value_label.sizePolicy().hasHeightForWidth())
        self.Shararam_Value_label.setSizePolicy(sizePolicy)
        self.Shararam_Value_label.setObjectName("Shararam_Value_label")
        self.verticalLayout_4.addWidget(self.Shararam_Value_label)
        self.Private_value_label = QtWidgets.QLabel(self.Launchers_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Private_value_label.sizePolicy().hasHeightForWidth())
        self.Private_value_label.setSizePolicy(sizePolicy)
        self.Private_value_label.setObjectName("Private_value_label")
        self.verticalLayout_4.addWidget(self.Private_value_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.Launchers_groupBox, 1, 0, 1, 1)
        self.Software_groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.Software_groupBox.setObjectName("Software_groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Software_groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.VPN_label = QtWidgets.QLabel(self.Software_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VPN_label.sizePolicy().hasHeightForWidth())
        self.VPN_label.setSizePolicy(sizePolicy)
        self.VPN_label.setObjectName("VPN_label")
        self.verticalLayout_5.addWidget(self.VPN_label)
        self.WPE_label = QtWidgets.QLabel(self.Software_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WPE_label.sizePolicy().hasHeightForWidth())
        self.WPE_label.setSizePolicy(sizePolicy)
        self.WPE_label.setObjectName("WPE_label")
        self.verticalLayout_5.addWidget(self.WPE_label)
        self.Wireshark_label = QtWidgets.QLabel(self.Software_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Wireshark_label.sizePolicy().hasHeightForWidth())
        self.Wireshark_label.setSizePolicy(sizePolicy)
        self.Wireshark_label.setObjectName("Wireshark_label")
        self.verticalLayout_5.addWidget(self.Wireshark_label)
        self.Charles_label = QtWidgets.QLabel(self.Software_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Charles_label.sizePolicy().hasHeightForWidth())
        self.Charles_label.setSizePolicy(sizePolicy)
        self.Charles_label.setObjectName("Charles_label")
        self.verticalLayout_5.addWidget(self.Charles_label)
        self.Fiddler_label = QtWidgets.QLabel(self.Software_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Fiddler_label.sizePolicy().hasHeightForWidth())
        self.Fiddler_label.setSizePolicy(sizePolicy)
        self.Fiddler_label.setObjectName("Fiddler_label")
        self.verticalLayout_5.addWidget(self.Fiddler_label)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.VPN_value_label = QtWidgets.QLabel(self.Software_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VPN_value_label.sizePolicy().hasHeightForWidth())
        self.VPN_value_label.setSizePolicy(sizePolicy)
        self.VPN_value_label.setObjectName("VPN_value_label")
        self.verticalLayout_6.addWidget(self.VPN_value_label)
        self.WPE_value_label = QtWidgets.QLabel(self.Software_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WPE_value_label.sizePolicy().hasHeightForWidth())
        self.WPE_value_label.setSizePolicy(sizePolicy)
        self.WPE_value_label.setObjectName("WPE_value_label")
        self.verticalLayout_6.addWidget(self.WPE_value_label)
        self.Wireshark_value_label = QtWidgets.QLabel(self.Software_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Wireshark_value_label.sizePolicy().hasHeightForWidth())
        self.Wireshark_value_label.setSizePolicy(sizePolicy)
        self.Wireshark_value_label.setObjectName("Wireshark_value_label")
        self.verticalLayout_6.addWidget(self.Wireshark_value_label)
        self.Charles_value_label = QtWidgets.QLabel(self.Software_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Charles_value_label.sizePolicy().hasHeightForWidth())
        self.Charles_value_label.setSizePolicy(sizePolicy)
        self.Charles_value_label.setObjectName("Charles_value_label")
        self.verticalLayout_6.addWidget(self.Charles_value_label)
        self.Fiddler_value_label = QtWidgets.QLabel(self.Software_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Fiddler_value_label.sizePolicy().hasHeightForWidth())
        self.Fiddler_value_label.setSizePolicy(sizePolicy)
        self.Fiddler_value_label.setObjectName("Fiddler_value_label")
        self.verticalLayout_6.addWidget(self.Fiddler_value_label)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.Software_groupBox, 2, 0, 1, 1)
        self.Interface_Widget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ReloadItems_button = QtWidgets.QPushButton(self.tab_4)
        self.ReloadItems_button.setObjectName("ReloadItems_button")
        self.horizontalLayout_8.addWidget(self.ReloadItems_button)
        self.gridLayout_10.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.InstantList = QtWebEngineWidgets.QWebEngineView(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InstantList.sizePolicy().hasHeightForWidth())
        self.InstantList.setSizePolicy(sizePolicy)
        self.InstantList.setUrl(QtCore.QUrl("http://instant.jjck.ru/all_items.html"))
        self.InstantList.setObjectName("InstantList")
        self.gridLayout_10.addWidget(self.InstantList, 1, 0, 1, 1)
        self.Interface_Widget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.Interface_Widget, 0, 0, 1, 1)
        ClearMod_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(ClearMod_Window)
        self.Interface_Widget.setCurrentIndex(0)
        self.Avatar_widget.setCurrentIndex(0)
        self.ReloadItems_button.clicked.connect(self.InstantList.reload)  # type: ignore
        self.ClearData_button.clicked.connect(self.Login_input.clear)  # type: ignore
        self.ClearData_button.clicked.connect(self.Password_input.clear)  # type: ignore
        self.ClearData_button.clicked.connect(self.Referal_input.clear)  # type: ignore
        self.ClearData_button_2.clicked.connect(self.Login_input_2.clear)  # type: ignore
        self.ClearData_button_2.clicked.connect(self.Password_input_2.clear)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ClearMod_Window)

    def retranslateUi(self, ClearMod_Window):
        _translate = QtCore.QCoreApplication.translate
        ClearMod_Window.setWindowTitle(_translate("ClearMod_Window", "Clear Mod"))
        self.start_label.setText(_translate("ClearMod_Window", "Выберите способ запуска"))
        self.LighTheam_radioButton.setText(_translate("ClearMod_Window", "Светлая тема"))
        self.DarkTheam_radioButton.setText(_translate("ClearMod_Window", "Тёмная тема"))
        self.reboot_checkBox.setText(_translate("ClearMod_Window", "Снять перманентный бан и перезагрузить компьютер"))
        self.Start_button.setText(_translate("ClearMod_Window", "Старт"))
        self.Interface_Widget.setTabText(self.Interface_Widget.indexOf(self.tab),
                                         _translate("ClearMod_Window", "Clear Mode"))
        self.Data_box.setTitle(_translate("ClearMod_Window", "Данные"))
        self.Login_label.setText(_translate("ClearMod_Window", "Имя"))
        self.Password_label.setText(_translate("ClearMod_Window", "Пароль"))
        self.Referal_label.setText(_translate("ClearMod_Window", "Ник пригласившего пользователя"))
        self.ShowPassword_checkBox.setText(_translate("ClearMod_Window", "Показывать пароль"))
        self.UserGen_button.setText(_translate("ClearMod_Window", "Случайный"))
        self.ClearData_button.setText(_translate("ClearMod_Window", "Отчистить"))
        self.Avatar_groupBox.setTitle(_translate("ClearMod_Window", "Аватар"))
        self.LeftPublicAvatar_button.setText(_translate("ClearMod_Window", "..."))
        self.PublicAvatar_image.setText(_translate("ClearMod_Window",
                                                   "<html><head/><body><p align=\"center\"><img src=\":/Public/Public/8.png\"/></p></body></html>"))
        self.RightPublicAvatar_button.setText(_translate("ClearMod_Window", "..."))
        self.Avatar_widget.setTabText(self.Avatar_widget.indexOf(self.widget),
                                      _translate("ClearMod_Window", "Общедоступные образы"))
        self.LeftSecretAvatar_button.setText(_translate("ClearMod_Window", "..."))
        self.SecretAvatar_image.setText(_translate("ClearMod_Window",
                                                   "<html><head/><body><p align=\"center\"><img src=\":/Secret/Secret/0.png\"/></p></body></html>"))
        self.RightSecretAvatar_button.setText(_translate("ClearMod_Window", "..."))
        self.Avatar_widget.setTabText(self.Avatar_widget.indexOf(self.tab_5),
                                      _translate("ClearMod_Window", "Прочие образы"))
        self.RegButtons_groupBox.setTitle(_translate("ClearMod_Window", "Регистрация"))
        self.CheckData_button.setText(_translate("ClearMod_Window", "Проверить данные"))
        self.Reg_button.setText(_translate("ClearMod_Window", "Зарегистрироваться"))
        self.Interface_Widget.setTabText(self.Interface_Widget.indexOf(self.tab_3),
                                         _translate("ClearMod_Window", "Регистрация"))
        self.Login_groupBox_1.setTitle(_translate("ClearMod_Window", "Войти по логину и паролю"))
        self.Login_label_2.setText(_translate("ClearMod_Window", "Имя"))
        self.Password_label_2.setText(_translate("ClearMod_Window", "Пароль"))
        self.ShowPassword2_checkBox.setText(_translate("ClearMod_Window", "Показывать пароль"))
        self.Login_groupBox_2.setTitle(_translate("ClearMod_Window", "Войти в уже добавленый аккаунт"))
        self.ClearData_button_2.setText(_translate("ClearMod_Window", "Отчистить"))
        self.Login_Button.setText(_translate("ClearMod_Window", "Войти"))
        self.Interface_Widget.setTabText(self.Interface_Widget.indexOf(self.tab_6),
                                         _translate("ClearMod_Window", "Авторизация"))
        self.System_groupBox.setTitle(_translate("ClearMod_Window", "Система"))
        self.OS_label.setText(_translate("ClearMod_Window", "Операционная система:"))
        self.MAC_label.setText(_translate("ClearMod_Window", "MAC-адрес:"))
        self.IP_label.setText(_translate("ClearMod_Window", "IP-адрес:"))
        self.ShowSystemData_checkBox.setText(_translate("ClearMod_Window", "Скрыть данные"))
        self.Launchers_groupBox.setTitle(_translate("ClearMod_Window", "Лаунчеры шарарама"))
        self.ClearMode_label.setText(_translate("ClearMod_Window", "Clear Mode:"))
        self.Shararam_label.setText(_translate("ClearMod_Window", "Официальный лаунчер шарарама"))
        self.Private_label.setText(_translate("ClearMod_Window", "Приватки:"))
        self.ClearMode_value_label.setText(_translate("ClearMod_Window", "Установлен"))
        self.Software_groupBox.setTitle(_translate("ClearMod_Window", "Специальное ПО"))
        self.VPN_label.setText(_translate("ClearMod_Window", "VPN:"))
        self.WPE_label.setText(_translate("ClearMod_Window", "WPE PRO:"))
        self.Wireshark_label.setText(_translate("ClearMod_Window", "Wireshark:"))
        self.Charles_label.setText(_translate("ClearMod_Window", "Charles Proxy:"))
        self.Fiddler_label.setText(_translate("ClearMod_Window", "Fiddler:"))
        self.Interface_Widget.setTabText(self.Interface_Widget.indexOf(self.tab_2),
                                         _translate("ClearMod_Window", "Система"))
        self.ReloadItems_button.setText(_translate("ClearMod_Window", "Обновить страницу"))
        self.Interface_Widget.setTabText(self.Interface_Widget.indexOf(self.tab_4),
                                         _translate("ClearMod_Window", "Список вещей"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ClearMod_Window = QtWidgets.QMainWindow()
    ui = Ui_ClearMod_Window()
    ui.setupUi(ClearMod_Window)
    ClearMod_Window.show()
    sys.exit(app.exec_())
