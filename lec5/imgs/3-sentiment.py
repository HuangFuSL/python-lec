import os

import numpy as np
import pandas as pd
import requests
from gensim import corpora, models
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve
from sklearn.model_selection import train_test_split
from sklearn.utils.class_weight import compute_sample_weight

os.chdir(os.path.dirname(__file__))
np.random.seed(3407)

# Load data
URL = 'https://datarepo.eng.ucsd.edu/mcauley_group/data/' \
    'amazon_2023/raw/review_categories/All_Beauty.jsonl.gz'
if not os.path.exists('All_Beauty.jsonl.gz'):
    with open('All_Beauty.jsonl.gz', 'wb') as f:
        f.write(requests.get(URL).content)
df = pd.read_json(
    'All_Beauty.jsonl.gz',
    lines=True, compression='gzip', nrows=5000
)

# Process label
df['sentiment'] = df['rating'].apply(lambda x: 0 if x <= 3 else 1)
# Split data
X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df['sentiment'], test_size=0.2
)
# Process text - remove stop words
stoplist = set('for a of the and to in'.split())
def remove_words(text, to_remove):
    return ' '.join(
        [word for word in text.lower().split() if word not in to_remove]
    )
fn_stop = lambda x: remove_words(x, stoplist)
t_train, t_test = X_train.apply(fn_stop), X_test.apply(fn_stop)
# Process text - remove low frequency words
frequnecy = t_train.str.split().explode().value_counts()
frequnecy = frequnecy[frequnecy <= 10]
fn_low = lambda x: remove_words(x, set(frequnecy.index))
t_train, t_test = t_train.apply(fn_low), t_test.apply(fn_low)
# Process text - construct bag of words
dictionary = corpora.Dictionary(t_train.str.split())
corpus = [dictionary.doc2bow(text) for text in t_train.str.split()]
# Transform to dense representation
lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=200)
X_train = pd.DataFrame(
    [dict(lsi[dictionary.doc2bow(text.split())]) for text in t_train]
).fillna(0)
X_test = pd.DataFrame(
    [dict(lsi[dictionary.doc2bow(text.split())]) for text in t_test]
).fillna(0)
sample_weight = compute_sample_weight('balanced', y_train)
# Train model
lr = LogisticRegression()
lr.fit(X_train, y_train, sample_weight=sample_weight)
y_pred = lr.predict(X_test)
print(accuracy_score(y_test, y_pred)) # ~0.7

fpr, tpr, _ = roc_curve(y_test, lr.predict_proba(X_test)[:, 1])
auc = roc_auc_score(y_test, lr.predict_proba(X_test)[:, 1])
# Plot ROC curve
fig, ax = plt.subplots(1, 1, figsize=(2.4, 2), layout='constrained')
ax.plot(fpr, tpr)
ax.plot([0, 1], [0, 1], '--', color='red')
ax.text(0.5, 0.3, f'AUC: {auc:.3f}')
ax.set_xlabel('False Positive Rate')
ax.set_ylabel('True Positive Rate')
plt.savefig('3-roc.pgf')

text = [
    'These are pretty and seem well made. I find them comfortable to wear and they are cute.',
    'this product was terrible, i will never recommend it to anyone',
]
text = [remove_words(sentence, stoplist) for sentence in text]
text = [remove_words(sentence, set(frequnecy.index)) for sentence in text]
text = pd.DataFrame([
    dict(lsi[dictionary.doc2bow(sentence.split())])
    for sentence in text
])
print(lr.predict(text))  # [1 0]
