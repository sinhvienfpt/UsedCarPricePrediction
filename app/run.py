from flask import Flask, render_template, request
import numpy as np
from predict_module import PredictModule

app = Flask(__name__)

Predictor = PredictModule()

@app.route('/')
def home():
    return render_template('master.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input values from form
        kilometers_driven = request.form['Kilometers_Driven']
        power = request.form['Power']
        engine = request.form['Engine']
        year = request.form['Year']
        seats = request.form['Seats']
        mileage = request.form['Mileage']
        brand = request.form['brand']
        location = request.form['location']
        fuel_type = request.form['fuelType']
        transmission = request.form['transmission']
        owner_type = request.form['Owner_Type']

        # Create a dictionary with the input values
        input_dict = {
            'Kilometers_Driven': kilometers_driven,
            'Power': power,
            'Engine': engine,
            'Year': year,
            'Seats': seats,
            'Mileage': mileage,
            'Brand': brand,
            'Location': location,
            'Fuel_Type': fuel_type,
            'Transmission': transmission,
            'Owner_Type': owner_type
        }

        # Predict the price
        predicted_price = Predictor.predict(input_dict)
        
        # Render the go.html with the predicted price and input parameters
        return render_template('go.html', 
                               PredictedPrice=round(predicted_price[0],2),
                               KilometersDriven=kilometers_driven,
                               Power=power,
                               Engine=engine,
                               Year=year,
                               Seats=seats,
                               Mileage=mileage,
                               Brand=brand,
                               Location=location,
                               FuelType=fuel_type,
                               Transmission=transmission,
                               OwnerType=owner_type)
        

if __name__ == '__main__':
    app.run(debug=True)