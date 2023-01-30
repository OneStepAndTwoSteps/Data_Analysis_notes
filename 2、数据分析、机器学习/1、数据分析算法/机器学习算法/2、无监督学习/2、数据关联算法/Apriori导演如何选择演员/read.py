from efficient_apriori import apriori
import csv

director="成龙"
data=open('导演'+ director +'.csv','r',encoding='utf-8')
lists=csv.reader(data)
print(data.read())

