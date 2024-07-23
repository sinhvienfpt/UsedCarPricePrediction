import pickle
import numpy as np
import pandas as pd


class PredictModule:
    def __init__(self):
        with open('../../model/model.pkl', 'rb') as model_file:
            self.model = pickle.load(model_file)
    
    def to_df(self, input_dict):
        features = ['Kilometers_Driven', 'Owner_Type', 'Mileage', 'Engine', 'Power',
            'Seats', 'Age', 'Ahmedabad', 'Bangalore', 'Chennai', 'Coimbatore',
            'Delhi', 'Hyderabad', 'Jaipur', 'Kochi', 'Kolkata', 'Mumbai', 'Pune',
            'CNG', 'Diesel', 'LPG', 'Petrol', 'Automatic', 'Manual', 'Ambassador',
            'Audi', 'BMW', 'Bentley', 'Chevrolet', 'Datsun', 'Fiat', 'Force',
            'Ford', 'Honda', 'Hyundai', 'ISUZU', 'Isuzu', 'Jaguar', 'Jeep',
            'Lamborghini', 'Land', 'Mahindra', 'Maruti', 'Mercedes-Benz', 'Mini',
            'Mitsubishi', 'Nissan', 'Porsche', 'Renault', 'Skoda', 'Smart', 'Tata',
            'Toyota', 'Volkswagen', 'Volvo']

        # Create a DataFrame with all zeros
        zeros_array = np.zeros((1, len(features)))
        # Create a DataFrame from the numpy array
        df = pd.DataFrame(zeros_array, columns=features)

        df['Kilometers_Driven'] = float(input_dict['Kilometers_Driven'])
        df['Power'] = float(input_dict['Power'])
        df['Engine'] = int(input_dict['Engine'])
        df['Seats'] = int(input_dict['Seats'])
        df['Mileage'] = float(input_dict['Mileage'])
        df['Age'] = 2019 - int(input_dict['Year'])  
        df[input_dict['Location']] = 1
        df[input_dict['Fuel_Type']] = 1
        df[input_dict['Transmission']] = 1
        df[input_dict['Brand']] = 1
        df['Owner_Type'] = int(input_dict['Owner_Type'])

        return df
    
    def predict(self, input_dict):
        df = self.to_df(input_dict)
        return self.model.predict(df)
    
    def print_result(self, input_dict):
        prediction = self.predict(input_dict)
        print("-------------------")
        print(f"The predicted price is: {prediction[0]:.2f} Lakh Rupees")
        print("-------------------")
    
# Test the class
if __name__ == '__main__':
    example_input_dict = {'Kilometers_Driven': 54840, 'Power': 99.6, 'Engine': 1485, 'Year': 2014, 'Seats': 5, 'Mileage': 18.8, 'Brand': 'Volkswagen', 'Location': 'Chennai', 'Fuel_Type': 'Petrol', 'Transmission': 'Automatic', 'Owner_Type': 3}

    predict_module = PredictModule()
    predict_module.print_result(example_input_dict)