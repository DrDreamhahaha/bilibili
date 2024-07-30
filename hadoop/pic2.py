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

df['点赞与投币比'] = df['点赞'] / df['投币']
df['点赞与收藏比'] = df['点赞'] / df['收藏']
df['收藏与投币比'] = df['收藏'] / df['投币']
df['点赞收藏投币比'] = (df['点赞'] + df['收藏']) / df['投币']


avg_ratio = df['点赞与投币比'].mean()

fig, ax = plt.subplots(figsize=(8, 6))

# 绘制散点图
ax.scatter(range(len(df)), df['点赞与投币比'], label='点赞与投币比')

# 绘制平均值线
ax.axhline(y=avg_ratio, color='r', linestyle='-', label='点赞与投币比 平均值')

# 设置标题和标签
ax.set_title('点赞数与投币数的比散点图')
ax.set_xlabel('视频编号')
ax.set_ylabel('点赞数与投币数的比')
ax.legend()

plt.tight_layout()
plt.savefig('../pic/点赞数与投币数比散点图.png')


fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))

# 绘制点赞和收藏的比散点图
ax1.scatter(range(len(df)), df['点赞与收藏比'], label='点赞与收藏比')
avg_ratio1 = df['点赞与收藏比'].mean()
ax1.axhline(y=avg_ratio1, color='r', linestyle='-', label='点赞与收藏比 平均值')
ax1.set_title('点赞与收藏比散点图')
ax1.set_ylabel('点赞与收藏比')
ax1.legend()

# 绘制收藏和投币的比散点图
ax2.scatter(range(len(df)), df['收藏与投币比'], label='收藏与投币比')
avg_ratio2 = df['收藏与投币比'].mean()
ax2.axhline(y=avg_ratio2, color='g', linestyle='-', label='收藏与投币比 平均值')
ax2.set_title('收藏与投币比散点图')
ax2.set_ylabel('收藏与投币比')
ax2.legend()

# 绘制点赞、收藏和投币的比散点图
ax3.scatter(range(len(df)), df['点赞收藏投币比'], label='点赞收藏投币比')
avg_ratio3 = df['点赞收藏投币比'].mean()
ax3.axhline(y=avg_ratio3, color='b', linestyle='-', label='点赞收藏投币比 平均值')
ax3.set_title('点赞收藏投币比散点图')
ax3.set_xlabel('视频编号')
ax3.set_ylabel('点赞收藏投币比')
ax3.legend()

plt.tight_layout()
plt.savefig('../pic/各种比值散点图.png')
plt.show()