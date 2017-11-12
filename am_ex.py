import pandas as pd
import numpy as np
import re

df = pd.read_csv("am_ex_data.csv")

def removeChar(string):
    regex = re.compile('[^a-zA-Z]')
    return regex.sub('', string)
df['Review Text'] = df['Review Text'].apply(lambda x: x.split())
df['Review Text'] = df['Review Text'].apply(lambda x: [removeChar(i) for i in x])
total = []
for i in df['Review Text'].iteritems():
    total += i[1]

# print total[4]
words = pd.Series(data=total)
word_counts = words.value_counts()
to_drop = ['is', 'at', 'are', 'employees', 'to', 'of', 'the', 'a', ' ', 'you', 'he', 'she', 'i', 'I', 'they', 'for', 'or', 'and', 'work', 'company', 'on', 'in']
word_counts = pd.DataFrame(data = word_counts)

word_counts['word'] = word_counts.index
word_counts['count'] = word_counts[0]
del word_counts[0]
word_counts.reset_index(drop = True)

word_counts = word_counts[~word_counts['word'].isin(to_drop)]
print word_counts
# print df.head()
# word_counts = df['Review Text'].value_counts()

# print word_counts
