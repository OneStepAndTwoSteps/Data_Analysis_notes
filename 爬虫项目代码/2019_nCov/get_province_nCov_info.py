#author py chen

import requests
from concurrent.futures import ThreadPoolExecutor,as_completed
import datetime,time
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']



class nCov_2019():

    def __init__(self):
        self.base_url = 'https://lab.isaaclin.cn'
        self.api = '/nCoV/api/area'
        self.url = self.base_url + self.api  # 不同地区新型冠状病毒的感染情况 API
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
                                "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}

    # 获取国家名称
    def get_province(self,province_url):
        province_names = []
        response = requests.get(province_url,headers=self.headers)
        if response.status_code == 200:
            data = response.json()['results']
            province_names = data

            # 排除中国地区
        province_names = filter(lambda x: '市' not in x and '省' not in x and '自治区' not in x,province_names)
        province_names = list(province_names)
        print('province_names: ',province_names[:20])

        return  province_names[:20]


    # 多线程
    def Multithreading(self,province_names):
        province_nCov_info = {}
        all_future = []

        # 注意：接口 api 做了反爬虫措施 限制单个IP每秒请求数量最多为5次，如果超过该访问频率，则返回503错误。
        # 所以多线程不建议使用，仍然使用单线程
        with ThreadPoolExecutor(max_workers=1) as executor:
            for province_name in province_names:

                future = executor.submit(self.get_info,province_name)
                all_future.append(future)


            for future in as_completed(all_future):
                data = future.result()
                if data:
                    # print('data: ',data)
                    province_nCov_info[data['countryName']] = data['confirmedCount']

        return province_nCov_info

    def get_info(self,province_name):

        params = {'latest': 1, 'province': province_name}
        print('params: ', params)
        time.sleep(0.5)
        response = requests.get(self.url, params=params,headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            results = data['results'][0]

            # print(results)
            # countryName : 国家（英文）名称
            # province(English)Name : 省份、地区或直辖市（英文）全称
            # provinceShortName : 省份、地区或直辖市简称
            # currentConfirmedCount :	现存确诊人数，值为confirmedCount - curedCount - deadCount
            # confirmedCount :	累计确诊人数
            # suspectedCount : 疑似感染人数
            # curedCount:  治愈人数
            # deadCount	: 死亡人数

            print(
                '国家名称：{countryName} 现存确诊人数: {currentConfirmedCount} 累计确诊人数: {confirmedCount} 疑似感染人数:{suspectedCount} 治愈人数:{curedCount} 死亡人数: {deadCount}' \
                .format(countryName=results['countryName'], currentConfirmedCount=results['currentConfirmedCount'],
                        confirmedCount=results['confirmedCount']
                        , suspectedCount=results['suspectedCount'], curedCount=results['curedCount'],
                        deadCount=results['deadCount']))
        else:
            results = None

            print('返回状态码为：{} {} 国家不存在,可能是某个国家的地区 '.format(response,province_name))

        return results


    def hist_plot(self,province_nCov_info):

        province_nCov_top10 = {}    # 累计感染数量前10名国家排名字典数据
        province_top10 = sorted(province_nCov_info.items(),key=lambda d: d[1],reverse=True)[:10] # 累计感染数量前10名国家名字
        print('province_nCov_info_top10',province_top10)

        for i in province_top10:
            province_nCov_top10[i[0]] = i[1]
        print('province_nCov_top10: ',province_nCov_top10)
        print(list(province_nCov_top10.keys()))
        print(list(province_nCov_top10.values()))

        plt.figure(figsize=(15,12))
        plt.bar(list(province_nCov_top10.keys()),list(province_nCov_top10.values()))
        plt.title('世界疫情受影响严重排名')
        plt.show()

if __name__ == '__main__':


    province_url = 'https://lab.isaaclin.cn/nCoV/api/provinceName?lang=zh'  # 获取支持搜索的国家名称

    # https://lab.isaaclin.cn/nCoV/api/provinceName?lang=zh # province 参数选项
    # https://lab.isaaclin.cn/nCoV/api/provinceName?lang=zh # provinceEng 参数选项

    spider = nCov_2019()
    province_names = spider.get_province(province_url)
    # print('province_names: ',province_names)

    start_time = datetime.datetime.now()
    province_nCov_info = spider.Multithreading(province_names)
    # print(province_nCov_info)
    end_time = datetime.datetime.now()

    spend_time = end_time - start_time
    print('抓取数据耗时：{}s'.format(spend_time.seconds))

    print('province_nCov_info: ',province_nCov_info)
    spider.hist_plot(province_nCov_info)
