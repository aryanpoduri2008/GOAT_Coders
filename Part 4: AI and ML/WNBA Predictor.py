import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

df = pd.read_csv('teamstats.csv')
train, test = train_test_split(df, test_size = 0.2, random_state = 0)

X_train = train[[col for col in train.columns if col in ['ppg', 'oreb']]]
y_train = train[['w']]
X_test = test[[col for col in test.columns if col in ['ppg', 'oreb']]]
y_test = test[['w']]

reg = LinearRegression().fit(X_train, y_train)
print(reg.predict(X_test))