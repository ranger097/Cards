#list of imports
import random , itertools
import curses
from curses import wrapper
import time

#main function
def gameloop(stdscr):
    stdscr.clear()
    rounds = 0
    score = 0
    legend = 0
    risk = 0
    money = 100
    
    #function to handle risk. There has to be a better way to do this fr.
    def  cardValueTotals(face):
        if face in ("J","Q","K"):
            return 10
        elif face == "A":
            return 11
        else: 
            return int(face)

    #welcome page
    stdscr.addstr(0,0,"Welcome to the Blackjack table!!!")
    stdscr.addstr(2,0,"Press 1 to continue")
    stdscr.refresh()
    key = stdscr.getch()
    
    #rules page
    if key == ord('1'):
        stdscr.clear()
        stdscr.addstr(0,0,"Alright Kidd the rules are simple.")
        stdscr.addstr(2,0,"First or closest to 21 wins")
        stdscr.addstr(4,0,"Buts theres a catch!!!")
        stdscr.addstr(6,0,"This game is about risk tolerance")
        stdscr.addstr(8,0,"So if you want to become a legend in this casino...")
        stdscr.addstr(10,0,"You are gonna need to take some pretty HIGH risk")
        stdscr.addstr(12,0,"Press 1 Kidd, lets see if you got what it takes!!")
        stdscr.refresh()
        key = stdscr.getch()
        
    #game loop
    if key == ord('1'):
        while rounds <= 2:
            stdscr.clear()
        
            #dictonary of suits
            x = {
                "H":"Hearts",
                "D":"Diamonds",
                "C":"Clubs",
                "S":"Spades"
                }
    
            #dictonary of numbers and face cards
            y = {
                "A":"Ace",
                "2":"2",
                "3":"3",
                "4":"4",
                "5":"5",
                "6":"6",
                "7":"7",
                "8":"8",
                "9":"9",
                "J":"Jack",
                "Q":"Queen",
                "K":"King"
                }

            #this makes an iterative list of the keys from both x and y dictionaries simulating all cards in a deck
            deck = list(itertools.product(y.keys(),x.keys()))
    
            #shuffles the deck but at this stage its just the pairs of keys being shuffled
            random.shuffle(deck)

            #this gives us a random pair of keys from the deck that were shuffled
            #might be overkill but each person can on have 5 cards per game of blackjack so we have 10 cards.
    
            card1 = deck.pop()
            card2 = deck.pop()
            card3 = deck.pop()
            card4 = deck.pop()
            card5 = deck.pop()
            card6 = deck.pop()
            card7 = deck.pop()
            card8 = deck.pop()
            card9 = deck.pop()
            card10 = deck.pop()
    
    
            #this is a formated string that takes the keys that were shuffled and gives us the value of both and then we format it like "The king of Spades"
            a = f"The {y[card1[0]]} of {x[card1[1]]}"
            b = f"The {y[card2[0]]} of {x[card2[1]]}"
            c = f"The {y[card3[0]]} of {x[card3[1]]}"
            d = f"The {y[card4[0]]} of {x[card4[1]]}"
            e = f"The {y[card5[0]]} of {x[card5[1]]}"
            f = f"The {y[card6[0]]} of {x[card6[1]]}"
            g = f"The {y[card7[0]]} of {x[card7[1]]}"
            h = f"The {y[card8[0]]} of {x[card8[1]]}"
            i = f"The {y[card9[0]]} of {x[card9[1]]}"
            j = f"The {y[card10[0]]} of {x[card10[1]]}"
        
            
            
            #keeps track of the cards and values of hits the player takes
            risk_value1 = cardValueTotals(card1[0]) + cardValueTotals(card2[0])
            risk_value2 = risk_value1 + cardValueTotals(card3[0])
            risk_value3 = risk_value2 + cardValueTotals(card4[0])
            risk_value4 = risk_value3 + cardValueTotals(card5[0])
            
            def tolerance(nums):
               if nums <= 11:
                   return stdscr.addstr(2,0, "no risk")
               elif nums > 11 and nums <= 16:
                   return stdscr.addstr(2,0, "Medium Risk")
               elif nums > 16 and nums <= 20:
                   return stdscr.addstr(2,0, "High Risk")
               elif nums == 21:
                   return stdscr.addstr(2,0, "Blackjack")
               elif nums > 21:
                   return stdscr.addstr(2,0, "Bust")
               
               
            #main game logic will be written here 
            #we need a money system, rounds, bets, UI, dealer banter, redemptions, and legendary mode
               
               
               
               
               
               
               
               
               
            
            #keeps track of the rounds but also how many times the game loops
            rounds+=1
            time.sleep(1)
        
       
        
        

wrapper(gameloop)
