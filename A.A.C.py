# Adidas Account Creator v2
# Dev: Simmy (bopped) Twitter: @Backdoorcook

import requests, time, os, json, sys
from classes.AdidasGen import AccountGEN
from colorama import *
init()

s = requests.Session()


def log(msg):
    currenttime = time.strftime("%H:%M:%S")
    sys.stdout.write("[%s] %s\n" % (currenttime, str(msg)))
    sys.stdout.flush()


if not os.path.exists("config.json"):
    print "%sConfig.json not Found!!!"  %  (Fore.RED)
    exit()

log("-------------------------------")
log("%sConfiguration loaded.%s" % (Fore.GREEN,Style.RESET_ALL))
with open('config.json') as json_data_file:
    config = json.load(json_data_file)

Start = AccountGEN(s,config)

log("%s%sRegions US | CA | GB | AU%s" % (Style.BRIGHT,Fore.BLUE,Style.RESET_ALL))

Region           = raw_input("Please Select a Region\t").upper()
NumberofAccounts = int(raw_input("Enter Amount Of Accounts To Generate\t"))


log("We are Generating %d Accounts for Region | %s |" % (NumberofAccounts,Region))

if Region == "US":
    Start.US(s,config,NumberofAccounts)
if Region == "UK" or Region == "GB":
    Start.UK(s,config,NumberofAccounts)
if Region == "CA":
    Start.CA(s, config, NumberofAccounts)
if Region == "AU":
    Start.AU(s, config, NumberofAccounts)

else:
    log("%sPlease Check Input!!" % (Fore.RED))






