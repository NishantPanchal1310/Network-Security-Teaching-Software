#SPRINT WEEK 1: BUILD 1.0
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
def loadingAnimation(redundantText, numberOfAnimationLoops):
    
    clearTerminal() # Clears the terminal 

    for a in range(0, numberOfAnimationLoops, ): # Loops animation twice
        loadingStr = "loading" # Resets the string to loading
        
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
def readFilePk(filename):
    try:
        pickle_in = open(str(filename),"rb")
        message_get = pickle.load(pickle_in)
        pickle_in.close()
        return message_get
    except:
        return "File not found"

#save given text to a pickle file of a given name
def saveFilePk(text, filename):
    pickle_out = open(str(filename),"wb")
    pickle.dump(text, pickle_out)
    pickle_out.close()
    
 

##TESTING FUNCTIONS##
#Test loading animation        
if __name__ == "__main__":
    loadingAnimation("test")
    sleep(3)
    loadingAnimation(None)
 
#Testing Hasing function
if __name__ == "__main__":
    text = "Test"
    print(hashText(text))
