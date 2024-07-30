import pandas
import quandl
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import numpy as np

#getting and predicting data
df = quandl.get("WIKI/FB")
#just closing prices
df = df[['Adj. Close']]



# A variable for prediciting 'n' days out into future
forecast_out = 1
#creating another column: target/dependent variable shifted 'n' units up
df['Prediction'] = df[['Adj. Close']].shift(-(forecast_out))


# creating independent(x) data set
#convert dataframe to numpy aray
X = np.array(df.drop(['Prediction'],axis=1))
#Remove the last 'n' rows
X = X[:-forecast_out]

1

#create dependent data set (y)
#covert data frame to numpy array
y= np.array(df['Prediction'])
#get all y values except the last 'n' rows
y = y[:-forecast_out]




# spliting data to 80 20
x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.2)



# Creeate and Train Linear Regression Model
lr = LinearRegression()
# Train the model
lr.fit(x_train, y_train)

#testing model
lr_confidence = lr.score(x_test, y_test)
#print('lr confidence:', lr_confidence)

#set x_forecast equal to last 30 rows of og data set from adj.close column

x_forecast = np.array(df.drop(['Prediction'], axis = 1))[-forecast_out:]


#print lr predictions for the next 'n' days
lr_predicition = lr.predict(x_forecast)
print(lr_predicition)

import pickle
pickle.dump(lr, open('model.pkl', 'wb'))

lr = pickle.load(open('model.pkl','rb'))
print(lr.predict(x_forecast))


