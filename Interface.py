from Functions_Module_WK1 import *
from RSA_module_WK2 import *
from Student_class import *

studentClassList = open_student_database()  

### Welcome screen
#------------------------------------------------------------------------#

# loadingAnimation("Welcome to Network Security Teaching Software", 2, "Loading")

### Welcome screen
#------------------------------------------------------------------------#

optionChosen = menuFunction(None, ["Login in", "Create new student"], studentClassList)

if optionChosen == "1":
    clearTerminal()
    student_number = None
    while student_number == None:
        student_logined_in = input("Enter student name: ")
        for i in range(0, len(studentClassList)):
            if studentClassList[i].get_name() == student_logined_in:
                student_number = i
                break
elif optionChosen == "2":
    clearTerminal()
    exist = True
    while exist == True:
        student_name = input("Enter new student name: ")
        if len(studentClassList) > 0:
            for i in range(0, len(studentClassList)):
                if student_name not in studentClassList[i].get_name():
                    exist = False
        elif len(studentClassList) == 0:
            exist = False
        
    print("Creating Keys")
    new_keys = gen_key(24)
    
    studentClassList.append(new_student(student_name, new_keys[0], new_keys[1], new_keys[2]))
    student_number = len(studentClassList) - 1

### Menu
#------------------------------------------------------------------------#

optionChosen = menuFunction("Main Menu", ["Hashing", "RSA", "Digital Signiture", "Edit user"], studentClassList)

### Hashing
#------------------------------------------------------------------------#

if optionChosen == "1":
    optionChosen = menuFunction("Hashing Menu", ["From file", "From terminal input"],studentClassList)
    
    if optionChosen == "1":
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
        
        optionChosen = menuFunction(None, ["Output to file", "Output to terminal"],studentClassList)
        
        if optionChosen == "1":
            print("File entry rules:")
            print(" - ONLY txt is supported") # For now!
            print(" - Do not enter the .txt at the end, otherwise you will get an error")
            
            outputFileName = input("Enter filename or path: ") + ".txt"
            
            outputFile = open(outputFileName, "w")
            outputFile.write(output)
            
            outputFile.close()
        
        if optionChosen == 2:
            print(f"Hashed text is: {output}")
    
    if optionChosen == "2":
        clearTerminal()
        
        text = input("Enter text here: ")
        
        output = hashText(text)
        
        loadingAnimation(None, 1, "Hashing")
        
        optionChosen = menuFunction(None, ["Output to file", "Output to terminal"],studentClassList)
        
        if optionChosen == "1":
            print("File entry rules:")
            print(" - ONLY txt is supported") # For now!
            print(" - Do not enter the .txt at the end, otherwise you will get an error")
            
            outputFileName = input("Enter filename or path: ") + ".txt"
            
            outputFile = open(outputFileName, "w")
            outputFile.write(output)
            
            outputFile.close()
        
        if optionChosen == "2":
            print(f"Hashed text is: {output}")
        
### RSA
#------------------------------------------------------------------------#       
        
if optionChosen == "2":
    optionChosen = menuFunction("RSA", ["Encrypt", "Decrypt"],studentClassList)
    
    if optionChosen == "1":
        
        optionChosen = menuFunction("Encrypt message", ["From file", "From terminal input"], studentClassList)
        
        if optionChosen == "1":
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
            
            optionChosen = menuFunction("Who's public key?", ["Mine", "Someone elses"],studentClassList)
            
            if optionChosen == "1":
                print(RSA_encode(text, studentClassList[student_number].get_pubkey(), studentClassList[student_number].get_nValue()))
               
            if optionChosen == '2':
                studentName == input('Enter student name: ')
                
                student = search_by_name(studentName,studentClassList)
                print(RSA_encode(text, student.get_pubkey(), student.get_nValue()))
                
         if optionChosen == '2':
            clearTerminal()
            
            
            
            
                
            
           
        

if optionChosen == "2":
    e = input(' ')
    d = input(' ')
    n = input(' ')
  
    if optionChosen == '1':
        M = input('Enter message: ')
        optionChosen = menuFunction(None,['Print to Terminal','Export to File'])

        if optionChosen == '1':
            encoder = RSA_encode(M,e,n)
            print(encoder)
        
        if optionChosen == '2':
            output = RSA_encode(M,e,n)
            
            print("File entry rules:")
            print(" - ONLY .txt is supported") # For now!
            print(" - Do not enter the .txt at the end, otherwise you will get an error")

            outputFileName = input('Enter file name or path: ') + '.txt'           
            outputFile = open(outputFileName, "w")
            outputFile.write(output)
            
            outputFile.close()

    if optionChosen == '2':
        print("File entry rules:")
        print(" - ONLY .txt is supported") # For now!
        print(" - Do not enter the .txt at the end, otherwise you will get an error")
        inputFileName = input('Enter file name: ') + ".txt"

        inputFile = open(inputFileName, 'r')
        content = inputFile.readlines()
        inputFile.close()
    
        for x in range(0, len(content)):
            if x == 0:
                text = content[x]
            elif x > 0:
                text += " " + content[x]

        RSA_encode(content,e,n)            
            
            
            
            
            
            
            
            
            
            '''
            optionChosen = menuFunction(None, ["Output to file", "Output to terminal"], studentClassList)
            
            if optionChosen == "1":
                print("File entry rules:")
                print(" - ONLY txt is supported") # For now!
                print(" - Do not enter the .txt at the end, otherwise you will get an error")
                
                outputFileName = input("Enter filename or path: ") + ".txt"
                
                outputFile = open(outputFileName, "w")
                outputFile.write(output)
                
                outputFile.close()
            
            if optionChosen == 2:
                print(f"Hashed text is: {output}")
        
        if optionChosen == "2":
            clearTerminal()
            
            text = input("Enter text here: ")
            
            output = hashText(text)
            
            loadingAnimation(None, 1, "Hashing")
            
            optionChosen = menuFunction(None, ["Output to file", "Output to terminal"], studentClassList)
            
            if optionChosen == "1":
                print("File entry rules:")
                print(" - ONLY txt is supported") # For now!
                print(" - Do not enter the .txt at the end, otherwise you will get an error")
                
                outputFileName = input("Enter filename or path: ") + ".txt"
                
                outputFile = open(outputFileName, "w")
                outputFile.write(output)
                
                outputFile.close()
            
            if optionChosen == "2":
                print(f"Hashed text is: {output}")
            '''
            
            
            
            
save_student_database(studentClassList)
