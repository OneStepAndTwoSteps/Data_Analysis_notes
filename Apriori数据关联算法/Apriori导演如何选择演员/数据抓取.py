
#author py chen

from lxml import etree
from selenium import webdriver
import time
import csv


driver=webdriver.Chrome()
HEADERS={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'https://movie.douban.com/'
}

url_path="https://movie.douban.com/subject_search?search_text=%E6%88%90%E9%BE%99&cat=1002&start={start}"

# 創建CSV文件
director="成龙"
# director_list=["成龙","Jackie Chan"]
director_list=["成龙"]

file_path='导演'+ director +'.csv'
# 用于区分换行符(只对文本模式有效，可以取的值有None,'\n','\r','','\r\n')
# csv标准库中的writerow在写入文件时会加入'\r\n'作为换行符，if newline is ''，换行符不会被转化而是直接输出就是'\r\n'
out=open(file_path,'w',newline='',encoding='utf-8')
csv_writer=csv.writer(out,dialect='excel')

# 用于标记已经写入文件的电影，防止重复
flag=[]

def download(page_url):
    driver.get(page_url)
    # driver.get('file:///D:/a%20py%20Place%20of%20storage/Blog%20work/sublime/python/%E7%AE%97%E6%B3%95/Apriori%E5%85%B3%E8%81%94%E7%AE%97%E6%B3%95/%E6%88%90%E9%BE%99%20-%20%E7%94%B5%E5%BD%B1%20-%20%E8%B1%86%E7%93%A3%E6%90%9C%E7%B4%A2.html')
    time.sleep(1)
    # text=requests.get(page_url,headers=HEADERS).text
    html=driver.find_element_by_xpath('//*').get_attribute('outerHTML')
    html=etree.HTML(html)

    print("html: ",etree.tostring(html))

    actor_name_lists=html.xpath("/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='meta abstract_2']/text()")
    movie_name_lists=html.xpath("/html/body/div[@id='wrapper']/div[@id='root']//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']/text()")

    # print("actor_name_list: ",actor_name_list)
    # for i in actor_name_list:
    #     print(i.text)
    # print("movie_name_list: ",movie_name_lists)
    # for j in movie_name_list:
    #     print(j.text)
    if len(movie_name_lists)>=16:
        movie_name_lists=movie_name_lists[1:]
        actor_name_lists=actor_name_lists[1:]

    print("actor_name_list: ",actor_name_lists)
    print("movie_name_list: ",movie_name_lists)

    for movie_name,actor_name in zip(movie_name_lists,actor_name_lists):
        names=actor_name.split('/')
        print("movie_name: ",movie_name)
        print("actor_name: ",actor_name)

        # names[0]是导演名称
        print("names[0] ",names[0])
        if names[0].strip() in  director_list and movie_name not in flag:
            # 如果第一个字段是导演，那么设置第一个字段为电影名称，并写入csv文件
            names[0]=movie_name
            flag.append(movie_name)
            print("开始写csv文件..........")
            csv_writer.writerow(names)


    if len(movie_name_lists) < 1:
        return False
    else:
        return True
if __name__ == '__main__':
    for i in range(0,10000):
        page_url=url_path.format(start=i*15)
        print(page_url)
        # exit()
        return_code=download(page_url)
        # loop=asyncio.get_event_loop()
        # return_code=loop.run_until_complete(download(page_url))
        # exit()
        if return_code:
            pass
        else:
            break

    out.close()
