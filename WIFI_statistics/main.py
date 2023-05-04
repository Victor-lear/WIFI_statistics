import sys
import pymongo
from pymongo import MongoClient
import pandas as pd
import csv
import os
from datetime import datetime ,timedelta
import time
import subfunction as sub

#拿最後一筆處理資料的時間
data=sub.WIFI_LastData("AP_test", "Day_count")
if(data!=False):#如果有找到最後一筆資料
    data=data[0]['Datetime'].date()+timedelta(days=1)
    #轉化成最後一筆資料的下一天開始時間跟最後時間
    start=datetime.combine(data,datetime.min.time())
    end=datetime.combine(data,datetime.max.time())
    now=datetime.now()
    if(start<now):
    #不是今天>>>>>>>>>處理資料
        Search={"Datetime":{'$gte':start,"$lte":end}}
        data_2=sub.WIFI_FindData("AP_test","Controller4",Search)
        if(data_2!=False):#如果有找到資料
            AP_data=[]
            insert_data=[]
            for i in range(len(data_2)):
                
                try:
                    inwhere=int(AP_data.index(data_2[i]['ap_name']))
                except:
                    AP_data.append(str(data_2[i]['ap_name']))
                
                    inwhere=int(len(AP_data)-1)
                    insert_data.append({"ap_name":str(data_2[i]['ap_name']),"count":0,"Datetime": start})
                insert_data[inwhere]["count"]=insert_data[inwhere]['count']+int(data_2[i]['sta_count'])
            sub.WIFI_WriteInDB("AP_test","Day_count",insert_data)
            print("Success")
        else:
            print("No data")
    else:
    #今天尚未過完>>>>>>>>>暫不處理
        print("NO")
else:
    print("No have last data")
