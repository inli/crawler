#字符和json文件处理
import string
import json
def addQuots():
    #给headers信息添加引号和逗号
    a = []
    while True:
    
        line = input("input:")
        if line == 'quit':
            break
        a.append(line)

    for line in a:
        line = line.replace(' ','')
        line = line.replace(':',"':'",1)
        line = "'"+line+"',"
        print(line)
    
def deleteSpace(filename):
    #去除json文件中多余的字符
    file = open(filename,'r',encoding='utf-8')
    s = json.load(file)
    file.close()
    for mv in s:
        name = mv['name']
        #mv['name'] = name.replace('\n','')
        play = mv['play']
        play2 = []
        for p in play:
            p=p.replace(' ','')
            p=p.replace('\n',' ')
            play2.append(p)
        mv['play'] = play2
    print(s)
    file = open(filename,'w',encoding='utf-8')
    json.dump(s,file,ensure_ascii=False)
    file.close()
    return

def sort(srcname):
    #修改json格式
    file = open(srcname,'r',encoding='utf-8')
    s = json.load(file)
    file.close()
    result = []
    all_webs = []
    for m in s:
        mv = {}     #new dict mv
        mv['name']=m['name']    #add key 'name'
        webs = m['play']        
        for w in webs:
            if w not in all_webs:
                all_webs.append(w)
            mv[w]=1
        
        for w in all_webs:
            mv.setdefault(w,'')        
        result.append(mv)
    file = open('mv_webs.json','w',encoding='utf-8')
    json.dump(result,file,ensure_ascii=False)
    file.close()
    return 







