#1. imports
import numpy as np

import uvicorn 
from fastapi import FastAPI
import pickle

#2. create app object
app = FastAPI()

#3. load the model
model_load = pickle.load(open(r'C:\Users\ShahwarN\model_pickle_4.pkl','rb'))

#3.  index route
#@app.get('/property-details')
#def index():
#    return {'NAME?': 'My name is Shahwar Alam Naqvi'}

@app.get('/predict')
def predictHousePrice(bhk: int,
                    size: int,
                    area_type: int,
                    city: int,
                    furnishing_stat: int,
                    tenant_pref: int,
                    bathroom: int,
                    poc: int,
                    house_floor: int,
                    total_floor: int):
    prediction = model_load.predict([[bhk, size, area_type, city, furnishing_stat, tenant_pref,bathroom,poc,house_floor,total_floor]])
    return {'The house price is : {}'.format(prediction)}
    

#if __name__ == '__main__':
#    uvicorn.run(app)
#{
#  "bhk": 2,
#  "size": 1100,
#  "area_type": 1,
#  "city": 4,
#  "furnishing_stat": 2,
#  "tenant_pref": 1,
# "bathroom": 2,
#  "poc": 1,
#  "house_floor": 0,
#  "total_floor": 2
#}
