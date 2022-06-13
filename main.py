#Import the required Libraries

from deck import Deck
from HandChecker import HandChecker
from Player import Player
import time, sys
#from GUIController import GameWindowController  
from gameWindow import Ui_MainWindow  # importing our generated file
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer, QThread
from LinkedList import SLinkedList, Node

def update_screen():
    # timer = QTimer()
    # timer.setInterval(1000)
    # timer.timeout.connect(self.recurring_timer)
    # timer.start()
    #QApplication.processEvents()
    ui.setupUi(MainWindow)
    time.sleep(1.5)
    


def find_winner():
    print("Show the winner...")
    hero_node = players.head
    hero = hero_node.dataval
    villain_node = players.head.next
    villain = villain_node.dataval
    split_pot = [hero]
    end = False
    global score_to_beat, player_hand_images
    
    # Draw each opponents hand face up and score the hands
    while(not end):
        # Remove hero cards from exposed cards list
        del deck.exposed_cards[0]
        del deck.exposed_cards[0]
     
        # Add villain card to exposed cards list
        deck.exposed_cards.insert(0, villain.card1)
        deck.exposed_cards.insert(0, villain.card2)
        
        # Read the new hand
        villain_hand_checker = HandChecker(deck.all_cards, deck.exposed_cards)
        villain_score = villain_hand_checker.identify_hand()
        del villain_hand_checker

        # Compare current score to previous winner's score
        for index in range(len(min(villain_score, score_to_beat))):
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
        player_hand_images[villain.seat - 1] = villain_hand
        ui = Ui_MainWindow(flop, turn, river, -1, *player_hand_images) 
        # Check if villain node is last node, if not, move villain node, else end
        if (villain_node.next is not None):
            villain_node = villain_node.next
            villain = villain_node.dataval
        else: 
            end = True

        # Update UI 
        ui.setupUi(MainWindow)
        #update_screen()
    
    if (len(split_pot) > 0):
        for i in split_pot:
            print("split between seats", i+1)
    else:
        print("Seat", hero.seat, "wins")
        

if __name__ == '__main__':
    pot_amount = 3.00
    bet_amount = 2.00
    # Button Functions
    #FIXME temporary place holder for find_winner() function
    def _send_clicked():
        find_winner()
    def _oneThird_clicked():
        if (pot_amount < 6.00):
            bet_amount = 2.00
        else:
            bet_amount = pot_amount * 0.33
        ui.betAmount.setText('$' + str(bet_amount))
        
    def _oneHalf_clicked():
        if (pot_amount < 6.00):
            bet_amount = 2.00
        else:
            bet_amount = pot_amount * 0.5
        ui.betAmount.setText('$' + str(bet_amount))
        
    def _threeQuarter_clicked():
        bet_amount = pot_amount * 0.75
        ui.betAmount.setText('$' + str(bet_amount))
        print("clicked")
        
    
    def _pot_clicked():
        bet_amount = pot_amount
        ui.betAmount.setText('$' + str(bet_amount))

    def _change_bet(value):
        ui.betAmount.setText('$' + str(value))

    def _call_clicked():
        global hero_pos
        
        if hero_pos < num_players:
            ui.player_turn += 1
            hero_pos += 1 
        else:
            ui.player_turn = 1
            hero_pos = 1

        # Update UI 
        ui.setupUi(MainWindow)
        update_screen()

        print("clicked")
        print(hero_pos)
    
        

    flop = ["","",""]
    turn = ""
    river = ""
    player_hand_images = []
    # Initialize the deck
    deck = Deck.get_deck()
    # Initialize HandChecker object
    hero_hand_checker = HandChecker(deck.all_cards, deck.exposed_cards)
    
    # Initialize players
    num_players = 4
    SB_pos = 1
    hero_pos = SB_pos

    players = SLinkedList()
    players.head = Node(Player(True, SB_pos))
    player_hand_images.append(players.head.dataval.create_hand_images())
    for i in range(1, num_players):
        new_player = Player(False, i+1)
        players.add_node(new_player)
        player_hand_images.append(new_player.create_hand_images())
    
    # Draw the flop
    flop = deck.draw_flop()

    # Draw the turn
    turn = deck.draw_one()

    # Draw the river
    river = deck.draw_one()
     
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    print(player_hand_images)
    ui = Ui_MainWindow(flop, turn, river, SB_pos, *player_hand_images)
                              
    ui.setupUi(MainWindow)

    # Link buttons to functions
    ui.SendButton.clicked.connect(_send_clicked) 
    ui.oneThird.clicked.connect(_oneThird_clicked)
    ui.oneHalf.clicked.connect(_oneHalf_clicked)
    ui.threeQuarter.clicked.connect(_threeQuarter_clicked)
    ui.Pot.clicked.connect(_pot_clicked)
    ui.Call.clicked.connect(_call_clicked)
    
    ui.slider.setMaximum(players.head.dataval.stack_size)
    ui.slider.valueChanged.connect(_change_bet)    

    score_to_beat = hero_hand_checker.identify_hand()
    
    MainWindow.show()
    sys.exit(app.exec_())

