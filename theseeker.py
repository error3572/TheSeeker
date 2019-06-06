#!/usr/bin/python3
import pygeoip as location
import time as time
import socket as connect
from ipwhois import IPWhois as whois
from datetime import datetime 
import nmap
import sys
import wget
import socket
class bcolors:
    
    NC='\033[0m' # No Color, reset all
    Bold='\033[1m'
    Underlined='\033[4m'
    Blink='\033[5m'
    Inverted='\033[7m'
    Hidden='\033[8m'
    
    Black='\033[30m'
    Red='\033[31m'
    Green='\033[32m'
    Yellow='\033[33m'
    Blue='\033[34m'
    Purple='\033[35m'
    Cyan='\033[36m'
    LightGray='\033[37m'
    DarkGray='\033[30m'
    LightRed='\033[31m'
    LightGreen='\033[32m'
    LightYellow='\033[93m'
    LightBlue='\033[34m'
    LightPurple='\033[35m'
    LightCyan='\033[36m'
    White='\033[97m'
    
    BckgrDefault='\033[49m'
    BckgrBlack='\033[40m'
    BckgrRed='\033[41m'
    BckgrGreen='\033[42m'
    BckgrYellow='\033[43m'
    BckgrBlue='\033[44m'
    BckgrPurple='\033[45m'
    BckgrCyan='\033[46m'
    BckgrLightGray='\033[47m'
    BckgrDarkGray='\033[100m'
    BckgrLightRed='\033[101m'
    BckgrLightGreen='\033[102m'
    BckgrLightYellow='\033[103m'
    BckgrLightBlue='\033[104m'
    BckgrLightPurple='\033[105m'
    BckgrLightCyan='\033[106m'
    BckgrWhite='\033[107m'
def banner():
    print(bcolors.LightRed+'''
  _______ _                          _             
 |__   __| |                        | |
    | |  | |__   ___   ___  ___  ___| | _____ _ __ 
    | |  | '_ \ / _ \ / __|/ _ \/ _ \ |/ / _ \ '__|
    | |  | | | |  __/ \__ \  __/  __/   <  __/ |
    |_|  |_| |_|\___| |___/\___|\___|_|\_\___|_|
''')
    print(bcolors.LightRed+bcolors.Blink+'       Coded by: Err0r'+bcolors.NC)
banner()
def domaintoip():
    target=input('Enter the domain of the target::>')
    dti=socket.gethostbyname(target)
    print(bcolors.LightYellow+'['+bcolors.Green+'+'+bcolors.LightYellow+']'+bcolors.Cyan+' '+'Ip found!:::'+bcolors.Underlined+dti+bcolors.NC)
def robots():
    url1=input(bcolors.Green+"Enter target's domain name::>")
    url=url1+'robots.txt'
    print(bcolors.Blue+bcolors.BckgrWhite)
    robots = wget.download(url)
    print(bcolors.NC)
def portscan():
     
    target=input('Enter the target::>')
    portr=input('enter the port range::>')
    smode=input('Would you like to switch to stealth mode?(y,n)')
    print (bcolors.Yellow+"Executing a port scan"+bcolors.White)  
    nmscan=nmap.PortScanner()
    if smode=='y':
        nmscan.scan(target,portr,'-A -sS -Pn -v')
    else:
        nmscan.scan(target,portr,'-A -sS -v')
    print(nmscan.scaninfo())
    
def geol():
    target=input('Enter the target::>')
    print (bcolors.Yellow+"Trying to locate the target"+bcolors.White)
    gip=location.GeoIP('GeoLiteCity.dat')
    res=gip.record_by_addr(target)

    for key,val in res.items():
        print(bcolors.LightYellow+'['+bcolors.Green+'+'+bcolors.LightYellow+']'+bcolors.White+' '+f'{key}: {val}')
def whoisinfo():
    target2=input('Enter the target::>')
    obj = whois(target2)
    ret = obj.lookup_rdap(depth=100)
    ret['updated'] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    for key,val in ret.items():
        print(bcolors.LightYellow+'['+bcolors.Green+'+'+bcolors.LightYellow+']'+bcolors.White+' '+f'{key}: {val}'+' \n')    
def byname():
    try:
        print('add functions')
    except Exception as e:
        print(bcolors.Red+f'ERROR: {e}')
def byip():
     
    print("Please enter the target's ip")
    
def choose():
    
    print (bcolors.Green+'''
    1.geolocation
    2.Whois by ip lookup(a little buggy)
    3.Robots.txt downloader
    4.Domain name to ip
    ''')
    choice=input('What option would you like to use?::>')
    if choice=="1":
        try:
            geol()
        except Exception as e:
            print(bcolors.Red+f'ERROR: {e}')        
    if choice=="2":
        try:
            whoisinfo()
        except Exception as e:
            print(bcolors.Red+f'ERROR: {e}')
    if choice=='3':
        robots()
    if choice== '4':
        domaintoip()
    
        
    

    
     
choose()
