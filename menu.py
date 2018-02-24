
#print('Success!')
def printMenu():
    import call_functions as cf
   
#menu items here 
    print('Main Menu\n------------------------------')
    print('Options:')
    print('sms\t\tSend SMS')
#    print('call\t\tMake a Call')
    print('audio\t\tChange call audio')
    print('add\t\tAdd Phone Number to List')
    print('load\t\tLoad Phone Numbers')
    print('help\t\tPrint Menu')
    print('q\t\tQuit')

    option = input('~')
 
    if option == 'sms':
        cf.sendText()
#   elif option == 'call':
#       cf.makeCall()
    elif option == 'audio':
        cf.textToSpeech()
    elif option == 'add':
        cf.addNumber()
    elif option == 'load':
        cf.loadPhoneNums()
    elif option == 'help':
        printMenu()
    elif option == 'q':
        exit()
    else:
        print("enter new input")
    option = '~'
    printMenu()

printMenu()
