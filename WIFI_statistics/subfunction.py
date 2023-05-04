import sys
import pymongo
from pymongo import MongoClient
import pandas as pd
import csv
import os
from datetime import datetime   
import time
mongo_url_01 = "mongodb://admin:bmwee8097218@140.118.122.115:30415/"
mongo_url_02 = "mongodb://admin:bmwee8097218@140.118.122.115:30415/"
def WIFI_LastData(DB, Collection):
    global mongo_url_01,mongo_url_02
    try:
        conn = MongoClient(mongo_url_01) 
        db = conn[DB]
        collection = db[Collection]
        cursor=collection.find().sort("_id",-1).limit(1)
        data=[d for d in cursor]
    except:
        conn = MongoClient(mongo_url_02) 
        db = conn[DB]
        collection = db[Collection]
        cursor=collection.find().sort("_id",-1).limit(1)
        data=[d for d in cursor]
    if data==[]:
        return False
    else:
        return data
def WIFI_FindData(DB, Collection,Search={}):
    global mongo_url_01,mongo_url_02
    try:
        conn = MongoClient(mongo_url_01) 
        db = conn[DB]
        collection = db[Collection]
        cursor=collection.find(Search)
        data=[d for d in cursor]
    except:
        conn = MongoClient(mongo_url_02) 
        db = conn[DB]
        collection = db[Collection]
        cursor=collection.find(Search)
        data=[d for d in cursor]
    if data==[]:
        return False
    else:
        return data
def WIFI_WriteInDB(DB,Collection,new_data):
    global mongo_url_01,mongo_url_02
    try:
        conn = MongoClient(mongo_url_01) 
        db = conn[DB]
        collection = db[Collection]
        collection.insert_many(new_data)
    except:
       
        conn = MongoClient(mongo_url_02)
        db = conn[DB]
        collection = db[Collection]
        collection.insert_many(new_data)


