import requests, json, pprint

import ssl
import requests
import urllib3

from urllib3.poolmanager import PoolManager
from requests.adapters import HTTPAdapter

class Ssl1HttpAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections, maxsize=maxsize, block=block, ssl_version=ssl.PROTOCOL_TLSv1)

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'

s = requests.Session()
s.mount("https://10.31.70.210:55443", Ssl1HttpAdapter())


host_ip = '10.31.70.210'
login = 'restapi'
password = 'j0sg1280-7@'
host_url = 'https://' + host_ip + ':55443'

r = s.post(host_url + '/api/v1/auth/token-services', auth=(login, password), verify=False)
token = r.json()["token-id"]

header = {"content-type": "application/json", "X-Auth-Token": token}
r = s.get(host_url + '/api/v1/interfaces', headers=header, verify=False)

#pprint.pprint(r.json())


list_r = r.json()


intr_name = []
m = len(list_r['items'])
for l in range(m):
    intr_name.append(list_r['items'][l]['if-name'])

#print(intr_name)

list_st = []
for l in range(m):
    r_st = s.get(host_url + '/api/v1/interfaces/'+intr_name[l]+'/statistics', headers=header, verify=False)
    list_st.append(r_st.json())

print(list_st)

m = len(list_st)
res = []
for l in range(m):
    res.append('if-name: '+list_st[l]['if-name']+' out-total-packets: '+str(list_st[l]['out-total-packets'])+' in-total-packets: '+str(list_st[l]['in-total-packets']))

print('\n'.join(res))

