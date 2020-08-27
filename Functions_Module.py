### Version Info
# Version: SW 1
# Build Number: 1.0
#------------------------------------------------------------------------#

import hashlib
import base64
import pickle
from time import sleep
import os

#Clears the terminal 
def clearTerminal():
    os.system('cls')


# Define the function to get a loading screen
## redundantText can be set to None is nothing is wanted as the redundant text
def loadingAnimation(redundantText, numberOfAnimationLoops, animatationText):
    
    clearTerminal() # Clears the terminal 

    for a in range(0, numberOfAnimationLoops): # Loops animation for the number specifed
        loadingStr = animatationText # Resets the string to the animationText
        
        for b in range(0, 4): # Code is repeated four times
            loadingStr += "." # An dot is added to the end of the string loading
            
            if redundantText != None: # Checks that redundantText is not None
                print(redundantText) # Prints the redundantText
            
            print(loadingStr) # Prints the loading string
            sleep(0.7) # Sleeps for 0.7 seconds
            clearTerminal() # Clears the terminal
           
           
#Hashes message with sha3_512      
def hashText(text):
    byte_obj = (str(text)).encode()
    hash_obj = hashlib.sha3_512(byte_obj)
    output = hash_obj.hexdigest()
    return output

    
#Reads pickle file with a given name and returns whatever is stored
def readFile(filename):
    try:
        pickle_in = open(str(filename),"rb")
        message_get = pickle.load(pickle_in)
        pickle_in.close()
        return message_get
    except:
        print("Error 1\n For more information, please go to the Error_Documentation.txt file")
        input("Press enter to dismiss")
        
        return "Error 1"


#save given text to a pickle file of a given name
def saveFile(text, filename):
    pickle_out = open(str(filename),"wb")
    pickle.dump(text, pickle_out)
    pickle_out.close()


#A time-saving method to quickly produce an interface for the user of this program
def menuFunction(menuTitle, optionList):
    validInput = 0
    
    while validInput != 1:
        clearTerminal()
        
        if menuTitle != None:
            print(menuTitle)
        
        for r in range(0, len(optionList)):
            print(f" [{r+1}] - {optionList[r]}")

        print("[99] - Exit")

        optionChoosen = input('Enter option: ')
        
        if optionChoosen == "99":
            exit()
        
        try:
            if int(optionChoosen) > 0 and int(optionChoosen) <= (r+1):
                return optionChoosen
            else:
                print("Error 2\n For more information, please go to the Error_Documentation.txt file")
                input("Press enter to dismiss")
        except:
            print("Error 2\n For more information, please go to the Error_Documentation.txt file")
            input("Press enter to dismiss")

    clearTerminal()


##TESTING FUNCTIONS##        
if __name__ == "__main__":
    #Test loading animation
    loadingAnimation("test",4)
    sleep(3)
 
    #Testing Hashing function
    text = "Test"
    print(hashText(text))
