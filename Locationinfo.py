import urllib.request #importing library urllib
import json #importing library json
import requests #importing library requests
import socket #importing library socket
import os #importing library os

############################## GET INFORMATION OF WIFI #########################################################

def Wlaninfo(): # create function infoWlan
    requestgateway = os.popen("ip -4 route show default").read().split() #use lib os.popen to get router ip and initial value getway
    # this command is stander "ip -4 route show default" of popen
    requestsocket  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)# intia value of socket and libraries first address famaily for ip V4
    #second library is data diagram of UDP connection
    requestsocket.connect((requestgateway[2],0))  # try connection to router to get ip address of router
    ip_address = requestsocket.getsockname()[0]  # get ip address V4 from connection and intial reqest to ip address value
    getway = requestgateway[2]   # intial value reqestgetway to getway value
    host = socket.gethostname()  # requst host of system from library socket using get host name and intial requst to host value
    print("\n")  # new line for space
    print("IP : " + ip_address ,"\n" + "Getway : " + getway, "\n" + "Host : " + host,"\n" )
    #printing all values by new lines
    public_ip = requests.get('http://checkip.amazonaws.com').text.strip() #getting public ip address
    print('public ip : ',public_ip) #printing public_ip
    print("\n") #new line

########### GET INFORMATION OF EXTARNAL IP ###########

def locationinfo(): # create functiom infolocation
    userip = input("Enter Ip Address : ")  # user enter ip Address
    ipextarnal = requests.get('http://checkip.amazonaws.com').text.strip()  # Get information from website
    if userip != '':  # check on ip user entered or getting your information if user enter empty
        ipextarnal = userip  # transfer date userip to ipextarnal
        try:
            socket.inet_aton(ipextarnal)  # check on ip address if it correct or incorrect
            print("ip address is correct")  # printing massage when ip address is correct
        except socket.error: # when ip address incorrect this exception run
            print("ip address is incorrect")  # printing this massage when ip address is incorrect
            ask = input("Do you try again [y/n] : ")  # asking the user if want use script again
            if ask == 'y':  # check on value user entered
                main()  # call main function
            elif ask == 'n':  # check on value user entered
                exit(0)  # exit from script
            else:
                print("you entered different value ")  # printing this massage when entered different
                exit(0)  # exit from script
    Url = 'https://ipinfo.io/' + ipextarnal  #getting information from website as json + ipextarnal to value Url
    response = urllib.request.urlopen(Url)  # transfer all information got to value response
    data = json.load(response)  # loading information from website as json from value response to data value
    # printing out information from data value
    for info in data:
        print(data[info])  # printing result of data value


def main(): #identify function

    print("""

██       ██████   ██████  █████  ████████ ██  ██████  ███    ██     ██ ███    ██ ███████  ██████  
██      ██    ██ ██      ██   ██    ██    ██ ██    ██ ████   ██     ██ ████   ██ ██      ██    ██ 
██      ██    ██ ██      ███████    ██    ██ ██    ██ ██ ██  ██     ██ ██ ██  ██ █████   ██    ██ 
██      ██    ██ ██      ██   ██    ██    ██ ██    ██ ██  ██ ██     ██ ██  ██ ██ ██      ██    ██ 
███████  ██████   ██████ ██   ██    ██    ██  ██████  ██   ████     ██ ██   ████ ██       ██████  @RoxCoderSA 
                                                                                                 """)

    print("""
    
    [1]  Network infomation 

    [2]  Extarnal ip information 

    [99]  Exit 
    
    """)

    choose = int(input("Please choose one of these : "))

    while True:
        if choose == 1:
            Wlaninfo()  # call function
            ask = input("Do you try again [y/n] : ")  # asking the user if want use script again
            if ask == 'y':  # check on value user entered
                main()   # call main function
            elif ask == 'n':  # check on value user entered
                exit(0)  # exit from script
            else:
                print("you entered different value ")  # printing this massage when entered different
                exit(0)  # exit from script
        elif choose == 2:
            locationinfo() # call function
            ask = input("Do you try again [y/n] : ")  # asking the user if want use script again
            if ask == 'y':  # check on value user entered
                main()   # call main function
            elif ask == 'n':  # check on value user entered
                exit(0)  # exit from script
            else:
                print("you entered different value ")  # printing this massage when entered different
                exit(0)  # exit from script
        elif choose == 99:
            exit(0)  # exit from script
        else:
            print('The value not found see you next time :)') #printing massage if the value incorrect
            exit(0) # exit from script

if __name__ == '__main__':
    main()
