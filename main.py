# Night at the Supermarket
# A game created by Tyler Bifolchi
# Based on Night Trap and Five Nights at Freddys

import os        #This is HEAVILY needed for wiping the damn screen every 5 seconds
import random       # We need the random library for the random passcode generator
import time       # We need the time library to build our sleep function
from sys import platform

#This little routine here is responsible for checking what operating system the game is running on, it denies access to MacOS and Linux users since the cls command only works on Windows. COMMENT THIS CODE OUT IF YOU ARE RUNNING THIS ON REPLIT
if platform == "linux" or platform == "macOS": #Is the computer linux or mac?
  print("Sorry! This program only works on computers running Microsoft Windows.") #Deny access
  input()
  exit()      #And exit

# This is the introduction text provided to the reader at the beginning of execution. I decided to store it in a variable to free up some space
introtext = "You wake up in a dark room.\n\nYou have no idea where you are, but you feel yourself sitting on a rather uncomfortable chair.\n\nSoon enough, the memories come back to you: you fell asleep again during your break, but now its too late.\n\nThe supermarket is closed, and they locked you inside. It's up to you to find a way out.\nWARNING! THIS GAME IS EXTREMELY CASE SENSITIVE!"

global firstcode, secondcode, thirdcode, fourthcode #Make these global because they are EVERYWHERE!
firstcode = 0        # The first door code is stored here
secondcode = 0      #Second door code is stored here
thirdcode = 0      #Third door code is stored here
fourthcode = 0       #Fourth door code is stored here
command = 0        # This variable is part of the command looping mechanism

password = ""

#Set the counter variable to global, so it can be used anywhere
global counter 
counter = "Off"  #The variable determines whether the Emergency Room is unlocked or not (Pretty much unused)
print (introtext)      # Print the beginning text at startup

commands = ["Look around", "Move to next area"]
#Make a command list for each room

#These variables control the various doors needed to exit the store. True is the equivelent of that door being locked. In this case, at the beginning, all doors are locked.
firstdoor = True
seconddoor = True
thirddoor = True
fourthdoor = True

# These variables are for the random number generator that each clue gives the player
# This is mostly just to avoid players cheating by looking at the source code
look = 0
Start = 0
Stop = 50
limit = 4

#These variables are for the Look around events, so the game avoids looping over and over and crashing
searched = "off"
searchedhall = "off"

gamestarted = 0  #This variable checks if the game has started or not. It will be set to 1, which means the game is currently running

global took   #Make a global variable. It will be used to store which item the player  took from the Storage Room

took = "Nothing to use"     #This is set to NULL since an item has not been selected yet

global security #Security marks whether the Security System is working or not, this will be on by default at the start, but the player can use a crowbar to destroy it and gain the manger's computer password


#This variable holds the value for how many tries the player can guess the door combination before they are booted from the room
doortries = 3

global boiler        #Boiler stores the value of whether the boilerverse is unlocked or not

boiler = "OFF"    #At the beginning, it will be set to OFF

def commandloop():  # This function prints the command list to the screen
  print (commands)  #Mainly because I'm too lazy to just write down the command every time

def clear():      # This function simply clears the console
  os.system("cls")   # It only supports Microsoft Windows

def sleep():  # Stop everything and wait for 2 seconds, then continue
  time.sleep(2)

def dead(): #This function gets called whenever the player loses the game
  from termcolor import cprint         #We need this library for the colors for the text
  clear()
  print("The Security Bot caught you sneaking around the store.")
  print("It starts to beep rapidly...")
  print("A cage comes flying down, preventing you from leaving")
  print("It looks like you're stuck for the rest of the night.")
  cprint("          GAME OVER!    ", "red")     #This is where it is used
  input()                       #Wait for user input
  exit()                  #Stop the game

#---------------------------------------
#           Debugging info
# Each room has it's own function, so the room can
# be accessed as much as the player wants.
#---------------------------------------
# breakagain - The main function for the Break room
# hallagain  - The main function for the Hallway
# mainagain - The main function for the Main Store area
# washagain - The main function for the Washrooms
# boyagain  - The main function for the boys section of washrooms
# girlagain - Same as boyagain, but for the girls section
# telephone - This is for whenever the user uses the phone
# groceryagain - Main function for the grocery area
# cashagain - Main function for the cash register area
# manageragain - Main function for the manager's lounge
# storageagain - Main function for the Storage Room
# securityagain - Main function for the Security Room
# ventagain - Main function for the little vent section
# emergency - Main function for the Emergency Exit
# computeragain - Main function for computer
# credits - Main function for the credits
# end - Main function for the ending dialouge after the quiz
# securityquiz - Main function for the quiz everytime the player enters the security room
# boilagain - Main function for the Boilerverse
# denyboileraccess - handler for denying access to the Boilerverse
#-----------------------------------------------------

def breakagain():               
 global currentroom, took, gotsomethin, itemselect, security, firstcode   #Some variables are used in various functions, so since the user starts here at the beginning, just make them global to be used for the other functions
 currentroom = "Break Room"      #Currentroom keeps track of which room the user is in. 
 global command  
 command = 0      # Command waits for a correct command to be inputted.
 global inventory #Inventory stores the grocery item the player has selected
 inventory = []  #Set it to zero for now
 itemselect = ""    #Same with itemselect, which stores data from the storage room
 commands.clear()               #Flush command list
 commands.append("Look around")           #And add our new commands
 commands.append("Move to next area")
 clear()
 print ("You check your surroundings. The break room is dark and barely identifiable.\nIt looks like you'll have to adjust to the darkness.\n\n")                                    #Print the description
 commandloop()              #Print command list to the screen
 while command not in commands: #Loop this progress until correct command
   command = input("What will you do: ")
   if command not in commands:  #Is this a valid command?
     print("Invalid command.") #No? Then loop until correct command inputted
   if command in commands:        #Is this a valid command?
       if command == commands[1]: #Is it located in index 1?
         clear()
         print("Moving to next area...")   #Get ready to move into the next room
         if commands == "Move to next area":    #Alternatively, if it is manually typed
           commands.remove("Move to next area")#Move to next area and remove the command
         sleep()               
         currentroom = "Hallway"                        #Next room is set
         hallagain()                                     #Start the next room!
         break                       #Exit the while loop
       if command == commands[0]:                     #Is command at index 0?
         clear()                                    
         print ("You look around the nearly pitch black room.")
         print ("\nBeside you lies a donut, waiting to be eaten...\n")
         commandloop()                                     #Print commands
         command = input("What will you do now: ")           #Continue further
         if command not in commands:                       
           print("Invalid command.")
         if command in command == commands[0]:     #Is the command at index 0 again?
           clear()
           print("Besides the donut, there is nothing identifiable in the room.")
           print("\nThere is a doorway in front of you. It leads into the outside hallway.")   #Print new description
           print("\nSeriously though, that donut looks really tasty")
           print("\nIt would be a shame to leave it by itself.\n")
           commands.remove("Look around")
           commands.append("Eat donut")         #Add a new command, eat donut
           commandloop()
           command = input("What will you do now: ")
           if command not in commands:
             print("Invalid command")
           if command in commands:
             if command in command == commands[0]:    #Eat donut will be stored at 1
                 clear()
                 print("\n\n\n\n\nYou move to the next area, leaving the donut behind")
                 print("\nGood bye, donut!")
                 sleep()
                 if commands == "Move to next area":
                   commands.remove("Move to next area")#Flush command list for next room
                 if commands == "Move to next area":
                   commands.remove("Move to next area")
                 commands.remove("Eat donut")
                 hallagain()                #Start the next room
           if command in command == commands[1]:      #Is the command at index 1
                 clear()                      #The user chose to eat the donut
                 print("You eat the donut regardless of whether it belonged to you or not.")
                 print("\nWait a minute! There's something hard inside!")
                 print("\nThere's a secret code inside! No way!")
                 firstcode = random.randint(0, 30) #Pick a random number from 0 to 30
                 print("\nThe code reads" + str(firstcode)) # Print it to screen
                 commands.remove("Eat donut")           #Remove the command
                 print("\nWrite it down on paper!")
                 input()
                 breakagain()
         if command == "Move to next area":    #After eating the donut, the only command
          clear()    #left will be to move to the next room
          print ("Moving to next area...")
          if commands == "Move to next area":
            commands.remove("Move to next area")
          sleep()
          currentroom = "Hallway"         #Set currentroom to the next room
          hallagain()
          break                      #Exit the loop
         if command == "Eat donut": #This is a repeat of the earlier code, but if it is inputted beforehand and/or manually
                 clear()
                 print("You eat the donut regardless of whether it belonged to you or not.")
                 print("\nWait a minute! There's something hard inside!")
                 print("\nThere's a secret code inside! No way!")
                 firstcode = random.randint(0, 30)
                 print("\nThe code reads" + str(firstcode))
                 commands.remove("Eat donut")
                 print("\nWrite it down on paper!")
                 input()      #Wait for user input
                 breakagain()

