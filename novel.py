#获取小说到txt
#（我被男神的白月光魂穿了）

import requests
import getLinks
from bs4 import BeautifulSoup


def getArticle(url):
    s = requests.get(url)
    page = s.content
    page = page.decode('utf-8')

    bs = BeautifulSoup(page,'html.parser')
    
    p = bs.find_all('p')   
    article = ''
    for i in p[:-3]:
        article += i.get_text()+'\n'
    
    line = p[-3].get_text()
   
    line = line[:-125]
    article += line+'\n'
        
     
    
    return article

def main():

    url_1 = 'https://www.52shuku.me/xiandaidushi/hsu0_'
    url_2 = '.html'
    i = 45
    article = ''
    for i in range(45,138):
        url = url_1+str(i)+url_2
        try:
            article += 'chapter '+str(i)+'\n'
            print('chapter '+str(i)+'\n')
            a = getArticle(url)
            article += a
        except:
            article += 'lose:'+str(i)
            print('lose:'+str(i))
            continue
 

    file = open('novel.txt','w',encoding='utf-8')
    file.write(article)
    file.close()
    return

main()



