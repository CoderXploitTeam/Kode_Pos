import requests
import json
import os
os.system('clear')
print('''
\t╭┳╮  ╭╮  ╭━╮ ╭━╮
\t┃╭╋━┳╯┣━╮┃╋┣━┫━┫
\t┃╰┫╋┃╋┃┻┫┃╭┫╋┣━┃
\t╰┻┻━┻━┻━╯╰╯╰━┻━╯
''')
print(70*'=')
url='https://kodepos-2d475.firebaseio.com/kota_kab/k69.json?print=pretty'
req=requests.get(url)
jeson=json.loads(req.text)
j=0

for data in jeson:
    j += 1
    print('\tnomor', str(j))
    print('\tKecamatan   :', data['kecamatan'])
    print('\tKelurahan   :', data['kelurahan'])
    print('\tKode Pos    :', data['kodepos'])
    print('\t'+37*'=')