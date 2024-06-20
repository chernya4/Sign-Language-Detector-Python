import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


## Data is split into training and testing datasets.

data_dict = pickle.load(open('data.pickle', 'rb')) # Storing all models

filtered_data = []
filtered_labels = []

# Filter out data that is not the correct length
for i,entry in enumerate(data_dict['data']):
    if len(entry) == 42: # 21 points per hand and for each landmark we have x and y
        filtered_data.append(entry)
        filtered_labels.append(data_dict['labels'][i])
    else:
        print(i)

data = np.asarray(filtered_data)
labels = np.asarray(filtered_labels)

# 21 landmarks ont he human hand each having an x and a y coordiante
xtrain, xtest, ytrain, ytest = train_test_split(data, labels, test_size=0.2, random_state=42) # 80% training, 20% testing

# Pulling in the various packages that are the models for these machine learning algorithms.
classifiers = {
    "Random Forest": RandomForestClassifier(),
    "Logistic Regression": LogisticRegression(),
    "Support Vector Machine": SVC(),
}

for name,model in classifiers.items():
    model.fit(xtrain, ytrain)
    y_predict = model.predict(xtest)

    score = accuracy_score(y_predict, ytest)
    print(f"{name}; {score*100:.2f}% of smaples were classified sucessfully!")

with open('model.pickle', 'wb') as f:
    pickle.dump({'model':classifiers['Random Forest']}, f)