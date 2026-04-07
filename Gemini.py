import speech_recognition as sr
import google.generativeai as genai
import win32com.client
from dotenv import load_dotenv
import os
import auth
load_dotenv()
API_key = os.getenv("API_KEY") #Loading API key from .env file 
genai.configure(api_key=API_key)
model = genai.GenerativeModel('gemini-2.5-flash')
speaker = win32com.client.Dispatch("SAPI.SpVoice") #configuring text to speech engine
speaker.Rate = 2
print("Welcome To Gemini, write 1 to login, 2 for Registeration, 3 to exit")
database = open("gemini_login.txt", "a").close()
while True:
   decision = input("Login(1), register(2), exit(3)") #main menu
   if decision in ("1", "2", "3"):
       if decision == "1":
        while True: 
            login_status = auth.login()
            if login_status == "l_b":
                break
            if login_status:  
                print("Login successful")
                print("Welcome " + login_status)
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
                                except Exception as e:
                                    print("Coudn't reach Gemini", e)
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
            elif login_status == None:
                print("Login Failed")
                continue
            
       elif decision == "2":
        while True:
            reg_user = auth.register()
            if reg_user == "r_b":
                break
            if reg_user == "r_d":
                break
            elif reg_user == "d_f":
                continue
            elif reg_user == "i_e":
                continue
       elif decision == "3":
           print("Exited")
           break
   else:
        print("pick from the option, Genius 😂")