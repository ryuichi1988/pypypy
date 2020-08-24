import requests,os,csv
from bs4 import BeautifulSoup
with open ("周杰伦歌曲.csv","w",encoding="UTF-8",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["歌曲","专辑","发行时间","时长","ID","链接"])

    n=1

    headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url="https://c.y.qq.com/soso/fcgi-bin/client_search_cp"
    for i in range(1,10):
        params = {
            'ct': '24',
            'qqmusic_ver': '1298',
            'new_json': '1',
            'remoteplace': 'txt.yqq.song',
            'searchid': '70639520445554566',
            't': '0',
            'aggr': '1',
            'cr': '1',
            'catZhida': '1',
            'lossless': '0',
            'flag_qc': '0',
            'p': str(n),
            'n': '10',
            'w': '周杰伦',
            'g_tk_new_20200303': '5381',
            'g_tk': '5381',
            'loginUin': '0',
            'hostUin': '0',
            'format': 'json',
            'inCharset': 'utf8',
            'outCharset': 'utf-8',
            'notice': '0',
            'platform': 'yqq.json',
            'needNewCode': '0'
        }
        get=requests.get(url, headers=headers,params=params)
        json = get.json()
        list = json["data"]["song"]["list"]



        for eachdir in list:
            songtitle = eachdir["title"]
            songid = eachdir["id"]
            songhrl = eachdir["url"]
            songpublictime = eachdir["time_public"]
            songalbum = eachdir["album"]["title_hilight"]
            songtime = eachdir["interval"]
            songtime = str(songtime//60)+"分 "+str(songtime%60)+"秒"
            row = [songtitle,songalbum,songpublictime,songtime,songid,songhrl]
            writer.writerow(row)
        n+=1

file.close()


