#author py chen

import requests
import sys
import re
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from PIL import Image
import numpy as np
from lxml import etree

headers = {
    'Referer': 'http://music.163.com',
    'Host': 'music.163.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Chrome/10'
}


def get_song(singer_id):
    # 这里有一个地方要注意 我们在查看我们的歌手的时候 我们的链接是这样的https://music.163.com/#/artist?id={id} 链接里面有一个#号这里我们要注意
    # 现在暂时没找出原因，加了井号之后数据好像变成动态加载了，歌单里面的信息我们无法查看
    base_url="https://music.163.com/artist?id={id}"
    singer_url=base_url.format(id=singer_id)
    # print(singer_url)
    # 请求页面
    html=requests.request('GET',singer_url,headers=headers).text
    # print(html)
    HTML=etree.HTML(html)

    # 返回前50首歌的跳转链接(其中有歌曲的id)可以通过id找歌词和歌名
    href_xpath = "//*[@id='hotsong-list']//a/@href"
    songs_xpath = "//*[@id='hotsong-list']//a/text()"
    hrefs=HTML.xpath(href_xpath)
    song_names=HTML.xpath(songs_xpath)
    # print(hrefs)
    # print(song_names)


    # 记录歌曲的id和name
    song_id_list=[]
    song_name_list=[]
    for href,name in zip(hrefs,song_names):
        song_id_list.append(href.split("=")[1])
        song_name_list.append(name)

    return song_name_list,song_id_list


def get_lyrics(song_id):
    # 这个链接是网易云音乐歌曲的api接口
    base_url='https://music.163.com/api/song/lyric?os=pc&id={id}&lv=-1&kv=-1&tv=-1'
    song_url=base_url.format(id=song_id)

    html=requests.request('GET',song_url,headers=headers).json()
    print(html)
    if 'lrc' in html:
       lyrics=html['lrc']['lyric']
       new_lyrics = re.sub(r'\[\S+\]', '', lyrics)
       return new_lyrics
    else:
        return ''

def create_wordcloud(all_lyrics):
    print('根据词频，开始生成词云!')
    f = remove_stop_words(all_lyrics)
    cut_text = " ".join(jieba.cut(f, cut_all=False, HMM=True))
    wc = WordCloud(
        font_path="./wc.ttf",
        max_words=100,
        width=2000,
        height=1200,
    )
    print(cut_text)
    wordcloud = wc.generate(cut_text)
    # 写词云图片
    wordcloud.to_file("wordcloud.jpg")
    # 显示词云文件
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


def remove_stop_words(all_lyrics):
    stop_words=['作词', '作曲', '编曲', 'Arranger', '录音', '混音', '人声', 'Vocal', '弦乐', 'Keyboard', '键盘', '编辑', '助理',
                  'Assistants', 'Mixing', 'Editing', 'Recording', '音乐', '制作', 'Producer', '发行', 'produced', 'and',
                  'distributed']
    for stop_word in stop_words:
        all_lyrics = all_lyrics.replace(stop_word, '')
    return all_lyrics

if __name__ == '__main__':
    singer_id=3684
    song_name_list,song_id_list=get_song(singer_id)
    print(song_name_list)
    print(song_id_list)
    all_lyrics=''
    for song_name,song_id in zip(song_name_list,song_id_list):
        lyrics=get_lyrics(song_id)
        all_lyrics = all_lyrics+ '' +lyrics

        print(song_name)

    create_wordcloud(all_lyrics)

