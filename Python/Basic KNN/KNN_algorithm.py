import numpy as np
from sklearn import preprocessing as prep
from sklearn.neighbors import KNeighborsClassifier as knc
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import datasets

weather = ["Summer", "Rainy", "Summer", "Snowy", "Rainy", "Rainy", "Snowy", "Snowy", "Snowy", "Summer", "Rainy"]
temp = ["Mild", "Cold", "Hot", "Cold", "Mild", "Cold", "Cold", "Cold", "Cold", "Hot", "Cold"]
play = ["Yes", "No", "No", "No", "Yes", "No", "No", "No", "Yes", "Yes", "No"]
matrix = []; columns = []


def knn_classifier(a, b, answer):
    le = prep.LabelEncoder()
    x = le.fit_transform(a)
    print(x)
    y = le.fit_transform(b)
    print(y)
    label = le.fit_transform(answer)
    print(label)
    features = list(zip(x, y))
    model = knc(n_neighbors=3)
    model.fit(features,label)
    predicted = model.predict(matrix)
    print(predicted)
    

for i in range(0,1):
    matrix += [0]
for j in range(0,2):
    columns += [0]
for i in range(0,1):
    matrix[i] = columns
for i in range (0,1):
    for j in range (0,2):
        print ('enter the feature number: ')
        matrix[i][j] = int(input())
print(matrix)


if matrix[i][j]<=2:
    knn_classifier(weather, temp, play)
else:
    print("Feature does not exist. Add the feature to train the model...y/n")
    a=input("Enter y or n: ")
    if a=='y':
        weather.append(input("Enter the weather feature you want to add: "))
        temp.append(input("Enter the temperature feature you want to add: "))
        play.append(input("Enter Yes/No for play: "))
        knn_classifier(weather, temp, play)
    else:
        print("Model is not trained for non-existent data")
        
