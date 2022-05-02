import requests
import re
import sys
import time
from threading import Thread

domain_one=[]
c_=[]

def get_c(url):
    get_ip='http://api.webscan.cc/?action=getip&domain='+url
    get_c_ip='http://api.webscan.cc/?action=query&ip='
    ip=requests.get(get_ip).text.split('"')[3]
    c=requests.get(get_c_ip+ip).text
    obj=re.compile(r'"domain": "(?P<c>.*?)"',re.S)
    r=obj.finditer(c)
    if sys.argv[1] != 'all':
        for i in r:
            print("[*]-[c] :",i.group('c'))
            time.sleep(0.1)
    else:
        for i in r:
            c_.append(i.group('c'))

class get_domain_url(Thread):
    def __init__(self,url,pet) -> None:
        self.url=url
        self.pet=pet
        super().__init__()
    def run(self):
        get_domain_url.domain_one(self.url,self.pet)
    def domain_one(url,pet):
        list_do='http://z.zcjun.com/run.php'
        domain_url='http://z.zcjun.com/run.php?url='
        header={
            'Host':'z.zcjun.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer': f'http://z.zcjun.com/?{url}'
        }
        data={
            'id':1
        }
        list=requests.post(list_do,data=data,headers=header).text
        obj=re.compile(r'"(?P<do>.*?)"',re.S)
        resp=obj.finditer(list)
        for i in resp:
            dom=i.group("do")
            dom_url=dom+'.'+url
            get=requests.get(domain_url+dom_url,headers=header).text
            if "url" in get:
                if pet=='all':
                    #print("[#]-[domain] :",get.split(':')[1].split('"')[1])
                    get_c(get.split(':')[1].split('"')[1])
                    domain_one.append(get.split(':')[1].split('"')[1])
                else:
                    print("[#]-[domain] :",get.split(':')[1].split('"')[1])
                    time.sleep(0.1)
            else:pass

def banner():
    banner='''
_        __
(_)_ __  / _| ___  _ __
| | '_ \| |_ / _ \| '__|
| | | | |  _| (_) | |
|_|_| |_|_|  \___/|_|

'''
    return banner
if __name__=='__main__':
    print(banner())
    print("""
    使用参数：
        all 进行c段和子域名扫描
        domain 只进行扫描子域名
        get_c 只进行c段扫描
         其他参数待更新>>>>>>>
        
        [#]-[eg] : python3 getinfo.py all http://www.baidu.com

    """)
    if sys.argv[1:] != None:
        if len(sys.argv) == 3:
            url=sys.argv[2]
            pet=sys.argv[1]
            if pet == 'domain':
                doma_url='.'.join(url.split('/')[2].split('.')[1:])
                get_domain_url.domain_one(doma_url,pet)
            if pet=='all':
                print("This will take a long time !")
                print("please wait !!")
                doma_url='.'.join(url.split('/')[2].split('.')[1:])
                r=get_domain_url(doma_url,pet)
                r.start()
                for g,i in zip(domain_one,c_):
                    print("[#]-[domain] :",g)
                    print("[*]-[c] :",i)
            if pet =='get_c':
                get_c(url)
        else:sys.exit(0)
    else:sys.exit(0)