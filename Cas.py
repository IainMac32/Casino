import colorama
from colorama import Fore, Back, Style
import random
import time

Ppoints = int(200)
Pbet = int(0)


def betwin13():
  global Ppoints
  Ppoints = Pbet * 13 + Ppoints
  print("you now have",Ppoints,"points")
def betwin():
  global Ppoints
  Ppoints += Pbet
  print(Fore.WHITE + "you now have",Ppoints,"points")
def betlose():
  global Ppoints
  Ppoints -= Pbet
  print(Fore.WHITE + "you now have",Ppoints,"points")


def BlackJack():
  #making the deck
  cards = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
  
    
  deck = []
  for i in range(1,14):
    for y in cards:
      deck.append([i,y])

  random.shuffle(deck)
  
  #K Q J and A are all = 10 so I need to fix this
  for i in range(1,14):
    if deck[i][0] > 10:
      deck[i][0] = 10

  global Pbet
  global Ppoints
  global betwin
  global betlose
  global menu
  print("Place Bet, your balance is", Ppoints)
  Pbet = int(input())
  while Pbet <= 0 or Pbet > Ppoints:
    print("Too high/low, please enter bet again")
    Pbet = int(input())
  print(Fore.GREEN + "your bet is", Pbet, Style.RESET_ALL)
  print("")
  print(Fore.BLUE + "PLAYER HAND")
  print(deck[1])
  print(deck[2])
  
  hand1 = deck[1][0]+deck[2][0]
  print(hand1, Style.RESET_ALL)
  
  print("==============")
  
  print(Fore.RED + "DEALER HAND")
  print(deck[10])
  #print(deck[11])
  
  dealer = deck[10][0]
  
  hit = 2
  
  while hand1 < 22:
    print(Style.RESET_ALL)
    print("hit or stand?")
    answer1 = input()
    if answer1 == 'hit':
      hit = hit + 1
      print(Fore.BLUE + "PLAYER HAND")
      print(deck[1])
      print(deck[2])
      print(deck[3])
      if hit > 3:
        print(deck[4])
      if hit > 4:
        print(deck[5])
      hand1 = hand1 + deck[hit][0]
      print(hand1)
    elif answer1 == 'stand':
      break
  
  Ddeal = 10
  while dealer < 16 and hand1 < 22:
    Ddeal = Ddeal + 1
    print(Fore.RED + "DEALER HAND")
    print(deck[10])
    print(deck[11])

    if Ddeal > 11:
      print(deck[12])
    if Ddeal > 12:
      print(deck[13])
    if Ddeal > 13:
      print(deck[14])
  
    dealer = dealer + deck[Ddeal][0]
    print(dealer)
    time.sleep(2)

  print(Style.RESET_ALL)
  print(Fore.BLUE + "Your total is", hand1)
  print(Fore.RED + "The dealers total is", dealer)
  print("")
  if hand1 > 21:
    print(Fore.RED +  "DEALER WINS")
    betlose()

  elif dealer > 21:
    print(Fore.BLUE + "PLAYER WINS")
    betwin()

  elif hand1 > dealer:
    print(Fore.BLUE + "PLAYER WINS")
    betwin()

  elif dealer > hand1:
    print (Fore.RED + "DEALER WINS")
    betlose()

  else:
    print(Fore.WHITE +"TIE")
  print(Fore.WHITE + "")
  print("to play again press 1")
  print("to return to menu press 2")
  answer = int(input())
  if answer == 1:
    BlackJack()
  elif answer == 2:
    menu()
  

def Roulette():
  global Pbet
  global Ppoints
  global betwin
  global betlose
  global menu
  print("Place Bet, your balance is", Ppoints)
  Pbet = int(input())
  while Pbet <= 0 or Pbet > Ppoints:
    print("Too high/low, please enter bet again")
    Pbet = int(input())
  print(Fore.GREEN + "your bet is", Pbet, Style.RESET_ALL)
  print("")
  print(Fore.RED + "1 2 3 4 5 6",Fore.WHITE + "7 8 9 10 11 12",Fore.GREEN + "13")
  print(Fore.WHITE + "please bet on a colour")
  colo = input()

  while colo != "green" and colo != "white" and colo != "red":
    print("please guess again")
    colo = input()
  
  sleep = 0.05
  
  for i in range(0,54): 
    ran = random.randint(1,13)
    if ran < 7:
      print(Fore.RED)
    elif ran > 6 and ran < 13:
      print(Fore.WHITE)
    elif ran == 13:
      print(Fore.GREEN )
    print(ran)
    if i > 35:
      sleep += 0.10
    time.sleep(sleep)

  if colo == "green" and ran == 13:
    print("you win 13x")
    print("")
    betwin13()
  elif colo == "red" and ran < 7:
    print("you win 2x (red)")
    print("")
    betwin()

  elif colo == "white" and ran > 6 and ran < 13:
    print("you win 2x white")
    print("")
    betwin()

  else:
    print("")
    print(Fore.RED + "YOU LOSE")
    betlose()
  print("")
  print("press 1 to play again")
  print("press 2 to go back to menu")
  answer = int(input())
  if answer == 1:
    Roulette()
  elif answer == 2:
    menu()


