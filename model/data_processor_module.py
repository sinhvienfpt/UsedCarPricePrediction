import pandas as pd
import numpy as np 
from sklearn.preprocessing import OneHotEncoder

def DataProcess(df : pd.DataFrame) -> pd.DataFrame:

    
    print("Step 0: Take Brand from Name")
    df['Name'] = df['Name'].str.replace('ISUZU','Isuzu')
    df["Brand"] = df["Name"].apply(lambda x : x.split()[0])
    print("Step 0 Done")
    
    print("Step 1: Convert Year to Age")
    df["Age"] = 2019 - df["Year"]
    print("Step 1 Done")
    
    # Convert km/kg to kmpl
    print("Step 2: Convert Mileage to kmpl")
    for i in range(len(df)):
        m = df.Mileage.iloc[i]
        m = str(m)
        if ' ' in m:
            m,unit = m.split(" ")
            
            if unit == "km/kg":
                if df.Fuel_Type.iloc[i] == "CNG":
                    m = float(m)*0.79
                elif df.Fuel_Type.iloc[i] == "LPG":
                    m = float(m)*0.535
        
        df["Mileage"].iloc[i] = round(float(m),2)
    print("Step 2 Done")
    
    print("Step 3: Convert Engine and Power to float")
    def safe_float(x):
        try:
            return float(x.split()[0])
        except:
            return np.nan

    df["Power"] = df["Power"].apply(safe_float)
    df["Engine"] = df["Engine"].apply(safe_float)
    print("Step 3 Done")
    
    print("Step 4: Convert owner type to int")
    transformation = {
    "First":3,
    "Second":2,
    "Third":1,
    "Fourth & Above":0
    }
    
    df['Owner_Type'] = df['Owner_Type'].map(transformation)
    print("Step 4 Done")
    
    print("Step 5: One hot encoding")
    _categorical = ['Location','Fuel_Type','Transmission','Brand']
    # One hot
    ohe = OneHotEncoder(sparse=False)
    for col in _categorical:
        ohe.fit(df[[col]])
        df[ohe.categories_[0]] = ohe.transform(df[[col]])
    print("Step 5 Done")

    print("Step 6: Drop columns")
    cols_to_drop = ["New_Price","Year","Fuel_Type","Transmission",'Name', 'Location', 'Brand']
    df = df.drop(cols_to_drop,axis=1)
    print("Step 6 Done")
    
    return df