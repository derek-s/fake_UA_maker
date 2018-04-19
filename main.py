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
def random_Chrome():
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




class fake_UA_maker:
    def chrome_pc_windows(self):
        ua_string = "Mozilla/5.0 (Windows NT {WinVer}; Win64; x64) AppleWebKit/{WebkitVer} " \
                    "(KHTML, like Gecko) Chrome/{ChromeVer} Safari/{WebkitVer}"
        return ua_string.format(
            **{"WinVer": random_Windows_Ver(), "WebkitVer": random_WebkitVer(), "ChromeVer": random_Chrome()}
        )

    def chrome_pc_linux(self):
        ua_string = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/{WebkitVer} (KHTML, like Gecko)" \
                    " Chrome/{ChromeVer} Safari/{WebkitVer}"
        return ua_string.format(
            **{"ChromeVer": random_Chrome(), "WebkitVer": random_WebkitVer()}
        )

    def chrome_mac(self):
        ua_string = "Mozilla/5.0 (Macintosh; Intel Mac OS X {MacVer}) AppleWebKit/{WebkitVer} " \
                    "(KHTML, like Gecko) Chrome/{ChromeVer} Safari/{WebkitVer}"
        return ua_string.format(
            **{"MacVer": random_Mac_Ver(), "ChromeVer": random_Chrome(), "WebkitVer": random_WebkitVer()}
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


if __name__ == "__main__":
    UAString = fake_UA_maker().chrome_mac()
    print(UAString)