def hallagain():
  command = 0       #Reset the command variable
  clear()
  currentroom = "Hallway"
  print("You walk into a fairly long hallway. There are two exits that lead you to different places. South of the hallway lies the Break Room\n")
  commands.clear()                            #Clear the command list
  commands.append("Look around")               #Add new entries
  commands.append("Go to middle exit")
  commands.append("Go to right exit")
  commands.append("Go to break room")
  commands.append("Go to manager lounge")
  if commands == ("Move to next area"):
    commands.remove("Move to next area")
  commandloop()                      #Print command list
  while command not in commands:
    command = input("What will you do: ")
    if command not in commands:
      print("Invalid command.")
    if command in commands:
        if command == commands[0]:          #Is it located at index 0?
          clear()
          print ("You take a look through the dark hallway.")
          print ("\nOn your right, awaits an emergency exit")
          print ("\nIt might be your only chance of escape!\n")
          commands.remove("Look around")        #Remove the command to prevent crashing
          hallagain()
          commandloop()
          command = input("What will you do now: ")
          if command not in commands:
            print("Invalid command.")
          if command in command == commands[0]:    #Is it at index 0?
            clear()
            print("Moving to middle exit...")       #Start moving to next room
            sleep()
            mainagain()        #This code for some reason had a lot of issues, so I inputted
            mainagain()        #the second function call as a failsafe (Replit hates me
            currentroom = "Main Store"
            break
          if command in command == commands[1]:  #Is player trying to go to Emergency Room?
            clear()                              
            if not firstcode and not secondcode and not thirdcode and not fourthcode:
              clear()                                #No? Deny access and loop itself
              print("The vault room is locked for now.\n")
              print("It cannot be opened without four codes.\n")
              input()
              hallagain()                           #And exit
            elif firstcode and secondcode and thirdcode and fourthcode:
              clear()
              print("Moving into next room...")
              sleep()
              currentroom = "Emergency Exit"
              
          if command in command == commands[2]:    #Is the command at index 2?
            clear()
            print("Moving to break room...")        #Then move to the previous room
            sleep()
            currentroom = "Break Room"              #Move completed
            break
        if command == "Go to middle exit":       #Did the player select the middle exit
          clear()
          print("Making way to the middle exit...") #Move there
          sleep()
          currentroom = "Main Store"             #Set to the next room
          searched = "off"                    #Turn searched off, since we're entering a new room
          mainagain()                #Start the function
          break                      #and exit
        if command == "Go to right exit":         #Is the user trying to go to right exit?
          clear()
          if not firstcode and not secondcode and not thirdcode and not fourthcode:
              clear()
              print("The vault room is locked for now.\n")
              print("It cannot be opened without four codes.\n")
              input()
              hallagain()
          elif firstcode and secondcode and thirdcode and fourthcode:
            clear()
            print("Moving into the next room...")
            sleep()
            currentroom = "Emergency Exit"
        if command == "Go to break room":    #did the user select the break room
          clear()
          print("Moving to break room...")    #move there
          sleep()
          currentroom = "Break Room"          #set to previous room 
          searched = "off"            #turn these off, since we're entering a new room
          searchedhall = "off"
          breakagain()              #Call the corresponding function
          break                      #Exit
        if command == "Go to manager lounge":      #Did the player select the lounge?
          print("Moving to manager lounge...")
          sleep()
          manageragain()                         #Move to manager lounge

def mainagain():
  clear()
  currentroom = "Main Store"
  command = 0
  commands.clear()         #Flush command list
  commands.append("Look around")               #Add our new entries
  commands.append("Go to washrooms")
  commands.append("Go to cash registers")
  commands.append("Go to grocery area")
  commands.append("Go back")
  print("You walk out into the dark store area. It feels like a ghost town, everything is ready for sale, but no one is there to buy it. Somewhere in the distance, you hear the mechanical clicking of the security system. It's a good idea that you stay away from it at all costs, or else you aren't getting out of here.\n")
  commandloop()    #Print description and command lists
  while command not in commands: #Loop until correct command
    command = input("What will you do: ")
    if command not in commands:
      print("Invalid command.")
    if command in commands:
      if command == "Look around":
        clear()
        print("\nThe main store is dark, so it's difficult to see anything familiar. Out in the distance the washrooms stand, a dim light shining from inside. The registers are deserted, almost as if frozen in time from the moment they were shut off.")          #Print the look around description
        input()
        mainagain()          #Go back to the start
    if command == "Go back":         #Does the player want to go back
        clear()                     #Then move back a room
        print("Moving to the hallway...")
        sleep()
        hallagain()               #call the corresponding function
    if command == "Go to cash registers":    #Does the player want to go to the next room?
      clear()
      print("Moving to cash registers...")   #then move there
      sleep()
      cashagain()                         #call its function
    if command == "Go to washrooms":    #does the player want to go to washroom area
      clear()
      print("Moving to washrooms...")      #move there
      sleep()
      washagain()                         #call its function
    if command == "Go to grocery area":      #else, if it is going to the grocery area
      clear() 
      print("Moving to grocery area...")    #move there
      sleep()
      groceryagain()         #and call its function

