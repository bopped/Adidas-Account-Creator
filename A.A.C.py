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

#Init
Region           = ""
NumberofAccounts = 0

if len(sys.argv) == 1:
    log("%s[ Auto Mode is now off! ]%s" % (Fore.RED,Style.RESET_ALL))

else:
    try:
        if sys.argv > 1:
            Region           = sys.argv[1]
            NumberofAccounts = int(sys.argv[2])
            [log("Arugement Loaded! Region [ %s%s%s ]" % (Fore.GREEN,Region,Style.RESET_ALL)) if Region != "" else ""]
            [log("Arugement Loaded! Number of Accounts [ %s%s%s ]" % (Fore.GREEN,NumberofAccounts,Style.RESET_ALL)) if Region != "" else ""]
    except:
        log("%sYou Forgot to add Region or Number of accounts in your argument!!%s" % (Fore.RED,Style.RESET_ALL))



if not os.path.exists("config.json"):
    log("%sConfig.json not Found!!!"  %  (Fore.RED))
    exit()

log("-------------------------------")
log("%sConfiguration loaded.%s" % (Fore.GREEN,Style.RESET_ALL))
with open('config.json') as json_data_file:
    config = json.load(json_data_file)

Start = AccountGEN(s,config)

log("%s%sRegions US | CA | GB | AU%s" % (Style.BRIGHT,Fore.BLUE,Style.RESET_ALL))

while True:
    if Region == "":
        Region           = raw_input("Please Select a Region\t").upper()
    Checked = True if Region == "US" or Region == "UK" or Region == "GB" or Region == "CA" or Region == "AU" else False

    if not Checked:
        log("%sSorry the following domain %s is not supported, or you mis-typed!%s" % (Fore.RED,Region,Style.RESET_ALL))
        Region = ""

    if Checked:
        break 

if NumberofAccounts == 0:
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






