from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QProgressBar, QLineEdit, QPushButton, QTextEdit, QStackedWidget, QRadioButton
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPixmap
import sys
from LinkedList import SLinkedList, Node
from Player import Player
from deck import Deck


class UI(QMainWindow):

    # Initialize function

    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("gameWindow.ui", self)
        self.numPlayers = 6
        num_players_hidden = 6 - self.numPlayers

        # Define our Widgets
        # Seat labels
        self.Seat1Label = self.findChild(QLabel, "Seat1Label")
        self.Seat2Label = self.findChild(QLabel, "Seat2Label")
        self.Seat3Label = self.findChild(QLabel, "Seat3Label")
        self.Seat4Label = self.findChild(QLabel, "Seat4Label")
        self.Seat5Label = self.findChild(QLabel, "Seat5Label")
        self.Seat6Label = self.findChild(QLabel, "Seat6Label")

        # Only show players that are in the game
        player_labels = [self.Seat1Label, self.Seat2Label, self.Seat3Label, self.Seat4Label, self.Seat5Label, self.Seat6Label]
        for i in range(len(player_labels)):
            player_labels[i].hide()

        for i in range(1, num_players_hidden): 
            player_labels.pop(-i)
            print(len(player_labels))
        for i in range(len(player_labels) - 1):
            player_labels[i].show()
        
        if self.numPlayers == 6:
            player_labels[5].show()

        # Cards
        self.cards = [self.findChild(QLabel, "S1C1"),
                      self.findChild(QLabel, "S1C2"),
                      self.findChild(QLabel, "S2C1"),
                      self.findChild(QLabel, "S2C2"),
                      self.findChild(QLabel, "S3C1"),
                      self.findChild(QLabel, "S3C2"),
                      self.findChild(QLabel, "S4C1"),
                      self.findChild(QLabel, "S4C2"),
                      self.findChild(QLabel, "S5C1"),
                      self.findChild(QLabel, "S5C2"),
                      self.findChild(QLabel, "S6C1"),
                      self.findChild(QLabel, "S6C2")]

        
            
        # Progressbars
        self.progress_bars = [self.findChild(QProgressBar, "Seat1ProgressBar"),
                             self.findChild(QProgressBar, "Seat2ProgressBar"),
                             self.findChild(QProgressBar, "Seat3ProgressBar"),
                             self.findChild(QProgressBar, "Seat4ProgressBar"),
                             self.findChild(QProgressBar, "Seat5ProgressBar"),
                             self.findChild(QProgressBar, "Seat6ProgressBar") ]

        # Table        
        self.Table = self.findChild(QLabel, "Table")

        # Hide all progress bars initially
        self.progress_bars[0].hide()
        self.progress_bars[1].hide()
        self.progress_bars[2].hide()
        self.progress_bars[3].hide()
        self.progress_bars[4].hide()
        self.progress_bars[5].hide()

        self.SendButton = self.findChild(QPushButton, "SendButton")
        self.CallButton = self.findChild(QPushButton, "Call")
        self.RaiseButton = self.findChild(QPushButton, "Raise")
        self.FoldButton = self.findChild(QPushButton, "Fold")

        self.betAmountEdit = self.findChild(QLineEdit, "betAmount")

        # Click Buttons
        self.SendButton.clicked.connect(self.find_winner)
        self.CallButton.clicked.connect(self.call_clicked)
        self.RaiseButton.clicked.connect(self.raise_clicked)


        self.flopCards = ["","",""]
        self.turnCard = ""
        self.riverCard = ""
        self.player_hand_images = []
        
        # Initialize the deck
        self.deck = Deck.get_deck()
        
        # Other Values
        self.potAmount = 3.00
        self.callAmount = 2.00
        
        self.betAmountEdit.setText(str(self.potAmount))
        self.SB_pos = 2
        self.player_turn = self.SB_pos
        
        
        # Create Linked List of Players
        self.players = SLinkedList()
        self.players.head = Node(Player(True, self.SB_pos))
        self.player_hand_images.append(self.players.head.dataval.create_hand_images())
        for i in range(1, self.numPlayers):
            new_player = Player(False, i+1)
            self.players.add_node(new_player)
            self.player_hand_images.append(new_player.create_hand_images())
            
        
        # Assign Pixmaps
        for hand in self.player_hand_images:
            for card in hand:
                pass
        # Show the App
        self.next_turn()
        self.show()
    
    def call_clicked(self):
        self.potAmount += self.callAmount
        self.betAmountEdit.setText(str(self.potAmount))
        self.next_turn()

    def raise_clicked(self):
        self.find_winner()

    def next_turn(self):

        if self.player_turn == 1:
            self.progress_bars[0].show()
            self.progress_bars[5].hide()
        elif self.player_turn == 2:
            self.progress_bars[1].show()
            self.progress_bars[0].hide()
        elif self.player_turn == 3:
            self.progress_bars[2].show()
            self.progress_bars[1].hide()
        elif self.player_turn == 4:
            self.progress_bars[3].show()
            self.progress_bars[2].hide()
        elif self.player_turn == 5:
            self.progress_bars[4].show()
            self.progress_bars[3].hide()
        elif self.player_turn == 6:
            self.progress_bars[5].show()
            self.progress_bars[4].hide()
        else:
            self.player_turn = 1
            self.progress_bars[0].show()
            self.progress_bars[5].hide()

        self.player_turn += 1


    def find_winner(self):
        print("Show the winner...")


        hero_node = self.players.head
        hero = hero_node.dataval
        villain_node = self.players.head.next
        villain = villain_node.dataval
        split_pot = [hero]
        end = False
        score_to_beat = hero.determine_hand_rank()
        
        # Draw each opponents hand face up and score the hands
        while(not end):
            # Remove hero cards from exposed cards list
            del self.deck.exposed_cards[0]
            del self.deck.exposed_cards[0]
        
            # Add villain card to exposed cards list
            self.deck.exposed_cards.insert(0, villain.card1)
            self.deck.exposed_cards.insert(0, villain.card2)
            
            hero_score = hero.determine_hand_rank()
            # Read the new hand
            villain_score = villain.determine_hand_rank()

            # Compare current score to previous winner's score
            for index in range(len(min(villain_score, hero_score))):
                # If hero wins
                if (score_to_beat[index] > villain_score[index]):
                    split_pot.clear()
                    break 
                # If villain wins
                elif (score_to_beat[index] < villain_score[index]):
                    score_to_beat = villain_score
                    hero_node = villain_node
                    hero = hero_node.dataval
                    split_pot.clear()
                    break
                else:
                    index += 1
                    if (index >= len(min(score_to_beat, villain_score))):
                        split_pot.append(villain)
                        print("Split Pot")
                        break
            
            if (not villain.auto_muck or score_to_beat == villain_score):
                villain.faceup = True
            else:
                #pass fold animation
                pass
            villain_hand = villain.create_hand_images()
            self.player_hand_images[villain.seat - 1] = villain_hand

            
         
            # Check if villain node is last node, if not, move villain node, else end
            if (villain_node.next is not None):
                villain_node = villain_node.next
                villain = villain_node.dataval
            else: 
                end = True

        
        if (len(split_pot) > 0):
            for i in split_pot:
                print("split between seats", i+1)
        else:
            print("Seat", hero.seat, "wins")
    

# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
