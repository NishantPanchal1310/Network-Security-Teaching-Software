from Functions_Module_WK1 import *
from RSA_module_WK2 import *
from Student_class import *
from signature_Wk3_ver3 import *

studentClassList = open_student_database()

### Welcome screen
#Need to comment everything here, will not be commented at all in the function documentation.
#------------------------------------------------------------------------#

# loadingAnimation("Welcome to Network Security Teaching Software", 2, "Loading")

### Welcome screen
#------------------------------------------------------------------------#

if len(studentClassList) == 0:
    optionChosen = menuFunction(None, ["Create new student"], studentClassList)
    
    if optionChosen == "1":
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
            
        new_keys = gen_key()
        
        pmatch = False
        while pmatch == False:
            password1 = input("Enter password: ")
            password2 = input("Enter password again: ")
            
            if password1 == password2:
                pmatch = True
            elif password1 != password2:
                clearTerminal()
                input("The password do not match please try again\nPress enter to dismiss")
        
        studentClassList.append(new_student(student_name, new_keys[0], new_keys[1], new_keys[2], password1))
        student_number = len(studentClassList) - 1
        
        
elif len(studentClassList) > 0:
    optionChosen = menuFunction(None, ["Login in", "Create new student"], studentClassList)

    if optionChosen == "1":
        student_number = None
        while student_number == None:
            clearTerminal()
            student_logined_in = input("Enter student name: ")
            for i in range(0, len(studentClassList)):
                if studentClassList[i].get_name() == student_logined_in:
                    student_number = i
                    break
            password = input("Enter password: ")
            if password != studentClassList[i].get_password():
                student_number = None

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
            
        new_keys = gen_key()
        
        pmatch = False
        while pmatch == False:
            password1 = input("Enter password: ")
            password2 = input("Enter password again: ")
            
            if password1 == password2:
                pmatch = True
            elif password1 != password2:
                clearTerminal()
                input("The password do not match please try again\nPress enter to dismiss")
        
        studentClassList.append(new_student(student_name, new_keys[0], new_keys[1], new_keys[2], password1))
        student_number = len(studentClassList) - 1

