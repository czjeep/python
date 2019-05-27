# coding: utf-8

import re
import requests
from pprint import pprint

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955'
response = requests.get(url, verify=False)
stations = re.findall(r'@[^|]+'   #拼音缩写三位
                    r'\|([^|]+)'#站点名称
                    r'\|([^|]+)'#编码
                    r'\|[^|]+'  #拼音
                    r'\|[^|]+'  #拼音缩写
                    r'\|[^@]+'  #序号
                    ,response.text)
stations = dict(stations)
stations = dict(zip(stations.keys(), stations.values()))
pprint(stations, indent=4)