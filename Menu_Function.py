def menuFunction(menuTitle, optionList):
    if menuTitle != None:
        print(menuTitle)
    
    for r in range(0, len(optionList)):
        print(f" [{r}], - {optionList[r]}")

    print("[99] - Exit")

    optionChoosen = input('Enter option: ')
    
    return optionChoosen
