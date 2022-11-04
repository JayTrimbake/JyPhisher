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

print(yellow,"[+] Starting Cloudflared.....")
print(blue,"""
    Choice Below Options
    
    1.Intel and Ryzen
    2.Termux
    3.Apple Silicon Chip M1/M2
 """)
user1 = input(colored("Here: ",'cyan'))
if user1 == "1":
 os.system("sudo ./cloudflared-linux-amd64 tunnel --url localhost:8484")
if user1 == "2":
 os.system("./cloudflared-linux-arm tunnel --url localhost:8484")
if user1 == "3":
 os.system("sudo ./cloudflared-linux-arm64 tunnel --url localhost:8484")
else:
 print("Thank you")

