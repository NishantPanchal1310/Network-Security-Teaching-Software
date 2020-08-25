from time import sleep
from Clear_Terminal_Function import clearTerminal

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
            

if __name__ == "__main__":
    loadingAnimation("test")
    sleep(3)
    loadingAnimation(None)