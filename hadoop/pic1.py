import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False    # 解决保存图像是负号'-'显示为方块的问题

df = pd.read_csv('../data/视频播放量数据.csv',encoding='utf-8-sig')

def convert_to_number(s):
    if '万' in s:
        return float(s.replace('万', '')) * 10000
    else:
        return float(s)

df['0']=df['0'].apply(convert_to_number).astype(int)

# 绘制直方图
plt.hist(df['0'], bins=100)
plt.xlabel('播放量')
plt.ylabel('频数')
plt.title('视频播放量直方图')

# 绘制平均播放量的线
mean_playback = df['0'].mean()
plt.axvline(mean_playback, color='r', linestyle='dashed', linewidth=2)
plt.text(mean_playback + 100, 100, f'平均播放量：{mean_playback:.2f}')

# 绘制直方图
plt.hist(df['0'], bins=100, density=True, alpha=0.6, color='b', label='播放量直方图')
plt.xlabel('播放量')
plt.ylabel('频数')
plt.title('视频播放量直方图')

plt.savefig('../pic/视频播放量直方图')

# 显示图形
plt.show()