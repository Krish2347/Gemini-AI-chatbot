import speech_recognition as sr
import google.generativeai as genai
import win32com.client
from dotenv import load_dotenv
import os
load_dotenv()
API_key = os.getenv("API_KEY") #Loading API key from .env file 
genai.configure(api_key=API_key)
model = genai.GenerativeModel('gemini-2.5-flash')
speaker = win32com.client.Dispatch("SAPI.SpVoice") #configuring text to speech engine
speaker.Rate = 2
print("Welcome To Gemini, write 1 to login, 2 for Registeration, 3 to exit")
while True:
   decision = input("Login(1), register(2), exit(3)") #main menu
   if decision in ("1", "2", "3"):
       if decision == "1":
        while True: 
           with open("gemini_login.txt") as Database:
            Login = False
            Login_email = input("Email(E to exit): ")
            Login_password = input("Password: ")
            for line in Database:
              email, password, username = line.strip().split(", ")
              if Login_email == email and Login_password == password:
                    Login = True
           if Login_email == "E" or Login_email == "e":
             print("Ok") 
             break   
           else:
            if Login == True:
                print("Login Successful")
                print("Welcome " + username)
                while True:
                    wish = input("text mode(1) or Voice mode(2), Logout(3)")
                    if wish == "1": 
                        print("type exit to go back")
                        while True:
                            user_Tinput = input("You: ")
                            if user_Tinput == 'exit':
                                print("Exiting...")
                                break
                            else:
                                try:
                                    response = model.generate_content(user_Tinput)
                                    print("Gemini: ", response.text)
                                except:
                                    print("Coudn't reach Gemini, Check Internet Buddy")
                    elif wish == "2":
                        print("Speak something...")
                        r = sr.Recognizer()
                        while True:
                                with sr.Microphone() as source:
                                    audio = r.listen(source)  
                                    try:
                                        user_Input =  r.recognize_google(audio)
                                        print("You said:", user_Input.lower())
                                        if user_Input.lower() == "exit":
                                            print("exiting...")
                                            break
                                        else:
                                            response = model.generate_content(user_Input)
                                            print("Gemini: ", response.text)
                                            reply = response.text
                                            speaker.speak(reply)
                                    except sr.UnknownValueError:
                                        print("Sorry, I could not understand what you said.")
                    elif wish == "3":
                        print("Logging out...")
                        break
            else:
                print("Login Failed")
                continue
            
       elif decision == "2":
        while True:
           Register_email = input("Enter your Email: ")
           if "@" in Register_email and "." in Register_email and Register_email.index("@") < Register_email.rindex("."): #checking if email is valid
                Duplicate = False
                with open("gemini_Login.txt", "r") as Database:
                    for line in Database:
                        if Register_email in line: #checking for Duplicates
                            Duplicate = True
                if Duplicate == True:
                        print("User with this Email already exists")
                        continue
                else:
                        Register_password = input("Choose a password: ")
                        with open("gemini_Login.txt", "a") as Database:
                            Register_Username = input("What should Gemini Call you?: ")
                            Database.write(Register_email + ", " + Register_password + ", " + Register_Username + "\n") #writing the new user to the database
                            print("Registration successful " + Register_Username + " Please login")
                            break
           else:
               print("Invalid Email")
               continue
       elif decision == "3":
           print("Exited")
           break
   else:
        print("pick from the option, Genius 😂")