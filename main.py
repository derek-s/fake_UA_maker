#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 14:40
# @Author  : Derek.S
# @Site    : 
# @File    : main.py

import yaml
import random
import string
import time

# read yml config file
with open("_config.yml", "r", encoding="utf-8") as config_file:
    config = yaml.load(config_file)
config_file.close()


net_type = ['4G', 'WIFI']


# random Windows Version
def random_Windows_Ver():
    config_OS_Windows = config["OS"]["Windows"]
    rand_Ver = random.choice(config_OS_Windows)
    return rand_Ver


# random Mac Version
def random_Mac_Ver():
    config_OS_Mac = config["OS"]["OSX"]
    rand_Ver = random.choice(config_OS_Mac)
    return rand_Ver


# random Android Phone
def random_Android():
    config_Android_list = config["Android"]
    rand_Phone = random.choice(config_Android_list)
    return rand_Phone


# random Android OS Version
def random_Android_OS():
    config_Android_OS = config["AndroidOS"]
    rand_Ver = random.choice(config_Android_OS)
    return rand_Ver


# random iOS Version
def random_iOS_Version():
    config_iOS_Ver = config["iOS"]
    rand_Ver = random.choice(config_iOS_Ver)
    return rand_Ver


# random iPhone MoblieKey
def random_iPhoneKey(length=8):
    rand_Key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
    return rand_Key


# random Chrome Version
def random_Chrome_Ver():
    config_Ver_range_low = int(config["ChromeVer"][0])
    config_Ver_range_high = int(config["ChromeVer"][1])
    rand_Ver = '{0}.{1}.{2}.{3}'.format(
        random.randint(config_Ver_range_low, config_Ver_range_high),
        random.randint(0, 9),
        random.randint(1000, 9000),
        random.randint(10, 99)
    )
    return rand_Ver


# random Webkit/Safari Version
def random_WebkitVer():
    rand_Ver = '{0}.{1}'.format(
        random.randint(400, 999),
        random.randint(0, 99)
    )
    return rand_Ver


# random Firefox Version
def random_Firefox_Ver():
    config_Ver_range_low = int(config["FirefoxVer"][0])
    config_Ver_range_high = int(config["FirefoxVer"][1])
    rand_Ver = '{}.0'.format(random.randint(
        config_Ver_range_low, config_Ver_range_high
    ))
    return rand_Ver


# random 360Brower Version
def random_Qihu_Ver():
    rand_Ver = random.choice(['EE', 'SE'])
    return rand_Ver


# random 2345Explorer Version
def random_2345_Ver():
    config_Ver_range_low = int(config["Brower2345V"][0])
    config_Ver_range_high = int(config["Brower2345V"][1])
    rand_Ver = '{0}.{1}.{2}.{3}'.format(
        random.randint(config_Ver_range_low, config_Ver_range_high),
        random.randint(0, 9),
        random.randint(0, 9),
        random.randint(0, 99999)
    )
    return rand_Ver


# random sougou Version
def random_Sougou_Ver():
    rand_Ver = 'SE {0}.X MetaSr {1}.{2}'.format(
        random.randint(1, 9),
        random.randint(1, 9),
        random.randint(1, 9)
    )
    return rand_Ver


# random qqbrower Version
def random_QQbrower_Ver():
    rand_Ver = '{0}.{1}.{2}.{3}'.format(
        random.randint(1, 10),
        random.randint(0, 99),
        random.randint(0, 9999),
        random.randint(0, 999)
    )
    return rand_Ver


# random baiduBrower Version
def random_Baidu_Ver():
    rand_Ver = '{0}.{1}'.format(
        random.randint(1, 99),
        random.randint(1, 99)
    )
    return rand_Ver


# random Maxthon Version
def random_Maxthon_Ver():
    rand_Ver = '{0}.{1}.{2}.{3}'.format(
        random.randint(5, 9),
        random.randint(0, 9),
        random.randint(0, 9),
        random.randint(0, 9999)
    )
    return rand_Ver


# random UC Version
def random_UC_Ver():
    rand_Ver = '{0}.{1}.{2}.{3}'.format(
        random.randint(5, 15),
        random.randint(0, 9),
        random.randint(0, 9),
        random.randint(0, 999)
    )
    return rand_Ver