### Menu
#------------------------------------------------------------------------#
while True:
    optionChosen = menuFunction("Main Menu", ["Hashing", "RSA", "Digital Signiture", "Edit user"], studentClassList)

    ### Hashing
    #------------------------------------------------------------------------#
    
    if optionChosen == "1":
        optionChosen = menuFunction("Hashing", ["From file", "From terminal"],studentClassList)
        
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
            
            if optionChosen == "2":
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
                input("press any key to dismiss")
        
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
                        
                output = hashText(text)
                
                optionChosen = menuFunction("Who's key?", ["My private", 'My public', "Someone elses"],studentClassList)
                
                clearTerminal()
                if optionChosen == '1':
                    clearTerminal()

                    optionChosen = menuFunction('Output format', ['Output to file', 'Output to terminal'],studentClassList)
                    if optionChosen == '1':
                        clearTerminal()
                        print("File entry rules:")
                        print(" - ONLY txt is supported") # For now!
                        print(" - Do not enter the .txt at the end, otherwise you will get an error")
                        output = RSA_encode(text, studentClassList[student_number].get_privkey(), studentClassList[student_number].get_nValue())
                        outputFileName = input("Enter filename or path: ") + ".txt"
                        outputFile = open(outputFileName, "w")
                        outputFile.write(output)
                        outputFile.close()
                        input("press any key to dismiss")

                if optionChosen == "2":
                    optionChosen = menuFunction('Output format', ['Output to file', 'Output to terminal'],studentClassList)
                    
                    if optionChosen == '1':
                        print("File entry rules:")
                        print(" - ONLY txt is supported") # For now!
                        print(" - Do not enter the .txt at the end, otherwise you will get an error")
                        output = RSA_encode(text, studentClassList[student_number].get_pubkey(), studentClassList[student_number].get_nValue())
                        outputFileName = input("Enter filename or path: ") + ".txt"
                        outputFile = open(outputFileName, "w")
                        outputFile.write(output)
                        outputFile.close()
                        input("press any key to dismiss")
                        
                    if optionChosen == '2':
                        print(RSA_encode(text, studentClassList[student_number].get_pubkey(), studentClassList[student_number].get_nValue()))
                        input("press any key to dismiss")
                        
                        
                if optionChosen == '2':
                    studentName = input('Enter student name: ')
                    
                    student = search_by_name(studentName,studentClassList)
                    print(RSA_encode(text, student.get_pubkey(), student.get_nValue()))
                    input("press any key to dismiss")

            if optionChosen == '2':
                clearTerminal()
                optionChosen = menuFunction("Who's key?", ["My private", 'My public', "Someone elses"],studentClassList)
                clearTerminal()
                
                if optionChosen == '1':
                    clearTerminal()

                    optionChosen = menuFunction('Output format', ['Output to file', 'Output to terminal'],studentClassList)
                    if optionChosen == '1':
                        clearTerminal()
                        print("File entry rules:")
                        print(" - ONLY txt is supported") # For now!
                        print(" - Do not enter the .txt at the end, otherwise you will get an error")
                        output = RSA_encode(text, studentClassList[student_number].get_privkey(), studentClassList[student_number].get_nValue())
                        outputFileName = input("Enter filename or path: ") + ".txt"
                        outputFile = open(outputFileName, "w")
                        outputFile.write(output)
                        outputFile.close()
                        input("press any key to dismiss")
                    
                    if optionChosen == '2':
                        clearTerminal()
                        print(RSA_encode(text, studentClassList[student_number].get_privkey(), studentClassList[student_number].get_nValue()))
                        input("press any key to dismiss")

                if optionChosen == "2":
                    clearTerminal()

                    optionChosen = menuFunction('Output format', ['Output to file', 'Output to terminal'],studentClassList)
                    if optionChosen == '1':
                        print("File entry rules:")
                        print(" - ONLY txt is supported") # For now!
                        print(" - Do not enter the .txt at the end, otherwise you will get an error")
                        output = RSA_encode(text, studentClassList[student_number].get_pubkey(), studentClassList[student_number].get_nValue())
                        outputFileName = input("Enter filename or path: ") + ".txt"
                        outputFile = open(outputFileName, "w")
                        outputFile.write(output)
                        outputFile.close()
                        RSA_encode(text, studentClassList[student_number].get_pubkey(), studentClassList[student_number].get_nValue())
                        input("press any key to dismiss")
                    
                    if optionChosen == '2':
                        clearTerminal()
                        print(RSA_encode(text, studentClassList[student_number].get_pubkey(), studentClassList[student_number].get_nValue()))
                        input("press any key to dismiss")

                if optionChosen == '3':
                    clearTerminal()
                    studentName = input('Enter student name: ')
                    student = search_by_name(studentName,studentClassList)

                    optionChosen = menuFunction('Output format', ['Output to file', 'Output to terminal'],studentClassList)
                    if optionChosen == '1':
                        print("File entry rules:")
                        print(" - ONLY txt is supported") # For now!
                        print(" - Do not enter the .txt at the end, otherwise you will get an error")
                        output = RSA_encode(text, studentClassList[student_number].get_pubkey(), studentClassList[student_number].get_nValue())
                        outputFileName = input("Enter filename or path: ") + ".txt"
                        outputFile = open(outputFileName, "w")
                        outputFile.write(output)
                        outputFile.close()
                        RSA_encode(text, student.get_pubkey(),student.get_nValue())
                        input("press any key to dismiss")
                    
                    if optionChosen == '2':
                        clearTerminal()
                        print(RSA_encode(text, student.get_pubkey(),student.get_nValue()))
                        input("press any key to dismiss")

                    
        if optionChosen == "2":
            optionChosen = menuFunction("Decrypt", ["From file", "From terminal input"], studentClassList)

            if optionChosen == '1':
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

                optionChosen = menuFunction("Who's RSA key?", ["Your private key", "Someone else's public key"],studentClassList)
                
                loadingAnimation(None, 1, "Hashing")
                
                optionChosen = menuFunction(None, ["Output to file", "Output to terminal"],studentClassList)
                
                if optionChosen == "1":
                    print("File entry rules:")
                    print(" - ONLY txt is supported") # For now!
                    print(" - Do not enter the .txt at the end, otherwise you will get an error")
                    
                    if optionChosen == '1':
                        print("File entry rules:")
                        print(" - ONLY txt is supported") # For now!
                        print(" - Do not enter the .txt at the end, otherwise you will get an error")
                        output = RSA_decode(text, studentClassList[student_number].get_privkey(), studentClassList[student_number].get_nValue())
                        outputFileName = input("Enter file name: ") + ".txt"
                        outputFile = open(outputFileName, "w")
                        outputFile.write(output)
                        outputFile.close()
                        input("press any key to dismiss")
                        
                    if optionChosen == '2':
                        print(RSA_decode(text, studentClassList[student_number].get_privkey(), studentClassList[student_number].get_nValue()))
                        input("press any key to dismiss")
                    
                    outputFile = open(outputFileName, "w")
                    outputFile.write(output)
                    
                    if optionChosen == '1':
                        print("File entry rules:")
                        print(" - ONLY txt is supported") # For now!
                        print(" - Do not enter the .txt at the end, otherwise you will get an error")
                        
                        output = RSA_decode(text, studentClassList[student].get_pubkey(), studentClassList[student].get_nValue())
                        
                        outputFileName = input("Enter file name: ") + ".txt"
                        outputFile = open(outputFileName, "w")
                        outputFile.write(output)
                        outputFile.close()
                        input("press any key to dismiss")
                        
                        
            if optionChosen == '2':
                clearTerminal()
                
                if optionChosen == "2":
                    print(f"Hashed text is: {output}")
                    input("press any key to dismiss")
            
    ### RSA
    #------------------------------------------------------------------------#       
            
            if optionChosen == '1':
                optionChosen = menuFunction('Output format', ['Output to file', 'Output to terminal'],studentClassList)
                if optionChosen == '1':
                    print("File entry rules:")
                    print(" - ONLY txt is supported") # For now!
                    print(" - Do not enter the .txt at the end, otherwise you will get an error")
                    
                    output = RSA_decode(text, studentClassList[student_number].get_privkey(), studentClassList[student_number].get_nValue())
                    
                    outputFileName = input("Enter file name: ") + ".txt"
                    outputFile = open(outputFileName, "w")
                    outputFile.write(output)
                    outputFile.close()
                    input("press any key to dismiss")
                    
                if optionChosen == '2':
                    print(RSA_decode(text, studentClassList[student_number].get_privkey(), studentClassList[student_number].get_nValue()))
                    input("press any key to dismiss")
                    
                    
            if optionChosen == '2':
                optionChosen = menuFunction('Output format', ['Output to file', 'Output to terminal'],studentClassList)
                if optionChosen == '1':
                    print("File entry rules:")
                    print(" - ONLY txt is supported") # For now!
                    print(" - Do not enter the .txt at the end, otherwise you will get an error")
                    
                    output = RSA_decode(text, studentClassList[student].get_pubkey(), studentClassList[student].get_nValue())
                    
                    outputFileName = input("Enter file name: ") + ".txt"
                    outputFile = open(outputFileName, "w")
                    outputFile.write(output)
                    outputFile.close()
                    input("press any key to dismiss")
                
                if optionChosen == '2':
                    print(RSA_decode(text, studentClassList[student].get_pubkey(), studentClassList[student].get_nValue()))
                    input("press any key to dismiss")
                    
