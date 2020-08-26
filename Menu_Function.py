def menuFunction():

    for r in range(0, len(optionList)):
        print(f"[{r}], - {optionList[r]}")
        print()
    print("[99] - Exit")

    str(option) = input('Enter option: ')
    if option == '99':
        exit()
        
