import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import pickle


df = pd.read_csv('heart.data.csv')

df = df.drop("Unnamed: 0", axis=1)

sns.lmplot(x='biking', y='heart.disease', data=df)
sns.lmplot(x='smoking', y='heart.disease', data=df)

x_df = df.drop('heart.disease', axis=1)
y_df= df['heart.disease']

X_train, X_test, y_train, y_test = train_test_split(x_df, y_df, test_size=0.3, random_state = 42)


model=linear_model.LinearRegression()
model.fit(X_train, y_train)
predicition_test = model.predict(X_test)

print(model.score(X_train,y_train))
print(np.mean(predicition_test-y_test)**2)


pickle.dump(model, open('model.pk1','wb'))
model = pickle.load(open('model.pkl','rb'))

print(model.predict([70.1, 26.3]))

