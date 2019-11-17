#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 二手房信息的数据结构


class ErShou(object):
    def __init__(self, district, area, position, url, name, price, desc, pic):
        """
        二手房模型数据
        :param url: 二手房的的访问地址, 具有唯一性
        :param position: 二手房的小区名  
        """
        self.district = district
        self.area = area
        self.position = position
        self.url = url
        self.price = price
        self.name = name
        self.desc = desc
        self.pic = pic

    def text(self):
        return self.district + "," + \
                self.area + "," + \
                self.position + "," + \
                self.url + "," + \
                self.name + "," + \
                self.price + "," + \
                self.desc + "," + \
                self.pic
