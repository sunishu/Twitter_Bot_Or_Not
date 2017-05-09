#Import the libraries
import pandas as pd
import datetime
import numpy as np
import re
from sklearn.metrics import accuracy_score

# Importing the dataset
dataset = pd.read_csv(r'C:\Users\parin\Desktop\training_data_2_csv_UTF.csv')
test_data = pd.read_csv(r'C:\Users\parin\Desktop\test_data_4_students.csv')
test_data = test_data.loc[:574,:]
# Importing the dataset
dataset = pd.read_csv(r'C:\Users\ramin\OneDrive - nyu.edu\Spring 2017\Machine Learning\Project\train_data.csv', encoding="cp437")
#descriptio_list = list(dataset["description"])
#dataset_new=dataset["has_extended_profile"].dropna()
dataset_new = dataset[["screen_name","followers_count","friends_count","listedcount","favourites_count","verified","statuses_count","default_profile","default_profile_image","bot"]]
    
X = dataset_new.iloc[:, :-1].values
#y = dataset_new.iloc[:, 9].values

                
# Preprocessing the screen name feature
#dataset_new["screen_name_bool"]=0
import re
pattern=r"bot"
for i in range(0, len(dataset_new)):
    if re.search(pattern, X[i,0]):
        dataset_new["screen_name"][i]=1
        
    else:
        dataset_new["screen_name"][i]=0
    X[i,0]= dataset_new["screen_name"][i]

y = dataset_new.iloc[:, 9].values

# Categorizing verified, default_profile, default_profile_image features
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
X[:,5]=labelencoder_X.fit_transform(X[:,5])
X[:,7]=labelencoder_X.fit_transform(X[:,7])
X[:,8]=labelencoder_X.fit_transform(X[:,8])

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Decision Tree classifier
from sklearn.tree import DecisionTreeClassifier
classifier_DT = DecisionTreeClassifier(criterion = "entropy", random_state=0)
classifier_DT.fit(X_train, y_train)
prediction_DT = classifier_DT.predict(X_test)

accuracy_score(y_test, prediction_DT)

#Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
classifier_RF = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
classifier_RF.fit(X_train, y_train)
prediction_RF = classifier_RF.predict(X_test)

accuracy_score(y_test, prediction_RF)

#Naive Bayes Classifier

from sklearn.naive_bayes import MultinomialNB
classifier=MultinomialNB()
classifier.fit(X_train, y_train)
prediction = classifier.predict(X_test)

#formatting the date
#X[2,9] = pd.to_datetime(X[2,9], format='%Y-%m-%d')

#import time

#ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(X[:, 9],'%a %b %d %H:%M:%S +0000 %Y'))

# Accuracy

from sklearn.metrics import accuracy_score
accuracy_score(y_test, prediction)
