import time
from datetime import datetime as dt


ipLocalMachine="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.instagram.com","instagram.com"]
hostsPath="C:\Windows\System32\drivers\etc\hosts"
startTime="09:0.0"
endTime="18:0.0"

now=dt.now()
current_time=now.strftime("%H:%M:%S")#string based time using time library
print(current_time)

while True:
    if(startTime<=current_time and current_time<=endTime):
        print("Working hours")
        with open(hostsPath,"r+")as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(ipLocalMachine+" "+website+"\n")
    else:
        print("Non working hours")
        with open(hostsPath,"r+")as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
    time.sleep(10)