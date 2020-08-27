# how we intract with system using python  as  a chat bot 
import os

while True:
    print("Hi, How can i help You.....", end='')
    

    user_choice= input()
    #print(user_choice)
    if("notepad" in user_choice) and (("run" in user_choice)or ("start" in user_choice)):
        print("Notepad is starting....")
        os.system("start Notepad")
        print("Notepad is ready for use")
    elif("chrome" in user_choice) and  (("run" in user_choice) or ("start" in user_choice)):
        print("Chrome is starting...")
        os.system("start chrome")
        print(" Chrome is ready for use")

    elif ("quit" in user_choice) or ("Exit" in user_choice):
        break
    else:
        print("This is Not supported for now")