# random MQQ Version
def random_MQQ_Ver():
    rand_Ver = '{0}.{1}.{2}'.format(
        random.randint(7, 9),
        random.randint(1, 9),
        random.randint(0, 99)
    )
    return rand_Ver

def random_MBaidu_Ver():
    rand_Ver = '{0}.{1}.{2}.{3}'.format(
        random.randint(7, 15),
        random.randint(0, 9),
        random.randint(0, 9),
        random.randint(0, 99)
    )
    return rand_Ver

def random_MBaidu_T():
    rand_Ver = '{0}.{1}'.format(
        random.randint(7, 9),
        random.randint(0, 9)
    )
    return rand_Ver

class fake_UA_maker:
    def chrome_pc_windows(self):
        ua_string = "Mozilla/5.0 (Windows NT {WinVer}; Win64; x64) " \
                    "AppleWebKit/{WebkitVer} (KHTML, like Gecko) " \
                    "Chrome/{ChromeVer} " \
                    "Safari/{WebkitVer}"
        return ua_string.format(
            **{"WinVer": random_Windows_Ver(), "WebkitVer": random_WebkitVer(), "ChromeVer": random_Chrome_Ver()}
        )

    def chrome_pc_linux(self):
        ua_string = "Mozilla/5.0 (X11; Linux x86_64) " \
                    "AppleWebKit/{WebkitVer} (KHTML, like Gecko) " \
                    "Chrome/{ChromeVer} " \
                    "Safari/{WebkitVer}"
        return ua_string.format(
            **{"ChromeVer": random_Chrome_Ver(), "WebkitVer": random_WebkitVer()}
        )

    def chrome_mac(self):
        ua_string = "Mozilla/5.0 (Macintosh; Intel Mac OS X {MacVer}) " \
                    "AppleWebKit/{WebkitVer} (KHTML, like Gecko) " \
                    "Chrome/{ChromeVer} " \
                    "Safari/{WebkitVer}"
        return ua_string.format(
            **{
                "MacVer": random_Mac_Ver(),
                "ChromeVer": random_Chrome_Ver(),
                "WebkitVer": random_WebkitVer()}
        )

    def mobile_chrome_android(self):
        ua_string = "Mozilla/5.0 (Linux; Android {AndroidVersion}; {AndroidPhone}) " \
                    "AppleWebKit/{WebkitVer} (KHTML, like Gecko) " \
                    "Chrome/{ChromeVer} Mobile Safari/{WebkitVer}"
        return ua_string.format(
            **{
                "AndroidVersion": random_Android_OS(),
                "AndroidPhone": random_Android(),
                "WebkitVer": random_WebkitVer(),
                "ChromeVer": random_Chrome_Ver()
            }
        )

    def mobile_chrome_iPhone(self):
        ua_string = "Mozilla/5.0 (iPhone; CPU iPhone OS {iOSVer} like Mac OS X) " \
                    "AppleWebKit/{WebkitVer} (KHTML, like Gecko) " \
                    "CriOS/{ChromeVer} Mobile/{iPhoneKey} Safari/{WebkitVer}"
        return ua_string.format(
            **{
                "iOSVer": random_iOS_Version(),
                "iPhoneKey": random_iPhoneKey(8),
                "WebkitVer": random_WebkitVer(),
                "ChromeVer": random_Chrome_Ver()
            }
        )

    def internet_explorer(self):
        ua_list = [
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv 11.0) like Gecko',
            'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)'
        ]
        rand_UA_String = random.choice(ua_list)
        return rand_UA_String

    def firefox_pc_windows(self):
        ua_string = "Mozilla/5.0 (Windows NT {WinVer}; WOW64; rv:{FirefoxVer}) Gecko/20100101 Firefox/{FirefoxVer}"
        return ua_string.format(
            **{"WinVer": random_Windows_Ver(), "FirefoxVer": random_Firefox_Ver()}
        )

    def firefox_pc_linux(self):
        ua_string = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:{FirefoxVer}) Gecko/20100101 Firefox/{FirefoxVer}"
        return ua_string.format(
            **{"FirefoxVer": random_Firefox_Ver()}
        )

    def firefox_mac(self):
        ua_string = "Mozilla/5.0 (Macintosh; Intel Mac OS X {MacVer}; rv:{FirefoxVer}) Gecko/20100101 Firefox/{FirefoxVer}"
        return ua_string.format(
            **{"MacVer": random_Mac_Ver(), "FirefoxVer": random_Firefox_Ver()}
        )

    def safari_mac(self):
        ua_string = "Mozilla/5.0 (Macintosh; Intel Mac OS X {MacVer} " \
                    "AppleWebKit/{WebkitVer} (KHTML, like Gecko) " \
                    "Version/{SafariVer} Safari/{WebkitVer}"
        return ua_string.format(
            **{
                "MacVer": random_Mac_Ver(),
                "WebkitVer": random_WebkitVer(),
                "SafariVer": '{0}.{1}'.format(
                    random.randint(10, 11),
                    random.randint(0, 9)
                )
            }
        )

    # 360se/ee
    def qihu360(self):
        ua_string = "Mozilla/5.0 (Windows NT {WinVer}; WOW64) " \
                    "AppleWebKit/{WebkitVer} (KHTML, like Gecko) " \
                    "Chrome/{ChromeVer} " \
                    "Safari/{WebkitVer} QIHU 360{Brower360Ver}"

        return ua_string.format(
            **{
                "WinVer": random_Windows_Ver(),
                "ChromeVer": random_Chrome_Ver(),
                "WebkitVer": random_WebkitVer(),
                "Brower360Ver": random_Qihu_Ver()}
        )

    # 2345 Explorer
    def Brower2345(self):
        ua_string = "Mozilla/5.0 (Windows NT {WinVer}; WOW64) " \
                    "AppleWebKit/{WebkitVer} (KHTML, like Gecko) " \
                    "Chrome/{ChromeVer} Safari/537.36 " \
                    "2345Explorer/{Brower2345Ver}"
        return ua_string.format(
            **{
                "WinVer": random_Windows_Ver(),
                "WebkitVer": random_WebkitVer(),
                "ChromeVer": random_Chrome_Ver(),
                "Brower2345Ver": random_2345_Ver()
            }
        )

    # liebao Brower
    def liebao(self):
        ua_string = "Mozilla/5.0 (Windows NT {WinVer}; WOW64) " \
                    "AppleWebKit/{WebkitVer} (KHTML, like Gecko) " \
                    "Chrome/{ChromeVer} " \
                    "Safari/{WebkitVer} LBBROWSER"

        return ua_string.format(
            **{
                "WinVer": random_Windows_Ver(),
                "WebkitVer": random_WebkitVer(),
                "ChromeVer": random_Chrome_Ver(),
            }
        )

    def sougou(self):
        ua_string = "Mozilla/5.0 (Windows NT {WinVer}; WOW64) " \
                    "AppleWebKit/{WebkitVer} (KHTML, like Gecko) " \
                    "Chrome/{ChromeVer} " \
                    "Safari/{WebkitVer} {SougouVer}"
        return ua_string.format(
            **{
                "WinVer": random_Windows_Ver(),
                "WebkitVer": random_WebkitVer(),
                "ChromeVer": random_Chrome_Ver(),
                "SougouVer": random_Sougou_Ver()
            }
        )

    def qqbrower(self):
        ua_string = "Mozilla/5.0 (Windows NT {WinVer}; WOW64) " \
                    "AppleWebKit/{WebkitVer} (KHTML, like Gecko) " \
                    "Chrome/{ChromeVer} " \
                    "Safari/{WebkitVer} " \
                    "Core/{QQbrowerVer} QQBrowser/{QQbrowerVer}"

        return ua_string.format(
            **{
                "WinVer": random_Windows_Ver(),
                "WebkitVer": random_WebkitVer(),
                "ChromeVer": random_Chrome_Ver(),
                "QQbrowerVer": random_QQbrower_Ver()
            }
        )

    def baidubrower(self):
        ua_string = "Mozilla/5.0 (Windows NT {WinVer}; WOW64) " \
                    "AppleWebKit/{WebkitVer} (KHTML, like Gecko) " \
                    "Chrome/{ChromeVer} " \
                    "BIDUBrowser/{BaiduVer} " \
                    "Safari/{WebkitVer}"
        return ua_string.format(
            **{
                "WinVer": random_Windows_Ver(),
                "WebkitVer": random_WebkitVer(),
                "ChromeVer": random_Chrome_Ver(),
                "BaiduVer": random_Baidu_Ver()
            }
        )

    def maxthon(self):
        ua_string = "Mozilla/5.0 (Windows NT {WinVer}; WOW64) " \
                    "AppleWebKit/{WebkitVer} (KHTML, like Gecko) " \
                    "Chrome/{ChromeVer} " \
                    "Safari{WebkitVer} " \
                    "Maxthon/{MaxthonVer}"
        return ua_string.format(
            **{
                "WinVer": random_Windows_Ver(),
                "WebkitVer": random_WebkitVer(),
                "ChromeVer": random_Chrome_Ver(),
                "MaxthonVer": random_Maxthon_Ver()
            }
        )

    def wechat_Android(self):
        ua_string = "Mozilla/5.0 (Linux; Android {AndroidVersion}; {AndroidPhone}) " \
                    "AppleWebKit/{WebKitVer} (KHTML, like Gecko) Version/4.0 " \
                    "Chrome/{ChromeVer} MQQBrowser/6.2 TBS/{TBS} Mobile Safari/{WebKitVer} " \
                    "MicroMessenger/{weChat}.{weChatsmall}(0x{weChatKey}) NetType/{NetType} Language/zh_CN"
        return ua_string.format(
            **{
                "AndroidVersion": random_Android_OS(),
                "AndroidPhone": random_Android(),
                "WebKitVer": random_WebkitVer(),
                "ChromeVer": random_Chrome_Ver(),
                "TBS": str(random.randint(1, 999999)).zfill(6),
                "weChat": config["weChat"][0],
                "weChatsmall": str(random.randint(1, 9999)),
                "weChatKey": str(''.join(random.choice("0123456789abcdef") for _ in range(8))),
                "NetType": str(random.choice(net_type))
            }
        )

    def wechat_iPhone(self):
        ua_string = "Mozilla/5.0 (iPhone; CPU iPhone OS {iOSVer} like Mac OS X) " \
                    "AppleWebKit/{WebkitVer} (KHTML, like Gecko) " \
                    "Mobile/{Mobile} " \
                    "MicroMessenger/{weChat} NetType/{NetType} Language/zh_CN"
        return ua_string.format(
            **{
                "iOSVer": random_iOS_Version(),
                "WebkitVer": random_WebkitVer(),
                "Mobile": random_iPhoneKey(6),
                "weChat": config["weChat"][0],
                "NetType": str(random.choice(net_type))
            }
        )

    def ucbrower_Android(self):
        # Android only
        ua_string = "Mozilla/5.0 (Linux; U; Android {AndroidVersion}; {AndroidPhone}) " \
                    "AppleWebKit/{WebKitVer} (KHTML, like Gecko) Version/4.0 " \
                    "Chrome/{ChromeVer} " \
                    "UCBrowser/{UCVer} Mobile Safari/{WebKitVer}"
        return ua_string.format(
            **{
                "AndroidVersion": random_Android_OS(),
                "AndroidPhone": random_Android(),
                "WebKitVer": random_WebkitVer(),
                "ChromeVer": random_Chrome_Ver(),
                "UCVer": random_UC_Ver()
            }
        )

    def mobile_QQ_Android(self):
        ua_string = "Mozilla/5.0 (Linux; U; Android {AndroidVersion}; {AndroidPhone}) " \
                    "AppleWebKit/{WebKitVer} (KHTML, like Gecko)Version/4.0 " \
                    "Chrome/{ChromeVer} " \
                    "MQQBrowser/{MQQBrowser} Mobile Safari/{WebKitVer}"
        return ua_string.format(
            **{
                "AndroidVersion": random_Android_OS(),
                "AndroidPhone": random_Android(),
                "WebKitVer": random_WebkitVer(),
                "ChromeVer": random_Chrome_Ver(),
                "MQQBrowser": random_MQQ_Ver()
            }
        )

    def mobile_QQ_iPhone(self):
        ua_string = "Mozilla/5.0 (iPhone; CPU iPhone OS {iOSVer} like Mac OS X) " \
                    "AppleWebKit/{WebkitVer} (KHTML, like Gecko) Version/10.0 " \
                    "MQQBrowser/{MQQBrowser} Mobile/{Mobile} " \
                    "Safari/{WebkitVer} MttCustomUA/2 QBWebViewType/1 WKType/1"
        return ua_string.format(
            **{
                "iOSVer": random_iOS_Version(),
                "WebkitVer": random_WebkitVer(),
                "Mobile": random_iPhoneKey(6),
                "MQQBrowser": random_MQQ_Ver(),
                "NetType": str(random.choice(net_type))
            }
        )

    def mobile_baidu_Android(self):
        ua_string = "Mozilla/5.0 (Linux; Android {AndroidVersion}; {AndroidPhone}) " \
                    "AppleWebKit/{WebKitVer} (KHTML, like Gecko) Version/4.0 " \
                    "Chrome/{ChromeVer} Mobile Safari/{WebKitVer} T7/{baidu_T} " \
                    "baiduboxapp/{baiduVer} (Baidu; P1 {AndroidVersion})"

        return ua_string.format(
            **{
                "AndroidVersion": random_Android_OS(),
                "AndroidPhone": random_Android(),
                "WebKitVer": random_WebkitVer(),
                "ChromeVer": random_Chrome_Ver(),
                "baidu_T": random_MBaidu_T(),
                "baiduVer": random_MBaidu_Ver()
            }
        )

    def mobile_baidu_iPhone(self):
        ua_string = "Mozilla/5.0 (iPhone; CPU iPhone OS {iOSVer} like Mac OS X) " \
                    "AppleWebKit/{WebkitVer} (KHTML, like Gecko) " \
                    "Mobile/{Mobile} search%2F1.0 " \
                    "baiduboxapp/{baiduAppiOS}/{baiduAppPi}_2C2%258enohPi/1099a/{key}/1"
        return ua_string.format(
            **{
                "iOSVer": random_iOS_Version(),
                "WebkitVer": random_WebkitVer(),
                "Mobile": random_iPhoneKey(6),
                "baiduAppiOS": "0_{0}.{1}.{2}.{3}_enohpi_{4}_{5}".format(
                    random.randint(1, 15),
                    random.randint(0, 9),
                    random.randint(0, 9),
                    random.randint(0, 9),
                    random.randint(999, 9999),
                    random.randint(1, 999)
                ),
                "baiduAppPi": "{0}.{1}.{2}".format(
                    random.randint(0, 9),
                    random.randint(0, 9),
                    str(random.randint(0, 9)).zfill(2)
                ),
                "key": random_iPhoneKey(51)
            }
        )

    def pc_Windows(self):
        ua = random.choice([
            self.chrome_pc_windows(),
            self.baidubrower(),
            self.Brower2345(),
            self.firefox_pc_windows(),
            self.sougou(),
            self.internet_explorer(),
            self.liebao(),
            self.maxthon(),
            self.qihu360(),
            self.qqbrower()
        ])
        return ua

    def pc_Linux(self):
        ua = random.choice([
            self.chrome_pc_linux(),
            self.firefox_pc_linux()
        ])
        return ua

    def pc_mac(self):
        ua = random.choice([
            self.chrome_mac(),
            self.firefox_mac(),
            self.safari_mac()
        ])
        return ua

    def android(self):
        ua = random.choice([
            self.mobile_chrome_android(),
            self.ucbrower_Android(),
            self.mobile_QQ_Android(),
            self.mobile_baidu_Android()
        ])

        return ua

    def iOS(self):
        ua = random.choice([
            self.mobile_QQ_iPhone(),
            self.mobile_baidu_iPhone(),
            self.mobile_chrome_iPhone()
        ])
        return ua

    def wechat(self):
        ua = random.choice([
            self.wechat_Android(),
            self.wechat_iPhone()
        ])
        return ua

    def random_PC(self):
        ua = random.choice([
            self.pc_Linux(),
            self.pc_mac(),
            self.pc_Windows()
        ])
        return ua

    def random_Mobile(self):
        ua = random.choice([
            self.android(),
            self.iOS()
        ])
        return ua

    def random_weChat(self):
        ua = random.choice([
            self.wechat_iPhone(),
            self.wechat_Android()
        ])
        return ua

    def random_all(self):
        ua = random.choice([
            self.random_PC(),
            self.random_Mobile(),
            self.random_weChat()
        ])
        return ua
if __name__ == "__main__":
    while(1):
        UAString = fake_UA_maker().wechat()
        print(UAString)
        time.sleep(1)
    # print(random_Android_OS())
