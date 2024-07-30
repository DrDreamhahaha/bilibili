import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# 创建 SparkSession
spark = SparkSession.builder \
    .appName("WordCount") \
    .config("spark.sql.sessionEncoding", "utf-8") \
    .getOrCreate()

# 定义数据架构
schema = StructType([
    StructField("text", StringType(), True)
])

# 读取数据
df = spark.read.csv("hdfs://192.168.10.21/niubi/视频分区数据.csv", schema=schema,encoding='utf-8')

# 处理数据
words = df.select(explode(split(df.text, " ")).alias("word"))

word_counts = words.groupBy("word").count()

# 显示结果
word_counts.show()

# 停止 SparkSession
spark.stop()