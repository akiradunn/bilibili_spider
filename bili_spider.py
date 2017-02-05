#coding=utf-8
import MySQLdb
import urllib2
import time, threading
import json
import requests
vid = 0
lock = threading.Lock()
conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='dzl123..',
        db ='bilibili',
        )
cur = conn.cursor()

def doit():
    global vid
    url = 'http://api.bilibili.com/archive_stat/stat?aid='+str(vid)
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    r = json.load(response)
    if r['code']==0:
	view = r['data']['view']
	danmu = r['data']['danmaku']
	reply = r['data']['reply']
	favorite= r['data']['favorite']
	coin= r['data']['coin'] 
	share = r['data']['share']
	his_rank = r['data']['his_rank']
	cur.execute("insert into  info_bilibili_video values('"+str(vid)+"','"+str(view)+"','"+str(danmu)+"','"+str(reply)+"','"+str(favorite)+"','"+str(coin)+"','"+str(share)+"','"+str(his_rank)+"')")
	print "1 items ok!"
	conn.commit()
	vid=vid+1

def run_thread():
	global lock
 	while True:
	    if lock.acquire(): 
		doit()
	        lock.release() 
    #for i in range(multiprocessing.cpu_count()):
if __name__=='__main__':
<<<<<<< HEAD
    while True: 
        doit()
conn.close()

=======
    for i in range(5):
        t = threading.Thread(target=run_thread)
        t.start()
''' 
if __name__ == '__main__':
	while True:
	    doit()
'''
>>>>>>> 5d48fbc6c8d5eac2381d76004200ab6177a751d7
