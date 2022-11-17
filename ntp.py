

#Program for implementation of Network Time Protocol 


import ntplib
import time

print("\nConnecting to server...")
link = 'time.google.com'
ntp = ntplib.NTPClient()
time.sleep(2)
print("\nConnected Successfully...")
ntpResponse = ntp.request(link)
print("\nGetting response from server...\n")
time.sleep(2)

if (ntpResponse):
   now = time.ctime()
   print(now)