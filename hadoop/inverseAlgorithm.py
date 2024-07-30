import pandas as pd
import matplotlib.pyplot as plt
# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False    # 解决保存图像是负号'-'显示为方块的问题


df_d = pd.read_csv('../data/视频点赞数据.csv',index_col=None)
df_s = pd.read_csv('../data/视频收藏数据.csv',index_col=None)
df_t = pd.read_csv('../data/视频投币数据.csv',index_col=None)

df = pd.DataFrame(columns=['点赞','投币','收藏'])
df['点赞']=df_d['点赞']
df['收藏']=df_s['收藏']
df['投币']=df_t['投币']

# 定义一个函数来处理带有单位的数据并转换为数值类型
def convert_to_number(s):
    if '万' in s:
        return float(s.replace('万', '')) * 10000
    else:
        return float(s)

# 对DataFrame中的每一列进行处理
df['点赞'] = df['点赞'].apply(convert_to_number).astype(int)
df['收藏'] = df['收藏'].apply(convert_to_number).astype(int)
df['投币'] = df['投币'].apply(convert_to_number).astype(int)

averages = df.mean()

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))

# Plot for 点赞
ax1.scatter(range(len(df)), df['点赞'], label='点赞')
ax1.axhline(y=averages['点赞'], color='r', linestyle='-', label='点赞 平均值')

# Plot for 收藏
ax2.scatter(range(len(df)), df['收藏'], label='收藏')
ax2.axhline(y=averages['收藏'], color='g', linestyle='-', label='收藏 平均值')

# Plot for 投币
ax3.scatter(range(len(df)), df['投币'], label='投币')
ax3.axhline(y=averages['投币'], color='b', linestyle='-', label='投币 平均值')

# Set titles and labels
ax1.set_title('点赞数据')
ax1.set_ylabel('点赞数')
ax1.legend()

ax2.set_title('收藏数据')
ax2.set_ylabel('收藏数')
ax2.legend()

ax3.set_title('投币数据')
ax3.set_ylabel('投币数')
ax3.set_xlabel('视频编号')
ax3.legend()

plt.tight_layout()
plt.savefig('../pic/视频数据散点图.png')
plt.show()