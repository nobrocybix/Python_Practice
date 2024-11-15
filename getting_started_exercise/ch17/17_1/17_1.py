import requests
import pygal
import os
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter

url = "https://api.github.com/search/repositories?q=language:javascript&sort=stars"
basedir = os.path.dirname(__file__)

# Make an API call, and store the response.
r = requests.get(url)
response_dict = r.json()

response_items = response_dict['items']

for key_items in sorted(response_items, key=itemgetter('forks_count'), reverse=True):
    print("\n")
    print("name: ", key_items['name'])
    print("owner: ", key_items['owner']['login'])
    print("forks_count: ", key_items['forks_count'])
    print("description: ", key_items['description'])
    print("homepage: ", key_items['homepage'])
    print("url: ", key_items['url'])
    print("downloads_url: ", key_items['downloads_url'])  
    print("releases_url: ", key_items['releases_url'])
    print("html_url:", key_items['html_url'])

names, forks_counts = [], []
for key_items in sorted(response_items, key=itemgetter('forks_count'), reverse=True):
    names.append(key_items['name'])
    
    y_plot = {
        'value' : key_items['forks_count'],
        'label' : key_items['description'],
        'xlink' : key_items['html_url'],
    }
    forks_counts.append(y_plot)

# Make visualization.
my_style = LS('#d44a16', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45  # X 軸標籤旋轉 45 度
my_config.show_legend = False      # 不顯示圖例
my_config.title_font_size = 24     # 標題字體大小為 24
my_config.label_font_size = 14      # 標籤字體大小為 14
my_config.major_label_font_size = 18 # 主要標籤字體大小為 18
my_config.truncate_label = 15       # 標籤長度超過 15 個字元時截斷
my_config.show_y_guides = False     # 不顯示 Y 軸輔助線
my_config.width = 1000              # 圖表寬度為 1000 畫素

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred JaveScript Projects on GitHub'
chart.x_labels = names

chart.add('', forks_counts)
chart.render_to_file(os.path.join(basedir, 'javascript_repos.svg'))

