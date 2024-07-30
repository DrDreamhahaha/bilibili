import os
from hdfs import InsecureClient

# 连接到Hadoop NameNode
client = InsecureClient(url='http://192.168.10.21:9870', user='root')

# 本地CSV文件夹路径
local_csv_folder = '../data'

# 列出data目录下所有CSV文件
for csv_file in os.listdir(local_csv_folder):
    if csv_file.endswith('.csv'):
        local_csv_path = os.path.join(local_csv_folder, csv_file)

        # 读取本地CSV文件内容
        with open(local_csv_path, 'r', encoding='utf-8') as f:
            csv_data = f.read()

        # 指定在HDFS中想要写入的CSV文件路径，以文件名命名
        hdfs_path = f'/niubi/{csv_file}'

        # 将CSV数据写入到Hadoop
        with client.write(hdfs_path, overwrite=True, encoding='utf-8') as writer:
            writer.write(csv_data)

        print(f"成功将CSV文件 '{local_csv_path}' 写入到Hadoop中：{hdfs_path}")