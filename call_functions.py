#Call a list of phone numbers from a .txt file 

def addNumber:
    import subprocess as sp
    number = ''
    while number != 'q':
        number = input('Number:\nEnter \'q\' to quit.')
    sp.call(['echo ',number,' >> spammers.txt'])
    return

#load phone numbers
def loadPhoneNums:
    import pygooglevoice
    with open(spammers.txt, 'r') as file:
        phoneNumbers = file.read().replace('\n','')
    file.close()
    return recipientNums

#text to speech here and saves the text as an MP3
def speechToText:
    from gtts import gTTS
    import subprocess as sp

    #text = input("What do you want to say?")
    tts = gTTS(text='This is a text', lang='en')
    tts.save('audio.mp3')
    sp.call(['afplay audio.mp3'])    
    
def sendText(recipientNums):
    from googlevoice import Voice
    from googlevoice.util import input

    text = "This is a text"
    #text = input("What do you want to send in an SMS?")

    voice.send_sms(recipientNum,origintext)
    print("SMS sent to "+toNum)

def makeCall(recipient,fromNum):
    
