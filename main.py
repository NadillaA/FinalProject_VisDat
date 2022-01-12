# -*- coding: utf-8 -*-
"""main.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WP0R4x4vadw9xc3uAdGwp03DnTuPHAho

## WordCloud dengan dataset mengenai Black Lives Matter

Kelompok 20, IF-42-GAB06
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

#bokeh libraries
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel

output_file('filename.html')
fig = figure() 
show(fig)

from google.colab import drive
drive.mount('/content/drive')
PATH_BASE = "/content/drive/MyDrive/Visualisasi Data/TugasBesar"
DATASET_FILENAME = "training-dataset.csv"
DATAPATH = os.path.join(PATH_BASE, DATASET_FILENAME)

df=pd.read_csv(DATAPATH)
df.head()

df.tail()

df_joy = df.loc[(df['sentiment'] == 'joy')]
df_joy.head()

stop_words = ["https", "co", "RT", "face_with_tears_of_joy", "smiling_face_with_open_mouth_", "smiling_face_with_heart_eyes", "pouting_face", "smiling_face_with_smiling_eyes", "face_with_stuck out_tongue_", 
              "smiling_face_with_heart", "smiling_face"] + list(STOPWORDS) 
wordcloud = WordCloud(stopwords=stop_words, max_words=100, background_color="white").generate(' '.join(df_joy['tweet_text']))

plt.figure(figsize =(12, 12))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title('Wordcloud Tweet Dengan Mood Joy')

plt.show()

df_disgust = df.loc[(df['sentiment'] == 'disgust')]
df_disgust.head()

wordcloud = WordCloud(stopwords=stop_words, max_words=100, background_color="white").generate(' '.join(df_disgust['tweet_text']))

plt.figure(figsize =(12, 12))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title('Wordcloud Tweet Dengan Mood Disgust')

plt.show()

df_anger = df.loc[(df['sentiment'] == 'anger')]
df_anger.head()

wordcloud = WordCloud(stopwords=stop_words, max_words=100, background_color="white").generate(' '.join(df_anger['tweet_text']))

plt.figure(figsize =(12, 12))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title('Wordcloud Tweet Dengan Mood Anger')

plt.show()