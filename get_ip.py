# --coding:utf-8--
#   @Author:    Alpaca
#   @Time:      2023/4/5 16:23
#   @Software:  PyCharm
#   @File:      get_ip

import setting
import requests
from lxml import etree
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 '
                  'Safari/537.36 Edg/111.0.1661.62',
}

resp = requests.get(setting.IP_PROVIDE_URL[0], headers=headers)
resp.encoding = 'gbk'
uuu = resp.text.encode('utf-8')
text = uuu.decode('utf-8')

tree = etree.HTML(resp.text)
tree_list = tree.xpath('//*[@id="main"]/div[1]/div[2]/div[1]/table/tr/td[1]/text()|//*[@id="main"]/div[1]/div[2]/div['
                      '1]/table/tr/td[2]/text()|//*[@id="main"]/div[1]/div[2]/div[1]/table/tr/td[3]/text()')[3:]

ip_list = []
for i in range(0, len(tree_list), 3):
    ip_list.append({
        'ip': str(tree_list[i]),
        'prot': str(tree_list[i+1]),
        # 'address': str(tree_list[i+2]),
    })

with open('ip.json', mode='w', encoding='gbk') as f:
    json.dump(ip_list, f)
