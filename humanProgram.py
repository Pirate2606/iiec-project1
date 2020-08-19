# Name - Aditya naitan
# Whatsapp group no. - 31

import os
import pyttsx3

# changing the voice to female voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


pyttsx3.speak("Hi there, please tell me your name")         # asking the name of the user
name = input("\nPlease enter your name: ")                  # taking input for name from the user

# Greetings
print()
pyttsx3.speak("Welcome" + name)
pyttsx3.speak("How can i help you?")

# Driver code
while True:                                               # running the program infinitely until user says exit or some other word with the same meaning

    query = input("\nEnter your query: ")                   # taking input for the query
    query = query.lower()                                 # converting the query to lower case

    if (("dont" in query) or ("wont" in query) or ("don't" in query) or ("won't" in query)):
        pyttsx3.speak("oh, i see that was a trick question")
        pyttsx3.speak("You need anything else?")

    else:
        # notepad
        if (("start" in query) or ("run" in query) or ("launch" in query) or ("execute" in query) or ("open" in query)) and (("notepad" in query) or ("editor" in query)):
            pyttsx3.speak("Here you go")
            pyttsx3.speak("Opening notepad")
            status = os.system("start notepad")
            if status == 1:
                pyttsx3.speak("Notepad is not installed on your system, plz install it and then try again.")
            pyttsx3.speak("You need anything else?")

        # Windows media player
        elif (("start" in query) or ("run" in query) or ("launch" in query) or ("execute" in query) or ("open" in query)) and (("wmplayer" in query) or ("media player" in query) or ("music player") in query):
            pyttsx3.speak("Here you go")
            pyttsx3.speak("Opening windows media player")
            status = os.system("start wmplayer")
            if status == 1:
                pyttsx3.speak("Window media player is not installed on your system, plz install it and then try again.")
            pyttsx3.speak("You need anything else?")

        # Google chrome
        elif (("start" in query) or ("run" in query) or ("launch" in query) or ("execute" in query) or ("open" in query)) and (("chrome" in query) or ("web browser" in query)):
            pyttsx3.speak("Which website you want me to open in google chrome")
            website = input("\tEnter website name: ")
            pyttsx3.speak("Here you go")
            pyttsx3.speak("Opening google chrome")
            status = os.system("start chrome " + website)
            if status == 1:
                pyttsx3.speak("Google chrome is not installed on your system, plz install it and then try again.")
            pyttsx3.speak("You need anything else?")

        # calculator
        elif (("start" in query) or ("run" in query) or ("launch" in query) or ("execute" in query) or ("open" in query)) and (("calculator" in query) or ("calc" in query)):
            pyttsx3.speak("Here you go")
            pyttsx3.speak("Opening calculator")
            status = os.system("start calc")
            if status == 1:
                pyttsx3.speak("Calculator is not installed on your system, plz install it and then try again.")
            pyttsx3.speak("You need anything else?")

        # camera
        elif (("start" in query) or ("run" in query) or ("launch" in query) or ("execute" in query) or ("open" in query)) and (("camera" in query) or ("cam" in query) or ("say cheeze" in query)):
            pyttsx3.speak("Here you go")
            pyttsx3.speak("Opening Camera")
            status = os.system("start microsoft.windows.camera:")
            if status == 1:
                pyttsx3.speak("Camera is not installed on your system, plz install it and then try again.")
            pyttsx3.speak("You need anything else?")

        # msWord
        elif (("start" in query) or ("run" in query) or ("launch" in query) or ("execute" in query) or ("open" in query)) and (("msword" in query) or ("word" in query) or ("winword" in query)):
            pyttsx3.speak("Here you go")
            pyttsx3.speak("Opening M S word")
            status = os.system("start winword")
            if status == 1:
                pyttsx3.speak("microsoft word is not installed on your system, plz install it and then try again.")
            pyttsx3.speak("You need anything else?")

        # msPowerpoint
        elif (("start" in query) or ("run" in query) or ("launch" in query) or ("execute" in query) or ("open" in query)) and (("mspowerpoint" in query) or ("powerpoint" in query) or ("powerpnt" in query)):
            pyttsx3.speak("Here you go")
            pyttsx3.speak("Opening M S powerpoint")
            status = os.system("start powerpnt")
            if status == 1:
                pyttsx3.speak("microsoft power point is not installed on your system, plz install it and then try again.")
            pyttsx3.speak("You need anything else?")

        # msPaint
        elif (("start" in query) or ("run" in query) or ("launch" in query) or ("want" in query) or ("execute" in query) or ("open" in query)) and (("mspaint" in query) or ("paint" in query) or ("draw" in query)):
            pyttsx3.speak("i also love to paint")
            pyttsx3.speak("Opening M S paint")
            status = os.system("start mspaint")
            if status == 1:
                pyttsx3.speak("microsoft power point is not installed on your system, plz install it and then try again.")
            pyttsx3.speak("You need anything else?")

        # python
        elif (("start" in query) or ("run" in query) or ("launch" in query) or ("execute" in query) or ("open" in query)) and (("python" in query) or ("py" in query)):
            pyttsx3.speak("Here you go")
            pyttsx3.speak("Opening python interpreter in C M D")
            status = os.system("start python")
            if status == 1:
                pyttsx3.speak("Python is not installed on your system, plz install it and then try again.")
            pyttsx3.speak("You need anything else?")

        # thankyou
        elif (("thankyou" in query) or ("thanks" in query) or ("thank you" in query)):
            pyttsx3.speak("i am glad that i was of a use to you")
            pyttsx3.speak("pleasure is mine")

        # close the program
        elif (("exit" in query) or ("quit" in query) or ("close" in query) or ("shut" in query)):
            pyttsx3.speak("I hope i was of a use to you.")
            pyttsx3.speak("Thank you")
            break

        # any other request other than above programs
        else:
            pyttsx3.speak("Sorry i don't know how to do that, i am still learning.")
            pyttsx3.speak("You need anything else?")
