import urllib.request
import json
from subprocess import call
import time

header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
url = "https://www.airbnb.com/api/core_guest_spa/all_phrases"
headers={'User-Agent':user_agent,} 

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
contents = response.read().decode('utf-8') # The data u need

parsed = json.loads(contents)
del parsed['not_licensed_to_provide_booking_service']
del parsed['online.cc:initial.info']

out = json.dumps(parsed, indent=4, sort_keys=True)

output1 = open("all_phrases.json","w")

output1.write(out)
output1.flush()
output1.close()

time.sleep(10)

call('git add .', shell = True)
call('git commit -m "commiting..."', shell = True)
call('git push origin master', shell = True)
