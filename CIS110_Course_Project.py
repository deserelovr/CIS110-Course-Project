print ("Hey there my friend, I hope you are ready for story time!")
print("Before we get to the story, I have some questions to ask.")
print('They are simple ones I promise.')
print("After you enter the answer to the question press the enter key.")
input("\nPress enter key to continue....")


playagin = 'yes'
while playagin.lower() == 'yes':
    tday = input("\nWhat day of the week is it?")
    while (len(tday) == 0):
        tday = input('Please enter a day of the week:')

    dogName = input("\nWhat is the dog name?")
    while (len(dogName) == 0):
        dogName = input('Please enter a dogs name: ')

    city = input("\nWhat is your home city?")
    while (len(city) == 0):
        city = input('Please enter your home city:')   

    hobby = input("\nWhat is your favorite project based activity to do at home?")
    while (len(hobby) == 0):
        hobby = input('Please enter a project based hobby:')

    num = input("\nEnter a number between 1-15: ")
    while not num.isdigit():
        num = input('Please enter a numeric value:')

    ownerName = input("\nWhat is your name?")
    while (len(ownerName) == 0):
        ownerName = input('Please enter your name:')

    print("\nNow that the questions are done.....Lets get to the story!")
    print('\nOn this one random nice' , tday, "your dog" , dogName , "was home with " , ownerName, " their loving owner.")
    print("\nSo today, " + str(dogName) + "throught it would be a great idea to see if they could be just like you.")
    print('Once you finally moved from the room after completing your latest project, ' + str(dogName) + " took this as a chance to see if they could do it just like you.")

    makeAchoice = input('Should ' + str(dogName) + " try to make the same project?")

    if makeAchoice == "yes":
        print('\nwhile you was resting in the other room. ')
        print("\nYou hear noise coming from the room so you get up to see what it is")
        print("\nWhen you did finally get up to see what the noise was you see " + str(dogName) + " trying to make the same project that you just finished")
        print("\nJust when you was about to yell, " + str(dogName) + ' must have felt you looking at them.')
        print(' Next thing you know they drop everything and run right out the room.')
        print("\nWhen  " + str(dogName) + " left out the room, they caught the zoomies.")
        print("\nJust when you thought it could not get any worst " + str(dogName) + " is running around knocking over everything in their path.")
        print("\nYou started to yelling stop but it did not work at first.")
        print(str(dogName) + " manage to break " + str(num) + "items in the room. After you had to yell stop 2 more times " + str(dogName) + " finally stop fore completely trashing the room.") 
    
    else:
        print("After standing there thinking " + str(dogName) + " decides it is to risky to " + str(hobby) + "so they just walked away.")
        print("Being to afraid of getting caught, " + str(dogName) + " choices to roll around the house for " + str(num) + "minutes.")
        print("Unfortunately, there was no fun in rolling around. So " + str(dogName) + " decides to stop and get ready to start exploring the city.")

    print("\nAfter walking two blocks " + str(dogName) + " saw the local Ice cream shop that yall always pass." )

    getTheCream = input("Should " + str(dogName) + " go get some ice cream?")

    if getTheCream == ("yes"):
        print("\nWhen " +str(dogName) + " walks-in, they are greeted with a smile and a friendly voice." )
        print("\nAt first they are scared, but " +str(dogName) + " ends up having the time of their life eating all of their favorite ice cream.")
        print(str(dogName) + " gets in line " + str(num) + " of times. Surprising, no one was even bothered by " +str(dogName) + " being at the ice cream shop.")

    else:
        print("After standing outside " + str(dogName) + " realized that they was to scared to go inside.")
        print("Being too afraid of all the people and thinking someone might call the police, " +str(dogName) + " decides to just keep walking trying not to make a scene.")
    
    if makeAchoice == 'yes' and getTheCream == 'yes':
        print('\nAfter spending the day making a  ' + str(hobby) + 'walking around ' + str(city) + " and stopping at the Ice Cream shop, " + str(dogName) + "was seen by your friend.")
        print("\nLuckily, your friend reconized " , dogName , "and saw your name " + str(ownerName) + " on the collar.")
        print(str(dogName) + "was brought home with a full belly and happy to see you.")

    elif makeAchoice == 'yes':
        print("\nAfter spending the day making a " , hobby , " and walking around " + str(city) + "someone you knew found your dog.")
        print("Your friend reconized " , dogName , "and saw your name  " , ownerName , "on the collar.")
        print(str(dogName) + ' was brought home without causing any trouble.')
    else:
        print('\nAfter making a mess in the house' , dogName , ' and taking a sroll around town.')
        print("Your friend reconized " , dogName , "and saw your name " , ownerName , "on the collar.")
        print(str(dogName) + ' was brought home without causing any trouble.')
        print('You realized you really have a great dog.')

    playagin = input('\nWould you like to play again? Enter yes or no: ')
    while playagin.lower() !='yes' and playagin.lower() != 'no':
        playagin = input('Enter yes or no: ')