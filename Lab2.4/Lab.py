import ssl
import requests
import urllib3
import requests, json, pprint
from flask import Flask, jsonify


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


host_ip = "10.31.70.210"
login = "restapi"
password = "j0sg1280-7@"

api_url = "/api/v1/global/memory/processes"
r = s.get(host_url + api_url, headers=header, verify=False)

#pprint.pprint(r.json())

list_r = r.json()
list_r = list_r['processes']
sort_list = (sorted(list_r, key=lambda x: x['memory-used'],reverse=True))
#print(len(sort_list))
#print(len(sort_list[0:10]))
#print(sort_list[0:10])

res = sort_list[0:10]


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Welcome"

@app.route('/memory')
def configs():
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)

