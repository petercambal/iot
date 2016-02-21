import requests
import json
import uuid
import platform
import re
import time
import socket
import os
import urllib


mac = ':'.join(re.findall('..','%012x' % uuid.getnode()))
uuid = uuid.uuid1()
os = platform.uname()[0]
ip = socket.getfqdn()

data = {}
data['id'] = "27540426-d705-11e5-8565-22000b954b24 "
data['name'] = 'RasPi'
data['description'] = 'Raspberri Pi co mam doma'
# data['mac'] = mac
data['mac_address'] = '22:00:0b:98:81:c4'
data['ip_address'] = ip
data['model'] = 'HP'
data['os'] = os

data['entity_id'] = "2fdd3d68-d6f3-11e5-abe6-22000b97c690"


device1 = {}
device2 = {}
device3 = {}
device4 = {}

device1['id'] = '278c5bd8-c818-11e5-a133-22000b96d1c9'
device1['proxy_id'] = data['id']
device1['name'] = 'Teplotny senzor'

device2['id'] = '33ed9194-c818-11e5-a133-22000b96d1c9'
device2['proxy_id'] = data['id']
device2['name'] = 'Pohybovy senzor'

device3['id'] = '3b84c1a2-c818-11e5-a133-22000b96d1c9'
device3['proxy_id'] = data['id']
device3['name'] = 'Infrecerveny senzor'

device4['id'] = '1365271e-d6f7-11e5-b63a-22000b954b24'
device4['proxy_id'] = data['id']
device4['name'] = 'Modry senzor'

data['devices'] = [device1,device2,device3,device4]

json_data = json.dumps(data)
url = "http://iot.pythonanywhere.com/api/proxy"
headers = {'Content-type': 'application/json'}

response = requests.post(url, data=json_data, headers=headers)
print(response.text)