def search(list, numb):
  for i in range(len(list)):
    if list[i] == numb:
        return True
  return False

def mines():
  global search
  global Ppoints
  global Pbet
  global guesses
  guesses = []
  multi = 0

  mine1 = 1
  mine2 = 2
  mine3 = 3
  mine4 = 4
  mine5 = 5
  mine6 = 6
  mine7 = 7
  mine8 = 8
  mine9 = 9
  
  print("Place Bet, your balance is", Ppoints)
  Pbet = int(input())
  while Pbet <= 0 or Pbet > Ppoints:
    print("Too high/low, please enter bet again")
    Pbet = int(input())
  print(Fore.GREEN + "your bet is", Pbet, Style.RESET_ALL)
  print("")

  RN = random.randint(1,9)

  
  print("Pick a box each box is worth 0.2x your earnings")
  print("but watch out there is a secret mine that")
  print("will make you lose all your money")
  print("")
  def MineChart():
    print(Fore.MAGENTA + "[",mine1,Fore.MAGENTA + "]","[",mine2,Fore.MAGENTA + "]","[",mine3,Fore.MAGENTA + "]")
    print("[",mine4,Fore.MAGENTA + "]","[",mine5,Fore.MAGENTA + "]","[",mine6,Fore.MAGENTA + "]")
    print("[",mine7,Fore.MAGENTA + "]","[",mine8,Fore.MAGENTA + "]","[",mine9,Fore.MAGENTA + "]")
    print(Style.RESET_ALL)
  MineChart()
    
  print("What number?")
  numb = int(input())
  while numb > 9 or numb < 1:
    print("Please enter valid number")
    numb = int(input())


  while RN != numb:
    if mine1 == numb:
      mine1 = Fore.GREEN + '$'
    if mine2 == numb:
      mine2 = Fore.GREEN + '$'
    if mine3 == numb:
      mine3 = Fore.GREEN + '$'
    if mine4 == numb:
      mine4 = Fore.GREEN + '$'
    if mine5 == numb:
      mine5 = Fore.GREEN + '$'
    if mine6 == numb:
      mine6 = Fore.GREEN + '$'
    if mine7 == numb:
      mine7 = Fore.GREEN + '$'
    if mine8 == numb:
      mine8 = Fore.GREEN + '$'
    if mine9 == numb:
      mine9 = Fore.GREEN + '$'

    
    if search(guesses,numb):
      print("number found already")
      print("guess another number")
      numb = int(input())
    else:
      print("")
      guesses.append(numb)
      multi += float(0.2)
      print("Multiplier:", round(multi,2))
      print("Winnings:",round(Pbet * multi,2))
      MineChart()
      print("Pick another number or type 0 to cashout")
      numb = int(input())
      
    while numb > 9 or numb < 0:
      print("Please enter valid number")
      numb = int(input())
    if numb == 0:
      print("")
      print(Fore.GREEN + "YOU WON:", Pbet * multi, "POINTS", Style.RESET_ALL)
      Ppoints += Pbet * multi
      print("You now have", Ppoints, "points")
      print("")
      print("press 1 to play again")
      print("press 2 to go back to menu")
      answer = int(input())
      if answer == 1:
        mines()
      elif answer == 2:
        menu()


  #making the number that is bomb to x
  if mine1 == numb:
    mine1 = Fore.RED + 'X'
  if mine2 == numb:
    mine2 = Fore.RED + 'X'
  if mine3 == numb:
    mine3 = Fore.RED + 'X'
  if mine4 == numb:
    mine4 = Fore.RED + 'X'
  if mine5 == numb:
    mine5 = Fore.RED + 'X'
  if mine6 == numb:
    mine6 = Fore.RED + 'X'
  if mine7 == numb:
    mine7 = Fore.RED + 'X'
  if mine8 == numb:
    mine8 = Fore.RED + 'X'
  if mine9 == numb:
    mine9 = Fore.RED + 'X'
      
  MineChart()
  print(Fore.RED + "YOU LOSE", Style.RESET_ALL)
  Ppoints -= Pbet
  print("total points is", Ppoints)
  print("")
  print("press 1 to play again")
  print("press 2 to go back to menu")
  answer = int(input())
  if answer == 1:
    mines()
  elif answer == 2:
    menu()


def menu():
  print(Back.GREEN + "    CASINO   ", Back.RESET + Style.RESET_ALL)
  print("1 = BlackJack")
  print("2 = Roulete")
  print("3 = Mines")
  
  game = int(input())
  print(game)
  if game == 1:
    BlackJack()
  elif game == 2:
    Roulette()
  elif game == 3:
    mines()

menu()
