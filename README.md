# getinfo
此工具使用https://www.webscan.cc和http://z.zcjun.com这两个网站进行子域名和c段扫描
优点是收集信息时不被对方网站所ban ip
因为我面临中考，这款工具可能会更新的慢，还请谅解

使用方法:
例如扫描子域名和c段
python3 getinfo.py all http://www.baidu.com
只进行子域名扫描
python3 getinfo.py domain http://www.baidu.com
只进行扫描c段
python3 getinfo.py get_c http://www.baidu.com
后续参数待更新......
