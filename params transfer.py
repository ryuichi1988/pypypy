import re
parttern = '^(.*?): (.*)$'
text="""
ct: 24
qqmusic_ver: 1298
new_json: 1
remoteplace: txt.yqq.song
searchid: 70639520445554566
t: 0
aggr: 1
cr: 1
catZhida: 1
lossless: 0
flag_qc: 0
p: 3
n: 10
w: 周杰伦
g_tk_new_20200303: 5381
g_tk: 5381
loginUin: 0
hostUin: 0
format: json
inCharset: utf8
outCharset: utf-8
notice: 0
platform: yqq.json
needNewCode: 0
"""
for i in text.splitlines():
    each = re.sub(parttern,r"'\1':'\2',",i)
    print(each)