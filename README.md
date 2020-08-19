# iiec-project1

## About the project: chatbot
    Problem: - Convert the OS based program into a menu driven program using Python Code which will execute the 
    required user query when user will give the input as a text. 

    -> So my application starts with a warm greeting to the user and then asks for the user's name. 
       * After the introduction and greeting to user the main code starts, my application asks the user to enter the query or 
         command they want to execute (eg. please launch text editor for me).
       * Then the application filters the important keywords from that command and performs the operation specified by the user.
       * The application is capable of opening various softwares which are installed on the system of the user.
       
    -> Edge cases:
        * If the user uses the words such as "dont" or "wont" the the app will not execute that command and will give a 
          sweet response.
        * If the software requsted by the user is not installed in the system, then also the app will not crash (this a taken 
          care with the help of status code which `os.system()` command returns.)
        * If the user enters some weired command then also the app will not crash and will respond with a reply.
        
     -> Features:
        * If user wants to open "web browser" then the app will also ask for the website user wants to open and after taking
          the input it will open the site
        * If the user says something like "i want to paint / draw" then the app will launch MSPaint.
        * All the conversation from the application side are done verbally using the `pyttsx3` module and also the voice is 
          changed from male to female.
        * The application will keep on asking for the input until user wants to exit.
