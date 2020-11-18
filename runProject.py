import os, time, webbrowser

print("\nrunning runProject.py...")
os.system("say \"running run project dot pie\"")

userNeedsDjango = input("Do you have django installed on your device? Press enter for yes or 'n' for no\n")
if userNeedsDjango:
    os.system("pip3 install django")
    os.system("say \"please wait while we make sure you have django\"")
    time.sleep(8)
print("===============================\nYou now have django\n===============================\n")
os.chdir("src")

os.system("say \"now running unit tests and local server\"")
os.system("python3 manage.py test profiles")
os.system("say \"test results appear above. Opening browser now. Please reload the page\"")
webbrowser.open_new_tab('http://127.0.0.1:8000/')
os.system("python3 manage.py runserver")