def groceryagain():
  clear()
  command = 0          #Reset the command variable
  global inventory, bag       #Make these existing variables global
  bag = []                  #Set bag to its default value
  inventory = 0             #Same with inventory
  foods = ["Banana", "Chocolate", "Tomato", "Pinapple", "Egg", "Go back"] #This is the food list the user can buy with the exception of Go back
  currentroom = "Grocery Area"        #Switch to current room
  print("The room is bright. There are different types of food you can buy! They all sit nicely on their little stock shelves, taking in the darkness of the store.")
  while command not in foods:     #Repeat until a valid command is inputted
    print(foods)                  #Print the list
    command = input("What will you buy? ")    #prompt the user
    if command not in foods:               #is it a valid command
      print("Invalid command.")           #if not, then repeat until so.
    if command in foods:                  #if it is a valid command
      if command == "Banana":            #if it is a banana
        print("You bought a banana!")
        if itemselect == "Banana":          #check if it was the intended food to buy
          print("This is what you were looking for!") #print the right message
          inventory = 1               #Set inventory to 1, which allows the game to realize that the player has bought an item
          bag = ["Banana"]         #put it in the bag
        else:
          print("This isn't what you're looking for...") #If this was not the item the player was meant to get, it's game over.
          if security == "ON":
            print("The cash register starts to cause a racket!")
            print("Suddenly, you hear beeping emerging slowly behind you.")
            time.sleep(4)
            dead()
          else:
            print("Remember to pay for it!") #hint hint
            input()
            cashagain()
      if command == "Egg":
        print("You bought an egg!")
        if itemselect == "Egg":
          print("This is what you were looking for!")
          inventory = 1   #Set inventory to being currently used
          bag = ["Egg"]   #Store item into bag
        else:
          print("This isn't what you're looking for...")
          if security == "ON":
            print("The cash register starts to cause a racket!")
            print("Suddenly, you hear beeping emerging slowly behind you.")
            time.sleep(4)
            dead()
          else:
            print("Remember to pay for it!")
            input()
            cashagain()
      if command == "Tomato":
        print("You bought a Tomato!")
        if itemselect == "Tomato":
          print("This is what you were looking for!")
          inventory = 1
          bag = ["Tomato"]
        else:
          print("This isn't what you're looking for...")
          if security == "ON":
            print("The cash register starts to cause a racket!")
            print("Suddenly, you hear beeping emerging slowly behind you.")
            time.sleep(4)
            dead()
          else:
            print("Remember to pay for it!")
            input()
            cashagain()
      if command == "Chocolate":
        print("You bought chocolate!")
        if itemselect == "Chocolate":
          print("This is what you were looking for!")
          inventory = 1
          bag = ["Chocolate"]
        else:
          print("This isn't what you're looking for...")
          if security == "ON":
            print("The cash register starts to cause a racket!")
            print("Suddenly, you hear beeping emerging slowly behind you.")
            time.sleep(4)
            dead()
          else:
            print("Remember to pay for it!")
            input()
            cashagain()
      if command == "Pinapple":
        print("You bought a pinapple!")
        if itemselect == "Pinapple":
          print("This is what you were looking for!")  #This is for debugging ONLY
          inventory = 1
          bag = ["Pinapple"]
        else:
         print("This isn't what you're looking for...")
         print("The cash register starts to cause a racket!")
         print("Suddenly, you hear beeping emerging slowly behind you.")
         time.sleep(5)
         dead()
      if command == "Go back":
       clear()
       print("Going back...")
       sleep()
       mainagain()

def cashagain():
  global thirdcode   #Make this global so it can be modified
  clear()                  
  command = 0
  currentroom = "Cash Registers" #Change currentroom
  print("You end up in the deserted cash registers. It is just as dark as the rest of the building. On the register counter sits a working telephone.\n")
  commands.clear()      #Flush command list
  commands.append("Use telephone")
  commands.append("Go back")
  commands.append("Go to Storage Room")
  commands.append("Go to Security Room")
  if inventory == 1:    #Is there something in the inventory
    commands.append("Scan item")  #Then add this command
  commandloop()
  while command not in commands:
    command = input("What will you do: ")
    if command not in commands:
      print("Invalid command.")
    if command in commands:
      if command == "Use telephone":
        telephone()           #Call the telephone function
      if command == "Go back":
       clear()
       print("Going back...")
       sleep()
       mainagain()
      if command == "Go to Storage Room":
        print("Going to Storage room...")
        sleep()
        storageagain()  #NOTE: THERE ARE TWO DIFFERENT INVENTORIES FOR BOTH THE GROCERY AND STORAGE AREAS
      if command == "Go to Security Room":
        print("Going to Security Room...")
        sleep()
        securityagain()
      if command == "Scan item":
        clear()
        print("Scanning item...")
        command = 0
        while command not in bag:   #Wait until a correct item was chosen
          print(bag)
          command = input("What are you scanning? ")
          if command not in bag:
            print("Invalid item")
          if command in bag:
            if command == "Egg": #Is the item an egg?
              if itemselect == "Egg": #Was the player meant to get it?
                print("You scanned the egg")
                print("The bar code revealed itself as a secret code")
                thirdcode = random.randint(0, 30) #pick a number from 0 to 30
                print("The third code is " + str(thirdcode))
                print("How did that happen anyway?") #display it to the user
                time.sleep(15)
                cashagain()
              else:
                print("You scanned the tomato")
                print("There's nothing significant on this bar code")  #This only happens if the player wasn't meant to get this item
                time.sleep(5)
                cashagain()
            if command == "Tomato":
              if itemselect == "Tomato":
                print("You scanned the tomato")
                print("The bar code revealed itself as a secret code")
                thirdcode = random.randint(0, 30)
                print("The third code is " + str(thirdcode))
                print("How did that happen anyway?")
                time.sleep(15)
                cashagain()
              else:
                print("You scanned the tomato")
                print("There's nothing significant on this bar code")
                time.sleep(5)
                cashagain()
            if command == "Chocolate":
              if itemselect == "Chocolate":
                print("You scanned the chocolate")
                print("The bar code revealed itself as a secret code")
                thirdcode = random.randint(0, 30)
                print("The third code is " + str(thirdcode))
                print("How did that happen anyway?")
                time.sleep(15)
                cashagain()
              else:
                print("You scanned the tomato")
                print("There's nothing significant on this bar code")
                time.sleep(5)
                cashagain()
            if command == "Banana":
              if itemselect == "Banana":
                print("You scanned the banana")
                print("The bar code revealed itself as a secret code")
                thirdcode = random.randint(0, 30)
                print("The third code is " + str(thirdcode))
                print("How did that happen anyway?")
                time.sleep(15)
                cashagain()
              else:
                print("You scanned the tomato")
                print("There's nothing significant on this bar code")
                time.sleep(5)
                cashagain()
            if command == "Pinapple":
              if itemselect == "Pinapple":
                print("You scanned the pinapple")
                print("The bar code revealed itself as a secret code")
                thirdcode = random.randint(0, 30)
                print("The third code is " + str(thirdcode))
                print("How did that happen anyway?")
                time.sleep(15)
                cashagain()
              else:
                print("You scanned the tomato")
                print("There's nothing significant on this bar code")
                time.sleep(5)
                cashagain()

