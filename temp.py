# coding=utf-8

"""
    create by wangjiawei
    测试用

"""

import requests


url = 'https://search.damai.cn/searchajax.html'

headers = {
    'Host': 'search.damai.cn',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'content-length': '83',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://search.damai.cn',
    'referer': 'https://search.damai.cn/search.htm?spm=a2oeg.home.card_0.dviewall.591b23e1iGKd0T&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&order=1&cty=%E6%88%90%E9%83%BD',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'keyword': '',
    'cty': '成都',
    'ctl': '',
    'currPage': '2',
    'singleChar': '',
    'tn': '',
    'sctl': '',
    'tsg': '0',
    'order': '1',
}

rsp = requests.post(url, headers=headers, data=data, timeout=30)

print(rsp.status_code)

print(rsp.content.decode('utf-8'))