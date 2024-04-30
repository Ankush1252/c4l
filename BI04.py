import numpy as np
import pandas as pd

data=pd.read_csv("gender_classification_v7.csv")
data.head()
data=pd.DataFrame(data)
data.info()
data["gender"].value_counts()
data
f=data[data.gender=="Female"]
m=data[data.gender=="Male"]
data.gender=[1 if each=="Male" else 0 for each in data.gender]
data["gender"].value_counts()
x=data.drop(["gender"],axis=1)
y=data.gender.values
x
y
x=(x-np.min(x))/(np.max(x)-np.min(x))
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(x_train,y_train)
print("test accuracy: {} ".format(lr.fit(x_train, y_train).score(x_test, y_test)))
print("train accuracy: {} ".format(lr.fit(x_train, y_train).score(x_train, y_train)))
y_pred=lr.predict(x_test)
y_true=y_test
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_true,y_pred)
cm
import seaborn as sns
import matplotlib.pyplot as plt
f,ax = plt.subplots(figsize=(5,5))
sns.heatmap(cm,annot = True,linewidths=0.5,linecolor="red",fmt = ".0f",ax=ax)
plt.xlabel("y_pred")
plt.ylabel("y_true")
plt.show()
