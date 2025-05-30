# -*- coding: utf-8 -*-
"""Q1Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hgpD6nTJXoaoamtI6XHzAlbF_MYjkjaV
"""

import pandas as pd
from google.colab import files
uploaded = files.upload()

df = pd.read_csv('stroke_dataset.csv')

df = df[df['Symptoms'].notna()]

symptom_set = set()
df['symptoms_list'] = df['Symptoms'].apply(lambda x: [s.strip() for s in x.split(',')])
for symptoms in df['symptoms_list']:
    symptom_set.update(symptoms)

for symptom in symptom_set:
    df[symptom] = df['symptoms_list'].apply(lambda symptoms: 1 if symptom in symptoms else 0)

df = df.drop(columns=['Symptoms', 'symptoms_list'])

print(df.head())

df.to_csv('symptoms_fixed.csv', index=False)
files.download('symptoms_fixed.csv')

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from google.colab import files
uploaded = files.upload()

df = pd.read_csv('filled_values.csv')

nominal_columns = [
    'Dietary_Habits', 'Work_Type_of_patient',
    'Marital_Status', 'Physical_Activity', 'Alcohol_Intake',
    'Smoking_Status'
]

label_encoder = LabelEncoder()

for column in nominal_columns:
    df[column] = label_encoder.fit_transform(df[column])

print(df.head())

df.to_csv('label_encoded.csv', index=False)
files.download('label_encoded.csv')

import pandas as pd
from google.colab import files
uploaded = files.upload()

df = pd.read_csv("normalized.csv")

df = df.round(3)

print(df.head())

df.to_csv('final.csv', index=False)
files.download('final.csv')

import sklearn
from google.colab import files
uploaded = files.upload()

import pandas as pd
from sklearn.model_selection import train_test_split

attribute = "ReliefF"

df = pd.read_csv(f'{attribute}.csv')

train_set, temp_set = train_test_split(df, test_size=0.3, random_state=42)
val_set, test_set = train_test_split(temp_set, test_size=0.5, random_state=42)

print("Training set size:", len(train_set))
print("Validation set size:", len(val_set))
print("Test set size:", len(test_set))

train_set.to_csv(f'{attribute}train.csv', index=False)
val_set.to_csv(f'{attribute}val.csv', index=False)
test_set.to_csv(f'{attribute}test.csv', index=False)

files.download(f'{attribute}train.csv')
files.download(f'{attribute}val.csv')
files.download(f'{attribute}test.csv')