def storageagain():
  global took, takemarker   #Took keeps track of what has been taken, while takemarker just serves as an indicator
  clear()
  storageitems = ["Crowbar", "Yellow paint", "Strange audiotape", "Go back"]
  if took == ["Yellow paint"]:   #Has the yellow paint been chosen?
    storageitems.remove("Yellow paint") #Then remove the command
  elif took == ["Crowbar"]:  #Same with the crowbar and the audiotape if they have been taken already
    storageitems.remove("Crowbar")
  elif took == ["Strange audiotape"]:
    storageitems.remove("Strange audiotape")
  command = 0
  currentroom = "Storage Room"
  print("The storage room is dark and narrow. There are countless miscellanous items strewn about, some sitting on shelves, while others lie on the floor, collecting dust.")
  commands.clear()
  while command not in storageitems:
    print (storageitems)
    command = input("What will you take: ")
    if command not in storageitems:
      print("Invalid command.")
    if command in storageitems:
      if command == "Crowbar":
        clear()
        print("You take the crowbar!")
        print("It's pretty heavy, but it can pretty much break anything!")
        input()        
        takemarker = 1 #Set this to 1 to note that something has been taken
        took = "Crowbar"  #Store it in the inventory
        storageagain()
      if command == storageitems[2]: #Is the command in index 2?
        clear()
        print("You take the Strange Audiotape!")
        print("Now you just need to find something to play it on")  #It can be played with the audio cassette player
        input()
        takemarker = 1
        took = "Strange Audiotape"
        storageagain()
      if command == "Yellow paint":
        clear()
        print("You take the yellow paint!")
        print("Why is there only yellow paint? Who knows!")
        input()
        takemarker = 1
        took = "Yellow paint" #The yellow paint is used for the boy's section of the washroom
        storageagain()
      if command == "Go back":
        clear()
        print("Going back...")
        sleep()
        cashagain()

def washagain():
  clear()
  command = 0
  robot = 0
  currentroom = "Washrooms"
  print("You enter the washroom area. The area divides itself into two sections respectively, one for boys and one for girls. In the center of the two corridors, a dim night light shines, the only source of light in the area.\n")
  commands.clear()
  commands.append("Go back")                #Flush list and add new entries
  commands.append("Go to boys room")
  commands.append("Go to girls room")
  while command not in commands:
    commandloop()
    command = input("What will you do: ")
    if command not in commands:
      print("Invalid command.")
    if command in commands:
      if command == "Go back":
        clear()
        print("Going back to main area...")   #This function is pretty straightforward
        sleep()
        mainagain()
      if command == "Go to boys room":
        clear()
        print("Going to boys room...")
        sleep()
        boyagain()
      if command == "Go to girls room":
        clear()
        print("Going to girls room...")
        sleep()
        girlagain()


def boyagain():
  global dryer, secondcode  #Make secondcode global to prepare to be modified
  dryer = "Off"   #Set dryer to off
  command = 0
  currentroom = "Boy's Washroom"
  print("The boys bathroom area is dark and narrow. \nOn the wall to the left, two urinals sit. \nThere is a stall beside them. \nOn the wall to your right, a sink with two air dryers.\n")
  commands.clear()
  commands.append("Go back")
  commands.append("Use urinal")
  if dryer == "Off":                  #Is the dryer off?
    commands.append("Turn on air dryer")  #Yes, then add this command
  while command not in commands:
    commandloop()
    command = input("What will you do: ")
    if command not in commands:
      print("Invalid command.")
    if command in commands:
      if command == "Go back":
        clear()
        print("Moving to washroom corridor...")
        sleep()
        washagain()
      if command == "Use urinal":
          print ("Inventory: " + (took))  #Display inventory
          print("Use <Go back> to go back")
          command = input("What will spill into the urinal: ")
          if command == "Yellow paint" and took == "Yellow paint":  #Is the selection the yellow paint?
           clear()
           print("You pour the yellow paint into the urinal.")
           print("Sure enough, the toliet senses the paint and flushes it down.")
           print("Through the clean toliet water, a piece of paper flows freely")
           print("There is a code written on it.")
           secondcode = random.randint(0, 30) #Pick a random number
           print("The paper reads: " + str(secondcode)) #Display it
           print("Looks like it will come in handy!") #store it in secondcode
           time.sleep(15)
           boyagain()
          else:
            print("You can't use this!")
      if command == "Turn on air dryer":
        clear()
        dryer = "On"
        print("You turn on the air dryer. It starts to buzz noisely.")
        time.sleep(4)
        boyagain()

#This function is almost identifiable to the boyagain function, but it does not give you a code
def girlagain():
  global dryer2
  dryer2 = "Off"
  command = 0
  robot = 0
  currentroom = "Girl's washroom"
  print("The girls bathroom area is dark and narrow. \nOn the wall to the left, stands three stalls.\nOn the wall to your right, a sink with two air dryers.\n")
  commands.clear()
  commands.append("Go back")
  commands.append("Flush toliet")
  if dryer2 == "Off":
    commands.append("Turn on air dryer")
  while command not in commands:
    commandloop()
    command = input("What will you do: ")
    if command not in commands:
      print("Invalid command.")
    if command in commands:
      if command == "Go back":
        clear()
        print("Moving to washroom corridor...")
        sleep()
        washagain()
      if command == "Flush toliet":
        clear()
        print("You flush the toliet.\n Hooray!")
        sleep()
        girlagain()
      if command == "Turn on air dryer":
        clear()
        dryer2 = "On"
        print("You turn on the air dryer. It starts to buzz noisely.")
        time.sleep(4)
        girlagain()

def manageragain():
  command = 0
  currentroom = "Manager Lounge"
  print("Entering the manager's lounge makes you feel strange, almost as if you shouldn't be here. Either way, there could be something in this room that might help you.")
  commands.clear()
  commands.append("Use tape player")
  commands.append("Use Manager's computer")
  commands.append("Go back")
  while command not in commands:
    commandloop()
    command = input("What will you do: ")
    if command not in commands:
      print("Invalid command.")
    if command in commands:
      if command == "Go back":
        clear()
        print("Going back...")
        sleep()
        hallagain()
      if command == "Use tape player":
          print (took) #display the inventory
          print("Use <Go back> to go back")
          command = input("What will you play: ")  #Prompt user for their choice
          if command == "Strange Audiotape": #Is it the Strange audiotape
           clear()
           print("You put the strange tape into the cassett player.")
           print("It takes a while, but the tape begins to play...")
           print("A voice can be heard from the recording.")
           time.sleep(3)
           print("*Hey you! Yeah, you!*")
           print("*The person listening to this right now.*")
           print("*Yeah, you fell asleep again, so I went ahead to tell the boss")
           print("to leave you here*")
           print("*Don't be such a slacker next time!*")
           print("*Don't worry, though! There is still a way out.")
           print("*I put some codes all over the place, find them and bring them to the Emergency Exit room.*")
           print("*It's going to be a fun night for you!*")
           print("*Heh heh heh heh heh*")
           time.sleep(10)
           print("The tape has ended")
           took.clear()
           sleep()
           manageragain()
          elif command == "Go back":
            clear()
            print("You turn the cassett player off and shut it tight.")
            sleep()
            manageragain()
          else:
            print("This is not a valid tape!")
            sleep()
            manageragain()
      if command == "Use Manager's computer":
        computerprompt()   #Prompt the user for the password


def computerprompt():
  global password #Global this, since it holds the password
  command = 0
  command = input("What is the Administrator password? ")
  if command == str(password):  #Is it the password from the Security Machine?
     print("The computer was unlocked..")
     print("The main operating system begins to boot up")
     input()
     computeragain()
  else:       #If not, then it's game over
    print("This is not the correct password!")
    print("Suddenly, you hear familiar beeping behind you")
    time.sleep(4)
    dead()


