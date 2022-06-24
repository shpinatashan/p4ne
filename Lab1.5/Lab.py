import glob

list_files = glob.glob("C:\\Users\\nv.solomennikova\\Documents\\pythonProject\\p4ne\\Lab1.5\\config_files\\*.txt")
str  = " ip address "

list_result = []
for fl in list_files:
    with open (fl) as f:
        for s in f:

            if str in s:
                pos = s.find(str)
                res_s = s.replace(" ip address ", "")
                list_result.append(res_s.strip())


res = list(set(list_result))
print(res)
print('\n'.join(res))





