#coding=utf-8
import MySQLdb
import time, threading
import json
import requests
vid = 0
lock = threading.Lock()
conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='',
        db ='bilibili',
        )
cur = conn.cursor()
def doit():
    global vid
    url = 'http://api.bilibili.com/archive_stat/stat?aid='+str(vid)
    response = requests.get(url)	
    r = json.load(response.text())
    if(r['code']==0):
       view = str(r['data']['view'])
       danmu = str(r['data']['danmaku'])
       reply = str(r['data']['reply'])
       favorite= str(r['data']['favorite'])
       coin= str(r['data']['coin']) 
       share = str(r['data']['share'])
       his_rank = str(r['data']['his_rank'])
       cur.execute("insert into  info_bilibili_video values('"+vid+"','"+view+"','"+danmu+"','"+reply+"','"+favorite+"','"+coin+"','"+share+"','"+his_rank+"')")
       conn.commit()
       vid=vid+1

def run_thread():
	global lock
 	while(true):
		lock.acquire()
        try:
        	doit()
        finally:
            	lock.release()

if __name__=='__main__':
    while True: 
        doit()
conn.close()

