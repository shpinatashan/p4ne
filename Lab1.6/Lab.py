import ipaddress
import re
import glob

def Return_IP_adr(str):
    if re.match("^ ip address ([0-9.]+) ([0-9.]+)$", str):
        r = re.match("^ ip address ([0-9.]+) ([0-9.]+)$", str)
        return ipaddress.IPv4Network((r.group(1), r.group(2)),strict = False)
    else:
        return "None"



list_files = glob.glob("C:\\Users\\nv.solomennikova\\Documents\\pythonProject\\p4ne\\Lab1.5\\config_files\\*.txt")
list_result = []
for fl in list_files:
    with open (fl) as f:
        for s in f:
            res = Return_IP_adr(s)
            if res != "None":
                list_result.append(res)



print((list(set(list_result))))



'''
r = re.match("^ ip address ([0-9.]+) ([0-9.]+)$", " ip address 192.168.1.1 255.255.255.0")
print(r.group(2))
res = ipaddress.IPv4Network((r.group(1), r.group(2)),strict = False)

'''