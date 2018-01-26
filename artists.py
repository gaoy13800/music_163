#-*-coding:utf-8-*-

import requests
from lxml import html
from selenium import webdriver
import json



'''
1、 歌手界面 获取所有的歌手字母分类列表id
2、 爬取每一个分类下所有的歌手id
3、 获取歌手专辑id
4、 调用api 
'''

list = []

header = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Host":"music.163.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
    "Referer":"music.163.com",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Cookie":"ntes_nnid=1d0870d9404288142e7ec059089bf65f,1512378846734; _ntes_nuid=1d0870d9404288142e7ec059089bf65f; vjuids=-176fc32a5.1602964ef8b.0.ab46c54df2253; mail_psc_fingerprint=cf410c14ef4123cbc105d050f854377d; _ngd_tid=vGxIWEP4kCA7Q00UK1xEBIY7qMwseu5T; P_INFO=gaoy13800@163.com|1513654852|0|urs|00&99|heb&1513654735&mail163#heb&130100#10#0#0|157665&0|mail163|gaoy13800@163.com; _ga=GA1.2.185968190.1513669430; mp_MA-A281-795C7131C131_hubble=%7B%22sessionReferrer%22%3A%20%22https%3A%2F%2Fm.mei.163.com%2Ftrial%3Futm_source%3DMUSIC%26utm_medium%3DPLzhoudafu%22%2C%22updatedTime%22%3A%201513669430120%2C%22sessionStartTime%22%3A%201513669430114%2C%22deviceUdid%22%3A%20%22774ad5a5-1857-43ae-8ee5-b6fff792c84e%22%2C%22initial_referrer%22%3A%20%22http%3A%2F%2Fiad.g.163.com%2Fwa%2Fad%3Fsite%3Dnetease%26affiliate%3Dmusic%26cat%3Ddetail%26type%3Dlogo200x220%26location%3D1%26uuid%3Dfb06dd9b045443e1969ff366782b8bd4%22%2C%22initial_referring_domain%22%3A%20%22iad.g.163.com%22%2C%22persistedTime%22%3A%201513669430109%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_screen%22%2C%22time%22%3A%201513669430120%7D%2C%22currentReferrer%22%3A%20%22https%3A%2F%2Fm.mei.163.com%2Ftrial%3Futm_source%3DMUSIC%26utm_medium%3DPLzhoudafu%22%2C%22sessionUuid%22%3A%20%22520f6f3f-dbbc-4f2a-90df-6255060bb86f%22%2C%22superProperties%22%3A%20%7B%22inMeixueApp%22%3A%20false%7D%7D; Province=0310; City=0311; __gads=ID=42aadbdcf9a68635:T=1516688395:S=ALNI_MY-yBSMt3-FQhJDGZu7WGJR5xvfRA; UM_distinctid=16121ac55c9968-02b946ef72faff-5b4b2b1d-1fa400-16121ac55ca89e; vjlast=1512522969.1516688399.23; NNSSPID=54e09e8f9b4c4218b2df59a090a959d5; vinfo_n_f_l_n3=8bb21205cf1fbffd.1.1.1516007560644.1516007710756.1516688406813; JSESSIONID-WYYY=KWJXIvCC5umE25jXae3%2FOGaUmmx%2BDauC3f5hAAFwRYumr1g6ep%2BY5C5tD3meSjGoN%2FbsPVbCjyaylY7WpySAVi8sgymE2A%5CjR3iPUWPskir%2Fy7qx2yEBd6P3hEnF0q%2FphS49%2FumoxpSvrgMlctt0PssPA7Pj7gaGtGco4Es0NCcK6Qed%3A1516846579877; _iuqxldmzr_=32; __utma=94650624.1311429690.1512378847.1513825920.1516844780.10; __utmb=94650624.2.10.1516844780; __utmc=94650624; __utmz=94650624.1516844780.10.9.utmcsr=baidu|utmccn=(organic)|utmcmd=organic",
    "Cache-Control":"no-cache",
    'Connection':'keep-alive'
}

