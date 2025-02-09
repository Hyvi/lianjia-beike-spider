#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 获得各城市的区县相关信息

import requests
from lxml import etree
from lib.zone.city import cities
from lib.const.xpath import *
from lib.request.headers import *
from lib.spider.base_spider import SPIDER_NAME
import sys
from lib.utility.version import PYTHON_3
from lib.utility.log import *

chinese_city_district_dict = dict()     # 城市代码和中文名映射
chinese_area_dict = dict()              # 版块代码和中文名映射
area_dict = dict()




def get_chinese_district(en):
    """
    拼音区县名转中文区县名
    :param en: 英文
    :return: 中文
    """
    return chinese_city_district_dict.get(en, None)

def create_prompt_text():
    return '请选择你要爬取的范围,多个之间用逗号分隔(例如:dongcheng,xicheng),如果不限制，则输入all \n'

def get_selectdistricts():
     districts = None
    # 允许用户通过命令直接指定
     if len(sys.argv) < 2:
        # 让用户选择爬取哪个城市的二手房小区价格数据
        prompt = create_prompt_text()
        # 判断Python版本
        if not PYTHON_3:  # 如果小于Python3
            districts = raw_input(prompt)
        else:
            districts = input(prompt)
     elif len(sys.argv) == 2:
        districts = str(sys.argv[1])
        print("区域 is: {0}".format(districts))
     else:
        print("At most accept one parameter.")
        exit(1)
     return districts.split(',')

def get_districts(city):
    """
    获取各城市的区县中英文对照信息
    :param city: 城市
    :return: 英文区县名列表
    """
    url = 'https://{0}.{1}.com/xiaoqu/'.format(city, SPIDER_NAME)
    headers = create_headers()
    response = requests.get(url, timeout=10, headers=headers)
    html = response.content
    root = etree.HTML(html)
    elements = root.xpath(CITY_DISTRICT_XPATH)
    en_names = list()
    ch_names = list()
    for element in elements:
        link = element.attrib['href']
        en_names.append(link.split('/')[-2])
        ch_names.append(element.text)

        # 打印区县英文和中文名列表
    for index, name in enumerate(en_names):
        chinese_city_district_dict[name] = ch_names[index]
        # print(name + ' -> ' + ch_names[index])
    return en_names


if __name__ == '__main__':
    for key in cities.keys():
        # 寻找那些网页格式不合规的城市
        chinese_city_district_dict = dict()
        get_districts(key)
        if len(chinese_city_district_dict.items()) == 0:
            print(key)