def securityroom():
  clear()
  global password  #Global this to be modified
  command = 0
  print("The Security Room blinds you with a red flashing light pulsating throughout the room. There are monitors all over the room, it looks like this is where the Security System lies.")
  commands.clear()
  commands.append("Go back")
  commands.append("Break Security System")
  while command not in commands:
    commandloop()
    command = input("What will you do: ")
    if command not in commands:
      print("Invalid command.")
    if command in commands:
      if command == "Break Security System":
        print(took)  #display inventory
        command = input("What will you use to break the system?> ")
        if command == "Crowbar" and took == "Crowbar":
          clear()  #Is it the crowbar?
          print("You use the crowbar and strike at the Security Machine.")
          print("The screen breaks into a million pieces, as a thousand circuits inside stop working.")
          print("The noise and the lights are finally gone")
          print("You have successfully killed one of the Security Systems!") #SMASSSSSH!!
          security = "OFF"
          input()
          print("Before the machine dies, a string of numbers fades in on the Security Machine's plexiglass screen.")
          print("It reads:")
          password = random.randint(0, 30) #make a random number for the password
          print("'The Administrator Password is'" + str(password))  #display it to the player
          input()
          securityroom()
        if command == "Yellow paint" and took == "Yellow paint":  #The yellow paint DOES NOT kill the Security System
          clear()
          print("You pour the yellow paint.")
          print("The machine garbles for a minute, but comes back on.")
          print("It seems like the paint only made it more angrier.")
          print("It begins to glow its menacing light.")
          time.sleep(4)
          dead()
        if command == "Strange audiotape" and took == "Strange audiotape":
          clear()
          print("How will this help destroy the machine?")
          input()  #There's no point in this!
          securityroom()
        else: #If there is anything else, it is unusable
          print("You can't use this!")
          input()
          securityroom()
      if command == "Go back":
        clear()
        print("Going back...")
        sleep()
        cashagain()

  
#This is the quiz that will play everytime the player enters the security room
def securityagain():
  clear()
  doortries = 3
  currentroom = "Securityquiz"
  score = 0
  if security == "OFF":
    securityroom()
  print("BEEP BEEP! I AM THE SECURITY SYSTEM!")
  print("TO ENTER THE SECURITY ROOM, YOU WILL NEED TO ANSWER ONE QUESTION.")
  print("THIS IS NATURAL SECURITY SYSTEM BEHAVIOR...")
  input()
  print("Possible answers:")
  print("-Open sesame!")
  print("-Abra kadabra")
  print("-Please and thank you")
  print("-Just open the damn door already!")
  while doortries > 0:  #Loop until 0 is greater
    question = input("What is the magic word? ")
    if question == "Open sesame":
      print("THAT IS VERY CLICHE, BUT I STILL CANNOT LET YOU PASS!")
      doortries -= 1
      print("YOU HAVE " + str(doortries) + " TRIES BEFORE YOU ARE LOCKED OUT.") #Display lives left
      input()
    if question == "Abra kadabra":
      print("YOU'RE A LOT SMARTER THAN I THOUGHT...")
      print("I GUESS I CAN LET YOU PASS....")
      input()
      securityroom()
    if question == "Please and thank you":
      print("VERY POLITE OF YOU, BUT THAT IS NOT THE ANSWER I AM LOOKING FOR...")
      print("YOU HAVE " + str(doortries) + " TRIES BEFORE YOU ARE LOCKED OUT.")  #display lives left
      input()
    if question == "Just open the damn door already!":
      print("HOW RUDE!")
      print("I WILL NOT OPEN THE DOOR FOR SUCH A RUDE INDIVIDUAL!!")
      print("YOU HAVE " + str(doortries) + " TRIES BEFORE YOU ARE LOCKED OUT.") #display lives left
      input()
    else:
      print("INVALID ANSWER!")  #If anything else, it is invalid
      doortries -= 1
      print("YOU HAVE " + str(doortries) + " BEFORE YOU ARE LOCKED OUT.")
      input() 
      #If 0 is greater, than it's game over, the player ran out of chances
  print("You have answered incorrectly too many times!")
  print("The Security will be here shortly.")
  input()
  dead()
def computeragain():
  clear()
  command = 0   #Reset command variable
  print("Gigantasoft Doors 11")   #Lol
  print("SERVICE PACKAGING 12")  
  commands.clear()
  commands.append("Log off")
  commands.append("Check Store Map")
  commands.append("Review all codes")
  commands.append("Go to Boilerverse") #This is where things get weird 
  while command not in commands:
    commandloop()
    command = input("What will you do: ")
    if command not in commands:
      print("Invalid command.")
    if command in commands:
      if command == "Log off":
        clear()
        print("Shutting down Gigantasoft Doors...")
        sleep()
        manageragain()
      if command == "Check Store Map":
        clear()
        print("   STORE MAP  ")
        print(" BREAK ROOM ")
        print("     |      ")
        print("     v      ")
        print("    Hallway   ")
        print("  |         |         |     ")
        print("  v         v         v    ")
        print("OFFICE   Main Store   Emergency Exit")
        print("         |    |     |        ")
        print("         v    v     v         ")
        print("       Cash   Washrooms Grocery Area")
        print("        |                             ")
        print("        v                               ")
        print("       Storage Room                  ")
        print("        |      ")
        print("        v ")
        print("    Security Room     ")
        print("\nFull map analysis complete!")
        print("All rooms enabled in: NIGHT VISION mode.")
        input()
        computeragain()
      if command == "Review all codes": #display all codes
        print("All commands collected by far...")
        print("First code is " + str(firstcode))
        print("Second code is " + str(secondcode))
        print("Third code is " + str(thirdcode))
        print("Fourth code is " + str(fourthcode))
        input()
        computeragain()
    if command == "Go to Boilerverse":
        clear()
        print("The moment you typed the command in, everything began to distort around you.")
        print("Soon enough, everything becomes a blur in the motion of time itself.")
        print("It's blinding, all this time moving at once.")
        print("Everything is moving too fast, your eyes can't keep up.")
        print("Finally, everything stops.")
        input()  #This kinda reminds me of Moonside from Earthbound
        boileragain()

def boileragain():
  clear()
  boilercom = ["START"]  #The boilerverse has its own command list, just because
  command = 0
  print("When the dizziness in your head finally stops, you uddely begin to feel weightless. Something about the place you are in feels so... cyberspace-ish. You stop and wonder if this is real life, or just a bad trip? Either way, welcome to the Boilerverse.")

  print("Suddenly, some cyberverse computer agent starts speaking to you.")

  print("HI THERE! WELCOME TO BOILERVERSE!")
  command = input("TO GET STARTED, USE THE START COMMAND> ")
  if command == "START":
     print("PLEASE SELECT YOUR COMMAND")
     boilercom.clear()
     boilercom.append("Get the code")
     print (boilercom)
     command = input("What is your command?> ")
     if command == "Get the code":
       print("SO THAT IS WHAT YOU WANT?")
       print("WELL I GUESS I HAVE NO CHOICE BUT TO GIVE IT TO YOU.")
       print("BUT...")
       print("NOT WITHOUT A QUIZ FIRST, OF COURSE!")
       finalquiz()
     else:
        print("THAT IS NOT A VALID COMMAND, SO I GUESS YOU WILL HAVE TO LEAVE NOW!")
        print("BUH BYE!")
        input()
        manageragain()
  else:   #If not a valid command, return back to the manager's lounge
     print("THAT IS NOT A VALID COMMAND, SO I GUESS YOU WILL HAVE TO LEAVE NOW!")
     print("BUH BYE!")
     input()
     manageragain()



