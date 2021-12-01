import numpy as np
import pandas as pd
import pickle as pkl
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

#Read the data
df=pd.read_csv('news.csv')
#Get shape and head
#print(df)
df.shape
#print(df.head())


#Get the labels
labels=df.label
#print(labels.head())

#Split the dataset
x_train,x_test,y_train,y_test=train_test_split(df['text'], labels, test_size=0.2, random_state=7)
print(x_test)
#Initialize a TfidfVectorizer
tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)
#Fit and transform train set, transform test set
tfidf_train=tfidf_vectorizer.fit_transform(x_train) 


tfidf_test=tfidf_vectorizer.transform(x_test)


#Initialize a PassiveAggressiveClassifier
pac=PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train,y_train)
#DataFlair - Predict on the test set and calculate accuracy
y_pred=pac.predict(tfidf_test)
score=accuracy_score(y_test,y_pred)
print(f'Accuracy: {round(score*100,2)}%')
#print(y_pred)

#Build confusion matrix
print(confusion_matrix(y_test,y_pred, labels=['FAKE','REAL']))





#print(prediction)

with open('/home/stellamarsh/ritu/Fake-News-Detection-System/model.pkl','wb')as f:
    pkl.dump(pac,f)

with open('/home/stellamarsh/ritu/Fake-News-Detection-System/model1.pkl','wb') as f:
    pkl.dump(tfidf_vectorizer,f)