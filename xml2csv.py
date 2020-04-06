import xmltodict
import pandas as pd
import numpy as np

with open('./wilson.xml', 'r', encoding="utf-8") as f:
    data = xmltodict.parse(f.read())['items']['item']

data_np = np.array((data))

id_list = []
quote_list = []
image_list = []
tag_list = []
likes_list = []
author_list = []

for i in range(len(data_np)):
    id_list.append(data[i]['id'])
    quote_list.append(data[i]['quote'])
    try:
        image_list.append(data[i]['image'])
    except:
        image_list.append("")
    tag_list.append(data[i]['tag'])
    likes_list.append(data[i]['likes'])
    author_list.append(data[i]['author'])

df = pd.DataFrame({'id': id_list, \
                   'quote': quote_list, \
                   'image': image_list, \
                   'tag': tag_list, \
                   'likes': likes_list, \
                   'author': author_list,
                  }, columns=['id','quote','image','tag','likes','author'])
df.set_index('id')
df.to_csv('./fromjohann_10000.csv')
