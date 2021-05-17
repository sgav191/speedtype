import time
import random
from os import system
system("clear")
phrases = ["Your mission, should you choose to accept it.","Desperate times, desperate measures.","Mission Accomplished!","Part of the journey is the end.","It's not about how much we lost. It's about how much we have left.","The hardest choices require the strongest wills.","We'll burn that bridge when we get to it."]
print ("Welcome to speedtype!")
time.sleep(1)
instructionsquestion = input ("Would you like to see some instructions, y/n: ")
if instructionsquestion == "y":
    print (f"You will be given a movie quote to type and you have to type it as fast as you can. There will be {len(phrases)} rounds. Prepare yourself!")
    input("Press enter when you have read through the instructions...")

for currentphrase in phrases:
    system("clear")
    errors = 0
    time.sleep(1)
    print (f"Your phrase to type is '{currentphrase}'")
    input ("Press enter when you're ready...")
    
    starttime = time.time()
    playerphrase = input ("Type here: ")
    endtime = time.time()
    timeroutput = round ((endtime - starttime),2)
    totalwords = currentphrase.split()
    playerwords = playerphrase.split()
    for i in range(len(playerwords)):
        if playerwords[i].lower() == totalwords[i].lower():
            continue
        else:
            errors = errors+1
    if errors == 1:
        
        print (f"Well done! It took you {timeroutput}secs to write the phrase. You wrote a total of {len(totalwords)} words, and there was {errors} mistake.")
    else:
        print (f"Well done! It took you {timeroutput}secs to write the phrase. You wrote a total of {len(totalwords)} words, and there was {errors} mistakes.")
        input("Press enter when you're ready to move on to the next question...")