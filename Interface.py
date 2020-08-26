from Functions_Module import *

### Welcome screen
#------------------------------------------------------------------------#

loadingAnimation("Welcome to Network Security Teaching Software", 2, "Loading")

### Menu
#------------------------------------------------------------------------#

optionChoosen = menuFunction("Main Menu", ["Hashing", "RSA", "Digital Signiture"])

### Hashing
#------------------------------------------------------------------------#

if optionChoosen == "1":
    optionChoosen = menuFunction("Hashing Menu", ["From file", "From terminal input"])
    
    if optionChoosen == "1":
        clearTerminal()
        
        print("File entry rules:")
        print(" - ONLY txt is supported") # For now!
        print(" - Do not enter the .txt at the end, otherwise you will get an error")
        
        inputFileName = input("Enter filename or path: ") + ".txt"
        
        inputFile = open(inputFileName, "r")
        
        content = inputFile.readlines()
        
        inputFile.close()
        
        for x in range(0, len(content)):
            if x == 0:
                text = content[x]
            elif x > 0:
                text += " " + content[x]
                
        output = hashText(text)
        
        loadingAnimation(None, 1, "Hashing")
        
        optionChoosen = menuFunction(None, ["Output to file", "Output to terminal"])
        
        if optionChoosen == "1":
            print("File entry rules:")
            print(" - ONLY txt is supported") # For now!
            print(" - Do not enter the .txt at the end, otherwise you will get an error")
            
            outputFileName = input("Enter filename or path: ") + ".txt"
            
            outputFile = open(outputFileName, "w")
            outputFile.write(output)
            
            outputFile.close()
        
        if optionChoosen == 2:
            print(f"Hashed text is: {output}")
    
    if optionChoosen == "2":
        clearTerminal()
        
        text = input("Enter text here: ")
        
        output = hashText(text)
        
        loadingAnimation(None, 1, "Hashing")
        
        optionChoosen = menuFunction(None, ["Output to file", "Output to terminal"])
        
        if optionChoosen == "1":
            print("File entry rules:")
            print(" - ONLY txt is supported") # For now!
            print(" - Do not enter the .txt at the end, otherwise you will get an error")
            
            outputFileName = input("Enter filename or path: ") + ".txt"
            
            outputFile = open(outputFileName, "w")
            outputFile.write(output)
            
            outputFile.close()
        
        if optionChoosen == "2":
            print(f"Hashed text is: {output}")
        
### 
#------------------------------------------------------------------------#       
        