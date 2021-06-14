#python 3.7.1
from time import sleep as sp
app=str(input("app: "))
username=str(input("username: "))
import socket
host = socket.gethostname()
ip = socket.gethostbyname(host)
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
all = lower + upper + number 

length = 8
password = "".join(random.sample(all,length))
  

def hacking():
  for h in f"Hacker".upper():
    print(h, end="", flush=True)
    sp(.1)
  hack = f"""
  
 <!--like plz....-->
<html>
 <head> 
  <script src="https://www.{app}.com/62826+{username}?!"></script> 
  <link href="https://www.password.com/css?family=Roboto" rel="stylesheet"> 
  <title>hacking {app}</title> 
 </head> 
 <body> 
  <div id="phone_outer_case"> 
   <div id="phonecase"> 
    <div id="phone"> 
     <div id="loading"> 
      <div id="android_text">
        Ro706 
      </div> 
      <div id="load_icon"></div> 
     </div> 
     <div id="info">
       Ro706 8.1.0 
      <br>[+]ip target :{ip}
      <br>[+]host :{host}
     </div> 
     <div id="time"> 
     </div> 
     <div id="home"> 
      </div> 
     </div> 
    </div> 
   </div> 
  </div> 
 </body>
</html>
+___________________+
|  ACCESS GRANHTED  |
+ ——————————————————+
password :{password}
  """.upper()
  for i in list(hack):
    print(i, end="", flush=True)
    sp(.1)
hacking()
print ("like plz")