def denyboileraccess():   #I don't think this is ever used
  clear()
  print("As soon as it all began, it ended immediantly.")
  print("It seems there is something you forgot to do.")
  print("You must remember what that is, before entering the Boilerverse.")
  input()
  computeragain()

def finalquiz():   #This is the quiz that procceeds from entering the boilerverse
  command = 0
  questions = 1
  doortries = 3
  print("YOU KNOW HOW MUCH US ROBOTS LOVE QUIZZES!")
  print("GET IT TOGETHER, WILL YOU?")
  print("LET'S GET THIS QUIZ STARTED!")
  print("YOU HAVE 3 TRIES, SO DON'T BLOW IT ALL ON ONE GUESS!")
  input()
  clear()
  while doortries > 0:
   while questions == 1:
      clear()
      print("Question 1:")
      print("What is the name of this game?")
      print("-Lost in the Supermarket")
      print("-Fun Python Game!")
      print("-Night at the Supermarket")
      print("-A supermarket")
      command = input("What is your guess? " )
      if command == "Lost in the Supermarket":
       print("Incorrect answer!")
       doortries -= 1
       print("You have " + str(doortries) + " tries left!")
       input()
      if command == "Fun Python Game":
       print("Incorrect answer!")
       doortries -= 1
       print("You have " + str(doortries) + " tries left!")
       input()
      if command == "Night at the Supermarket":
       print("Correct answer!")
       questions = 2
       input()
      if command == "A supermarket":
       print("Incorrect answer!")
       doortries -= 1
       print("You have " + str(doortries) + " tries left!")
       input()
   while questions == 2:
       clear()
       print("Question 2:")
       print("Frozen ice is just ______")
       print("-A knockoff hip-hop artist")
       print("-Frozen water")
       print("-Old news")
       print("-Frozen ice")
       command = input("What is your guess?" )
       if command == "A knockoff hip-hop artist":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()
       if command == "Frozen water":
         print("Incorrect answer!")
         doortries -= 1
         print("You have " + str(doortries) + " tries left!")
         input()
       if command == "Old news":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()
       if command == "Frozen ice":
         print("Correct Answer!")
         questions = 3
         input()
   while questions == 3:
       clear()
       print("Question 3:")
       print("What does my basement smell like?")
       print("-Mold")
       print("-Bananas")
       print("-A normal generic basement smell")
       print("-Empty Mountain Dew cans")
       command = input("What is your answer? ")
       if command == "Mold":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()
       if command == "Bananas":
         print("Correct Answer!")
         questions = 4
         input()
         break
       if command == "A normal generic basement smell":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
       input()
       if command == "Empty Mountain Dew cans":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()  
   while questions == 4:
       clear()
       print("Question 4:")
       print("Who ya gonna call?")
       print("-GHOSTBUSTERS")
       print("-The Police")
       print("-My mom")
       print("-The next function")
       command = input("What is your answer? ")
       if command == "GHOSTBUSTERS":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()
       if command == "The Police":
         print("Correct Answer!")
         questions = 5
         input()
         break
       if command == "My mom":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()
       if command == "The next function":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()
   while questions == 5:
       clear()
       print("Question 5:")
       print("Who wins Total Drama Action?")
       print("-Gwen")
       print("-Owen")
       print("-Duncan")
       print("-Ezekiel")
       command = input("What is your answer? ")
       if command == "Gwen":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()
       if command == "Owen":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()
       if command == "Duncan":
         print("Correct answer!")
         questions = 6
         input()
         break
       if command == "Ezekiel":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()
   while questions == 6:
       clear()
       print("Question 6:")
       print("What is my favourite color?")
       print("-Gray")
       print("-Grayish")
       print("-Grayer Gray")
       print("-Graaaay")
       command = input("What is your answer? ")
       if command == "Gray":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()
       if command == "Grayish":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()
       if command == "Grayer Gray":
         print("Correct answer!")
         questions = 7
         input()
         break
       if command == "Graaaay":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()
   while questions == 7:
       clear()
       print("Question 7:")
       print("Did that last question bother you?")
       print("-Of course")
       print("-Nah it's okay")
       print("-The correct answer")
       print("-YES! IT DID! I'M GONNA FIND YOUR HOUSE")
       command = input("What is your answer? ")
       if command == "Of course":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()
       if command == "Nah it's okay":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()
       if command == "The correct answer":
         print("Correct answer!")
         questions = 8
         input()
         break
       if command == "YES! IT DID! I'M GONNA FIND YOUR HOUSE":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()
   while questions == 8:
       clear()
       print("Question 8:")
       print("Here comes the sun")
       print("-It's alright")
       print("-NO I hate sunlight")
       print("-Okay")
       print("-It's nighttime")
       command = input("What is your answer? ")
       if command == "It's alright":
         print("Correct answer!")
         questions = 9
         input()
         break
       if command == "NO I hate sunlight":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()
       if command == "Okay":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()
       if command == "It's nighttime":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()
   while questions == 9:
       clear()
       print("Question 9:")
       print("What is the Price Lookup code for Asparagus?")
       print("-4011")
       print("-4053")
       print("-4421")
       print("-4080")
       command = input("What is your answer? ")
       if command == "4011":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()
       if command == "4053":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()
       if command == "4421":
        print("Incorrect answer!")
        doortries -= 1
        print("You have " + str(doortries) + " tries left!")
        input()
       if command == "4080":
         print("Correct answer!")
         questions = 10
         print("Coming up next...")
         print("It's the last question!")
         print("Think this one through!")
         input()
         break
   while questions == 10:
       clear()
       print("Question 10:")
       print("You are a computer virus tester, running the Worm.Win32.Blaster worm on a Virtual Machine ran by VirtualBox. Blaster, or MSBLAST is known for exploiting an RPC vulnerability in order to spread to different clients on the network as packets and being sent to and from the router. The worm is successfully compiled into machine code and you go to run the file, but it does not spread to the other clients. You take note that the virtual machine is a Windows Vista running Service Pack 2, with no antivirus software present on the attacking machine or its clients. Why did the worm fail at spreading?\n")
       print("-The original author of the worm is not very skilled with C++, thus it contains many unneccessary failsafes and errors")
       print("-Blaster only works for Windows XP and Windows 2000 machines")
       print("-Windows Defender is running in the background")
       print("-The C++ source file was not successfully compiled and/or corrupted from conversion.")
       command = input("What is your answer? ")
       if command == "The original author of the worm is not very skilled with C++, thus it contains many unneccessary failsafes and errors":
           print("Incorrect answer!")
           doortries -= 1
           print("You have " + str(doortries) + " tries left!")
           input()
       if command == "Blaster only works for Windows XP and Windows 2000 machines":
         print("Correct answer!")
         end()
       if command == "Windows Defender is running in the background":
         print("Incorrect answer!")
         doortries -= 1
         print("You have " + str(doortries) + " tries left!")
         input()
       if command == "The C++ source file was not successfully compiled and/or corrupted from conversion":
         print("Incorrect answer!")
         doortries -= 1
         print("You have " + str(doortries) + " tries left!")
         input()

