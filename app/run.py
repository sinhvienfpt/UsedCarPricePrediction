from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# # Load the trained model
# model = joblib.load('car_price_model.pkl')

# Function to preprocess input data







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

        # In ra tất cả các giá trị input trong terminal
        print("Input values:")
        print(f"Kilometers Driven: {kilometers_driven}")
        print(f"Power: {power}")
        print(f"Engine: {engine}")
        print(f"Year: {year}")
        print(f"Seats: {seats}")
        print(f"Mileage: {mileage}")
        print(f"Brand: {brand}")
        print(f"Location: {location}")
        print(f"Fuel Type: {fuel_type}")
        print(f"Transmission: {transmission}")
        print(f"Owner Type: {owner_type}")

        return "Form submitted successfully"

if __name__ == '__main__':
    app.run(debug=True)