params = {
    "params":"IN5vLG8VqJfiPRKfTKRLQa9wWkkwOP3LXRKlcFGceGVOCaDSPni6ul3fWhYbvIFe0uLmSC3TsWciAnYEP5c1IVKJ0FlUvQWjrMj01zknoUkCEc6Z4LQ57H8NARqZbqtCGTmwzdgwmsGCW9Dn5bVH3HGc7TYuSakEX+8TBZdSACa4tMOUQfsGO2UIu2MTs6n4",
    "encSecKey":"226ba4128ead17e7948bff608a7ea8c92bc129190710648a1a4d9b405a3c27c9546480d7092c1e75b902eac3ded0b8bc1d63d8190240efe88e111e3a21bf1b5fd706538d134b9c992d4067c77eb06e78228339de1635cec53def7d0313160e27dffe744ae0ac56a139e938a31b6c6090fd2f849e5d5ca01f51919ddf5d0741b8"
}

Music_163_url = 'http://music.163.com/discover/artist/cat'
etree = html.etree
main_url = 'http://music.163.com'

artistIds = []

def save_artist(group_id, initial):
    params = {
        'id' : group_id,
        'initial' : initial
    }

    get_artist_ids()



    for artist_id in artistIds:
        prefix = 'http://music.163.com/#'

        info = requests.get(prefix + artist_id, headers= header)


        detailHt = etree.HTML(info.text)
        list = detailHt.xpath('//div[@class="ttc"]//a//@href')

        num = artist_id.replace('/artist?id=', '')

        getAlbum(num)

def getAlbum(artistId):
    params = {'id': artistId, 'limit': '200'}
    album_url = 'http://music.163.com/#/artist/album?id='+artistId + '&limit=200'

    # response = requests.get(album_url, headers=header, params=params)
    #
    # if response.status_code != 200:
    #     return False




    driver = webdriver.Chrome()
    driver.get(album_url)
    driver.switch_to.frame("g_iframe")
    html = driver.page_source
    driver.close()

    # print(html)

    albumHt = etree.HTML(html)

    hrefList = albumHt.xpath('//a[@class="msk"]/@href')
    artist_name = albumHt.xpath('//h2[@id="artist-name"]/@title')[0]

    print("开始爬取专辑  artist:" + artist_name)


    # soup = BeautifulSoup(response.content.decode(), 'html.parser')
    # body = soup.body
    #
    # albums = body.find_all('a', attrs={'class': 'tit f-thide s-fc0'})  # 获取所有专辑

    for i in hrefList:
        num = i.replace('/album?id=', '')
        getComment(num, artist_name)

    #
    # for i in hrefList:
    #
    # exit(0)

    # albumHt = etree.HTML(response.text)
    #

    #
    # print(hrefList)

def getComment(id, artist_name):
    url = 'http://music.163.com/weapi/v1/resource/comments/R_AL_3_'+ id + '?csrf_token='

    print(url)

    response = requests.post(url, headers=header, params=params)

    json_dict = json.loads(response.text)
    hot_comment = json_dict['hotComments']

    fileHandle = open('./comment.cfg', 'a', encoding='utf-8')
    fileHandle.write('歌手名:' + artist_name +'\n')



    num = 1
    for item in hot_comment:

        fileHandle.write(str(num) + '.' + item['content'] + '\n')
        num+=1
        pass

    fileHandle.write('\n=================================\n\n')
    fileHandle.close()

def get_artist_ids():
    response = requests.get(url=Music_163_url, headers=header)

    classify = etree.HTML(response.text)

    letter_classify = classify.xpath('//ul[@class="n-ltlst f-cb"]//a/@href') #获取字母分类

    for ext in letter_classify:
        url = main_url + ext
        page_ret = requests.get(url=url, headers=header)
        page_html = etree.HTML(page_ret.text)
        artist_ids = page_html.xpath('//a[@class="msk"]/@href | //a[@class="nm nm-icn f-thide s-fc0"]/@href') #获取当前页面所有的歌手id，存放到list中

        for id_ext in artist_ids:
            artistIds.append(id_ext.replace('/artist?id=', ''))

save_artist(1001, -1)