def end():
      clear()
      global fourthcode  #Make this global for modification
      if doortries < 0:    #Did the player run out of lives
        denyboileraccess()  #Then they fail
      print("WOW! YOU REALLY GOT THROUGH ALL MY QUESTIONS...")
      print("YOU MUST BE SOME SORT OF BRAINIAC OR SOMETHING.")
      print("OR MAYBE THE QUIZ WAS A LITTLE TOO EASY...")
      input()
      print("IN THAT CASE...")
      print("I GUESS I HAVE NO CHOICE!")
      input()
      print("I'LL HAVE TO GIVE YOU ONE MORE SUPER TRICKY QUESTION!")
      print("ARE YOU PREPARED?")
      input()
      print("HERE IT COMES!!")
      input()
      print("...")
      print("Ha ha...")
      input()
      print("I WAS ONLY KIDDING!")
      print("JUST TAKE YOUR STUPID CODE AND GET OUTTA HERE!")
      fourthcode = random.randint(0,30) #Make one last code 
      print("The code is " + str(fourthcode)) #And display it
      print("You have gained all four codes!")
      print("Take them to the Emergency Exit room and get out quick!")
      input()
      print("THE EMERGENCY EXIT IS LOCKED RIGHT NOW, SO I'LL BE A LITTLE GENEROUS AND TELEPORT YOU SOMEWHERE NEAR...")
      print("LIKE A VENT!")
      print("THEN YOU'LL BE ABLE TO CRAWL THROUGH AND GET IN TO THE ROOM!")
      input()
      print("The digital world around you began to fade out of focus.")
      print("You feel yourself become distant from the virtual space that surrounds you.")
      print("It's only a matter of time until find yourself somewhere new.")
      input()
      ventagain()

def ventagain():
  command = 0
  clear()
  print("You were teleported to the air vent right above the Emergency Exit. It is narrow, but just enough for you to squeeze through. For such a small space, it's not as dirty as you think.")
  commands.clear()
  commands.append("Move forward to the Emergency Exit")
  commands.append("Drop back into the Hallway")
  while command not in commands:
    print(commands)
    command = input("What will you do?> ")
    if command not in commands:
      print("Invalid command.")
    if command in commands:
      if command == commands[0]:
        clear()
        print("You squeeze yourself forward to the next exit...")
        print("Making way to the Emergency Exit")
        sleep()
        currentroom = "Emergency Exit"
        emergency()
      if command == commands[1]:
        clear()
        print("You turn around and take the exit behind you.")
        print("You fall out of the opening and land on the cold floor of the hallway.")
        input()
        hallagain()

def telephone():
  robot = 0
  currentroom = "Cash Registers"
  command = 0
  phonelist = ["HELP", "Hang up"]  #Technically, there are more numbers but they're easter eggs
  global numberpeople, itemselect    #Make numberpeople a global variable
  numberpeople = ["Banana Business", "Pinapple People", "Tomato Toppers", "Chocolate Cheerers","Egg Enthusiasts"] #Whichever company calls you is the food you got to buy.
  clear()
  print("You pick up the phone\n")
  print("*Ring* *Ring* *Hello?*")
  while command not in phonelist:
    print(phonelist)
    command = input("Enter a number to call: ")
    if command not in phonelist:
      print("Please specify a number.")
    if command in phonelist:
      if command == phonelist[0]:
        clear()
        print("You dial the number and wait...\n")
        time.sleep(1)
        print("*Beeep* *Beeep*")
        sleep()
        print("Hello!\n")
        avalue = random.choice(numberpeople)
        print("This is " + avalue) #Get a random company name from our list
        if avalue == "Banana Business":
          itemselect = "Banana"
          #print("Item select is " + itemselect)
        if avalue == "Pinapple People":
          itemselect = "Pinapple"
          #print("Item select is " + itemselect)
        if avalue == "Chocolate Cheerers":
          itemselect = "Chocolate"
          #print("Item select is " + itemselect)
        if avalue == "Tomato Toppers":
          itemselect = "Tomato"
          print("Item select is " + itemselect)
        if avalue == "Egg Enthusiasts":
          itemselect = "Egg"
         # print("Item select is " + itemselect)
        print("Judging by you calling this number,\nyou need some help.")
        print("Well, we can't help you right now if you're \nstuck in the building.")
        print("You're just going to have to hang tight until morning, or find another way out")
        print("Bye Bye!")
        time.sleep(10)
        telephone()
      if command == "Tyler Bifolchi":
        clear()
        print("You dial the number and wait...\n")
        time.sleep(1)
        print("*Beeep* *Beeep*")
        sleep()
        print("Hello?\n")
        print("Wow! You found the Easter Egg!")
        print("You must be proud of yourself, even though you found this easter egg by digging in the source code.")
        print("Hey, Mr. Robinson!")  #Hee hee
        time.sleep(10)
        telephone()
      elif command == "Hang up":
        clear()
        sleep()
        cashagain()

#Okay, just to explain, in the beginning, you're in the break room, but what if you want to go back to a room you were previously in? The answer is pretty complex and it legit took me half a night to come up with
#That is why I put each room into a function
def emergency():
  guess = 0
  door = 0
  doortries = 1
  print("You have finally made it, the small Emergency Exit room is the last thing in your way from getting out of here!")
  print("A robot begins to speak")
  print("OPEN SESAME!")
  print("I AM THE EMERGENCY BOT!!")
  print("YOU NEED A REQUIREMENT OF FOUR CODES TO EXIT!!")
  input()
  guess = 1
  while guess == 1: #Loop until the value is changed
    print("What is the first door code?")
    door = input("Enter your answer> ")
    if door != str(firstcode):  #Is it different from the code
      print("Incorrect answer!") #Then it is incorrect
      doortries -= 1
    if door == str(firstcode): #Is it the same?
        print("Combination OK") #Then it is correct
        print("Unlocking first door...")
        firstdoor = False  #Unlock this door
        guess = 2  #Change the value to break out of looping
  while guess == 2: #And enter the next one
    print("What is the second door code?")
    door = input("Enter your answer> ")
    if door != str(secondcode):  #Is it different?
      print("Incorrect answer!") #Then it is incorrect
      doortries -= 1
    if door == str(secondcode): #Is it the same?
        print("Combination OK") #Then it is correct
        print("Unlocking second door...")
        seconddoor = False #Set this door to unlocked
        guess = 3  #Change the value...again
  while guess == 3:  #Rince and repeat!
    print("What is the third door code?")
    door = input("Enter your answer> ")
    if door != str(thirdcode):
      print("Incorrect answer!")
      doortries -= 1
    if door == str(thirdcode):
        print("Combination OK")
        print("Unlocking third door...")
        thirddoor = True
        guess = 4
  while guess == 4:
    print("What is the final door code?")
    door = input("Enter your answer> ")
    if door != str(fourthcode):
      print("Incorrect answer!")
      doortries -= 1
    if door == str(fourthcode):
        print("Combination OK")
        print("Unlocking final door...")
        fourthdoor = True
        guess = 5
  while doortries < 0:
    print("YOU HAVE FAILED TO ANSWER CORRECTLY!")
    print("NOW YOU WILL BE ESCOURTED BACK TO YOUR ORIGINAL LOCATION!")
    print("...IN A CAGE THAT IS")
    
    print("  GAME OVER!")
    print("You were locked in by the Emergency Bot")
  while guess == 5:
    print("Opening enterance...")
    sleep()
    clear()
    print("The main door opens to reveal the night sky and the air blowing through the wind. Your best friend is standing there with a stupid grin on his face.")
    print("*Hey man, you finally got yourself out of there*")
    print("*I didn't expect you to take that long, but I knew you'd find your way out eventually.")
    print("*It took a lot of convincing to get the boss to go along with it.*")
    print("*Heh heh heh...*")
    print("*Now what are you waiting for? I'm going home, I've had my fun, but now I need some serious sleep.*")
    print("*I bet you're tired, too. You should get on going home...*")

    print("You find your car and you drive back home. It is 2 in the morning.")
    print("You collapse on your bed and fall asleep within seconds, the events of tonight playing from the beginning in your mind.")
    print("               THE END!               ")
    command = input("Enter your name here!")
    f = open("Congrats.txt", "x")   #Put it into a file
    f.write((command) + "successfully escaped the supermarket!") # write to file
    credits()

