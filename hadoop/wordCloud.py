import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv('../data/视频分区数据.csv',encoding='utf-8-sig')

# Count term occurrences
term_counts = df['0'].value_counts()

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=50, font_path=r'C:\Windows\Fonts\STLITI.TTF').generate_from_frequencies(term_counts)

# Plotting the word cloud
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('../pic/热门分区词云图.png')
plt.show()