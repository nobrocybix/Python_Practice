import requests
import pygal
import os
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

basedir = os.path.dirname(__file__)

# Make an API call, and store the response.
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code:", r.status_code)

# Store API response in a variable.
response_dict = r.json()

print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    
    plot_dict = {
    'value': repo_dict['stargazers_count'],
    'label': repo_dict['description'],
    'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

# Make visualization.
my_style = LS('#333366', base_style=LCS)

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
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file(os.path.join(basedir, 'python_repos.svg'))