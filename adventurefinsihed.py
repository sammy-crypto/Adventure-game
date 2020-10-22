#--imports
import random
import time
#--function

def start_room():
    start_room_options = ["1","2","3"]
    choice =""
    while choice not in start_room_options:
        print("You enter a room and there is are three foods sitting on the table, an apple, another " +
          "apple, and a third apple, which apple you want? \nApple number 1 \nApple number 2\nApple number 3")
        choice = str(input("Pick: "))
    print("You picked " + choice)
    if choice == start_room_options[0]:
        room01()
    elif choice == start_room_options[1]:
        room02()
    elif choice == start_room_options[2]:
        room03()

def room01():
    print("\n\nYou shat in your pants from this apple")
    time.sleep(3)
    room1options = ["1","2"]
    room1_choice =""
    while room1_choice not in room1options:
        print("Do you want to 1)Go all the way home and change pants or 2)Try to wipe the shit out of your pants "
               + "with a paper towel")
        room1_choice =  str(input("Pick: "))
    print("You picked " + room1_choice)
    if room1_choice == room1options[0]:
        room11()
    elif room1_choice == room1options[1]:
        room12()
def room11():
    print("You made it home but your boss calls and says you need to get to work asap")
    time.sleep(3)
    room11_options = ["1", "2"]
    room11_choice =""
    while room11_choice not in room11_options:
        print("Do you 1)rush to work or 2)call in sick.")
        room11_options = str(input("Pick: "))
    print("You picked " + room11_choice)
    time.sleep(3)
    if room11_choice == room11_options[0]:
        room21()
    elif room11_choice == room11_options[1]:
        roomend()
def room12():
    print("A coworker caught you wiping and posted the video on instagram")
    time.sleep(3)
def room02():
    print("\n\nYou enjoyed this apple")
    time.sleep(3)
    room02_options = ["1", "2"]
    room2choice =""
    while room2choice not in room02_options:
        print("You loved the apple so much you want another one, do you 1)Drive to the store and get a new apple, "
              "or 2)Just eat one of the other apples off the table")
        room2choice = str(input("Pick: "))
    print("You picked " + room2choice)
    if room2choice == room02_options[1]:
        room22()
    elif room2choice == room02_options[0]:
        room21()
def room21():
    print("You run out of gas on the way and pull over to a hardware store")
    time.sleep(3)
    room21_options = ["1","2"]
    room21choice =""
    while room21choice not in room21_options:
        print("A large man aproaches you and offers you a ride home, do you 1)Get in the car with him "
              "2)or politely decline and walk 12 miles home")
        room21choice = str(input("Pick: "))
    print("You picked " + room21choice)
    if room21choice == room21_options[0]:
        room211()
    elif room21choice == room21_options[1]:
        room222()
def room211():
    print("You got raped and thrown out on the side of the road.")
    time.sleep(3)
    room211_options = ["1","2"]
    room211choice = ""
    while room211choice not in room211_options:
        print("You see a Grandma on the side of the road carrying a baby with 1,000,000 dollars. Do you "
              + "1)Beat the shit out of them or 2)Die")
        room211choice = str(input("Pick: "))
    print("You picked: " + room211choice)
    if room211choice == room211_options[0]:
        print("You get away with the money and live as a millionaire. The end")
        time.sleep(7)
def room222():
    print("You slip on a pebble walking along the highway and get runover and die, The End")
    time.sleep(7)
def room22():
    print("You pick apple number 1 and shit yourself")
    time.sleep(3)
    room01()

def room03():
    print("\n\nYou died from the poison apple")
    time.sleep(5)
def roomend():
    print("Your boss found out you were faking and fired you , The End.")
    time.sleep(7)


start_room()
