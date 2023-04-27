#author py chen

from lxml import etree
from selenium import webdriver
import time
import csv

## 可以在 chrome 中安装一个 Xpath Helper 的插件
driver=webdriver.Chrome()
HEADERS={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'https://movie.douban.com/'
}

url_path="https://movie.douban.com/subject_search?search_text={director}&cat=1002&start={start}"

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
    time.sleep(1)
    ## 获取 HTML 结构
    html=driver.find_element_by_xpath('//*').get_attribute('outerHTML')
    ## 在这里我们首先导入了 LXML 库的 etree 模块，然后声明了一段 HTML 文本，调用 HTML 类进行初始化，这样我们就成功构造了一个 XPath 解析对象
    html=etree.HTML(html)

    print("html: ",etree.tostring(html))

    actor_name_lists=html.xpath("/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='meta abstract_2']/text()")
    movie_name_lists=html.xpath("/html/body/div[@id='wrapper']/div[@id='root']//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']/text()")

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
        page_url=url_path.format(director=director,start=i*15)
        print(page_url)
        return_code=download(page_url)
        if return_code:
            pass
        else:
            break

    out.close()
