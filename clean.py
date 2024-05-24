import pandas as pd
car = pd.read_csv('quikr_car.csv')
car=car[car['year'].str.isnumeric()]
car['year']=car['year'].astype(int)
car=car[car['Price']!='Ask For Price']
car['Price']=car['Price'].str.replace(',','').astype(int)
car['kms_driven']=car['kms_driven'].str.split().str.get(0).str.replace(',','')
car=car[car['kms_driven'].str.isnumeric()]
car['kms_driven']=car['kms_driven'].astype(int)
car=car[~car['fuel_type'].isna()]
car['name']=car['name'].str.split().str.slice(start=0,stop=3).str.join(' ')
car=car.reset_index(drop=True)
car=car[car['Price']<6000000]
car.to_csv('Cleaned_car.csv')