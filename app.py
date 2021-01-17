import numpy as np
from flask import Flask, render_template, request
import jsonify
import requests
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    
    if request.method == 'POST':
        year = int(request.form['Year'])
        km_driven = float(request.form['Km_Driven'])
        owner_ddn = request.form['Owner']
        mileage = float(request.form['Mileage'])
        engine = float(request.form['Engine'])
        max_power = float(request.form['Max_Power'])
        seats = float(request.form['Seats'])
        fuel_ddn = request.form['Fuel']
        seller_ddn = request.form['Seller_Type']
        transmission_ddn = request.form['Transmission']
        
        if owner_ddn == 'First Owner':
            owner = 4
        elif owner_ddn == 'Second Owner':
            owner = 3
        elif owner_ddn == 'Third Owner':
            owner = 2
        elif owner_ddn == 'Fourth & Above Owner':
            owner = 1
        else:
            owner = 0
        
        if fuel_ddn == 'Diesel':
            fuel_Diesel = 1
            fuel_LPG = 0
            fuel_Petrol = 0
        elif fuel_ddn == 'Petrol':
            fuel_Diesel = 0
            fuel_LPG = 0
            fuel_Petrol = 1
        elif fuel_ddn == 'LPG':
            fuel_Diesel = 0
            fuel_LPG = 1
            fuel_Petrol = 0
        else:
            fuel_Diesel = 0
            fuel_LPG = 0
            fuel_Petrol = 0
            
        if seller_ddn == 'Individual':
            seller_type_Individual = 1
            seller_type_Trustmark_Dealer = 0
        elif seller_ddn == 'Trustmark Dealer':
            seller_type_Individual = 0
            seller_type_Trustmark_Dealer = 1
        else:
            seller_type_Individual = 0
            seller_type_Trustmark_Dealer = 0
        
        if transmission_ddn == 'Manual':
            transmission_Manual = 1
        else:
            transmission_Manual = 0
        
    prediction = model.predict([[year, km_driven, owner, mileage, engine, max_power, seats, fuel_Diesel, fuel_LPG, fuel_Petrol, seller_type_Individual, seller_type_Trustmark_Dealer, transmission_Manual]])

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Used vehicle selling price should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)