#获取电影详情页链接列表
#获取网站播放情况
#记录电影名称、链接、可播放网站 保存到movie_webs.json

import requests        #导入requests包
import urllib.request
from bs4 import BeautifulSoup
import json

headers={
#'Accept':'application/json,text/javascript,*/*;q=0.01',
#'Cookie':'ll="108169";bid=gUI-t_jeeqc;__utmc=30149280;_vwo_uuid_v2=D90A1AF44AF5F20869375665616EAADBB|197afb214cd056f196fde97619e9a91d;douban-fav-remind=1;__utmv=30149280.6503;push_noty_num=0;push_doumail_num=0;gr_user_id=54963405-6e53-4493-8b81-b4df2c6cfac4;douban-profile-remind=1;viewed="1998341_4736167_1148282";dbcl2="65038921:FjDUV0LykE4";ck=vCYx;frodotk="ba84b38b80112c0c2f8e1aa280338424";__utmz=30149280.1580452995.66.21.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/;ct=y;__utma=30149280.1287688373.1556266116.1581857771.1581862224.82;__utmb=30149280.0.10.1581862224;ap_v=0,6.0;UM_distinctid=1704e753e59462-06dfb094f5e6be-313f69-e1000-1704e753e5a459;_ga=GA1.2.1287688373.1556266116;_gid=GA1.2.879820098.1581864272;Hm_lvt_19fc7b106453f97b6a84d64302f21a04=1581864272;Hm_lpvt_19fc7b106453f97b6a84d64302f21a04=1581864272',
#'Host':'m.douban.com',
'Origin':'https://movie.douban.com',
'Referer':'https://movie.douban.com/subject/1304102/',
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Mobile Safari/537.36'
    }

def getLinks(filename):
    file = open(filename,'r',encoding='utf-8')
    s = json.load(file)
    file.close()
    return s

def getHtml(url,headers):    
    req = urllib.request.Request(url=url,headers=headers)
    res = urllib.request.urlopen(req)
    data = res.read()
    data = data.decode('utf-8')
    print('get html:'+url)
    file = open('moviePage0.txt','w',encoding='utf-8')
    file.write(data)
    file.close()
    return data


def getPlayWeb(data):
    webs = []
    page = BeautifulSoup(data, 'html.parser')
    playbtn = page.find_all("a",class_="playBtn")
    buy = page.find_all("span",class_="buylink-price")
    for i in range(len(playbtn)):
        web=playbtn[i]['data-cn']
        price = buy[i].get_text()
        webs.append(web+price)
    print(webs)
    return webs

def saveWebs(data):
    file = open('movie_webs.json','w',encoding="utf-8")
    json.dump(data,file,ensure_ascii=False)
    file.close

links = getLinks('movie_links.json')
play_list = []

for s in links:
    link = s['link']
    try:
        data = getHtml(link,headers)
        webs = getPlayWeb(data)    
    except:
        print('fail:'+s['name'])
        continue
    else:
        s['play']=webs
        play_list.append(s)
        saveWebs(play_list)

    

saveWebs(play_list)
print(play_list)    
