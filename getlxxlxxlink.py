import requests, re, sqlite3,time
from bs4 import BeautifulSoup

def getlink(listpage):
    res0 = requests.get(listpage)
    soup0 = BeautifulSoup(res0.text, "html.parser")
    kk1 = soup0.find_all(name='a', attrs={"href": re.compile(r'^/video/')})
    #title = [ i.get("title") for i in kk1]
    videolink = ["http://zhs.lxxlxx.com"+i.get("href") for  i in kk1]
    for i in videolink:
        getvideolink(i)
    
def getvideolink(ss):
        res1 = requests.get(ss)
        res1.encoding = 'utf-8'
        soup1 = BeautifulSoup(res1.text, "html.parser")
        name = soup1.find(class_="contenthead").h1.text
        print(name)
        gg = soup1.find_all(class_="video")
        scripturl = "http://m4.player.a.lx.7mao.club/10_mByjd" + (gg[0].script.get("src"))
                    # "http://m4.player.a.lx.7mao.club/10_mByjd/vjs/8660.js"
        res2 = requests.get(scripturl)
        soup2 = BeautifulSoup(res2.text, "html.parser")
        dd = str(soup2.html).replace('''document.writeln("''',"").replace('''");''',"")
        soup3 = BeautifulSoup(dd, "html.parser")
        sss = soup3.find(name="video")
        link = str(sss.source.get("src")).replace("\\'","")
        print(link)
        c.execute("INSERT or IGNORE INTO yazhou VALUES (?,?,?)", (name,link,"0"))
        conn.commit()

if __name__ == '__main__':
    conn = sqlite3.connect("lxx.db")
    c = conn.cursor()

    yazhou = "http://zhs.lxxlxx.com/tags/Asian/"
    ouzhou = "http://zhs.lxxlxx.com/tags/European/"
    alabo = "http://zhs.lxxlxx.com/tags/Arab/"
    lading = "http://zhs.lxxlxx.com/tags/Latin/"
    feizhou = "http://zhs.lxxlxx.com/tags/African/"
    jinfa = "http://zhs.lxxlxx.com/tags/Blondes/"
    heizong = "http://zhs.lxxlxx.com/tags/Brunettes/"
    hongzong = "http://zhs.lxxlxx.com/tags/Redheads/"
    lesbian = "http://zhs.lxxlxx.com/tags/Lesbians/"
    duzi = "http://zhs.lxxlxx.com/tags/Solo/"
    threesomes = "http://zhs.lxxlxx.com/tags/Threesomes/"
    cartoons = "http://zhs.lxxlxx.com/tags/Cartoons/"
    amateur = "http://zhs.lxxlxx.com/tags/Amateur/"
    gangjiao = "http://zhs.lxxlxx.com/tags/Anal/"
    lamei = "http://zhs.lxxlxx.com/tags/Babes/"
    juru = "http://zhs.lxxlxx.com/tags/Big-Tits/"
    jutun = "http://zhs.lxxlxx.com/tags/Big-Butts/"
    yanshe = "http://zhs.lxxlxx.com/tags/Facials/"
    koujiao = "http://zhs.lxxlxx.com/tags/Blowjobs/"
    cosplay = "http://zhs.lxxlxx.com/tags/Cosplay/"
    qinglv = "http://zhs.lxxlxx.com/tags/Couple/"
    zhongchu = "http://zhs.lxxlxx.com/tags/Creampie/"
    youqu = "http://zhs.lxxlxx.com/tags/Funny/"
    qunjiao = "http://zhs.lxxlxx.com/tags/Group-Sex/"
    dafeiji = "http://zhs.lxxlxx.com/tags/Handjobs/"
    xingjiao = "http://zhs.lxxlxx.com/tags/Hardcore/"
    jiudian = "http://zhs.lxxlxx.com/tags/Hotel/"
    neiyi = "http://zhs.lxxlxx.com/tags/Lingerie/"
    keai = "http://zhs.lxxlxx.com/tags/Lovely/"
    ziwei = "http://zhs.lxxlxx.com/tags/Masturbation/"
    shunv = "http://zhs.lxxlxx.com/tags/Matures/"
    gaochao = "http://zhs.lxxlxx.com/tags/Orgasms/"
    yewai = "http://zhs.lxxlxx.com/tags/Outdoor/"
    public = "http://zhs.lxxlxx.com/tags/Public/"
    zipai = "http://zhs.lxxlxx.com/tags/Selfie/"
    chaopen = "http://zhs.lxxlxx.com/tags/Squirting/"
    siwa = "http://zhs.lxxlxx.com/tags/Stockings/"
    striptease = "http://zhs.lxxlxx.com/tags/Striptease/"
    shaonv = "http://zhs.lxxlxx.com/tags/Teens/"
    kongjie = "http://zhs.lxxlxx.com/tags/Stewardess/"
    toukui = "http://zhs.lxxlxx.com/tags/Voyeur/"
    zhibo = "http://zhs.lxxlxx.com/tags/Webcams/"
    wife = "http://zhs.lxxlxx.com/tags/Wife/"
    yujia = "http://zhs.lxxlxx.com/tags/Yoga/"

    '''
    创建数据表
    lis =["yazhou","ouzhou","alabo","lading","feizhou","jinfa","heizong","hongzong","lesbian","duzi","threesomes","cartoons","amateur","gangjiao","lamei","juru","jutun","yanshe","koujiao","cosplay","qinglv","zhongchu","youqu","qunjiao","jiudian","neiyi","keai","ziwei","shunv","gaochao","yewai","public","zipai","chaopen","siwa","striptease","shaonv","kongjie","toukui","zhibo","wife","yujia"]
    for i in lis:
        comm = "create table " + i + " (name text,link text unique,token text)"
        c.execute(comm)
        conn.commit()
    '''

    lis = ["yazhou","ouzhou","alabo","lading","feizhou","jinfa","heizong","hongzong","lesbian","duzi","threesomes","cartoons","amateur","gangjiao","lamei","juru","jutun","yanshe","koujiao","cosplay","qinglv","zhongchu","youqu","qunjiao","jiudian","neiyi","keai","ziwei","shunv","gaochao","yewai","public","zipai","chaopen","siwa","striptease","shaonv","kongjie","toukui","zhibo","wife","yujia"]
    for i in lis:
        for j in range(1,1000):
            url = eval(i)+str(j)+"/"
            if j==1:
                #print(url[:-3])
                getlink(url[:-3])
                #quit()
            else:
                #print(url)
                #getlink(url)
                try:
                    getlink(url)
                except:
                    break
            #print(url)
        break
    conn.close()

