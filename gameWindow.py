

from tracemalloc import start
from PyQt5 import QtCore, QtGui, QtWidgets
import stylesheets

class Ui_MainWindow(object):

    
    def __init__(self,  flop , 
                        turn , 
                        river,
                        player_turn,
                        seat1 = ["", ""], 
                        seat2 = ["", ""], 
                        seat3 = ["", ""],
                        seat4 = ["", ""], 
                        seat5 = ["", ""], 
                        seat6 = ["", ""],
                ):
                        
        #Initialize player cards
        self.S1Card1 = seat1[0]
        self.S1Card2 = seat1[1]
        self.S2Card1 = seat2[0]
        self.S2Card2 = seat2[1]
        self.S3Card1 = seat3[0]
        self.S3Card2 = seat3[1]
        self.S4Card1 = seat4[0]
        self.S4Card2 = seat4[1]
        self.S5Card1 = seat5[0]
        self.S5Card2 = seat5[1]
        self.S6Card1 = seat6[0]
        self.S6Card2 = seat6[1]
        self.flop1_card = flop[0]
        self.flop2_card = flop[1]
        self.flop3_card = flop[2]
        self.turn_card = turn
        self.river_card = river
        self.player_turn = player_turn

    def setupUi(self, MainWindow):
        MIN_CARD_SIZE = QtCore.QSize(53, 80)
        MAX_CARD_SIZE = QtCore.QSize(53, 80)
        MIN_PLAYERLABEL_SIZE = QtCore.QSize(123, 50)
        MAX_PLAYERLABEL_SIZE = QtCore.QSize(123, 50)
        PROGRESSBAR_MIN_SIZE = QtCore.QSize(126, 15)
        PROGRESSBAR_MAX_SIZE = QtCore.QSize(126, 15)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1022, 531)
        MainWindow.setStyleSheet("")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.Seat2 = QtWidgets.QHBoxLayout()
        self.Seat2.setSpacing(6)
        self.Seat2.setObjectName("Seat2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Seat2.addItem(spacerItem)
        self.Seat2VLayout = QtWidgets.QVBoxLayout()
        self.Seat2VLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.Seat2VLayout.setContentsMargins(-1, 0, -1, 0)
        self.Seat2VLayout.setObjectName("Seat2VLayout")
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Seat2VLayout.addItem(spacerItem20)
        self.Seat2HLayout = QtWidgets.QHBoxLayout()
        self.Seat2HLayout.setObjectName("Seat2HLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Seat2HLayout.addItem(spacerItem1)
        self.S2C1 = QtWidgets.QLabel(self.centralwidget)
        self.S2C2 = QtWidgets.QLabel(self.centralwidget)
        self.S2C1.setMinimumSize(MIN_CARD_SIZE)
        self.S2C1.setMaximumSize(MAX_CARD_SIZE)
        if (self.S2Card1 != ""):
                self.S2C1.setStyleSheet("border: 2px solid rgb(0,0,0);\n"
                "border-radius: 10px;\n")
                self.S2C2.setStyleSheet("border: 2px solid rgb(0,0,0);\n"
                "border-radius: 10px;\n")
        self.S2C1.setPixmap(QtGui.QPixmap(self.S2Card1)) # Draw S2C1
        self.S2C1.setScaledContents(True)
        self.S2C1.setObjectName("S2C1")
        self.Seat2HLayout.addWidget(self.S2C1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.S2C2.sizePolicy().hasHeightForWidth())
        self.S2C2.setSizePolicy(sizePolicy)
        self.S2C2.setMinimumSize(MIN_CARD_SIZE)
        self.S2C2.setMaximumSize(MAX_CARD_SIZE)
        self.S2C2.setPixmap(QtGui.QPixmap(self.S2Card2)) # Draw S2C2
        self.S2C2.setScaledContents(True)
        self.S2C2.setObjectName("S2C2")
        self.Seat2HLayout.addWidget(self.S2C2)

        self.Seat2HLayout.setStretch(1, 1)
        self.Seat2VLayout.addLayout(self.Seat2HLayout)
        self.Seat2Label = QtWidgets.QLabel(self.centralwidget)
        self.Seat2Label.setMinimumSize(MAX_PLAYERLABEL_SIZE)
        self.Seat2Label.setMaximumSize(MAX_PLAYERLABEL_SIZE)
        self.Seat2Label.setStyleSheet(stylesheets.player_label)
        self.Seat2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Seat2Label.setObjectName("Seat2Label")
        self.Seat2VLayout.addWidget(self.Seat2Label, 0, QtCore.Qt.AlignRight)
        
        if self.player_turn == 2:
            self.Seat2ProgressBar = QtWidgets.QProgressBar(self.centralwidget)
            self.Seat2ProgressBar.setMinimumSize(PROGRESSBAR_MIN_SIZE)
            self.Seat2ProgressBar.setMaximumSize(PROGRESSBAR_MAX_SIZE)
            self.Seat2ProgressBar.setAutoFillBackground(False)
            self.Seat2ProgressBar.setStyleSheet("background-color: rgb(0, 0, 0);")
            self.Seat2ProgressBar.setProperty("value", 24)
            self.Seat2ProgressBar.setTextVisible(False)
            self.Seat2ProgressBar.setObjectName("Seat2ProgressBar")
            self.Seat2VLayout.addWidget(self.Seat2ProgressBar, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.Seat2.addLayout(self.Seat2VLayout)
        self.gridLayout.addLayout(self.Seat2, 1, 0, 1, 1)

        self.topSeats = QtWidgets.QGridLayout()
        self.topSeats.setContentsMargins(-1, 0, -1, -1)
        self.topSeats.setObjectName("topSeats")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.topSeats.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.topSeats.addItem(spacerItem3, 0, 1, 1, 1)
        self.Seat4VLayout = QtWidgets.QVBoxLayout()
        self.Seat4VLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.Seat4VLayout.setContentsMargins(-1, 0, -1, 0)
        self.Seat4VLayout.setObjectName("Seat4VLayout")
        self.Seat4HLayout = QtWidgets.QHBoxLayout()
        self.Seat4HLayout.setObjectName("Seat4HLayout")
        self.S4C1 = QtWidgets.QLabel(self.centralwidget)
        self.S4C2 = QtWidgets.QLabel(self.centralwidget)
        self.S4C1.setMinimumSize(MIN_CARD_SIZE)
        self.S4C1.setMaximumSize(MAX_CARD_SIZE)
        if (self.S4Card1 != ""):
                self.S4C1.setStyleSheet("border: 2px solid rgb(0,0,0);\n"
                "border-radius: 10px;\n")
                self.S4C2.setStyleSheet("border: 2px solid rgb(0,0,0);\n"
                "border-radius: 10px;\n")
                
        self.S4C1.setPixmap(QtGui.QPixmap(self.S4Card1)) # Draw S4C1 
        self.S4C1.setScaledContents(True)
        self.S4C1.setObjectName("S4C1")
        self.Seat4HLayout.addWidget(self.S4C1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.S4C2.sizePolicy().hasHeightForWidth())
        self.S4C2.setSizePolicy(sizePolicy)
        self.S4C2.setMinimumSize(MIN_CARD_SIZE)
        self.S4C2.setMaximumSize(MAX_CARD_SIZE)
        self.S4C2.setPixmap(QtGui.QPixmap(self.S4Card2)) # Draw S4C2
        self.S4C2.setScaledContents(True)
        self.S4C2.setObjectName("S4C2")
        self.Seat4HLayout.addWidget(self.S4C2)

        self.Seat4HLayout.setStretch(0, 1)
        self.Seat4VLayout.addLayout(self.Seat4HLayout)
        self.Seat4Label = QtWidgets.QLabel(self.centralwidget)
        self.Seat4Label.setMinimumSize(MIN_PLAYERLABEL_SIZE)
        self.Seat4Label.setMaximumSize(MAX_PLAYERLABEL_SIZE)
        self.Seat4Label.setStyleSheet(stylesheets.player_label)
        self.Seat4Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Seat4Label.setObjectName("Seat4Label")
        self.Seat4VLayout.addWidget(self.Seat4Label)
        if self.player_turn == 4:
                self.Seat4ProgressBar = QtWidgets.QProgressBar(self.centralwidget)
                self.Seat4ProgressBar.setEnabled(False)
                self.Seat4ProgressBar.setMinimumSize(PROGRESSBAR_MIN_SIZE)
                self.Seat4ProgressBar.setMaximumSize(PROGRESSBAR_MAX_SIZE)
                self.Seat4ProgressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.Seat4ProgressBar.setAutoFillBackground(False)
                self.Seat4ProgressBar.setStyleSheet("background-color: rgb(0, 0, 0);")
                self.Seat4ProgressBar.setProperty("value", 24)
                self.Seat4ProgressBar.setTextVisible(False)
                self.Seat4ProgressBar.setObjectName("Seat4ProgressBar")
                self.Seat4VLayout.addWidget(self.Seat4ProgressBar, 0, QtCore.Qt.AlignTop)
        self.topSeats.addLayout(self.Seat4VLayout, 1, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.topSeats.addItem(spacerItem4, 1, 2, 1, 1)

        self.Seat3VLayout_2 = QtWidgets.QVBoxLayout()
        self.Seat3VLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.Seat3VLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.Seat3VLayout_2.setObjectName("Seat3VLayout_2")
        self.Seat3HLayout_2 = QtWidgets.QHBoxLayout()
        self.Seat3HLayout_2.setObjectName("Seat3HLayout_2")

        self.S3C1 = QtWidgets.QLabel(self.centralwidget)
        self.S3C2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.S3C1.sizePolicy().hasHeightForWidth())
        self.S3C1.setSizePolicy(sizePolicy)
        self.S3C1.setMinimumSize(MIN_CARD_SIZE)
        self.S3C1.setMaximumSize(MAX_CARD_SIZE)
        if (self.S3Card1 != ""):
                self.S3C1.setStyleSheet("border: 2px solid rgb(0,0,0);\n"
                "border-radius: 10px;\n")
                self.S3C2.setStyleSheet("border: 2px solid rgb(0,0,0);\n"
                "border-radius: 10px;\n")
        self.S3C1.setPixmap(QtGui.QPixmap(self.S3Card1)) # Draw S3C1
        self.S3C1.setScaledContents(True)
        self.S3C1.setObjectName("S3C1")
        self.S3C2.setMinimumSize(MIN_CARD_SIZE)
        self.S3C2.setMaximumSize(MAX_CARD_SIZE)
        
        self.S3C2.setPixmap(QtGui.QPixmap(self.S3Card2)) # Draw S3C2
        self.S3C2.setScaledContents(True)
        self.S3C2.setObjectName("S3C2")
        self.Seat3HLayout_2.addWidget(self.S3C2)
        self.Seat3HLayout_2.addWidget(self.S3C1)
        self.Seat3HLayout_2.setStretch(0, 1)
        self.Seat3VLayout_2.addLayout(self.Seat3HLayout_2)
        self.Seat3Label = QtWidgets.QLabel(self.centralwidget)
        self.Seat3Label.setMinimumSize(MIN_PLAYERLABEL_SIZE)
        self.Seat3Label.setMaximumSize(MAX_PLAYERLABEL_SIZE)
        self.Seat3Label.setStyleSheet(stylesheets.player_label)
        self.Seat3Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Seat3Label.setObjectName("Seat3Label")
        self.Seat3VLayout_2.addWidget(self.Seat3Label)
        if self.player_turn == 3:
                self.Seat3ProgressBar = QtWidgets.QProgressBar(self.centralwidget)
                self.Seat3ProgressBar.setMinimumSize(PROGRESSBAR_MIN_SIZE)
                self.Seat3ProgressBar.setMaximumSize(PROGRESSBAR_MAX_SIZE)
                self.Seat3ProgressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.Seat3ProgressBar.setAutoFillBackground(False)
                self.Seat3ProgressBar.setStyleSheet("background-color: rgb(0, 0, 0);")
                self.Seat3ProgressBar.setProperty("value", 24)
                self.Seat3ProgressBar.setTextVisible(False)
                self.Seat3ProgressBar.setObjectName("Seat3ProgressBar")
                self.Seat3VLayout_2.addWidget(self.Seat3ProgressBar, 0, QtCore.Qt.AlignTop)
        self.topSeats.addLayout(self.Seat3VLayout_2, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.topSeats.addItem(spacerItem5, 1, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.topSeats.addItem(spacerItem6, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.topSeats, 0, 1, 1, 1)

        self.ChatboxPanel = QtWidgets.QVBoxLayout()
        self.ChatboxPanel.setObjectName("ChatboxPanel")
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ChatboxPanel.addItem(spacerItem22)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setMaximumSize(QtCore.QSize(275, 200))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ChatboxPanel.addItem(spacerItem19)
        self.ChatboxPanel.addWidget(self.textEdit)
        self.LineEditPanel = QtWidgets.QHBoxLayout()
        self.LineEditPanel.setObjectName("LineEditPanel")
        self.ChatboxLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ChatboxLineEdit.setMinimumSize(QtCore.QSize(60, 0))
        self.ChatboxLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.ChatboxLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ChatboxLineEdit.setObjectName("ChatboxLineEdit")
        self.LineEditPanel.addWidget(self.ChatboxLineEdit, 0, QtCore.Qt.AlignTop)
        self.SendButton = QtWidgets.QPushButton(self.centralwidget)
        self.SendButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.SendButton.setStyleSheet("background-color: rgb(81, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.SendButton.setObjectName("SendButton")
        self.LineEditPanel.addWidget(self.SendButton, 0, QtCore.Qt.AlignTop)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.LineEditPanel.addItem(spacerItem23)
        self.ChatboxPanel.addLayout(self.LineEditPanel)
        self.gridLayout.addLayout(self.ChatboxPanel, 2, 0, 1, 1)

        self.Table = QtWidgets.QLabel(self.centralwidget)
        self.Table.setMinimumSize(QtCore.QSize(300, 198))
        self.Table.setMaximumSize(QtCore.QSize(16777215, 350))
        self.Table.setStyleSheet(stylesheets.table_style)
        self.Table.setTextFormat(QtCore.Qt.PlainText)
        self.Table.setScaledContents(True)
        self.Table.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Table.setObjectName("Table")

        show_flop = True
        show_turn = True
        show_river = True
        # Board Cards
        self.boardLayout = QtWidgets.QHBoxLayout(self.Table)
        if (show_flop):
                self.flop1 = QtWidgets.QLabel()
                self.flop1.setMinimumSize(QtCore.QSize(53, 65))
                self.flop1.setMaximumSize(QtCore.QSize(53, 80))
                self.flop1.setPixmap(QtGui.QPixmap(self.flop1_card)) # Draw first flop card
                self.flop1.setScaledContents(True)
                if (self.flop1_card == ""):
                        self.flop1.setStyleSheet("border: 0px solid rgb(0,0,0);")
                else:
                        self.flop1.setStyleSheet("border-radius: 10px;\n")
                #spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                #self.boardLayout.addItem(spacerItem18)
                self.boardLayout.addWidget(self.flop1)

                self.flop2 = QtWidgets.QLabel()
                self.flop2.setMinimumSize(QtCore.QSize(53, 65))
                self.flop2.setMaximumSize(QtCore.QSize(53, 80))
                self.flop2.setPixmap(QtGui.QPixmap(self.flop2_card)) # Draw second flop card
                self.flop2.setScaledContents(True)
                if (self.flop2_card == ""):
                        self.flop2.setStyleSheet("border: 0px solid rgb(0,0,0);")
                else:
                        self.flop2.setStyleSheet("border-radius: 10px;\n")
                self.boardLayout.addWidget(self.flop2)
                
                self.flop3 = QtWidgets.QLabel()
                self.flop3.setMinimumSize(QtCore.QSize(53, 65))
                self.flop3.setMaximumSize(QtCore.QSize(53, 80))
                self.flop3.setPixmap(QtGui.QPixmap(self.flop3_card)) # Draw third flop card
                self.flop3.setScaledContents(True)
                if (self.flop3_card == ""):
                        self.flop3.setStyleSheet("border: 0px solid rgb(0,0,0);")
                else:
                        self.flop3.setStyleSheet("border-radius: 10px;\n")
                self.boardLayout.addWidget(self.flop3)
        
        if (show_turn):
                self.turn = QtWidgets.QLabel()
                self.turn.setMinimumSize(QtCore.QSize(53, 65))
                self.turn.setMaximumSize(QtCore.QSize(53, 80))
                self.turn.setPixmap(QtGui.QPixmap(self.turn_card)) # Draw turn
                self.turn.setScaledContents(True)
                if (self.turn_card == ""):
                        self.turn.setStyleSheet("border: 0px solid rgb(0,0,0);")
                else:
                        self.turn.setStyleSheet("border-radius: 10px;\n")
                self.boardLayout.addWidget(self.turn)
        
        if (show_river):
                self.river = QtWidgets.QLabel()
                self.river.setMinimumSize(QtCore.QSize(53, 65))
                self.river.setMaximumSize(QtCore.QSize(53, 80))
                self.river.setPixmap(QtGui.QPixmap(self.river_card)) # Draw river
                self.river.setScaledContents(True)
                if (self.river_card == ""):
                        self.river.setStyleSheet("border: 0px solid rgb(0,0,0);")
                else:
                        self.river.setStyleSheet("border-radius: 10px;\n")
                self.boardLayout.addWidget(self.river)
        
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.boardLayout.addItem(spacerItem17)

        self.gridLayout.addWidget(self.Table, 1, 1, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 40, 221, 151))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.PreDecisionPanel = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.PreDecisionPanel.setContentsMargins(0, 0, 0, 0)
        self.PreDecisionPanel.setSpacing(31)
        self.PreDecisionPanel.setObjectName("PreDecisionPanel")
        self.PreRaise = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.PreRaise.setStyleSheet("color: rgb(255, 255, 255);")
        self.PreRaise.setObjectName("PreRaise")
        self.PreDecisionPanel.addWidget(self.PreRaise)
        self.PreCall = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.PreCall.setStyleSheet("color: rgb(255, 255, 255);")
        self.PreCall.setObjectName("PreCall")
        self.PreDecisionPanel.addWidget(self.PreCall)
        self.PreFold = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.PreFold.setStyleSheet("color: rgb(255, 255, 255);")
        self.PreFold.setObjectName("PreFold")
        self.PreDecisionPanel.addWidget(self.PreFold)
        self.stackedWidget.addWidget(self.page)

        self.DecisionPanel = QtWidgets.QWidget()
        self.DecisionPanel.setObjectName("DecisionPanel")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.DecisionPanel)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.DecisionVLayout = QtWidgets.QVBoxLayout()
        self.DecisionVLayout.setContentsMargins(-1, -1, -1, 10)
        self.DecisionVLayout.setSpacing(0)
        self.DecisionVLayout.setObjectName("DecisionVLayout")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.DecisionVLayout.addItem(spacerItem9)
        self.DecisionHLayout = QtWidgets.QHBoxLayout()
        self.DecisionHLayout.setContentsMargins(-1, -1, -1, 10)
        self.DecisionHLayout.setSpacing(17)
        self.DecisionHLayout.setObjectName("DecisionHLayout")
        self.oneThird = QtWidgets.QPushButton(self.DecisionPanel)
        self.oneThird.setMinimumSize(QtCore.QSize(40, 40))
        self.oneThird.setStyleSheet(stylesheets.button_style)
        self.oneThird.setObjectName("oneThird")
        self.DecisionHLayout.addWidget(self.oneThird, 0, QtCore.Qt.AlignBottom)
        self.oneHalf = QtWidgets.QPushButton(self.DecisionPanel)
        self.oneHalf.setMinimumSize(QtCore.QSize(40, 40))
        self.oneHalf.setStyleSheet(stylesheets.button_style)
        self.oneHalf.setObjectName("oneHalf")
        self.DecisionHLayout.addWidget(self.oneHalf, 0, QtCore.Qt.AlignBottom)
        self.threeQuarter = QtWidgets.QPushButton(self.DecisionPanel)
        self.threeQuarter.setMinimumSize(QtCore.QSize(40, 40))
        self.threeQuarter.setStyleSheet(stylesheets.button_style)
        self.threeQuarter.setObjectName("threeQuarter")
        self.DecisionHLayout.addWidget(self.threeQuarter, 0, QtCore.Qt.AlignBottom)
        self.Pot = QtWidgets.QPushButton(self.DecisionPanel)
        self.Pot.setMinimumSize(QtCore.QSize(40, 40))
        self.Pot.setStyleSheet(stylesheets.button_style)
        self.Pot.setObjectName("Pot")
        
        self.DecisionHLayout.addWidget(self.Pot, 0, QtCore.Qt.AlignBottom)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.DecisionHLayout.addItem(spacerItem8)
        self.DecisionVLayout.addLayout(self.DecisionHLayout)
        self.sliderHLayout = QtWidgets.QHBoxLayout()
        self.sliderHLayout.setContentsMargins(-1, -1, -1, 0)
        self.sliderHLayout.setSpacing(2)
        self.sliderHLayout.setObjectName("sliderHLayout")
        self.slider = QtWidgets.QSlider(self.DecisionPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider.sizePolicy().hasHeightForWidth())
        self.slider.setSizePolicy(sizePolicy)
        self.slider.setMinimumSize(QtCore.QSize(150, 0))
        self.slider.setMaximumSize(QtCore.QSize(150, 16777215))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.sliderHLayout.addWidget(self.slider, 0, QtCore.Qt.AlignTop)
        self.betAmount = QtWidgets.QLineEdit(self.DecisionPanel)
        self.betAmount.setMinimumSize(QtCore.QSize(0, 30))
        self.betAmount.setMaximumSize(QtCore.QSize(50, 16777215))
        self.betAmount.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sliderHLayout.setSpacing(10)
        self.betAmount.setObjectName("betAmount")
        self.sliderHLayout.addWidget(self.betAmount, 0, QtCore.Qt.AlignTop)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.sliderHLayout.addItem(spacerItem9)
        self.DecisionVLayout.addLayout(self.sliderHLayout)
        self.ButtonsPanel = QtWidgets.QHBoxLayout()
        self.ButtonsPanel.setContentsMargins(-1, 20, -1, -1)
        self.ButtonsPanel.setSpacing(33)
        self.ButtonsPanel.setObjectName("ButtonsPanel")

        self.Call = QtWidgets.QPushButton(self.DecisionPanel)
        self.Call.setMinimumSize(QtCore.QSize(50, 40))
        self.Call.setMaximumSize(QtCore.QSize(106, 62))
        self.Call.setStyleSheet(stylesheets.button_style)

        self.Call.setObjectName("Call")
        self.ButtonsPanel.addWidget(self.Call, 0, QtCore.Qt.AlignTop)
        self.Raise = QtWidgets.QPushButton(self.DecisionPanel)
        self.Raise.setMinimumSize(QtCore.QSize(50, 40))
        self.Raise.setMaximumSize(QtCore.QSize(106, 62))
        self.Raise.setStyleSheet(stylesheets.button_style)

        self.Raise.setObjectName("Raise")
        self.ButtonsPanel.addWidget(self.Raise, 0, QtCore.Qt.AlignTop)
        self.Fold = QtWidgets.QPushButton(self.DecisionPanel)
        self.Fold.setMinimumSize(QtCore.QSize(50, 40))
        self.Fold.setMaximumSize(QtCore.QSize(106, 62))
        
        self.Fold.setStyleSheet(stylesheets.button_style)
        self.Fold.setObjectName("Fold")
        self.ButtonsPanel.addWidget(self.Fold, 0, QtCore.Qt.AlignTop|QtCore.Qt.AlignLeft)
        self.DecisionVLayout.addLayout(self.ButtonsPanel)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ButtonsPanel.addItem(spacerItem21)
        self.DecisionVLayout.setStretch(1, 1)
        self.DecisionVLayout.setStretch(3, 1)
        self.horizontalLayout_5.addLayout(self.DecisionVLayout)
        self.stackedWidget.addWidget(self.DecisionPanel)
        self.gridLayout.addWidget(self.stackedWidget, 2, 2, 1, 1)

        self.bottomSeats = QtWidgets.QGridLayout()
        self.bottomSeats.setObjectName("bottomSeats")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottomSeats.addItem(spacerItem10, 0, 4, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottomSeats.addItem(spacerItem11, 0, 0, 1, 1)
        self.Seat6VLayout = QtWidgets.QVBoxLayout()
        self.Seat6VLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.Seat6VLayout.setContentsMargins(-1, 0, -1, 0)
        self.Seat6VLayout.setObjectName("Seat6VLayout")
        self.Seat6HLayout = QtWidgets.QHBoxLayout()
        self.Seat6HLayout.setObjectName("Seat6HLayout")
        self.S6C1 = QtWidgets.QLabel(self.centralwidget)
        self.S6C1.setMinimumSize(MIN_CARD_SIZE)
        self.S6C1.setMaximumSize(MAX_CARD_SIZE)
        if (self.S6Card1 != ""):
                self.S6C1.setStyleSheet("border: 2px solid rgb(0,0,0);\n"
                "border-radius: 10px;\n")
                self.S6C2.setStyleSheet("border: 2px solid rgb(0,0,0);\n"
                "border-radius: 10px;\n")
        self.S6C1.setPixmap(QtGui.QPixmap(self.S6Card1)) # Draw S6C1
        self.S6C1.setScaledContents(True)
        self.S6C1.setObjectName("S6C1")
        self.Seat6HLayout.addWidget(self.S6C1)
        
        self.S6C2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.S6C2.sizePolicy().hasHeightForWidth())
        self.S6C2.setSizePolicy(sizePolicy)
        self.S6C2.setMinimumSize(MIN_CARD_SIZE)
        self.S6C2.setMaximumSize(MAX_CARD_SIZE)
        
        self.S6C2.setPixmap(QtGui.QPixmap(self.S6Card2)) # Draw S6C2
        self.S6C2.setScaledContents(True)
        self.S6C2.setObjectName("S6C2")
        self.Seat6HLayout.addWidget(self.S6C2)

        self.Seat6HLayout.setStretch(0, 1)
        self.Seat6VLayout.addLayout(self.Seat6HLayout)
        self.Seat6Label = QtWidgets.QLabel(self.centralwidget)
        self.Seat6Label.setMinimumSize(MIN_PLAYERLABEL_SIZE)
        self.Seat6Label.setMaximumSize(MAX_PLAYERLABEL_SIZE)
        self.Seat6Label.setStyleSheet(stylesheets.player_label)

        self.Seat6Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Seat6Label.setObjectName("Seat6Label")
        self.Seat6VLayout.addWidget(self.Seat6Label)
        self.Seat6ProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.Seat6ProgressBar.setMinimumSize(PROGRESSBAR_MIN_SIZE)
        self.Seat6ProgressBar.setMaximumSize(PROGRESSBAR_MAX_SIZE)
        self.Seat6ProgressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Seat6ProgressBar.setAutoFillBackground(False)
        self.Seat6ProgressBar.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Seat6ProgressBar.setProperty("value", 24)
        self.Seat6ProgressBar.setTextVisible(False)
        self.Seat6ProgressBar.setObjectName("Seat6ProgressBar")
        self.Seat6VLayout.addWidget(self.Seat6ProgressBar, 0, QtCore.Qt.AlignTop)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Seat6VLayout.addItem(spacerItem12)
        self.bottomSeats.addLayout(self.Seat6VLayout, 0, 3, 1, 1)

        self.Seat1VLayout = QtWidgets.QVBoxLayout()
        self.Seat1VLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.Seat1VLayout.setContentsMargins(-1, 0, -1, 0)
        self.Seat1VLayout.setObjectName("Seat1VLayout")
        self.Seat1HLayout = QtWidgets.QHBoxLayout()
        self.Seat1HLayout.setObjectName("Seat1HLayout")
        self.S1C1 = QtWidgets.QLabel(self.centralwidget)
        self.S1C2 = QtWidgets.QLabel(self.centralwidget)
        self.S1C1.setMinimumSize(MIN_CARD_SIZE)
        self.S1C1.setMaximumSize(MAX_CARD_SIZE)
        if (self.S1Card1 != ""):
                self.S1C1.setStyleSheet("border: 2px solid rgb(0,0,0);\n"
                "border-radius: 10px;\n")
                self.S1C2.setStyleSheet("border: 2px solid rgb(0,0,0);\n"
                "border-radius: 10px;\n")
        self.S1C1.setPixmap(QtGui.QPixmap(self.S1Card1)) # Draw S1C1
        self.S1C1.setScaledContents(True)
        self.S1C1.setObjectName("S1C1")
        self.Seat1HLayout.addWidget(self.S1C1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.S1C2.sizePolicy().hasHeightForWidth())
        self.S1C2.setSizePolicy(sizePolicy)
        self.S1C2.setMinimumSize(MIN_CARD_SIZE)
        self.S1C2.setMaximumSize(MAX_CARD_SIZE)
        self.S1C2.setPixmap(QtGui.QPixmap(self.S1Card2)) # Draw S1C2
        self.S1C2.setScaledContents(True)
        self.S1C2.setObjectName("S1C2")
        self.Seat1HLayout.addWidget(self.S1C2)
        self.Seat1HLayout.setStretch(0, 1)
        self.Seat1VLayout.addLayout(self.Seat1HLayout)
        self.Seat1Label = QtWidgets.QLabel(self.centralwidget)
        self.Seat1Label.setMinimumSize(MIN_PLAYERLABEL_SIZE)
        self.Seat1Label.setMaximumSize(MAX_PLAYERLABEL_SIZE)
        self.Seat1Label.setStyleSheet(stylesheets.player_label)
        self.Seat1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Seat1Label.setObjectName("Seat1Label")
        self.Seat1VLayout.addWidget(self.Seat1Label)
        if self.player_turn == 1:
                self.Seat1ProgressBar = QtWidgets.QProgressBar(self.centralwidget)
                self.Seat1ProgressBar.setMinimumSize(PROGRESSBAR_MIN_SIZE)
                self.Seat1ProgressBar.setMaximumSize(PROGRESSBAR_MAX_SIZE)
                self.Seat1ProgressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.Seat1ProgressBar.setAutoFillBackground(False)
                self.Seat1ProgressBar.setStyleSheet("background-color: rgb(0, 0, 0);")
                self.Seat1ProgressBar.setProperty("value", 24)
                self.Seat1ProgressBar.setTextVisible(False)
                self.Seat1ProgressBar.setObjectName("Seat1ProgressBar")
                self.Seat1VLayout.addWidget(self.Seat1ProgressBar, 0, QtCore.Qt.AlignTop)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Seat1VLayout.addItem(spacerItem13)
        self.bottomSeats.addLayout(self.Seat1VLayout, 0, 1, 1, 1)

        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottomSeats.addItem(spacerItem14, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.bottomSeats, 2, 1, 1, 1)

        self.Seat5 = QtWidgets.QGridLayout()
        self.Seat5.setContentsMargins(-1, -1, 0, -1)
        self.Seat5.setObjectName("Seat5")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Seat5.addItem(spacerItem15, 0, 1, 1, 1)
        self.Seat5VLayout = QtWidgets.QVBoxLayout()
        self.Seat5VLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.Seat5VLayout.setContentsMargins(-1, 0, -1, 0)
        self.Seat5VLayout.setObjectName("Seat5VLayout")
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Seat5VLayout.addItem(spacerItem16)
        self.Seat5HLayout = QtWidgets.QHBoxLayout()
        self.Seat5HLayout.setObjectName("Seat5HLayout")

        self.S5C1 = QtWidgets.QLabel(self.centralwidget)
        self.S5C2 = QtWidgets.QLabel(self.centralwidget)
        self.S5C1.setMinimumSize(MIN_CARD_SIZE)
        self.S5C1.setMaximumSize(MAX_CARD_SIZE)
        if (self.S5Card1 != ""):
                self.S5C1.setStyleSheet("border: 2px solid rgb(0,0,0);\n"
                "border-radius: 10px;\n")
                self.S5C2.setStyleSheet("border: 2px solid rgb(0,0,0);\n"
                "border-radius: 10px;\n")
        self.S5C1.setPixmap(QtGui.QPixmap(self.S5Card1)) # Draw S5C1
        self.S5C1.setScaledContents(True)
        self.S5C1.setObjectName("S5C1")
        self.Seat5HLayout.addWidget(self.S5C1)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.S5C2.sizePolicy().hasHeightForWidth())
        self.S5C2.setSizePolicy(sizePolicy)
        self.S5C2.setMinimumSize(MIN_CARD_SIZE)
        self.S5C2.setMaximumSize(MAX_CARD_SIZE)       
        self.S5C2.setPixmap(QtGui.QPixmap(self.S5Card2)) # Draw S5C2
        self.S5C2.setScaledContents(True)
        self.S5C2.setObjectName("S5C2")
        self.Seat5HLayout.addWidget(self.S5C2)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Seat5HLayout.addItem(spacerItem17)
        self.Seat5HLayout.setStretch(0, 0)
        self.Seat5VLayout.addLayout(self.Seat5HLayout)
        self.Seat5Label = QtWidgets.QLabel(self.centralwidget)
        self.Seat5Label.setMinimumSize(MIN_PLAYERLABEL_SIZE)
        self.Seat5Label.setMaximumSize(MAX_PLAYERLABEL_SIZE)
        self.Seat5Label.setStyleSheet(stylesheets.player_label)
        self.Seat5Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Seat5Label.setObjectName("Seat5Label")
        self.Seat5VLayout.addWidget(self.Seat5Label)
        self.Seat5ProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.Seat5ProgressBar.setMinimumSize(PROGRESSBAR_MIN_SIZE)
        self.Seat5ProgressBar.setMaximumSize(PROGRESSBAR_MAX_SIZE)
        self.Seat5ProgressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Seat5ProgressBar.setAutoFillBackground(False)
        self.Seat5ProgressBar.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Seat5ProgressBar.setProperty("value", 24)
        self.Seat5ProgressBar.setTextVisible(False)
        self.Seat5ProgressBar.setObjectName("Seat5ProgressBar")
        self.Seat5VLayout.addWidget(self.Seat5ProgressBar, 0, QtCore.Qt.AlignTop)
        self.Seat5.addLayout(self.Seat5VLayout, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.Seat5, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Seat2Label.setText(_translate("MainWindow", "PlayerName\n"
"$1000"))
        self.Seat4Label.setText(_translate("MainWindow", "PlayerName\n"
"$1000"))
        self.Seat3Label.setText(_translate("MainWindow", "PlayerName\n"
"$1000"))
        self.SendButton.setText(_translate("MainWindow", "Send"))
        self.Table.setText(_translate("MainWindow", "No-Limit Holdem\n"
"($1/$2) 6-Max"))
        self.PreRaise.setText(_translate("MainWindow", "Raise Any"))
        self.PreCall.setText(_translate("MainWindow", "Call"))
        self.PreFold.setText(_translate("MainWindow", "Fold"))
        self.oneThird.setText(_translate("MainWindow", "1/3"))
        self.oneHalf.setText(_translate("MainWindow", "1/2"))
        self.Pot.setText(_translate("MainWindow", "Pot"))
        self.threeQuarter.setText(_translate("MainWindow", "3/4"))
        self.Call.setText(_translate("MainWindow", "Call"))
        self.Raise.setText(_translate("MainWindow", "Raise"))
        self.Fold.setText(_translate("MainWindow", "Fold"))
        self.Seat6Label.setText(_translate("MainWindow", "PlayerNamePlayerName\n"
"$1000"))
        self.Seat1Label.setText(_translate("MainWindow", "PlayerName\n"
"$1000"))
        self.Seat5Label.setText(_translate("MainWindow", "PlayerName\n"
"$1000"))

    