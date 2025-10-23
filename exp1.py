import pandas as pd
import numpy as np
import re
import nltk
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from transformers import pipeline

nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

data = pd.read_csv("/content/IMDB Dataset.csv")
print("Original Dataset:\n", data.head())

data['review'].fillna("No review provided", inplace=True)
data['sentiment'].fillna("unknown", inplace=True)


def clean_text(text):
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = text.lower()
    text = " ".join([w for w in text.split() if w not in stop_words])
    return text

data['cleaned_review'] = data['review'].apply(clean_text)

encoder = LabelEncoder()
''
data['sentiment_encoded'] = encoder.fit_transform(data['sentiment'])


data['review_length'] = data['review'].apply(lambda x: len(x.split()))

scaler = MinMaxScaler()
data['review_length_norm'] = scaler.fit_transform(data[['review_length']])

data.to_csv("imdb_cleaned.csv", index=False)

print("\nProcessed Dataset Sample:\n", data.head())
