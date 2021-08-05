# -*- coding: utf-8 -*-
"""
Created on *********

@author: 了不起的田所李

目的：新浪财经爬取资产负债表、利润表、现金流量表
"""
import sys
import requests


stockNum = str(sys.argv[1])


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status() #如果状态不是200，引发HTTPError异常#
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


def getHTMLGET(url):
    try:
        r = requests.get(url)
        print(r.text)
        r.raise_for_status()  # 如果状态不是200，引发HTTPError异常#
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


if __name__ == "__main__":
    # 资产负债表
    liabilities_url = "http://money.finance.sina.com.cn/corp/go.php/vDOWN_BalanceSheet/displaytype/4/stockid/"\
          + stockNum + "/ctrl/all.phtml"
    liabilities_url_text = getHTMLGET(liabilities_url)
    # 利润表
    profit_url = "https://money.finance.sina.com.cn/corp/go.php/vDOWN_ProfitStatement/displaytype/4/stockid/" + stockNum\
                 + "/ctrl/all.phtml"
    profit_url_text = getHTMLGET(profit_url)
    # 现金流量表
    flow_url = "https://money.finance.sina.com.cn/corp/go.php/vDOWN_CashFlow/displaytype/4/stockid/" + stockNum + \
                 "/ctrl/all.phtml"
    flow_url_text = getHTMLGET(flow_url)
    # print(text.replace("	", ','))
    with open("./Assets_and_liabilities/" + stockNum + ".csv", "w+") as Assets_and_liabilities_csvfile:
        Assets_and_liabilities_csvfile.write(liabilities_url_text.replace("	", ','))
    with open("./Total_operating_costs/" + stockNum + "-profit.csv", "w+") as profit_csvfile:
        profit_csvfile.write(profit_url_text.replace("	", ','))
    with open("./Funds_inflow_for_financing_activities/" + stockNum + "-flow.csv", "w+") as flow_csvfile:
        flow_csvfile.write(flow_url_text.replace("	", ','))
