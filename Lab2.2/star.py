


import ipaddress
import re
import glob
from flask import Flask, jsonify


def Return_IP_adr(str):
    if re.match("^ ip address ([0-9.]+) ([0-9.]+)$", str):
        r = re.match("^ ip address ([0-9.]+) ([0-9.]+)$", str)
        return ipaddress.IPv4Network((r.group(1), r.group(2)), strict=False)
    else:
        return "None"


def Return_hostname(str):
    if re.match("^hostname ", str):
        return str
    else:
        return "None"


list_files = glob.glob("C:\\Users\\nv.solomennikova\\Documents\\pythonProject\\p4ne\\Lab1.5\\config_files\\*.txt")
result = {}
list_host = []

for fl in list_files:
    with open(fl) as f:
        list_result = []
        for s in f:
            res = Return_IP_adr(s)
            if res != "None":
                list_result.append(res)

    with open(fl) as f:
        for sl in f:
            res_host = Return_hostname(sl)
            res = Return_IP_adr(sl)
            if res_host != "None":
                res_host = res_host.replace('\n', '')
                result[res_host] = list_result
                list_host.append(res_host)

print(result)
print(list_host)

str_all = ''
for l in list_host:
    str1 = '<a href="http://127.0.0.1:5000/configs/'+ l +'">' + l +'</a><br>'
    str_all = str_all + str1
print(str1)
print(str_all)


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Welcome"


@app.route('/configs')
def configs():
    return str_all
    #return jsonify(list_host)


@app.route('/configs/<hostname>')
def configs_hostname(hostname):
    return str(result[hostname])


if __name__ == '__main__':
    app.run(debug=True)













