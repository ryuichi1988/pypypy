import csv,os
with open ("周杰伦歌曲.csv","w",newline="",encoding="UTF-8") as file:
    writer = csv.writer(file)
    listtitle = ["歌曲","专辑","发行时间","时长","ID","链接"]
    writer.writerow(listtitle)