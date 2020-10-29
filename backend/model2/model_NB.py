import numpy as np
import json
import pickle
import csv

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score, confusion_matrix, classification_report


tagged_pgm_list=[]
X=[]
y=[]
with open('dataset_encoded.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    
    for r in reader:
        if r != []:
            # print(r,"\n",len(r),"\n\n\n")
            tagged_pgm_list.append(r)
            tag=r[-1]
            y.append(tag)
            r.remove(tag)
            # print(r)
            r=[float(rr) for rr in r]
            X.append(r)

# print(X,y)

print('Splitting between training and test data')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

print('Declaring NB')
nb = MultinomialNB()
print ('Fitting')
nb.fit(X_train, y_train)

print ('Predicting values for test data')
y_pred = nb.predict(X_test)
print("Accuracy: ",nb.score(X_test, y_test))
# print("F1 Score: ",f1_score(y_test, y_pred))
# result = {
#         'accuracy': nb.score(X_test, y_test),
#         'f1': f1_score(y_test, y_pred),
#         'f1_weighted': f1_score(y_test, y_pred, average='weighted'),
#         'precision': precision_score(y_test, y_pred),
#         'precision_weighted': precision_score(y_test, y_pred, average='weighted'),
#         'recall': recall_score(y_test, y_pred),
#         'recall_weighted': recall_score(y_test, y_pred, average='weighted')
#         }
# print(result)

filename = 'naivebayes.sav'
pickle.dump(nb, open(filename, 'wb'))
