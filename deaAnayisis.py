# -*- coding: utf-8 -*-
"""
Created on *********

@author: 了不起的田所李
"""
import pydea
import matplotlib as plt
import pandas as pd
import numpy as np
import sys


stockNum = str(sys.argv[1])

try:
    #读取csv文件
    data = pd.read_csv("./Assets_and_liabilities/" + stockNum + ".csv", encoding="utf-8")
except UnicodeDecodeError:
    data = pd.read_csv("./Assets_and_liabilities/" + stockNum + ".csv", encoding="gbk")

# 资产总计
total_assets = data.iloc[46, ]
# 负债合计
total_liabilities = data.iloc[80, :]
# 所有者权益
owners_equity = data.iloc[81, :]
# 营业总成本
data_total_operating_costs = pd.read_csv("./Total_operating_costs/" + stockNum + "-profit.csv", encoding="utf-8")
total_operating_costs = data_total_operating_costs.iloc[3, :]
# 筹资活动的现金流入量
data_Funds_inflow_for_financing_activities = pd.read_csv("./Funds_inflow_for_financing_activities/"
                                                         + stockNum + "-flow.csv", encoding="utf-8")
funds_inflow_for_financing_activities = data_Funds_inflow_for_financing_activities.iloc[32, :]

# 营业收入
operating_income = data_total_operating_costs.iloc[2, :]
# 净利润
profit = data_total_operating_costs.iloc[21, :]

# 输入数据合并
inputData = pd.concat([total_assets, total_liabilities, owners_equity, total_operating_costs,
                       funds_inflow_for_financing_activities], axis=1, sort=False)
# inputData.rename(columns={'46':'资产总计','80':'负债合计', "81":'所有者权益', '3':'营业总成本', '32':'偿还债务支付的现金'})
inputData = inputData.iloc[1:, :].astype("float64")
inputData = inputData.fillna(value=0)
# print(inputData)

outputData = pd.concat([operating_income, profit], axis=1, sort=False)
# outputData = outputData.rename(columns={'2':'营业收入','21':'净利润'})
outputData = outputData.iloc[1:, :].astype("float64")
outputData = outputData.fillna(value=0)
# print(outputData)

#执行计算
uni_prob_CRS = pydea.DEAProblem(inputData, outputData, returns='CRS')
myresults_CRS = uni_prob_CRS.solve()

#执行计算
uni_prob_VRS = pydea.DEAProblem(inputData, outputData, returns='VRS')
myresults_VRS = uni_prob_VRS.solve()

# myresults_CRS['综合效率'] = myresults_CRS['Efficiency']
# myresults_VRS['纯技术效率'] = myresults_VRS['Efficiency']
myresults = pd.DataFrame()
myresults['综合效率'] = myresults_CRS['Efficiency']
myresults['CRS_Status'] = myresults_CRS['Status']
myresults['纯技术效率'] = myresults_VRS['Efficiency']
myresults['VRS_Status'] = myresults_VRS['Status']
myresults['规模效率'] = (myresults_CRS['Efficiency'] / myresults_VRS['Efficiency']).fillna(0)
# myresults
# myresults['规模效率']
# 输出数据
myresults.to_csv("DeaResultFrom" + stockNum + ".csv", encoding="utf_8_sig")