### SIGNATURES ###
if optionChosen == '3':
    clearTerminal()
    optionChosen = menuFunction("Digital Signatures", ["Generate Signature", "Check Signature"],studentClassList)

    if optionChosen == '1':
        clearTerminal()
        optionChosen = menuFunction("Who's key?",["My private","Somebody else's public"],studentClassList)
        
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
                    optionChosen = menuFunction('Output format', ['Output to file', 'Output to terminal'],studentClassList)
                    
                    if optionChosen == '1':
                        print("File entry rules:")
                        print(" - ONLY txt is supported") # For now!
                        print(" - Do not enter the .txt at the end, otherwise you will get an error")
                        output = RSA_encode(text, studentClassList[student_number].get_pubkey(), studentClassList[student_number].get_nValue())
                        outputFileName = input("Enter filename or path: ") + ".txt"
                        outputFile = open(outputFileName, "w")
                        outputFile.write(output)
                        outputFile.close()
                        
                    if optionChosen == '2':
                        print(RSA_encode(text, studentClassList[student_number].get_pubkey(), studentClassList[student_number].get_nValue()))
                        input("press any key to dismiss")
                        
                        
                if optionChosen == '2':
                    studentName = input('Enter student name: ')
                    
                    student = search_by_name(studentName,studentClassList)
                    print(RSA_encode(text, student.get_pubkey(), student.get_nValue()))
                    
            if optionChosen == '2':
                clearTerminal()
                optionChosen = menuFunction("Who's public key?", ["Mine", "Someone elses"],studentClassList)
                clearTerminal()
                text = input('Enter text: ')
                
                
                if optionChosen == "1":
                    print(RSA_encode(text, studentClassList[student_number].get_pubkey(), studentClassList[student_number].get_nValue()))
                    input("press any key to dismiss")
                    
                if optionChosen == '2':
                    studentName = input('Enter student name: ')
                    student = search_by_name(studentName,studentClassList)
                    RSA_encode(text, student.get_pubkey(),student.get_nValue())
                    
        if optionChosen == "2":
            optionChosen = menuFunction("Decrypt", ["From file", "From terminal input"], studentClassList)

            if optionChosen == '1':
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

                optionChosen = menuFunction("Who's RSA key?", ["Your private key", "Someone else's public key"],studentClassList)
                
                if optionChosen == '1':
                    optionChosen = menuFunction('Output format', ['Output to file', 'Output to terminal'],studentClassList)
                    
                    if optionChosen == '1':
                        print("File entry rules:")
                        print(" - ONLY txt is supported") # For now!
                        print(" - Do not enter the .txt at the end, otherwise you will get an error")
                        output = RSA_decode(text, studentClassList[student_number].get_privkey(), studentClassList[student_number].get_nValue())
                        outputFileName = input("Enter file name: ") + ".txt"
                        outputFile = open(outputFileName, "w")
                        outputFile.write(output)
                        outputFile.close()
                        
                    if optionChosen == '2':
                        print(RSA_decode(text, studentClassList[student_number].get_privkey(), studentClassList[student_number].get_nValue()))
                        input("press any key to dismiss")
                    
                if optionChosen == '2':
                    studentName = input('Enter student name: ')
                    student = search_by_name(studentName,studentClassList)
                    optionChosen = menuFunction('Output format', ['Output to file', 'Output to terminal'],studentClassList)
                    
                    if optionChosen == '1':
                        print("File entry rules:")
                        print(" - ONLY txt is supported") # For now!
                        print(" - Do not enter the .txt at the end, otherwise you will get an error")
                        
                        output = RSA_decode(text, studentClassList[student].get_pubkey(), studentClassList[student].get_nValue())
                        
                        outputFileName = input("Enter file name: ") + ".txt"
                        outputFile = open(outputFileName, "w")
                        outputFile.write(output)
                        outputFile.close()
                        
                        
            if optionChosen == '2':
                clearTerminal()
                text = input('Enter message: ')
            
                optionChosen = menuFunction('Output', ['To File', 'To Terminal'], studentClassList)
                if optionChosen == '1':
                    clearTerminal()
                    print("File entry rules:")
                    print(" - ONLY txt is supported") # For now!
                    print(" - Do not enter the .txt at the end, otherwise you will get an error")

                    output = gen_sig(text,studentClassList[student].get_pubkey(), studentClassList[student].get_nValue())
                    
                    outputFileName = input("Enter file name: ") + ".txt"
                    outputFile = open(outputFileName, "w")
                    outputFile.write(output)
                    outputFile.close()
                
                text = input('Enter encoded message: ')
                
                optionChosen = menuFunction("Who's RSA key?", ["Your private key", "Someone else's public key"],studentClassList)
                
                if optionChosen == '1':
                    optionChosen = menuFunction('Output format', ['Output to file', 'Output to terminal'],studentClassList)
                    if optionChosen == '1':
                        print("File entry rules:")
                        print(" - ONLY txt is supported") # For now!
                        print(" - Do not enter the .txt at the end, otherwise you will get an error")
                        
                        output = RSA_decode(text, studentClassList[student_number].get_privkey(), studentClassList[student_number].get_nValue())
                        
                        outputFileName = input("Enter file name: ") + ".txt"
                        outputFile = open(outputFileName, "w")
                        outputFile.write(output)
                        outputFile.close()
                        
                    if optionChosen == '2':
                        print(RSA_decode(text, studentClassList[student_number].get_privkey(), studentClassList[student_number].get_nValue()))
                        input("press any key to dismiss")
                        
                        
                if optionChosen == '2':
                    optionChosen = menuFunction('Output format', ['Output to file', 'Output to terminal'],studentClassList)
                    if optionChosen == '1':
                        print("File entry rules:")
                        print(" - ONLY txt is supported") # For now!
                        print(" - Do not enter the .txt at the end, otherwise you will get an error")
                        
                        output = RSA_decode(text, studentClassList[student].get_pubkey(), studentClassList[student].get_nValue())
                        
                        outputFileName = input("Enter file name: ") + ".txt"
                        outputFile = open(outputFileName, "w")
                        outputFile.write(output)
                        outputFile.close()
                    
                    if optionChosen == '2':
                        print(RSA_decode(text, studentClassList[student].get_pubkey(), studentClassList[student].get_nValue()))
                        input("press any key to dismiss")
                        


                    
    ### SIGNATURES ###
    if optionChosen == '3':
        clearTerminal()
        optionChosen = menuFunction("Digital Signatures", ["Generate Signature", "Check Signature"],studentClassList)

        if optionChosen == '1':
            clearTerminal()
            optionChosen = menuFunction("Who's key?",["My private","Somebody else's public"],studentClassList)
            
            if optionChosen == '1':
                clearTerminal()
                optionChosen = menuFunction('Format', ['From File','From Terminal Input'], studentClassList)

                if optionChosen == '1':
                    clearTerminal()

                    print("File entry rules:")
                    print(" - ONLY txt is supported") # For now!
                    print(" - Do not enter the .txt at the end, otherwise you will get an error")

                    output = check_sig(text,studentClassList[student_number].get_privkey(), studentClassList[student_number].get_nValue())
                    
                    outputFileName = input("Enter file name: ") + ".txt"
                    outputFile = open(outputFileName, "w")
                    outputFile.write(output)
                    outputFile.close()
                
                if optionChosen == '2':
                    clearTerminal()
                    text = input('Enter message: ')
                
                    optionChosen == menuFunction('Output', ['To File', 'To Terminal'], studentClassList)
                    if optionChosen == '1':
                        clearTerminal()
                        print("File entry rules:")
                        print(" - ONLY txt is supported") # For now!
                        print(" - Do not enter the .txt at the end, otherwise you will get an error")

                        output = gen_sig(text,studentClassList[student_number].get_privkey(), studentClassList[student_number].get_nValue())
                        
                        outputFileName = input("Enter file name: ") + ".txt"
                        outputFile = open(outputFileName, "w")
                        outputFile.write(output)
                        outputFile.close()
                    
                    if optionChosen == '2':
                        clearTerminal()
                        print(gen_sig(text,studentClassList[student_number].get_privkey(), studentClassList[student_number].get_nValue()))
                        input("press any key to dismiss")

            if optionChosen == '2':
                clearTerminal()
                studentName = input('Enter student name: ')
                student = search_by_name(studentName,studentClassList)

                optionChosen = menuFunction('Format', ['From File','From Terminal Input'], studentClassList)
                if optionChosen == '1':
                    clearTerminal()

                    print("File entry rules:")
                    print(" - ONLY txt is supported") # For now!
                    print(" - Do not enter the .txt at the end, otherwise you will get an error")

                    inputFileName = input("Enter file name: ") + ".txt"

                    inputFile = open(inputFileName, "r")

                    content = inputFile.readlines()

                    inputFile.close()

                    for x in range(0, len(content)):
                        if x == 0:
                            text = content[x]
                        elif x > 0:
                            text += " " + content[x]

                    optionChosen = menuFunction('Output',['To file','To Terminal'],studentClassList)
                    if optionChosen == '1':
                        clearTerminal()
                        
                        print("File entry rules:")
                        print(" - ONLY txt is supported") # For now!
                        print(" - Do not enter the .txt at the end, otherwise you will get an error")

                        output = gen_sig(text,studentClassList[student].get_pubkey(), studentClassList[student].get_nValue())
                        
                        outputFileName = input("Enter file name: ") + ".txt"
                        outputFile = open(outputFileName, "w")
                        outputFile.write(output)
                        outputFile.close()

                    if optionChosen == '2':
                        clearTerminal()
                        print(gen_sig(text,studentClassList[student].get_pubkey(), studentClassList[student].get_nValue()))
                        input("press any key to dismiss")

                if optionChosen == '2':
                    clearTerminal()
                    text = input('Enter message: ')
                
                    optionChosen = menuFunction('Output', ['To File', 'To Terminal'], studentClassList)
                    if optionChosen == '1':
                        clearTerminal()
                        print("File entry rules:")
                        print(" - ONLY txt is supported") # For now!
                        print(" - Do not enter the .txt at the end, otherwise you will get an error")

                        output = gen_sig(text,studentClassList[student].get_pubkey(), studentClassList[student].get_nValue())
                        
                        outputFileName = input("Enter file name: ") + ".txt"
                        outputFile = open(outputFileName, "w")
                        outputFile.write(output)
                        outputFile.close()
                    
                    if optionChosen == '2':
                        clearTerminal()
                        print(gen_sig(text,studentClassList[student].get_pubkey(), studentClassList[student].get_nValue()))
                        input("press any key to dismiss")

        if optionChosen == '2':
            clearTerminal()

            optionChosen = menuFunction("Who's key?",["My private","Somebody else's public"],studentClassList)
            if optionChosen == '1':
                clearTerminal()

                optionChosen = menuFunction('Format', ['From File','From Terminal Input'], studentClassList)
                if optionChosen == '1':
                    clearTerminal()
                    print("File entry rules:")
                    print(" - ONLY txt is supported") # For now!
                    print(" - Do not enter the .txt at the end, otherwise you will get an error")

                    inputFileName = input("Enter file name: ") + ".txt"

                    inputFile = open(inputFileName, "r")

                    content = inputFile.readlines()

                    inputFile.close()

                    for x in range(0, len(content)):
                        if x == 0:
                            text = content[x]
                        elif x > 0:
                            text += " " + content[x]

                    optionChosen = menuFunction('Output', ['To File', 'To Terminal'], studentClassList)
                    if optionChosen == '1':
                        clearTerminal()
                        print("File entry rules:")
                        print(" - ONLY txt is supported") # For now!
                        print(" - Do not enter the .txt at the end, otherwise you will get an error")

                        output = check_sig(text,studentClassList[student_number].get_privkey(), studentClassList[student_number].get_nValue())
                        
                        outputFileName = input("Enter file name: ") + ".txt"
                        outputFile = open(outputFileName, "w")
                        outputFile.write(output)
                        outputFile.close()
                    
                    if optionChosen == '2':
                        clearTerminal()
                        print(check_sig(text,studentClassList[student_number].get_privkey(), studentClassList[student_number].get_nValue()))
                        input("press any key to dismiss")
                    
                if optionChosen == '2':
                    clearTerminal()
                    text = input('Enter message: ')
                
                    optionChosen == menuFunction('Output', ['To File', 'To Terminal'], studentClassList)
                    if optionChosen == '1':
                        clearTerminal()
                        print("File entry rules:")
                        print(" - ONLY txt is supported") # For now!
                        print(" - Do not enter the .txt at the end, otherwise you will get an error")

                        output = check_sig(text,studentClassList[student_number].get_privkey(), studentClassList[student_number].get_nValue())
                        
                        outputFileName = input("Enter file name: ") + ".txt"
                        outputFile = open(outputFileName, "w")
                        outputFile.write(output)
                        outputFile.close()
                    
                    if optionChosen == '2':
                        clearTerminal()
                        print(check_sig(text,studentClassList[student_number].get_privkey(), studentClassList[student_number].get_nValue()))
                        input("press any key to dismiss")
                
            if optionChosen == '2':
                clearTerminal()
                studentName = input('Enter student name: ')
                student = search_by_name(studentName,studentClassList)

                optionChosen = menuFunction('Format', ['From File','From Terminal Input'], studentClassList)
                if optionChosen == '1':
                    clearTerminal()

                    print("File entry rules:")
                    print(" - ONLY txt is supported") # For now!
                    print(" - Do not enter the .txt at the end, otherwise you will get an error")

                    output = check_sig(text,studentClassList[student].get_pubkey(), studentClassList[student].get_nValue())
                    
                    outputFileName = input("Enter file name: ") + ".txt"
                    outputFile = open(outputFileName, "w")
                    outputFile.write(output)
                    outputFile.close()
                
                if optionChosen == '2':
                    clearTerminal()
                    text = input('Enter message: ')
                
                    optionChosen = menuFunction('Output', ['To File', 'To Terminal'], studentClassList)
                    if optionChosen == '1':
                        clearTerminal()
                        print("File entry rules:")
                        print(" - ONLY txt is supported") # For now!
                        print(" - Do not enter the .txt at the end, otherwise you will get an error")

                        output = check_sig(text,studentClassList[student].get_pubkey(), studentClassList[student].get_nValue())                        
                        outputFileName = input("Enter file name: ") + ".txt"
                        outputFile = open(outputFileName, "w")
                        outputFile.write(output)
                        outputFile.close()
                    
                    if optionChosen == '2':
                        clearTerminal()
                        print(check_sig(text,studentClassList[student].get_pubkey(), studentClassList[student].get_nValue()))
                        input("press any key to dismiss")
            
    ## Edit user ##
    if optionChosen == "4":
        optionChosen = menuFunction("User Settings", ["Custom RSA keys", "Change password", "Delete User"], studentClassList)
        if optionChosen == "1":
            new_public_key = input("Enter new public key here: ")
            studentClassList[student_number].edit_pubkey(new_public_key)
            
            new_private_key = input("Enter new private key here: ")
            studentClassList[student_number].edit_privkey(new_private_key)
            
            new_n_value = input("Enter new n value here: ")
            studentClassList[student_number].edit_nValue(new_n_value)
                
        if optionChosen == "2":
            old_password = input("Enter your old password here: ")
            if old_password != studentClassList[student_number].get_password():
                input("Incorrect password!\nAutomatic program shutdown activated\nPress any key to dismiss")
                exit()
            elif old_password == studentClassList[student_number].get_password():
                pmatch = False
                while pmatch == False:
                    clearTerminal()
                    password1 = input("Enter password: ")
                    password2 = input("Enter password again: ")
                    
                    if password1 == password2:
                        pmatch = True
                    elif password1 != password2:
                        clearTerminal()
                        input("The password do not match please try again\nPress any key to dismiss")
        
        if optionChosen == "3":
            old_password = input("Enter your old password here: ")
            if old_password != studentClassList[student_number].get_password():
                input("Incorrect password!\nAutomatic program shutdown activated\nPress enter to dismiss")
                exit()
            elif old_password == studentClassList[student_number].get_password():
                studentClassList.pop(student_number)
                input("Done!\nEnter any key to dimiss")
                save_student_database(studentClassList)
                exit()
                
    save_student_database(studentClassList)
