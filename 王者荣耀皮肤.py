# 爬取王者荣耀全皮肤
import os
import re
import json
import requests
if not os.path.exists('img'):
    os.mkdir('img')
url = 'https://pvp.qq.com/web201605/js/herolist.json'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
response = requests.get(url, headers=headers)
json_data = response.text
json2list = json.loads(json_data) # 将json转换为list
for i, hero in enumerate(json2list):
    ename = hero['ename']  # 英雄编号
    cname = hero['cname']  # 英雄名称
    url_hero = 'https://pvp.qq.com/web201605/herodetail/{}.shtml'.format(ename)
    response_hero = requests.get(url_hero, headers=headers)
    response_hero.encoding = response_hero.apparent_encoding  # 将默认解码方式改为网页编码方式，以防乱码
    html = response_hero.text
    skin_name_list = re.findall('<ul class="pic-pf-list pic-pf-list3" data-imgname="(.*?)">', html)[0].split('|')
    for skin_num in range(1, len(skin_name_list)+1):
        skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+str(ename)+'/'+str(ename)+'-bigskin-'+str(skin_num)+'.jpg'
        skin_jpg = requests.get(skin_url, headers=headers).content
        # print(skin_name_list[skin_num-1], skin_name_list[skin_num-1].split('&')[0])
        with open('img/'+cname+'-'+skin_name_list[skin_num-1].split('&')[0]+'.jpg', 'wb') as f:
            print('正在下载第{}个英雄{}的第{}个皮肤:'.format(i+1, cname, skin_num), skin_name_list[skin_num-1].split('&')[0])
            f.write(skin_jpg)