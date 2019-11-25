#!/usr/bin/env python 
# coding=utf-8
# author: Tan Hyvi
# 对比两天的二手房的变化信息，比如降价、涨价、新增、下架。

import os 

if __name__ == "__main__": 
    # 准备旧的数据， 默认昨天的
    old_date = "20191124" 
    old_ershous = {}
    # 读取新的数据，默认今天的
    new_date = "20191125"
    new_ershous = {}
    # 保存对比后的数据
    trend_asc_ershous = [] # 涨价的二手 
    trend_dsc_ershous = [] # 降价的二手 
    trend_new_ershous = [] # 新上架的二手房
    trend_old_ershous = [] # 下架的二手房 
    data_base_path = "data/ke/ershou/sz"


    old_ershou_path = os.path.join(data_base_path, old_date) 
    for root, dirs, files in os.walk(old_ershou_path):
        for filename in files: 
            f = open(os.path.join(old_ershou_path, filename), "r")
            lines = f.readlines()
            for line in lines: 
                oldershoufang = line.split(",")
                old_ershous[oldershoufang[4]] = oldershoufang 
            

    new_ershou_path = os.path.join(data_base_path, new_date)
    for root, dirs, files in os.walk(new_ershou_path):
        for filename in files: 
            f = open(os.path.join(new_ershou_path, filename), "r")
            lines = f.readlines()
            for line in lines: 
                newershoufang =line.replace("\n", "").split(",")
                if len(newershoufang) < 7:
                    print(newershoufang)
                    continue
                if newershoufang[4] in old_ershous:
                    new_price = float(newershoufang[6])
                    old_price = float(old_ershous[newershoufang[4]][6])
                    if new_price > old_price: 
                        print(new_price)
                        print(old_price)
                        newershoufang.append(str(new_price - old_price))
                        trend_asc_ershous.append(newershoufang)
                    elif new_price < old_price: 
                        newershoufang.append(str(new_price - old_price))
                        trend_dsc_ershous.append(newershoufang)
                else:
                    newershoufang.append(newershoufang[6])
                    trend_new_ershous.append(newershoufang)
    # 写入csv表格里 
    csv_file = os.path.join(data_base_path, "trend_%s.csv" % new_date )

    with open(csv_file, "w") as f: 
        for trend_dsc_ershou in trend_dsc_ershous:
            f.write(",".join(trend_dsc_ershou) + "\n")

        for trend_asc_ershou in trend_asc_ershous: 
            f.write(",".join(trend_asc_ershou) + "\n")

        for trend_new_ershou in trend_new_ershous:
            f.write(",".join(trend_new_ershou) + "\n")

