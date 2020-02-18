#获取我想看的电影列表
#保存电影名字和链接到 movie_links.json
#保存html页面到 doubanX.txt

import requests        #导入requests包
import urllib.request
from bs4 import BeautifulSoup
import json

url_1 = 'https://movie.douban.com/people/65038921/wish?sort=time&amp;start='
url_2 = '&amp;filter=all&amp;mode=list&amp;tags_sort=count'
url = ''


headers = {
    #'Accept': 'text/event-stream',
    #'Accept-Encoding':'gzip, deflate, br',
    #'Host': 'push.douban.com:4397',
    #'Origin': 'https://movie.douban.com',
    #'Referer': 'https://movie.douban.com/people/65038921/wish?start=0&sort=time&rating=all&filter=all&mode=list',   
    
    'Referer': 'https://movie.douban.com/people/65038921/wish',
    'Sec-Fetch-Dest': 'document',
    'Upgrade-Insecure-Requests': '1',
    
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Mobile Safari/537.36'
    }

def getHtml(url,headers,filename):
    #s = requests.session()
    #s.cookies.update(cookie)
    #s.headers.update(headers)

    req = urllib.request.Request(url=url,headers=headers)
    res = urllib.request.urlopen(req)
    data = res.read()
    data = data.decode('utf-8')
    #print(data)
    #print(type(res))
    print(res.geturl())
    #print(res.info())
    #print(res.getcode())
    print('get html:'+url)
    file = open(filename,'w',encoding='utf-8')
    file.write(data)
    file.close()
    return data


def getHtmlByFile(filename):
    print('get html by file:')
    file = open(filename,'r',encoding='utf-8')
    data = file.read()
    print(data)
    return data


def getMovieName(data):
    movies=[]
    page = BeautifulSoup(data, 'html.parser')
    titles = page.find_all("div", class_="title")
    for title in titles:
        movie = {}
        a = title.find('a')
        
        str = a.get_text()
        movie['name']=str
        
        href = a['href']
        movie['link']=href        
        
        movies.append(movie)
    print('--------------')
    
    return movies

#data = getHtml(url,headers)
#data = getHtmlByFile('html_douban.txt')


def savelink(movies):
    file = open('movie_links.json','w',encoding='utf-8')
    json.dump(movies,file,ensure_ascii=False)
    file.close()
    
    return

def main():
    movies=[]
    for i in range(0,151,30):
        url = url_1 + str(i) + url_2
        filename = 'douban'+str(i)+'.txt'
        data = getHtml(url,headers,filename)
        movies += getMovieName(data)
    
    print(movies)
    savelink(movies)
