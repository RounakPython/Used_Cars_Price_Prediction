import requests

url = 'http://localhost:5000/predict'
r = requests.post(url,json={'year':2016, 'km_driven':1584.52, 'owner'=2, 'mileage':102.2, 'engine':1420, 'max_power':235, 'seats':6, 'fuel_Diesel':0, 'fuel_LPG':0, 'fuel_Petrol':0, 'seller_type_Individual':1, 'seller_type_Trustmark_Dealer':0, 'transmission_Manual':0})

print(r.json())