def credits():  #All the people I have to thank lol
  clear()
  print("Created by")
  print("Tyler Bifolchi\n")
  
  print("Programming")
  print("Tyler Bifolchi\n")

  print("Pretty much everything else")
  print("Tyler Bifolchi\n")

  print("THANKS FOR PLAYING!")
  input()
  exit()

#The debug room can be accessed through using the code Beef women on the starting screen. I made this so that I could test the game a lot easier.
def debugroom():
  global firstcode, secondcode, thirdcode, fourthcode
  from termcolor import cprint  #We legit only need this library for one thing, and that's for some super cool debugging special effect
  clear()
  debug = ["Set all codes", "Start Quiz", "Print telephone listing", "Reset all variables", "Add commands to command list", "Color test", "Emergency Exit", "Ending"]
  emptylist = []
  print("ACCESSGRANTEDACCESSGRANTEDACCESSGRANTEDACCESSGRANTEDACCESSGRANTEDACCESSGRANTEDACCESSGRANTEDACCESSGRANTEDACCESSGRANTINGACCESSGRANTEDACCESSGRANTEDACCESSGRANTEDACCESSGRANTEDACCESSGRANTEDACCESSGRANTED")
  time.sleep(2)
  print("Breaking mainframe!")
  time.sleep(0.1)
  print("Index 0")
  command = 0
  time.sleep(4)
  cprint("The debugging menu is meant to access each event of the game individually. Tampering with settings without knowledge of what they do can result in very bad things!", "red")   
  print("Please note that once you input a command, you will be booted from the menu.")
  input()
  cprint('\n               Hello!', 'green', attrs=['blink'])
  input()
  clear()
  cprint("\n      TONIGHT'S SCHEDULE............\n", "blue")
  while command not in debug:
    print(debug)
    command = input("> ")
    if command not in debug:
      print("Invalid command.")
    if command in debug:
      if command == "Color test":
        clear()
        print("              Color test        ")
        cprint("Yellow", "yellow")
        cprint("Green", "green")
        cprint("Red", "red")
        cprint("Blue", "blue")
        cprint("Purple?" " not purple")
        print("White")
        print("There's really no point of of this, since the beginning works just fine")
      if command == "Start Quiz":
        finalquiz()
      if command == "Print telephone listing":
        print("HELP, Tyler Bifolchi")
        print("Tyler Bifolchi is only accessible through some manual rearranging.")
      if command == "Add commands to command list":
          y = input("Type commands to add> ")
          emptylist = y
          print ("The command list is " + emptylist)
      if command == "Reset all variables":
        currentroom = "None"
        dryer = "Off"
        dryer2 = "Off"
        command = 0
        securityinroom = "Main Store"
        light = "In Place"
        securitytick = "Off"
        activated = "Off"
        firstdoor = True
        seconddoor = True
        thirddoor = True
        fourthdoor = True
        doortries = 3
        print("All variables resetted")
      if command == "Set all codes":
        firstcode = random.randint(0,30)
        secondcode = random.randint(0,30)
        thirdcode = random.randint(0,30)
        fourthcode = random.randint(0,30)
        print("All codes unlocked!")      #Skip the whole game
        print("First code is " + str(firstcode))
        print("Second code is " + str(secondcode))
        print("Third code is " + str(thirdcode))
        print("Fourth code is " + str(fourthcode))
        counter = "On"
        hallagain()
      if command == "Emergency Exit":
        firstcode = random.randint(0,30)
        secondcode = random.randint(0,30)
        thirdcode = random.randint(0,30)
        fourthcode = random.randint(0,30)
        print("All codes unlocked!")      #Skip the whole game
        print("First code is " + str(firstcode))
        print("Second code is " + str(secondcode))
        print("Third code is " + str(thirdcode))
        print("Fourth code is " + str(fourthcode))
        counter = "On"
        currentroom = "Emergency Exit"
        emergency()
      if command == "Ending":
        end()
 
Introinput = input("\n\n\nType START to continue ")
if Introinput == "START":
  os.system("cls")
  print ("\n\n\n\n\nNight at the Supermarket")
  print ("By Tyler Bifolchi")
  Introinput = 0
elif Introinput == "HELP":
  clear()
  print("You are a worker at your local supermarket. Your boss told you to go on your 15 minute break, but you accidentally sleep for the rest of your shift. Now when you wake up, the lights are off and the store is closed. You are locked in the supermarket, and now you must find a way out so you can drive back home and go to bed.")
  time.sleep(55)
  exit()
elif Introinput == "statcheck":
  clear()
  commandloop()
  numberpeople = ["Banana Business", "Pinapple People", "Tomato Toppers", "Chocolate Cheerers","Egg Enthusiasts"]
  print("The codes are " + str(firstcode))
  print("Second code is " + str(secondcode))
  print("Third code is " + str(thirdcode))
  print("Fourth code is " + str(fourthcode))
  print("Tries are set to " + str(doortries))
  print("Phone number is " + random.choice(numberpeople))
elif Introinput == "Beef women": #Nice Harry Potter reference
      debugroom()
else:
  os.system("cls")
  print ("\nThe game cannot begin until you type START")
  print ("\nThanks for playing!")
  sleep()
  exit()               # The exit function will return an error in replit, but it should terminate with no problems
input()
clear()
print("     GAMEPLAY TIPS:            ")
print("-Find something to break the Security Machine. IT WATCHES EVERYTHING!")
print("-Check your surroundings. You might look past something right in front of you.")
print("-Think carefully! Any wrong move, and the Security Machine will discover your location!")
print("-Read carefully!")
print("-Type carefully! This game is extremely case sensitive!")
print(" Find your way out of the store. If the Security Machine catches you, it's game over!")
input()
security = "ON"
breakagain()
gamestarted = 1

#The next little piece of code is for DEBUGGING ONLY!
#Remove the comments to enable the debugging feature.
#UPDATE 6/19/2021
#BOTH THE DEBUG VARIABLE AND THE CODE GOES UNUSED
#     if door == ("debug"): 
#       print("Displaying codes collected so far...")
#       print("Code1 is " + str(firstcode))
#     else:
#       print("\nIncorrect combination!")