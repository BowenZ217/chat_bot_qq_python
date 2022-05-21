import requests
from bs4 import BeautifulSoup


def get_img_list_1(key):
    img_list = []
    for j in [0, 24, 48, 72, 96, 120]:
        # 获取网站数据
        url = requests.get('https://www.duitang.com/search/?kw={}&type=feed&start={}'.format(key, j))
        # url.encoding = 'utf-8'  #如果需要用到页面中的汉字内容，则需要进行解码，否则中文会出现乱码
        html = url.text
        # 解析网页
        soup = BeautifulSoup(html, 'html.parser')
        # 获取所有的img标签
        movie = soup.find_all('div', class_='mbpho')
        # print(movie)
        # 获取src路径
        for i in movie:
            img_src = i.find_all('img')[0].get('src')
            img_list.append(img_src)
    return img_list
