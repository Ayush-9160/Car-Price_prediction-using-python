import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle as pk
car =pd.read_csv('Cleaned_car.csv')
x=car[['name','company','year','kms_driven','fuel_type']]
y=car['Price']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1,random_state=665)

ohe=OneHotEncoder()
ohe.fit(x[['name','company','fuel_type']])
column_trans=make_column_transformer((OneHotEncoder(categories=ohe.categories_),['name','company','fuel_type']),remainder='passthrough')
lr=LinearRegression()
pipe=make_pipeline(column_trans,lr)
pipe.fit(x_train,y_train)
p=pipe.predict(pd.DataFrame(columns=x_test.columns,data=np.array(['Maruti Suzuki Swift','Maruti',2019,100,'Petrol']).reshape(1,5)))
print(p)
pk.dump(pipe,open('LinearRegressionModel.pkl','wb'))