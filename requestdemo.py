#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import pymysql
import json

# 跨域请求地址
request_url = 'https://ecs-buy.aliyun.com/api/ecsCommodity/getCommodity.jsonp?commodityCode=vm&orderType=BUY'
# 设置请求价格的url
request_price_url = 'https://tco.aliyun.com/tco/ecs/price.json'
# 设置请求头，注明请求发出原地址
headers = {'Referer': "https://tco.aliyun.com/tco/ecs/calculator?spm=5176.8030368.1058474.1.22c43aa4TZEd79"}
# 发起请求,获取返回的json
response = requests.get(request_url, headers=headers).json()
# 获取地区名及相应代号
region_list = response['data']['components']['vm_region_no']['vm_region_no']
# 获取所有虚拟机规格
vm_list = response['data']['components']['instance_type']['instance_type']

# 将地区信息存入数据库
# 建立连接通道，建立连接填入（连接数据库的IP地址，端口号，用户名，密码，要操作的数据库，字符编码）
config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "root",
    "database": "local_db"
}

sql = "INSERT INTO t_region(T_REGION_CODE, T_REGION_NAME, T_REGION_DISABLED, T_REGION_ALIAS, T_REGINALIZATION) VALUES(%s, %s, %s, %s, %s)"

price_sql = "INSERT INTO t_aliyun_prcie(T_REGION, T_MECHINE_FORMAT, N_VCPU, N_MEMORY, N_PRCIE) VALUES(%s, %s, %s, %s, %s)"
# 循环遍历
for each in region_list:
    db = pymysql.connect(**config)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 执行插入数据到T_REGION表
    cursor.execute(sql, (each['value'], each['text'], each['disabled'], each['regionAlias'], each['isReginalization']))
    # 提交数据
    db.commit()
    for vm in vm_list:
        # 设置请求参数
        components = {
            "instances": [{
                "RegionId": each['value'],
                "ZoneId": "random",
                "NetworkType": "vpc",
                "IoOptimized": True,
                "InstanceType": vm['value'],
                "SystemDiskSize": 20,
                "SystemDiskCategory": "cloud_efficiency",
                "PriceUnit": "Month",
                "Period": 1,
                "Amount": 1
            }],
            "disks": [],
            "bandwidths": [{
                "RegionId": each['value'],
                "InternetMaxBandwidthOut": 0,
                "InternetChargeType": "PayByBandwidth",
                "PriceUnit": "Month",
                "Period": 1,
                "Amount": 1
            }]
        }
        payload = {
            'components': json.dumps(components)
        }
        # response_price = requests.get(request_price_url, params=payload).json()
        response_price = requests.get(request_price_url, params=payload)
        print(response_price.url)
        res = response_price.json()
        print(res)
        if res['code'] == '200':
            result_price = response_price.json()['data']['instances'][0]['data']['tradePrice']
            cursor.execute(price_sql, (each['value'], vm['value'], vm['cpu'], vm['memory'], result_price))
            db.commit()
        else:
            print('所选区域中该配置的虚拟机不存在！')





