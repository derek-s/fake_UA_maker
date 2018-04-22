#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 14:40
# @Author  : Derek.S
# @Site    : 
# @File    : main.py


import yaml
import random

# read yml config file

with open("_config.yml", "r", encoding="utf-8") as config_file:
    config = yaml.load(config_file)
config_file.close()

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
            **{"MacVer": random_Mac_Ver(), "ChromeVer": random_Chrome_Ver(), "WebkitVer": random_WebkitVer()}
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
        ua_string = "ozilla/5.0 (Windows NT {WinVer}; WOW64) " \
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

if __name__ == "__main__":
    UAString = fake_UA_maker().baidubrower()
    print(UAString)
