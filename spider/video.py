from functions.requests_func import url_get
import pandas as pd
from bs4 import BeautifulSoup


def crawler():
    d = {}
    i = 0
    for av_num in pf.url:
        try:
            url = f"https:{av_num}"
            get_html = url_get(url=url)
            soup = BeautifulSoup(get_html.text, 'html.parser')
            h1_tag = soup.find('h1')

            if h1_tag:
                # 获取 h1 标签下的内容
                h1_content = h1_tag.text
                h1_content
                if '标题' not in d:
                    d['标题'] = [h1_content]
                else:
                    d['标题'].append(h1_content)

            div_tag = soup.find('div', class_='video-like video-toolbar-left-item')

            span_tag = div_tag.find('span', class_='video-like-info video-toolbar-item-text')

            if span_tag:
                # 获取 <span> 标签中的文本内容
                content = span_tag.text
                if '点赞' not in d:
                    d['点赞'] = [content]
                else:
                    d['点赞'].append(content)

            div_tag = soup.find('div', class_='video-coin video-toolbar-left-item')

            if div_tag:
                # 在<div>标签中查找<span>标签
                span_tag = div_tag.find('span', class_='video-coin-info video-toolbar-item-text')

                if span_tag:
                    # 获取<span>标签中的文本内容
                    content = span_tag.text

                    # 将内容存入字典中
                    if '投币' not in d:
                        d['投币'] = [content]
                    else:
                        d['投币'].append(content)

            div_tag = soup.find('div', class_='video-fav video-toolbar-left-item')

            if div_tag:
                # 在<div>标签中查找<span>标签
                span_tag = div_tag.find('span', class_='video-fav-info video-toolbar-item-text')

                if span_tag:
                    # 获取<span>标签中的文本内容
                    content = span_tag.text

                    # 将内容存入字典中
                    if '收藏' not in d:
                        d['收藏'] = [content]
                    else:
                        d['收藏'].append(content)

            div_tag = soup.find('div', class_='tag-panel')

            if div_tag:
                # 查找所有的<a>标签
                a_tags = div_tag.find_all('a')
                for a_tag in a_tags:
                    # 获取<a>标签中的文本内容
                    content = a_tag.text
                    # 将内容存入列表中
                if '分区列表' not in d:
                    d['分区列表'] = [content]
                else:
                    d['分区列表'].append(content)

            div_tag = soup.find('div', class_='view-text')

            if div_tag:
                content = div_tag.text.strip()
                if '播放量' not in d:
                    d['播放量'] = [content]
                else:
                    d['播放量'].append(content)

            # print(d)
        except:
            i += 1
            print(i)
    return d


if __name__ == '__main__':
    pf = pd.read_csv('../data/每周必看.csv')
    pf = pf.drop_duplicates()
    d = crawler()
    data=pd.DataFrame(d['标题'])
    data.to_csv('../data/视频标题数据.csv', encoding='utf-8-sig',index=False)
    data = pd.DataFrame(d['点赞'])
    data.to_csv('../data/视频点赞数据.csv', encoding='utf-8-sig', index=False)
    data = pd.DataFrame(d['收藏'])
    data.to_csv('../data/视频收藏数据.csv', encoding='utf-8-sig', index=False)
    data = pd.DataFrame(d['投币'])
    data.to_csv('../data/视频投币数据.csv', encoding='utf-8-sig', index=False)
    data = pd.DataFrame(d['分区列表'])
    # data.to_csv('../data/视频分区数据.csv', encoding='utf-8-sig', index=False)
    data = pd.DataFrame(d['播放量'])
    data.to_csv('../data/视频播放量数据.csv', encoding='utf-8-sig', index=False)